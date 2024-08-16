import nltk
from nltk.chat.util import Chat, reflections

# Define a more extensive set of patterns and responses
patterns_responses = [
    (r'hi|hello|hey', ['Hello!', 'Hi there!', 'Hey! How can I assist you today?']),
    (r'how are you\??', ['I am doing well, thank you for asking!', 'I’m good! How about you?']),
    (r'what is your name\??', ['I’m a chatbot created by OpenAI.', 'You can call me Chatbot.']),
    (r'what can you do\??', ['I can chat with you, answer questions, and have a conversation.', 'I can help with various questions and have a friendly chat.']),
    (r'how is the weather\??', ['I don’t have access to real-time data, but you can check a weather website or app for updates.', 'I recommend checking a weather app for the latest updates.']),
    (r'what is your favorite color\??', ['I don’t have personal preferences, but I like all colors!', 'I don’t have a favorite, but I think all colors are beautiful.']),
    (r'tell me a joke\??', ['Why don’t scientists trust atoms? Because they make up everything!', 'What do you call fake spaghetti? An impasta!']),
    (r'bye|goodbye|see you', ['Goodbye! Have a great day!', 'See you later!']),
    (r'help', ['I’m here to help! You can ask me questions or talk about various topics.', 'How can I assist you today?']),
    (r'(.*)', ['I’m not sure how to respond to that. Can you ask something else?', 'I’m still learning. Can you tell me more?'])
]

# Create a Chat instance with patterns and responses
chatbot = Chat(patterns_responses, reflections)

# Function to start the chatbot conversation
def start_chat():
    print("Hi! I am a chatbot. Type 'quit' to end the chat.")
    while True:
        user_input = input("You: ")
        response = chatbot.respond(user_input)
        if response:
            print("Chatbot:", response)
        if user_input.lower() in ['quit', 'bye', 'goodbye', 'see you']:
            break

# Start the chatbot
if __name__ == "__main__":
    start_chat()