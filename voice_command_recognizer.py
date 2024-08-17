
import speech_recognition as sr

def listen_and_recognize():
    recognizer = sr.Recognizer()
    recognizer.energy_threshold = 4000

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio_data = recognizer.listen(source)

        try:
            text = recognizer.recognize_sphinx(audio_data)
            print("You said: {}".format(text))
            return text
        except sr.UnknownValueError:
            print("Sphinx could not understand audio")
        except sr.RequestError as e:
            print("Sphinx error; {0}".format(e))

def main():
    while True:
        command = listen_and_recognize()
        if command:
            command = command.lower()
            if 'exit' in command or 'stop' in command:
                print("Exiting program.")
                break
            elif 'hello' in command:
                print("Hello! How can I help you?")
            # You can add more commands here

if __name__ == '__main__':
    main()
