import nltk
from nltk.chat.util import Chat, reflections

# Download the punkt tokenizer if not already downloaded
nltk.download('punkt')

# Define the pairs of patterns and responses
pairs = [
    [
        r"hi|hello|hey",
        ["Hello!", "Hi there!", "Hey!"]
    ],
    [
        r"how are you|how are you doing",
        ["I'm doing well, thank you!", "I'm fine, thanks for asking."]
    ],
    [
        r"what is your name",
        ["I am a simple chatbot.", "You can call me Chatbot."]
    ],
    [
        r"quit|bye|goodbye",
        ["Goodbye!", "It was nice chatting with you. Have a great day!"]
    ],
    [
        r"(.*)",
        ["I'm sorry, I didn't understand that.", "Can you please rephrase that?"]
    ]
]

# Create a chatbot with the defined pairs
chatbot = Chat(pairs, reflections)

def simple_chatbot():
    print("Hello! I'm a simple chatbot. Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print("Chatbot: Goodbye!")
            break
        response = chatbot.respond(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    simple_chatbot()

