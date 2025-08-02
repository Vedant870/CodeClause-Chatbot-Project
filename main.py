import nltk
import re
import random

# Download NLTK data once
# nltk.download('punkt')

greetings = ['hi', 'hello', 'hey', 'greetings']
responses = ['Hello there!', 'Hi!', 'Hey!', 'Nice to meet you!']

def bot_response(user_input):
    user_input = user_input.lower()

    # Greeting response
    for word in greetings:
        if re.search(r'\b' + word + r'\b', user_input):
            return random.choice(responses)

    # Custom Q&A pattern
    if re.search(r'how are you', user_input):
        return "I'm just a bot, but I'm doing great! 😊"

    elif re.search(r'what is your name', user_input):
        return "I'm a rule-based chatbot made using Python and NLTK!"

    elif re.search(r'bye', user_input):
        return "Goodbye! Have a great day!"

    else:
        return "Sorry, I didn't understand that. Can you rephrase?"

# Run chatbot in terminal
print("Bot: Hello! Type something to start chatting. Type 'bye' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'bye':
        print("Bot:", bot_response(user_input))
        break
    print("Bot:", bot_response(user_input))
