import os
import json

def notes_manager(action: str, title: str = "", content: str = "") -> str:
    try:
        notes_dir = "quick_notes"
        os.makedirs(notes_dir, exist_ok=True)
        
        if action == "create":
            filename = f"{notes_dir}/{title}.txt"
            with open(filename, 'w') as f:
                f.write(content)
            return json.dumps({
                "status": "success",
                "message": f"Note '{title}' created successfully"
            })
        elif action == "list":
            notes = [f.replace('.txt', '') for f in os.listdir(notes_dir) if f.endswith('.txt')]
            return json.dumps({
                "status": "success",
                "notes": notes,
                "message": f"Found {len(notes)} notes"
            })
        elif action == "read":
            filename = f"{notes_dir}/{title}.txt"
            with open(filename, 'r') as f:
                content = f.read()
            return json.dumps({
                "status": "success",
                "content": content,
                "message": f"Note '{title}' retrieved successfully"
            })
    except Exception as e:
        return json.dumps({
            "status": "error",
            "message": str(e)
        })