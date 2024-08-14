from word_forms.word_forms import get_word_forms

word = str(input("Enter the root word: "))

word_forms = get_word_forms(word)
abr = {"a": "adjectives", "r": "adverbs", "v": "verbs", "n": "nouns"}

for key in word_forms:
	print(f"{abr[key]}: {word_forms[key]}")