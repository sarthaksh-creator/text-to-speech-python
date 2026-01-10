import pyttsx3

# Initialize the engine
engine = pyttsx3.init()

# Optional: Change voice properties
# Get available voices
voices = engine.getProperty('voices')
# Set to a different voice (0 is usually male, 1 is usually female)
engine.setProperty('voice', voices[1].id) 

# Set speaking rate (speed)
engine.setProperty('rate', 150) 

# Text to speak
# This lets you type what you want the AI to say in the terminal
my_text = input("What should I say? ")
# Speak the text immediately
engine.say(my_text)

# Save to a file
engine.save_to_file(my_text, 'offline_voice.mp3')

# Run and wait
engine.runAndWait()

print("Done!")
