import speech_recognition as srec
import pyttsx3 as pyt
import os
from time import sleep
from gtts import gTTS

engine = pyt.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)


def speak(text):
    print("Start Text to Speech Model")
    engine.setProperty("rate", 150)
    engine.setProperty("voice", "id/female")
    engine.say(run_model)
    engine.runAndWait()


def text_to_speech(text, CONFIG_DATA, lang="id"):
    tts = gTTS(text=text, lang=lang, slow=False)
    tts.save(CONFIG_DATA["speech_result"])


def greeting(CONFIG_DATA):
    speech_opening = CONFIG_DATA["opening"]
    os.system(f"start {speech_opening}")
    print("Silahkan katakan apapun.")
    sleep(3)


def start_speech(CONFIG_DATA):
    while True:
        greeting(CONFIG_DATA)
        hearing = srec.Recognizer()
        with srec.Microphone() as source:
            print("Hearing....")
            sounds = hearing.listen(source, phrase_time_limit=5)
            try:
                print("Afirmated...")
                hear = hearing.recognize_google(sounds, language="id-ID")
                print(hear)
                return hear

            except srec.UnknownValueError:
                print("Google Speech Recognition could not understand audio.")
            except srec.RequestError as e:
                print(
                    f"Could not request results from Google Speech Recognition service; {e}"
                )

            print("Error detected. Retrying...")
            sleep(2)


def speech_file(file):
    recognizer = srec.Recognizer()

    with srec.AudioFile(file.file) as source:
        audio_text = recognizer.record(source)

    try:
        text = recognizer.recognize_google(audio_text, language="id-ID")
        return text
    except srec.UnknownValueError:
        return {"error": "Could not understand the audio"}
    except srec.RequestError as e:
        return {"error": f"Error with the speech recognition service; {e}"}


def run_model(CONFIG_DATA):
    try:
        services = start_speech(CONFIG_DATA)
        if "keluar" in services or "tutup" in services:
            exiting = CONFIG_DATA["exit"]
            os.system(f"start {exiting}")
            print("Sampai jumpa lagi, terimakasih..")
            sleep(4)
            exit()

        else:
            return services

    except Exception as e:
        return f"Error in Speech Recognition: {e}"
