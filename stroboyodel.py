import streamlit as st
import numpy as np
import sounddevice as sd

# Set the sampling frequency and duration for each sound
fs = 44100  # 44.1 kHz
duration = 0.1  # in seconds

# Function to generate and play the sound
def play_sound(x):
    # Calculate the sound frequency based on your formula
    sound_frequency = 440 + 220 * np.sin(x**2)

    # Generate a time array
    t = np.linspace(0, duration, int(fs * duration), endpoint=False)

    # Generate the sound wave
    wave = 0.5 * np.sin(2 * np.pi * sound_frequency * t)

    # Play the sound
    sd.play(wave, fs)
    sd.wait()

# Streamlit app
st.title("Sound Synchronization Example")

# Create a button to trigger the sound update
if st.button("Play Sound"):
    x = 0
    play_sound(x)

    # Update the x value for the next iteration
    x += 0.01

    st.text("Sound played!")

# Note: This will play the sound each time the button is clicked.
