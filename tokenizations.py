from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

example_sent = "i am Vipul Bhoir. i am from the city of dreams that is Mumbai. i am currently persuing computer engineering at prestigious college that is VCET."


stop_words = set(stopwords.words('english'))

word_tokens = word_tokenize(example_sent)

# converts the words in word_tokens to lower case and then checks whether 
filtered_sentence = []

print("====Stop Words====")
for w in word_tokens:
	if w not in stop_words:
		filtered_sentence.append(w)
	else:
		print(w)
	
print()
print("====Tokens====")
for token in filtered_sentence:
	if token != '.':
		print(token)

