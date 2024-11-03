TOOLS_CONFIG = {
    "files": [{
        "type": "function",
        "function": {
            "name": "file_operations",
            "description": "Perform file operations like read, write, list, and delete",
            "parameters": {
                "type": "object",
                "properties": {
                    "operation": {"type": "string", "enum": ["read", "write", "list", "delete"]},
                    "filename": {"type": "string", "description": "Name of the file to operate on"},
                    "content": {"type": "string", "description": "Content to write (for write operation)"}
                },
                "required": ["operation"]
            }
        }
    }],
    "system": [{
        "type": "function",
        "function": {
            "name": "system_info",
            "description": "Get system information like OS details, memory usage, and disk space",
            "parameters": {
                "type": "object",
                "properties": {
                    "info_type": {"type": "string", "enum": ["os", "memory", "disk"]}
                },
                "required": ["info_type"]
            }
        }
    }],
    "process": [{
        "type": "function",
        "function": {
            "name": "process_manager",
            "description": "Manage and monitor system processes",
            "parameters": {
                "type": "object",
                "properties": {
                    "action": {"type": "string", "enum": ["list", "find"]},
                    "process_name": {"type": "string", "description": "Name of process to find (for find action)"}
                },
                "required": ["action"]
            }
        }
    }],
    "weather": [{
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get current weather information for any city",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {"type": "string", "description": "Name of the city"}
                },
                "required": ["city"]
            }
        }
    }],
    "currency": [{
        "type": "function",
        "function": {
            "name": "convert_currency",
            "description": "Convert amount from one currency to another",
            "parameters": {
                "type": "object",
                "properties": {
                    "amount": {"type": "number", "description": "Amount to convert"},
                    "from_currency": {"type": "string", "description": "Source currency code (e.g., USD)"},
                    "to_currency": {"type": "string", "description": "Target currency code (e.g., EUR)"}
                },
                "required": ["amount", "from_currency", "to_currency"]
            }
        }
    }],
    "notes": [{
        "type": "function",
        "function": {
            "name": "notes_manager",
            "description": "Manage quick notes",
            "parameters": {
                "type": "object",
                "properties": {
                    "action": {"type": "string", "enum": ["create", "list", "read"]},
                    "title": {"type": "string", "description": "Title of the note"},
                    "content": {"type": "string", "description": "Content of the note (for create action)"}
                },
                "required": ["action"]
            }
        }
    }]
}