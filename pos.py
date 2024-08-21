import spacy

# Load the 'en_core_web_sm' model
nlp = spacy.load('en_core_web_sm')

# Define a sentence
sentence = "I am learning NLP in Python"

# Process the sentence using spaCy's NLP pipeline
doc = nlp(sentence)

# Iterate through the token and print the token text and POS tag
for token in doc:
    print(token.text, token.pos_)