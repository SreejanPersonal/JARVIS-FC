import json
from utils.logger import setup_logger
from termcolor import colored

logger = setup_logger(__name__)

class FunctionCallError(Exception):
    """Custom exception for function calling errors"""
    pass

class ConversationHandler:
    def __init__(self, assistant):
        self.assistant = assistant

    def handle_conversation(self, user_prompt: str):
        # Remove the print statement here since it's redundant
        self.assistant.add_to_history({
            "role": "user",
            "content": user_prompt
        })

        try:
            response = self._process_conversation()
            return response
        except Exception as e:
            logger.error(f"Error: {str(e)}")
            return f"An error occurred: {str(e)}"

    def _process_conversation(self):
        messages = self.assistant.conversation_history
        
        initial_response = self.assistant.ai.chat(messages)
        # Only log if it's a function call
        if self._is_function_call_response(initial_response):
            logger.info(colored("Processing function call...", "cyan"))

        if self._is_function_call_response(initial_response):
            function_call_data = self._parse_function_call(initial_response)
            function_name = function_call_data.get('tool_name')
            arguments = function_call_data.get('tool_input', {})

            function_result = self.execute_function(function_name, arguments)
            # Only log the processed result in a clean format
            logger.info(colored(f"Function {function_name} result processed", "green"))

            self.assistant.add_to_history({
                "role": "assistant",
                "content": initial_response
            })
            self.assistant.add_to_history({
                "role": "function",
                "name": function_name,
                "content": json.dumps(function_result)
            })

            self.assistant.add_to_history({
                "role": "user",
                "content": "Please provide a natural response based on this function result."
            })

            final_response = self.assistant.ai.chat(self.assistant.conversation_history)
            self.assistant.add_to_history({
                "role": "assistant",
                "content": final_response.strip()
            })

            return final_response.strip()
        else:
            self.assistant.add_to_history({
                "role": "assistant",
                "content": initial_response.strip()
            })
            return initial_response.strip()

    def _is_function_call_response(self, response: str) -> bool:
        try:
            response_json = json.loads(response)
            return 'tool_name' in response_json
        except json.JSONDecodeError:
            return False

    def _parse_function_call(self, response: str) -> dict:
        try:
            response_json = json.loads(response)
            return {
                "tool_name": response_json.get('tool_name'),
                "tool_input": response_json.get('tool_input', {})
            }
        except Exception as e:
            logger.error(f"Error parsing function call: {e}")
            raise FunctionCallError(f"Error parsing function call: {str(e)}")

    def execute_function(self, function_name: str, arguments: dict) -> dict:
        try:
            if function_name not in self.assistant.available_functions:
                raise FunctionCallError(f"Function {function_name} not found")

            result = self.assistant.available_functions[function_name](**arguments)
            return result

        except Exception as e:
            logger.error(f"Error executing function: {e}")
            raise FunctionCallError(f"Error executing function: {str(e)}")