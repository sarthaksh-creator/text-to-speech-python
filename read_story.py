import pyttsx3
import os

# 1. Configuration
file_name = "story.txt"
output_file = "audiobook.mp3"

# SETTINGS: Adjust these to change the output
SPEED = 150   # 200 is normal, 100 is slow, 300 is fast
VOLUME = 1.0  # 0.0 to 1.0
VOICE_ID = 1  # 0 for Male, 1 for Female (usually)

def text_to_speech():
    # Initialize the engine
    engine = pyttsx3.init()

    # --- ADJUST PROPERTIES ---
    
    # 1. Set Speed (Rate)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', SPEED) 

    # 2. Set Volume
    engine.setProperty('volume', VOLUME)

    # 3. Set Voice (This affects Pitch/Tone)
    # Voices are OS dependent. Usually 0 is Male, 1 is Female.
    voices = engine.getProperty('voices')
    # Use try/except to prevent errors if index is out of range
    try:
        engine.setProperty('voice', voices[VOICE_ID].id)
    except IndexError:
        engine.setProperty('voice', voices[0].id)
        print("Selected voice ID not found, defaulting to 0.")

    # --- READ AND SAVE ---
    
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            my_text = file.read()

        if my_text.strip() == "":
            print("The file is empty!")
            return

        print(f"Reading {file_name}...")
        print(f"Settings -> Speed: {SPEED}, Voice Index: {VOICE_ID}")
        
        # Save to file
        engine.save_to_file(my_text, output_file)
        
        # Run the engine
        engine.runAndWait()
        
        print(f"Success! Saved to {output_file}")
        
        # Play automatically (Windows)
        os.system(f"start {output_file}")

    except FileNotFoundError:
        print(f"Error: '{file_name}' not found.")

if __name__ == "__main__":
    text_to_speech()