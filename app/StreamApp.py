import streamlit as st
import speech_recognition as sr

def recognize_speech_from_mic():
    # Initialize recognizer
    recognizer = sr.Recognizer()

    # Set up the microphone
    with sr.Microphone() as source:
        st.info("Please speak into the microphone")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        audio = recognizer.listen(source)  # Listen for the first phrase

    try:
        # Recognize speech using Google's speech recognition
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        return "Sorry, I couldn't understand the audio"
    except sr.RequestError:
        return "Sorry, there was an issue with the speech recognition service"

def main():
    st.title("Speech to Text App")
    st.write("This app will convert your speech to text.")
    
    if st.button("Start Listening"):
        text = recognize_speech_from_mic()
        st.write("You said: ", text)

if __name__ == "__main__":
    main()
