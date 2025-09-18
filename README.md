# Alexa
I built a simple Alexa voice assistant. It listens to commands and can open YouTube or perform Google searches by converting speech to text and executing actions automatically.
# Simple Alexa Voice Assistant

## Description
This is a simple voice-controlled assistant inspired by Alexa. It can perform basic tasks such as:  
- Playing songs on YouTube  
- Telling the current time  
- Searching Wikipedia for information  
- Telling jokes  

The assistant listens to voice commands, processes them using speech recognition, and responds using text-to-speech.  

## Features
- **Speech Recognition**: Listens to user commands.  
- **Text-to-Speech**: Responds to commands using pyttsx3.  
- **YouTube Access**: Plays songs directly on YouTube using pywhatkit.  
- **Wikipedia Search**: Provides short summaries.  
- **Jokes**: Tells one-line jokes using pyjokes.  

## Installation
1. Clone this repository or download the code.
2. Install the required libraries:
   ```bash
   pip install SpeechRecognition pyttsx3 pywhatkit wikipedia pyjokes
