# VOICE-AGENTIC-AI
# 🎙️ Voice Agentic AI Assistant

An intelligent Voice-based Agentic AI Assistant built using Python that can:

- Accept voice input from users
- Convert speech to text
- Process text using RegEx and intent detection
- Generate AI responses using Gemini/Ollama
- Convert AI response back to speech
- Store conversations in CSV files
- Perform basic agentic actions like task handling, note saving, summarization, etc.

---

# 🚀 Features

## ✅ Voice-to-Text
- Captures user voice using microphone
- Converts speech into text

## ✅ RegEx & Pattern Matching
Extracts:
- Email IDs
- Phone Numbers
- Dates
- Greetings
- Commands
- Keywords

## ✅ Agentic Workflow
Routes requests based on detected intent:
- Save Notes
- Show Tasks
- Summarize Text
- General AI Chat

## ✅ GenAI Integration
Supports:
- Gemini AI
- Ollama + Mistral/Llama

## ✅ Text-to-Speech
AI response converted into voice.

## ✅ CSV Storage
Stores:
- User transcript
- AI response
- Timestamp
- Intent

---

# 🏗️ Project Architecture

```text
Voice Input
     ↓
Speech-to-Text
     ↓
Regex & Intent Detection
     ↓
Agent Router
     ↓
AI/Conditional Action
     ↓
CSV Logging
     ↓
Text-to-Speech
```

---

# 📂 Project Structure

```text
voice-agentic-ai/
│
├── app.py
├── requirements.txt
├── README.md
│
├── modules/
│   ├── speech_to_text.py
│   ├── text_to_speech.py
│   ├── regex_processor.py
│   ├── intent_router.py
│   ├── ai_engine.py
│   ├── csv_handler.py
│   ├── task_manager.py
│   └── note_manager.py
│
├── data/
│   ├── conversations.csv
│   ├── tasks.csv
│   └── notes.csv
```

---

# ⚙️ Installation Steps

## 1️⃣ Clone Repository

```bash
git clone <your-github-link>
cd voice-agentic-ai
```

---

## 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 3️⃣ Install Ollama (Recommended)

Download:
https://ollama.com/

Run:

```bash
ollama run mistral
```

---

## 4️⃣ Run Application

```bash
python app.py
```

---

# 📦 Requirements

```text
speechrecognition
pyttsx3
pandas
requests
pyaudio
streamlit
google-generativeai
openpyxl
```

---

# 🧠 Supported Intents

| Intent | Example |
|---|---|
| Greeting | Hello |
| Save Note | Save note Python basics |
| Add Task | Add task submit report |
| Show Tasks | Show tasks |
| Summarize | Summarize this message |
| General AI | Explain REST APIs |

---

# 🧪 Sample Inputs

## Example 1

Input:
```text
My email is abc@gmail.com
```

Output:
```text
Email Extracted Successfully
```

---

## Example 2

Input:
```text
Add task complete AI project tomorrow
```

Output:
```text
Task Added Successfully
```

---

## Example 3

Input:
```text
Explain Python decorators
```

Output:
```text
AI-generated explanation
```

---

# 📊 CSV Storage Example

| Timestamp | User Text | AI Response | Intent |
|---|---|---|---|
| 2026-05-16 | Hello | Hi User | GREETING |

---

# 🛡️ Error Handling

The application handles:

- Empty voice input
- Microphone failure
- API failure
- Invalid patterns
- CSV file absence
- Network issues
- Unsupported commands

---

# 🔮 Future Enhancements

- Multi-language support
- Emotion detection
- WhatsApp integration
- Email automation
- Cloud deployment
- Database integration

---

# 🎯 Evaluation Criteria Covered

| Area | Status |
|---|---|
| Python Programming | ✅ |
| RegEx & Pattern Matching | ✅ |
| Voice-to-Text | ✅ |
| Text-to-Voice | ✅ |
| GenAI Integration | ✅ |
| CSV Handling | ✅ |
| Agentic Workflow | ✅ |
| Error Handling | ✅ |
| Documentation | ✅ |

---

# 👨‍💻 Developed For

Mphasis Hack Culture Hackathon

---

# 📹 Demo

Include:
- Project screenshots
- Terminal execution
- Voice interaction demo video

---

# 🙌 Thank You
