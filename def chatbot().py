def chatbot():
    print("🤖 ChatBot: Hello! I am a simple chatbot.")
    print("Type 'bye' to end the chat.\n")

    while True:
        user = input("You: ").lower()

        if user == "hello":
            print("🤖 ChatBot: Hi! Nice to meet you.")

        elif user == "how are you":
            print("🤖 ChatBot: I'm fine, thanks! How about you?")

        elif user == "i am fine":
            print("🤖 ChatBot: That's great to hear!")

        elif user == "what is your name":
            print("🤖 ChatBot: My name is SimpleBot.")

        elif user == "who created you":
            print("🤖 ChatBot: I was created using Python.")

        elif user == "thank you":
            print("🤖 ChatBot: You're welcome!")

        elif user == "bye":
            print("🤖 ChatBot: Goodbye! Have a great day!")
            break

        else:
            print("🤖 ChatBot: Sorry, I don't understand that.")

# Run the chatbot
chatbot()