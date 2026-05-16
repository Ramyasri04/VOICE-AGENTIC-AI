from modules.speech_to_text import listen
from modules.regex_processor import extract_patterns
from modules.intent_router import detect_intent
from modules.ai_engine import ask_ai
from modules.csv_handler import save_conversation
from modules.text_to_speech import speak
from modules.task_manager import add_task, get_tasks
from modules.note_manager import save_note

def process_intent(intent, text):

    if intent == "GREETING":
        return "Hello! How can I help you today?"

    elif intent == "ADD_TASK":
        add_task(text)
        return "Task added successfully."

    elif intent == "SHOW_TASKS":
        tasks = get_tasks()

        if not tasks:
            return "No tasks available."

        return f"Your tasks are: {tasks}"

    elif intent == "SAVE_NOTE":
        save_note(text)
        return "Note saved successfully."

    elif intent == "SUMMARIZE":
        prompt = f"Summarize this text:\n{text}"
        return ask_ai(prompt)

    else:
        return ask_ai(text)

def main():

    print("\n=== Voice Agentic AI Assistant ===\n")

    user_text = listen()

    if not user_text:
        print("No voice detected.")
        return

    print("User:", user_text)

    extracted = extract_patterns(user_text)

    print("\nExtracted Patterns:")
    print(extracted)

    intent = detect_intent(user_text)

    print("\nDetected Intent:", intent)

    response = process_intent(intent, user_text)

    print("\nAI Response:", response)

    save_conversation(user_text, response, intent)

    speak(response)

if __name__ == "__main__":
    main()
