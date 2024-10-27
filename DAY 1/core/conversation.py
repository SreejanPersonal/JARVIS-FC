import json
from termcolor import colored
from utils.logger import logger

class ConversationHandler:
    def __init__(self, assistant):
        self.assistant = assistant

    def handle_conversation(self, user_prompt: str):
        print("\n" + colored("👤 User Query: ", "green", attrs=['bold']) + user_prompt + "\n")
        
        self.assistant.add_to_history({
            "role": "user",
            "content": user_prompt
        })

        try:
            return self._process_conversation()
        except Exception as e:
            logger.error(f"ERROR: {str(e)}")
            return f"Error occurred: {str(e)}"

    def _process_conversation(self):
        response = self.assistant.client.chat.completions.create(
            model=self.assistant.model,
            messages=self.assistant.conversation_history,
            tools=self.assistant.get_all_tools(),
            tool_choice="auto",
            max_tokens=4096
        )

        response_message = response.choices[0].message
        tool_calls = response_message.tool_calls

        if tool_calls:
            return self._handle_tool_calls(response_message, tool_calls)
        else:
            self.assistant.add_to_history({
                "role": "assistant",
                "content": response_message.content
            })
            return response_message.content

    def _handle_tool_calls(self, response_message, tool_calls):
        self.assistant.add_to_history({
            "role": "assistant",
            "content": response_message.content if response_message.content else "",
            "tool_calls": [{
                "type": "function",
                "id": tool_call.id,
                "function": {
                    "name": tool_call.function.name,
                    "arguments": tool_call.function.arguments
                }
            } for tool_call in tool_calls]
        })

        for tool_call in tool_calls:
            function_name = tool_call.function.name
            function_args = json.loads(tool_call.function.arguments)
            
            logger.info(f"TOOL CALLED: {function_name}")
            logger.info(f"WITH PARAMETERS: {json.dumps(function_args, indent=2)}")

            function_to_call = self.assistant.available_functions[function_name]
            function_response = function_to_call(**function_args)
            
            response_data = json.loads(function_response)
            logger.info(f"FUNCTION RESPONSE: {response_data['message']}")

            self.assistant.add_to_history({
                "role": "tool",
                "tool_call_id": tool_call.id,
                "name": function_name,
                "content": function_response
            })

        final_response = self.assistant.client.chat.completions.create(
            model=self.assistant.model,
            messages=self.assistant.conversation_history
        )
        
        ai_response = final_response.choices[0].message.content
        
        self.assistant.add_to_history({
            "role": "assistant",
            "content": ai_response
        })
        
        logger.info(f"AI RESPONSE: {ai_response}")
        return ai_response