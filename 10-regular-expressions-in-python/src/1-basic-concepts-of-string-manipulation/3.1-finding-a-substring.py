import pandas as pd

movies_list = [
  "it's clear that he's passionate about his beliefs , and that he's not just a punk looking for an excuse to beat people up .",
  "I believe you I always said that the actor actor actor is amazing in every movie he has played",
  "it's astonishing how frightening the actor actor norton looks with a shaved head and a swastika on his chest."
]

movies = pd.Series(movies_list)

for movie in movies:
  	# If actor is not found between character 37 and 41 inclusive
    # Print word not found
    if movie.find("actor", 37, 42) == -1:
        print("Word not found")
    # Count occurrences and replace two with one
    elif movie.count("actor") == 2:  
        print(movie.replace("actor actor", "actor"))
    else:
        # Replace three occurrences with one
        print(movie.replace("actor actor actor", "actor"))