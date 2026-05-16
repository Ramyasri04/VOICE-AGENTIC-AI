def detect_intent(text):

    text = text.lower()

    if "hello" in text or "hi" in text:
        return "GREETING"

    elif "add task" in text:
        return "ADD_TASK"

    elif "show tasks" in text:
        return "SHOW_TASKS"

    elif "save note" in text:
        return "SAVE_NOTE"

    elif "summarize" in text:
        return "SUMMARIZE"

    else:
        return "GENERAL_AI"
