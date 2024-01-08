from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QTextEdit, QMainWindow
from PyQt5.QtCore import Qt
import speech_recognition as sr
import pyttsx3
import os
from openai import OpenAI


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.centralWidget = QWidget() 
        self.setCentralWidget(self.centralWidget)
        self.setWindowTitle("Voice2AI")
        self.layout = QVBoxLayout(self.centralWidget)
        
        self.resultLabel = QLabel("Test")
        self.layout.addWidget(self.resultLabel)
        
        self.recordButton = QPushButton("Record")
        self.layout.addWidget(self.recordButton)
        self.recordButton.clicked.connect(self.voice2AI)
        
        self.recog = sr.Recognizer()
        
        self.client = OpenAI(
            api_key = os.environ.get("CHATGPT_API_KEY")
        )
        
    def voice2AI(self):
        self.resultLabel.clear()
        with sr.Microphone() as source:
            self.recog.adjust_for_ambient_noise(source, duration=0.1)
            # Will wait ~5secs for the question to be asked
            self.text2Voice("Ask me a question")
            audioText = self.recog.listen(source)
            audioText = self.recog.recognize_google(audioText)
            audioText = audioText.lower()
            
            chat_completion = self.client.chat.completions.create(
                messages=[
                {
                    "role": "user",
                    "content": audioText,
                }
                ],
                model="gpt-3.5-turbo",
                stream=True
                    )
            try:
                generatedContent = ''
                for chunk in chat_completion:
                    if chunk.choices[0].delta.content is not None:
                        generatedContent += chunk.choices[0].delta.content
                        current_text = self.resultLabel.text()
                        updatedText = current_text + ' ' + generatedContent
                self.resultLabel.setText(updatedText)
            except:
                self.resultLabel.setText("Try Again")
                
    def text2Voice(self, command):
        engine = pyttsx3.init()
        engine.say(command)
        engine.runAndWait()
        
                    
app = QApplication([])
window = MainWindow()
window.show()
# Uncomment to make window transparent
# window.setWindowOpacity(0.1) 
app.exec()

