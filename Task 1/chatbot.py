import re

def chatbot_response(user_input):
    user_input = user_input.lower()

    # Greeting
    if re.search(r'\bhello\b|\bhi\b|\bhey\b|\bgreetings\b', user_input):
        return "Hello! How can I assist you today?"

    # Inquiry about bot's status
    elif re.search(r'how are you|how\'s it going', user_input):
        return "I'm doing well, thank you! How about you?"

    # Asking for help
    elif re.search(r'can you help me|i need help|assist me', user_input):
        return "Of course! I'm here to help. What do you need assistance with?"

    # Asking about time
    elif re.search(r'what time is it|tell me the time|current time', user_input):
        from datetime import datetime
        current_time = datetime.now().strftime("%H:%M:%S")
        return f"The current time is {current_time}."

    # Asking about date
    elif re.search(r'what is the date today|tell me the date|current date', user_input):
        from datetime import datetime
        current_date = datetime.now().strftime("%Y-%m-%d")
        return f"Today's date is {current_date}."

    # Farewell
    elif re.search(r'\bbye\b|\bexit\b|\bsee you\b|\blater\b', user_input):
        return "Goodbye! Have a wonderful day ahead!"

    # Asking about weather
    elif re.search(r'what\'s the weather like|current weather|weather today', user_input):
        return "I'm not equipped to check the weather, but you can use your favorite weather app for that!"

    # Asking for a joke
    elif re.search(r'tell me a joke|make me laugh|joke', user_input):
        return "Why don't scientists trust atoms? Because they make up everything!"

    # Asking about the chatbot
    elif re.search(r'what can you do|who are you|what are you', user_input):
        return "I'm a simple rule-based chatbot designed to assist with basic queries. How can I help you today?"

    # Default fallback response
    else:
        return "I'm sorry, I didn't quite understand that. Could you please rephrase your question?"

def run_chatbot():
    print("Chatbot: Hello! I'm your friendly chatbot. Type 'exit' to end the conversation.")

    while True:
        user_input = input("You: ")
        response = chatbot_response(user_input)
        print("Chatbot:", response,"\n")

        if re.search(r'\bbye\b|\bexit\b', user_input):
            break


print("\n\t\t\t\tChatBot")
run_chatbot()
