import speech_recognition as sr
import pyttsx3
import os
from openai import OpenAI

# Generate a secret key and set up as environment variable
client = OpenAI(
    api_key = os.environ.get("CHATGPT_API_KEY")
)

# Initialize speech recognizer
recog = sr.Recognizer()

def voice2AI():
    # Use microphone as a source for audio input 
    with sr.Microphone() as source:
        # Improves recognition accuracy by adjusting for ambient noise
        recog.adjust_for_ambient_noise(source, duration=0.1)
        # Will wait ~5secs for the question to be asked
        text2Voice("Ask me a question")
        audioText = recog.listen(source)
        audioText = recog.recognize_google(audioText)
        audioText = audioText.lower()
        # Use GPT-3.5 Turbo model to generate responses
        chat_completion = client.chat.completions.create(
            messages=[
            {
                "role": "user",
                "content": audioText,
            }
            ],
            model="gpt-3.5-turbo",
            stream=True
                )
        
        text2Voice("Time over, thanks")
        
        try:
            text2Voice("Here is what I found")
            generatedContent = ''
            for chunk in chat_completion:
                if chunk.choices[0].delta.content is not None:
                    generatedContent += chunk.choices[0].delta.content
                    print(chunk.choices[0].delta.content, end="")
                    
            text2Voice(generatedContent)
            
        except:
            text2Voice("Sorry, I did not get that")
            voice2AI()

def text2Voice(command):
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()
  
voice2AI()