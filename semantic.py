import spacy
nlp = spacy.load('en_core_web_md')

word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))
# cat and monkey seems to have some kind of similarity 
# monkey and banana also have some kind of similarity 
# while cat and banana have the least similarity 

token = nlp('cat dog mouse')

for token1 in token:
    for token2 in token:
        print (token1.text, token2.text, token1.similarity(token2))
# cat and dog have the best similarity - probably they are both house pets 
# cat and mouse have some kind of similarity probably becouse the cat eat mouses
# dog and mouse have the least similarity because they don't have much in comomn apart they both can live around the house

sentence_to_compare = "why is my cat on the car"

sentences = ["where did my dog go",
"Hello, there is my car",
"I\'ve lost my car in my car",
"I\'d like my boat back",
"I will name my dog Diana"]

model_sentence = nlp(sentence_to_compare)

for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)

# if we run with lower model 'sm' this model is not using vectors and therfore we may not get the 
# results we require as it use diferent compare technics to find the similarity 