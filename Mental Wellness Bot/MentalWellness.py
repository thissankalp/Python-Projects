import os
from dotenv import load_dotenv
import google.generativeai as genai
from datetime import datetime

# Load environment variables
load_dotenv()
API_KEY = os.getenv("API_KEY")  # Or GOOGLE_API_KEY
genai.configure(api_key=API_KEY)

# Define the model with safety + persona
model = genai.GenerativeModel(
    "gemini-2.0-flash",
    system_instruction=(
        "You are a supportive and empathetic mental wellness assistant. "
        "You listen carefully, respond kindly, and offer helpful strategies "
        "like mindfulness, journaling, breathing exercises, and positive self-talk. "
        "You are not a medical professional. If the user expresses severe distress "
        "or mentions self-harm, gently encourage them to reach out to a trusted "
        "person or a professional helpline."
    )
)

chat = model.start_chat()

# File to store mood logs
MOOD_LOG_FILE = "mood_log.txt"

def log_mood(user_input, response_text):
    """Save mood entry to a text file with timestamp."""
    with open(MOOD_LOG_FILE, "a", encoding="utf-8") as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"[{timestamp}]\n")
        file.write(f"User: {user_input}\n")
        file.write(f"Companion: {response_text}\n")
        file.write("-" * 100 + "\n")

print(f"-" * 40)
print("🌱 Welcome to your Wellness Chat. Type 'exit' anytime to quit.")

try:
    while True:
        print(f"-" * 100)
        user_input = input("|You|: ")
        print(f"-" * 100)
        if user_input.lower() == "exit":
            print("🌸 Take care of yourself. Goodbye!")
            break

        try:
            # Send user message to Gemini
            response = chat.send_message(user_input)
            response_text = response.text.strip()

        except Exception as e:
            # If API error or internet issue
            response_text = "🌼 I'm having trouble connecting right now. Let's try again in a moment."

        # Show Gemini's reply
        print("|Companion|:", response_text)

        # Save to mood log
        log_mood(user_input, response_text)

except KeyboardInterrupt:
    print("\n🌸 Take care of yourself. Goodbye!")