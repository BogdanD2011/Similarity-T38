# import spacy
import spacy

#load spacy module md
nlp = spacy.load('en_core_web_md')

#function bellow search for simetry between the passed argument and a list of descritions
# from the movie.txt file
# it return the line from text file with most sometry 
def movie_to_watch(description):

    model = nlp(description)
    temp_sim=0.0
    sugested_movie = str
    # we look for most simetry in the list
    for sentence in movies_list:
        sim = nlp(sentence).similarity(model)
        if sim > temp_sim:
            sugested_movie = sentence
            temp_sim = sim
    return sugested_movie # return result with most simetry

# === main function ===
#open and read movie.txt file in list movie_list
with open ('movies.txt', 'r') as f:
    movies_list = f.readlines()

sintax_to_compare = '''Will he save their world or destroy it? When the Hulk becomes too dangerous for the
Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a
planet where the Hulk can live in peace. Unfortunately, Hulk land on the
planet Sakaar where he is sold into slavery and trained as a gladiator.'''

#calling function with sintax to compare as argument 
sugested_movie = movie_to_watch(sintax_to_compare)

# printing first 7 char of the line (movie title)
print (f"You should watch {sugested_movie[:7]}")