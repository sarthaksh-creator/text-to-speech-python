import asyncio
import edge_tts
import os

# 1. Configuration
FILE_NAME = "story.txt"
OUTPUT_FILE = "audiobook.mp3"

# VOICE SELECTION
# 'en-US-AriaNeural' (Female) or 'en-US-GuyNeural' (Male)
# 'en-IN-NeerjaNeural' (Indian Female) or 'en-IN-PrabhatNeural' (Indian Male)
VOICE = "en-US-AriaNeural"

# 2. Adjust Speed and Pitch here
# Speed: +50% is fast, -20% is slow
RATE = "+10%"    
# Pitch: +5Hz is higher voice, -5Hz is deeper voice
PITCH = "-2Hz"   

async def text_to_speech():
    # Check if text file exists
    if not os.path.exists(FILE_NAME):
        print(f"Error: {FILE_NAME} not found!")
        return

    with open(FILE_NAME, "r", encoding="utf-8") as file:
        text = file.read()

    if not text.strip():
        print("The file is empty!")
        return

    print(f"Reading {FILE_NAME} on Mac...")
    print(f"Settings -> Voice: {VOICE}, Speed: {RATE}, Pitch: {PITCH}")

    # Communicate with the edge-tts engine
    communicate = edge_tts.Communicate(text, VOICE, rate=RATE, pitch=PITCH)

    # Save the output
    await communicate.save(OUTPUT_FILE)
    
    print(f"Success! Saved to {OUTPUT_FILE}")
    
    # PLAY AUDIO ON MAC
    # We use 'afplay' which is the native Mac audio player
    print("Playing audio...")
    os.system(f"afplay {OUTPUT_FILE}")

if __name__ == "__main__":
    asyncio.run(text_to_speech())