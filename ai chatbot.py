import nltk
nltk.download('punkt')
nltk.download('wordnet')
import nltk
from nltk.chat.util import Chat, reflections

# Define patterns and responses
pairs = [
    [
        r"hi|hello|hey",
        ["Hello!", "Hi there!", "Hey! How can I help you?"]
    ],
    [
        r"what is your name?",
        ["I'm an AI chatbot created using NLTK.", "They call me ChatBot."]
    ],
    [
        r"how are you ?",
        ["I'm doing well, thanks!", "All good! How about you?"]
    ],
    [
        r"sorry (.*)",
        ["No problem", "Don't worry about it", "It's okay"]
    ],
    [
        r"quit",
        ["Bye, have a great day!", "Goodbye!"]
    ],
    [
        r"(.*)",
        ["I'm not sure I understand. Can you rephrase?", "Tell me more."]
    ]
]

# Initialize chatbot
chatbot = Chat(pairs, reflections)

# Start conversation
print("🤖 Chatbot: Hello! Type 'quit' to exit.")
chatbot.converse()
