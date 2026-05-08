# Experiment 1
# Tokenization, Stemming and Lemmatization

import nltk

from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

# Download required data
nltk.download('punkt')
nltk.download('wordnet')

# Input sentence
text = "I am playing and learning NLP"

# Tokenization
tokens = word_tokenize(text)

print("Tokens:")
print(tokens)

# Stemming
ps = PorterStemmer()

print("\nStemming:")

for word in tokens:
    print(word, "->", ps.stem(word))

# Lemmatization
lemmatizer = WordNetLemmatizer()

print("\nLemmatization:")

for word in tokens:
    print(word, "->", lemmatizer.lemmatize(word))