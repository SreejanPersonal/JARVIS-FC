def format_message_for_storage(message):
    if isinstance(message, dict):
        formatted = {
            "role": message.get("role", "unknown"),
            "content": message.get("content", "")
        }
        
        if "tool_calls" in message:
            formatted["tool_calls"] = []
            for tool_call in message["tool_calls"]:
                formatted_tool_call = {
                    "type": "function",
                    "id": tool_call.get("id") if isinstance(tool_call, dict) else tool_call.id,
                    "function": {
                        "name": tool_call["function"]["name"] if isinstance(tool_call, dict) else tool_call.function.name,
                        "arguments": tool_call["function"]["arguments"] if isinstance(tool_call, dict) else tool_call.function.arguments
                    }
                }
                formatted["tool_calls"].append(formatted_tool_call)
        
        if message.get("role") == "tool":
            formatted["tool_call_id"] = message.get("tool_call_id")
            formatted["name"] = message.get("name")
        
        return formatted
    
    return {
        "role": getattr(message, "role", "unknown"),
        "content": getattr(message, "content", "")
    }

def format_history_for_storage(messages):
    formatted_messages = []
    
    for message in messages:
        if isinstance(message, str):
            formatted_messages.append({
                "role": "unknown",
                "content": message
            })
            continue
        
        formatted_messages.append(format_message_for_storage(message))
    
    return formatted_messages