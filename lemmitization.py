from nltk.stem import WordNetLemmatizer
 
lemmatizer = WordNetLemmatizer()

text = "programming running rocks corpora birds and better airplanes are flying in the sky"
text = text.split()
print(text)

for word in text:
	t = lemmatizer.lemmatize(word)
	print(f"{word}: {t}")
 
