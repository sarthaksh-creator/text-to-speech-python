from gtts import gTTS
import os

# 1. Name of the file you want to read
file_name = "story.txt"

try:
    # 2. Open and read the file
    with open(file_name, "r", encoding="utf-8") as file:
        my_text = file.read()

    if my_text.strip() == "":
        print("The file is empty!")
    else:
        print(f"Reading {file_name}...")
        
        # 3. Convert the text to speech
        tts = gTTS(text=my_text, lang='en')
        
        # 4. Save the output
        output_file = "audiobook.mp3"
        tts.save(output_file)
        
        print(f"Success! Saved to {output_file}")
        
        # Play the file automatically (Windows)
        os.system(f"start {output_file}")

except FileNotFoundError:
    print(f"Error: The file '{file_name}' was not found. Make sure it is in the same folder as this script.")