import nltk
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

nltk.download('punkt')

def lemmatize_text(text):
    # Tokenize the input text
    words = word_tokenize(text)

    # Initialize the WordNet Lemmatizer
    lemmatizer = WordNetLemmatizer()

    # Lemmatize each word in the text
    lemmatized_words = [lemmatizer.lemmatize(word, get_pos(word)) for word in words]

    # Join the lemmatized words back into a string
    lemmatized_text = ' '.join(lemmatized_words)

    return lemmatized_text

def get_pos(word):
    # Map POS tagger output to WordNet POS tagset
    tag = nltk.pos_tag([word])[0][1][0].upper()
    tag_dict = {"N": wordnet.NOUN, "V": wordnet.VERB, "R": wordnet.ADV, "J": wordnet.ADJ}

    return tag_dict.get(tag, wordnet.NOUN)

if __name__ == "__main__":
    # Input text for lemmatization
    input_text = "The cats are running and the mice are squeaking loudly."

    # Perform lemmatization
    lemmatized_result = lemmatize_text(input_text.lower())  # Converting to lowercase for better results

    # Display the original and lemmatized text
    print("Original Text:")
    print(input_text)
    print("\nLemmatized Text:")
    print(lemmatized_result)

