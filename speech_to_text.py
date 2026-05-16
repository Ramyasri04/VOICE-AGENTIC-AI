import speech_recognition as sr

def listen():

    recognizer = sr.Recognizer()

    try:
        with sr.Microphone() as source:

            print("Listening...")

            recognizer.adjust_for_ambient_noise(source, duration=1)

            audio = recognizer.listen(source, timeout=5)

        text = recognizer.recognize_google(audio)

        return text

    except sr.WaitTimeoutError:
        return None

    except sr.UnknownValueError:
        return "Could not understand audio."

    except sr.RequestError:
        return "Speech service unavailable."

    except Exception as e:
        return f"Error: {e}"