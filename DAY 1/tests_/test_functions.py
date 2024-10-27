from termcolor import colored
from core.conversation import ConversationHandler
from core.assistant import JarvisAssistant

def run_all_tests():
    assistant = JarvisAssistant()
    conversation_handler = ConversationHandler(assistant)

    test_queries = [
        ("File Operations Test", "List all files in the current directory"),
        ("File Write Test", "Create a file named test.txt with content 'Hello World'"),
        ("System Information Test", "Show me the current memory usage"),
        ("Disk Information Test", "What's my disk space usage?"),
        ("Process Management Test", "Show me the list of running processes"),
        ("Weather Information Test", "What's the weather like in London?"),
        ("Currency Conversion Test", "Convert 100 USD to EUR"),
        ("Notes Management Test", "Create a note titled 'reminder' with content 'Buy groceries'"),
        ("Notes List Test", "List all my notes"),
        ("Multiple Operations Test", "Show me the weather in London and create a note about it"),
        ("Complex Query Test", "Check system memory usage and if it's above 80%, create a warning note about it")
    ]

    for test_name, prompt in test_queries:
        print(colored(f"\n=== {test_name} ===", "white", attrs=['bold']))
        conversation_handler.handle_conversation(prompt)