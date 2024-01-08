# Voice2AI

Voice2AI is a Python script that utilizes speech recognition and the OpenAI GPT-3.5 Turbo model to convert spoken questions into text, generate responses, and vocalize the answers. It integrates the SpeechRecognition library for audio input, pyttsx3 for text-to-speech synthesis, and the OpenAI API for natural language understanding.


## Features

- Utilizes the SpeechRecognition library to capture spoken input from a microphone.
- Employs pyttsx3 for converting text responses into audible speech.
- Interacts with the OpenAI GPT-3.5 Turbo model to generate context-aware responses.
- Handles user questions, processes them with the GPT-3.5 Turbo model, and outputs synthesized answers.
- Includes a user-friendly interface using PyQT5

## Usage

1. Set up the OpenAI API key as an environment variable named "CHATGPT_API_KEY".
2. Run the script/GUI to initiate the voice-to-text and text-to-speech interaction.
3. Ask a question when prompted, and the script will provide a GPT-3.5 Turbo model-generated response.

Feel free to explore and enhance the capabilities of Voice2AI for various voice-driven applications and interactions.

## TODO
- Update label as content is being generated as opposed to updating when content has been generated (Threading?)
- Make GUI "prettier"

## Requirements

- Python 3.x
- SpeechRecognition library
- pyttsx3 library
- OpenAI GPT-3.5 Turbo API key

## Disclaimer

Ensure you have the necessary permissions and adhere to OpenAI's usage policies when using their API.
