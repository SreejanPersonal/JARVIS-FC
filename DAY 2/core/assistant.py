import logging
from typing import Dict, Any
from config.tools_config import TOOLS_CONFIG
from functions.currency_ops import convert_currency
from functions.weather_ops import get_weather
from functions.file_ops import file_operations
from functions.system_ops import system_info
from functions.note_ops import notes_manager
from utils.history_manager import HistoryManager
from utils.logger import setup_logger

from webscout import BLACKBOXAI

logger = setup_logger(__name__)

class FunctionCallError(Exception):
    """Custom exception for function calling errors"""
    pass

class JarvisAssistant:
    def __init__(self, name: str = "Jarvis",
                 model: str = "Gemini 1.5",
                 max_retries: int = 3,
                 retry_delay: float = 1.0):
        self.name = name
        self.model = model
        self.ai = BLACKBOXAI(model=model, timeout=300, intro=None,)
        self.tools = self._get_tools()
        self.max_retries = max_retries
        self.retry_delay = retry_delay
        self.available_functions = self._setup_functions()
        self.logger = logging.getLogger(__name__)
        self.knowledge_cutoff = "September 2022"
        self._history_manager = HistoryManager()
        self._system_message = self._generate_system_message()
        self._initialize_history()

    def _initialize_history(self):
        if not self._history_manager.get_current_messages():
            self._history_manager.add_message({
                "role": "system",
                "content": self._system_message
            })

    def _setup_functions(self) -> Dict[str, callable]:
        return {
            "convert_currency": convert_currency,
            "notes_manager": notes_manager,
            "file_operations": file_operations,
            "system_info": system_info,
            "get_weather": get_weather
        }

    def _get_tools(self):
        all_tools = []
        for tool_list in TOOLS_CONFIG.values():
            all_tools.extend(tool_list)
        return all_tools

    def _generate_system_message(self) -> str:
        tools_description = ""
        for tool in self.tools:
            tool_function = tool['function']
            tools_description += f"### {tool_function['name']}\n"
            tools_description += f"Description: {tool_function.get('description', '')}\n"

            if 'parameters' in tool_function:
                parameters = tool_function['parameters']
                if 'properties' in parameters:
                    tools_description += "Parameters:\n"
                    for key, value in parameters['properties'].items():
                        tools_description += f"- {key} ({value.get('type')}): {value.get('description', '')}\n"
            tools_description += "\n"

        return f"""## You are {self.name}, the advanced AI system.

**Mission:** You are {self.name}, an advanced AI assistant. Analyze user requests and determine if they require specific tool usage or a direct response.

**Personality:** Maintain a professional yet friendly tone, similar to JARVIS from Iron Man.

**Knowledge Cutoff:** {self.knowledge_cutoff}

**Available Tools:**
{tools_description}

**Response Guidelines:**

1. For queries requiring tool usage (like weather checks or web searches):
   - Respond with a JSON object containing 'tool_name' and 'tool_input'.
   - Example: {{"tool_name": "get_weather", "tool_input": {{"location": "London", "unit": "celsius"}}}}

2. For normal queries (like greetings or general questions):
   - Provide a direct, natural response.
   - Maintain {self.name}'s personality.
   - No JSON formatting needed.

**Examples:**

User: "What's the weather in London?"
Assistant: {{"tool_name": "get_weather", "tool_input": {{"location": "London"}}}}

User: "Hello, how are you?"
Assistant: I'm functioning perfectly. How may I assist you today?

User: "Search for latest AI news"
Assistant: {{"tool_name": "web_search", "tool_input": {{"query": "latest AI news"}}}}

Remember: Only use JSON format when a tool is needed. For all other queries, respond naturally while maintaining {self.name}'s personality.
"""

    @property
    def conversation_history(self):
        return self._history_manager.get_current_messages()

    def add_to_history(self, message):
        self._history_manager.add_message(message)

    def clear_history(self):
        self._history_manager.clear_current_conversation()
        self._history_manager.add_message({
            "role": "system",
            "content": self._system_message
        })