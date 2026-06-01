with open("chat_history.txt", "a") as file:
    file.write(f"You: {user_input}\n")
    file.write(f"Bot: {response}\n")