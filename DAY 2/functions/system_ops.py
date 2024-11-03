import psutil
import json

def system_info(info_type: str) -> str:
    try:
        if info_type == "os":
            info = {
                "system": psutil.os.name,
                "platform": psutil.sys.platform,
                "processor": psutil.os.processor()
            }
        elif info_type == "memory":
            memory = psutil.virtual_memory()
            info = {
                "total": f"{memory.total / (1024**3):.2f} GB",
                "available": f"{memory.available / (1024**3):.2f} GB",
                "percent_used": f"{memory.percent}%"
            }
        elif info_type == "disk":
            disk = psutil.disk_usage('/')
            info = {
                "total": f"{disk.total / (1024**3):.2f} GB",
                "free": f"{disk.free / (1024**3):.2f} GB",
                "percent_used": f"{disk.percent}%"
            }
        return json.dumps({
            "status": "success",
            "info": info,
            "message": f"Retrieved {info_type} information successfully"
        })
    except Exception as e:
        return json.dumps({
            "status": "error",
            "message": str(e)
        })

def process_manager(action: str, process_name: str = None) -> str:
    try:
        if action == "list":
            processes = [p.name() for p in psutil.process_iter()]
            return json.dumps({
                "status": "success",
                "processes": processes[:10],
                "message": f"Listed top 10 of {len(processes)} running processes"
            })
        elif action == "find" and process_name:
            found = [p.info for p in psutil.process_iter(['name', 'pid']) 
                    if process_name.lower() in p.info['name'].lower()]
            return json.dumps({
                "status": "success",
                "found": found,
                "message": f"Found {len(found)} matching processes"
            })
    except Exception as e:
        return json.dumps({
            "status": "error",
            "message": str(e)
        })