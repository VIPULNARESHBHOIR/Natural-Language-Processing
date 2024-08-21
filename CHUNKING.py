import nltk
sample_text= "I am a coding ninja and I am the best in coding."

tokenized=nltk.sent_tokenize(sample_text)
for i in tokenized:
  words=nltk.word_tokenize(i)
  tagged_words=nltk.pos_tag(words)
  print(tagged_words)
  chunkGram = r"""Chunk: {<RB.?>*<VB.?>*<NNP>+<NN>?}""" # this is the grammar that we define,
  chunkParser=nltk.RegexpParser(chunkGram)
  chunked=chunkParser.parse(tagged_words)
  chunked.draw()