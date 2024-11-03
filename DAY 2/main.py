from core.assistant import JarvisAssistant
from core.conversation import ConversationHandler
from termcolor import colored

class Jarvis:
    def __init__(self):
        print("Initializing Jarvis Assistant...")
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
                user_input = input(colored("\nYou: ", "green")).strip()
                if user_input.lower() == 'exit':
                    print(colored("Goodbye!", "yellow"))
                    break
                elif user_input.lower() == 'clear':
                    self.assistant.clear_history()
                    print(colored("Started new conversation (previous conversations preserved).", "yellow"))
                    continue
                elif user_input.lower() == 'new':
                    self.assistant._history_manager.save_conversations([])
                    self.assistant._history_manager.load_or_create_conversation()
                    print(colored("All conversation history cleared.", "yellow"))
                    continue
                if user_input:
                    response = self.process_command(user_input)
                    print(colored(f"\nJarvis: {response}", "cyan"))
            except KeyboardInterrupt:
                print(colored("\nGoodbye!", "yellow"))
                break
            except Exception as e:
                print(colored(f"\nError: {str(e)}", "red"))

    def process_command(self, command: str):
        return self.conversation_handler.handle_conversation(command)

if __name__ == "__main__":
    jarvis = Jarvis()
    jarvis.start()