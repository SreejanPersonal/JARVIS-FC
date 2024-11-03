import os
import json

def file_operations(operation: str, filename: str = "", content: str = "") -> str:
    try:
        if operation == "list":
            files = os.listdir('.')
            return json.dumps({
                "status": "success",
                "files": files,
                "message": f"Found {len(files)} files in current directory"
            })
        elif operation == "read":
            with open(filename, 'r') as f:
                return json.dumps({
                    "status": "success",
                    "content": f.read(),
                    "message": f"File {filename} read successfully"
                })
        elif operation == "write":
            with open(filename, 'w') as f:
                f.write(content)
            return json.dumps({
                "status": "success",
                "message": f"Content written to {filename} successfully"
            })
        elif operation == "delete":
            os.remove(filename)
            return json.dumps({
                "status": "success",
                "message": f"File {filename} deleted successfully"
            })
    except Exception as e:
        return json.dumps({
            "status": "error",
            "message": str(e)
        })