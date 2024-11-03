import json
import os
from datetime import datetime
from .message_formatter import format_history_for_storage

class HistoryManager:
    def __init__(self, history_file="history/conversation_history.json"):
        self.history_file = history_file
        self.current_conversation = None
        self.ensure_history_file()
        self.load_or_create_conversation()

    def ensure_history_file(self):
        if not os.path.exists(self.history_file):
            os.makedirs(os.path.dirname(self.history_file), exist_ok=True)
            with open(self.history_file, 'w', encoding='utf-8') as f:
                json.dump([], f)

    def load_or_create_conversation(self):
        """Load existing conversation or create new one if none exists"""
        conversations = self.load_all_conversations()
        if conversations:
            self.current_conversation = conversations[-1]  # Get the last conversation
        else:
            self.start_new_conversation()

    def start_new_conversation(self):
        """Start a fresh conversation"""
        self.current_conversation = {
            "timestamp": datetime.now().isoformat(),
            "messages": []
        }
        conversations = self.load_all_conversations()
        conversations.append(self.current_conversation)
        self.save_conversations(conversations)

    def load_all_conversations(self):
        try:
            with open(self.history_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except:
            return []

    def save_conversations(self, conversations):
        with open(self.history_file, 'w', encoding='utf-8') as f:
            json.dump(conversations, f, indent=2, ensure_ascii=False)

    def add_message(self, message):
        if not self.current_conversation:
            self.load_or_create_conversation()

        if isinstance(message, dict) and "role" in message:
            self.current_conversation["messages"].append(message)
        else:
            formatted_message = format_history_for_storage([message])
            self.current_conversation["messages"].extend(formatted_message)

        conversations = self.load_all_conversations()
        conversations[-1] = self.current_conversation
        self.save_conversations(conversations)

    def get_current_messages(self):
        if not self.current_conversation:
            self.load_or_create_conversation()
        return self.current_conversation["messages"]

    def clear_current_conversation(self):
        """Clear only the current conversation and start a new one"""
        conversations = self.load_all_conversations()
        if conversations:
            conversations.pop()  # Remove the last conversation
        self.current_conversation = {
            "timestamp": datetime.now().isoformat(),
            "messages": []
        }
        conversations.append(self.current_conversation)
        self.save_conversations(conversations)