

print("=== DecodeLabs Chatbot ===")
print("Type 'bye' to exit.")

while True:
    user_input = input("You: ").lower()

    if user_input == "hello" or user_input == "hi":
        print("Bot: Hello! How can I help you?")

    elif user_input == "how are you":
        print("Bot: I'm doing great. Thanks for asking!")

    elif user_input == "what is your name":
        print("Bot: I am a Rule-Based Chatbot.")

    elif user_input == "help":
        print("Bot: You can greet me, ask my name, or ask how I am.")

    elif user_input == "bye" or user_input == "exit":
        print("Bot: Goodbye! Have a nice day.")
        break

    else:
        print("Bot: Sorry, I don't understand that.")