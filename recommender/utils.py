import math
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pylab import rcParams
#from sklearn.feature_extraction.text import TfidfVectorizer
#from sklearn.metrics.pairwise import cosine_similarity
#from .models import ContentRec as movies

#movies_subset = movies.dropna(subset=['keywords'])
#movies_subset = movies_subset.reset_index(drop=True)

#tfidf_vectorizer = TfidfVectorizer(stop_words='english')
#tfidf_matrix = tfidf_vectorizer.fit_transform(movies_subset.keywords)

# generating the cosine similarity matrix
#cosine_sim = cosine_similarity(tfidf_matrix,tfidf_matrix)

#indices = pd.Series(movies_subset.title)
#indices[:5]

def rec(title):
    return('hi')
    #recommended_movies = []
    
    # gettin the index of the movie that matches the title
    #idx = indices[indices == title].index[0]

    # creating a Series with the similarity scores in descending order
    #score_series = pd.Series(cosine_sim[idx]).sort_values(ascending = False)

    # getting the indexes of the 10 most similar movies
    #top_10_indexes = list(score_series.iloc[0:11].index)
    
    # populating the list with the titles of the best 10 matching movies
    #for i in top_10_indexes:
    #    recommended_movies.append([movies_subset.title.iloc[i],movies_subset.genres.iloc[i],movies_subset.keywords.iloc[i],movies_subset.popularity.iloc[i],movies_subset.average_vote.iloc[i],movies_subset.num_votes.iloc[i],score_series[i]])
        
    #return pd.DataFrame(recommended_movies,columns=['movie_title','genres','keywords','popularity','average_vote','num_votes','cosine_score'])
