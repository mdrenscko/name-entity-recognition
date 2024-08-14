import spacy

# Load the English model for spaCy
nlp = spacy.load('en_core_web_sm')

# Create a list of sentences
gardenpathSentences = ["The old man the boat", "The horse raced past the barn fell"]
s1 = "Mary gave the child a Band-Aid"
s2 = "That Jill is never here hurts"
s3 = "The cotton clothing is made of grows in Mississippi"
gardenpathSentences.append(s1)
gardenpathSentences.append(s2)
gardenpathSentences.append(s3)

#Tokenize each sentence
res = [sub.split() for sub in gardenpathSentences]
print(str(res))



# Perform named entity recognition
for sentence in gardenpathSentences:
  doc = nlp(sentence)
  doc.text.split()
  for token in doc:
     print(token.text, token.pos_, token.tag_)
     print(spacy.explain(token.tag_))


for sentence in gardenpathSentences:
  nlp_sentence = nlp(sentence)
  print([(i, i.label_, i.label) for i in nlp_sentence.ents])

# Look up and print the meaning of entities that you don’t understand
print(spacy.explain("FAC"))

#Write a comment about two entities that you looked up. For each entity answer the following questions:
# ○ What was the entity and its explanation that you looked up?
# ○ Did the entity make sense in terms of the word associated with it?

#Entity 1: GPE (Geopolitical entity, i.e., countries, cities, states)
# Explanation: This entity represents countries, cities, and states.
# The entity makes sense in terms of the word "Mississippi" in the sentence "The cotton clothing is made of grows in Mississippi."
#Entity 2: PERSON (Name of a person)
# The entity make sense in terms of the names of persons in the sentences "Mary gave the child a Band-Aid" and "That Jill is never here hurts".