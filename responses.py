import random
import datetime


def get_response(user_input):

    greetings = ["hi", "hello", "hey", "good morning", "good evening"]

    if user_input in greetings:
        return random.choice([
            "Hello! 👋",
            "Hi there 😊",
            "Hey! How can I help you?"
        ])

    elif "how are you" in user_input:
        return "I'm doing great! Thanks for asking 😊"

    elif "your name" in user_input:
        return "My name is DecodeBot 🤖"

    elif "time" in user_input:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        return f"The current time is {current_time}"

    elif "date" in user_input:
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")
        return f"Today's date is {current_date}"

    elif "help" in user_input:
        return """
You can try:
- hi
- how are you
- what is your name
- date
- time
- joke
- bye
"""

    elif "joke" in user_input:
        jokes = [
            "Why do programmers hate bugs? Because they take too long to debug 😂",
            "Why was the computer cold? Because it forgot to close windows 😂",
            "AI is great until the WiFi disconnects 😅"
        ]

        return random.choice(jokes)

    elif "ai" in user_input:
        return "Artificial Intelligence is the simulation of human intelligence using machines."

    elif "python" in user_input:
        return "Python is one of the most popular programming languages for AI development."

    elif "weather" in user_input:
        return "I cannot check live weather yet 🌦"

    elif "who made you" in user_input:
        return "I was created by a DecodeLabs AI intern 🚀"

    else:
        return "Sorry, I don't understand that yet 😅"