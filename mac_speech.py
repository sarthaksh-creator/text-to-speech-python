import asyncio
import edge_tts
import os

# -----------------------------
# AVAILABLE VOICES
# -----------------------------
VOICES = {
    "1": ("English US Female", "en-US-AriaNeural"),
    "2": ("English US Male", "en-US-GuyNeural"),
    "3": ("English India Female", "en-IN-NeerjaNeural"),
    "4": ("English India Male", "en-IN-PrabhatNeural"),
}

async def text_to_speech():
    print("\n🎤 TEXT TO SPEECH APPLICATION\n")

    file_name = input("Enter text file name (default: story.txt): ") or "story.txt"

    if not os.path.exists(file_name):
        print("❌ File not found!")
        return

    with open(file_name, "r", encoding="utf-8") as f:
        text = f.read()

    if not text.strip():
        print("❌ Text file is empty!")
        return

    print("\nChoose Voice:")
    for key, value in VOICES.items():
        print(f"{key}. {value[0]}")

    voice_choice = input("Select voice number: ")
    voice = VOICES.get(voice_choice, VOICES["1"])[1]

    rate = input("Enter speed (example: +10%, -20%) [default +0%]: ") or "+0%"
    pitch = input("Enter pitch (example: +5Hz, -2Hz) [default 0Hz]: ") or "0Hz"

    output_file = input("Output audio file (default: output.mp3): ") or "output.mp3"

    print("\n🔊 Generating audio...")
    communicate = edge_tts.Communicate(text, voice, rate=rate, pitch=pitch)
    await communicate.save(output_file)

    print(f"✅ Saved as {output_file}")
    os.system(f"afplay {output_file}")

if __name__ == "__main__":
    asyncio.run(text_to_speech())
