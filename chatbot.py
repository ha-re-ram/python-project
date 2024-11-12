def chatbot():
    responses = {
        "hello": "Hi! How can I help you today?",
        "hi": "Hey! What's up?",
        "goodbye": "See you later!",
        "thanks": "You're welcome!",
        "default": "I didn't understand that. Can you please rephrase?"
    }

    while True:
        user_input = input("You: ").lower()
        response = responses.get(user_input, responses["default"])
        print("Chatbot:", response)

chatbot()