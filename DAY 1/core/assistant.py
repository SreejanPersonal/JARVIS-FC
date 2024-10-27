from groq import Groq
from config.tools_config import TOOLS_CONFIG
from functions.file_ops import file_operations
from functions.system_ops import system_info, process_manager
from functions.weather_ops import get_weather
from functions.currency_ops import convert_currency
from functions.note_ops import notes_manager
from utils.history_manager import HistoryManager

class JarvisAssistant:
    def __init__(self):
        self._client = Groq(api_key="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")
        self._model = "llama-3.1-70b-versatile"
        self._available_functions = {
            "file_operations": file_operations,
            "system_info": system_info,
            "process_manager": process_manager,
            "get_weather": get_weather,
            "convert_currency": convert_currency,
            "notes_manager": notes_manager
        }
        self._system_message = """You are Jarvis, an AI assistant focused on efficiency and precise responses. 
        When using tools:
        1. Always use the tool_calls format for function calls
        2. Never return function calls as text in content
        3. Keep responses brief and to the point
        4. Process tool responses and provide clear answers
        
        Example tool usage:
        - Use tool_calls for all function interactions
        - Process tool responses before answering
        - Provide direct, clear answers from tool results"""

        self._history_manager = HistoryManager()
        
        # Only add system message if starting fresh conversation
        if not self._history_manager.get_current_messages():
            self._history_manager.add_message({
                "role": "system",
                "content": self._system_message
            })

    @property
    def client(self):
        return self._client

    @property
    def model(self):
        return self._model

    @property
    def available_functions(self):
        return self._available_functions

    @property
    def system_message(self):
        return self._system_message

    @property
    def conversation_history(self):
        return self._history_manager.get_current_messages()

    def get_all_tools(self):
        all_tools = []
        for tool_list in TOOLS_CONFIG.values():
            all_tools.extend(tool_list)
        return all_tools

    def add_to_history(self, message):
        self._history_manager.add_message(message)

    def clear_history(self):
        self._history_manager.clear_current_conversation()
        self._history_manager.add_message({
            "role": "system",
            "content": self._system_message
        })