import nltk
import random
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# Initialize Lemmatizer
lemmatizer = WordNetLemmatizer()

# Preprocess input text: remove punctuation, lowercase, tokenize, and lemmatize
def preprocess(text):
    # Convert to lowercase
    text = text.lower()
    
    # Remove punctuation
    text = ''.join([char for char in text if char not in string.punctuation])
    
    # Tokenize the text
    words = word_tokenize(text)
    
    # Lemmatize words and remove stopwords
    words = [lemmatizer.lemmatize(word) for word in words if word not in stopwords.words('english')]
    
    return words

# Define a list of responses
responses = {
    "hello": ["Hi there!", "Hello!", "Hey! How can I help you today?"],
    "how are you": ["I'm doing well, thank you for asking!", "I'm just a bot, but I'm great!"],
    "bye": ["Goodbye!", "See you later!", "Have a great day!"],
    "default": ["Sorry, I didn't quite understand that. Can you rephrase?", "Can you please clarify?"]
}

# Match input with responses
def get_response(user_input):
    user_input = preprocess(user_input)
    for key in responses:
        # If any word in the user input matches a keyword
        if any(word in user_input for word in key.split()):
            return random.choice(responses[key])
    
    # If no match found, return default response
    return random.choice(responses["default"])

# Chatbot Function
def chatbot():
    print("Hello! I'm your chatbot. Type 'bye' to exit.")
    
    while True:
        # Get user input
        user_input = input("You: ")
        
        if user_input.lower() == 'bye':
            print("Chatbot: Goodbye!")
            break
        
        # Get chatbot's response
        response = get_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    chatbot()
