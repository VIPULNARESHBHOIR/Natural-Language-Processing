import pandas as pd 
import spacy 


model = spacy.load("en_core_web_sm")
pd.set_option("display.max_rows", 200)

content = str(input("Text = "))

doc = model(content)

print()
entities = [(ent.text, ent.label_) for ent in doc.ents]
df = pd.DataFrame(entities, columns=['Name', 'Entity'])
print(df)

"""hello, i am Vipul Bhoir from Saphale. currently pursuing Computer Engineering at Vidyavardhini's college of Engineeing situated at Vasai."""