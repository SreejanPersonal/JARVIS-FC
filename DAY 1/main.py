from core.assistant import JarvisAssistant
from core.conversation import ConversationHandler

class Jarvis:
    def __init__(self):
        print("Initializing Jarvis...")
        self.assistant = JarvisAssistant()
        self.conversation_handler = ConversationHandler(self.assistant)

    def start(self):
        self.run_interactive_mode()

    def run_interactive_mode(self):
        print("\nJarvis is ready! Commands available:")
        print("- 'exit' to quit")
        print("- 'clear' to start a new conversation (preserves history)")
        print("- 'new' to start fresh (clears all history)")
        
        while True:
            try:
                user_input = input("\nYou: ").strip()
                if user_input.lower() == 'exit':
                    print("Goodbye!")
                    break
                elif user_input.lower() == 'clear':
                    self.assistant.clear_history()
                    print("Started new conversation (previous conversations preserved).")
                    continue
                elif user_input.lower() == 'new':
                    self.assistant._history_manager.save_conversations([])
                    self.assistant._history_manager.load_or_create_conversation()
                    print("All conversation history cleared.")
                    continue
                if user_input:
                    response = self.process_command(user_input)
                    print("\nJarvis:", response)
            except Exception as e:
                print(f"An error occurred: {str(e)}")

    def process_command(self, command: str):
        return self.conversation_handler.handle_conversation(command)

if __name__ == "__main__":
    jarvis = Jarvis()
    jarvis.start()