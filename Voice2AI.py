import speech_recognition as sr
import pyttsx3
import os
from openai import OpenAI

# Generate a secret key and set up as environment variable
client = OpenAI(
    api_key = os.environ.get("CHATGPT_API_KEY")
)


recog = sr.Recognizer()

def voice2AI():
    with sr.Microphone() as source:
        recog.adjust_for_ambient_noise(source, duration=0.1)
        # Will wait ~5secs for the question to be asked
        text2Voice("Ask me a question")
        audioText = recog.listen(source)
        audioText = recog.recognize_google(audioText)
        audioText = audioText.lower()
        chat_completion = client.chat.completions.create(
            messages=[
            {
                "role": "user",
                "content": audioText,
            }
            ],
            model="gpt-3.5-turbo",
                )
        text2Voice("Time over, thanks")
        try:
            text2Voice("Here is what I found")
            # Request takes ~20secs to generate
            print(chat_completion.choices[0].message.content)
            text2Voice(chat_completion.choices[0].message.content)
        except:
            text2Voice("Sorry, I did not get that")

def text2Voice(command):
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()
    
voice2AI()