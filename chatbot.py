from responses import get_response
import datetime

print("=" * 50)
print("🤖 Welcome to DecodeBot AI Chatbot")
print("Type 'bye' to exit")
print("=" * 50)

while True:

    # Get user input
    user_input = input("\nYou: ").lower().strip()

    # Exit condition
    if user_input in ["bye", "exit", "quit"]:
        print("Bot: Goodbye! Have a nice day 😊")
        break

    # Get chatbot response
    response = get_response(user_input)

    # Print response
    print("Bot:", response)