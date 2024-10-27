import logging
from termcolor import colored

class ColoredFormatter(logging.Formatter):
    def format(self, record):
        if "TOOL CALLED" in record.msg:
            record.msg = colored("🔧 " + record.msg, "yellow", attrs=['bold'])
        elif "FUNCTION RESPONSE" in record.msg:
            record.msg = colored("📤 " + record.msg, "cyan", attrs=['bold'])
        elif "AI RESPONSE" in record.msg:
            record.msg = colored("🤖 " + record.msg, "magenta", attrs=['bold'])
        elif "ERROR" in record.msg:
            record.msg = colored("❌ " + record.msg, "red", attrs=['bold'])
        return super().format(record)

logger = logging.getLogger("groq_function_calling")
logger.setLevel(logging.INFO)
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
formatter = ColoredFormatter('%(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)