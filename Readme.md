## Showing now at screen near you .....

<p align="center"><img width=100% src="https://github.com/himanshu20792/moviebuddy/blob/master/meta_data/Homepage_picture.bmp"></p>


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


## MovieBuddy Features
- THE website for movie recommendations
- Home of the 1-click-recommendation
- Clean interface - Avoidance of too many recommendations
- Wide selection of over +44,000 movies
- Three different look-up experiences
- Eliminates the cold start problem
- Login-free

<p>

The login-free way to search for movies is here with its ease and simplicity.
One click and you will have recommended movies through interacting with a fun word cloud.
The app offers three different experiences to cover all movie markets. 

</p>

- the new user : word cloud
- the casual user : find similar
- movie buff : login

<br>

### General Motivation
Customers are frustrated with logging into exclusive recommenders and are wary about pre-personalized recommendations. Additionally there are too many  recommendations. The MovieBuddy offers a seamless experience tailored to the customer in a way that is unobtrusive. MovieBuddy has three tailored levels of interaction. Being login-free, MovieBuddy is easy to use because of its minimal interaction and solves the cold start problem. The MovieBuddy recommends from a vast array of movies, over 44,000 movies and would easily accomodate new movies into the recommender.

### Technical Motivation
Most movie recommender systems are based on purely a collaborative filtering (CF) and content based filtering system (CBF). However, these systems typically don't address the cold start (CS) problem very well. MovieBuddy solves the coldstart issue plaguing many recommender systems on the market. By utilizing the minimal login-free interaction from the user, this solves the cold start problem. In particular by selecting a word cloud keyword OR the find similar genres/movies. By gathering these human-generated preferences in a non-intrusive yet structured manner, it eliminates the noisy data collection, non-expensive to collect, and the human-generated information is required for the recommendations.

### General recommendation systems
The purpose of recommendation systems is to gather some preference from the market to predict the level of interest a user has in a new item. There are three different and distinct systems in existence today. 

1. Popularity Based recommenders use a similar recommendation to every market, based on the usage and popularity of an item.
2. Content-Based recommender focus on certain aspects of items. The similarity of items is determined by measuring the similarity in their aspects. There are different types of content-based systems : classification/regression and item content similarity.
3. Collaborative Filtering recommenders try to pinpoint the relationship between the market and items. Similarity of items is determined by the rating similarity of those items by the users who have rated both items.

The cold start problem is not addressed fully with the common recomendation system. We minimize this cold start challenge with the MovieBuddy App.

### Market groups
Three market segments will be targeted : spontaneous, casual, and movie buff markets.
<p align="center"><img width=100% src="https://github.com/himanshu20792/moviebuddy/blob/master/meta_data/clients_picture.png"></p>

### MovieBuddy application powered by Flask
For this app we chose a content-based recommender for the spontaneous and casual market group and a collaborative filtering recommender for the dedicated movie buff.  

The Word Cloud button leads to a word cloud that uses keyword search. This method of searching minimizes the cold start problem. On the Word Cloud page one click get you to the first recommendations. Once one word is selected from the word cloud, the recommendations appear. 

The Movie Preferences button leads to a page where selections of three genres with the ability to select like movies in each genre. This portion of the website would recommend after only three clicks. 

<p align="center"><img width=100% src="https://github.com/himanshu20792/moviebuddy/blob/master/meta_data/Organization_website.bmp"></p>

<p align="center"><img width=80% src="https://github.com/himanshu20792/moviebuddy/blob/master/meta_data/development_overview.png"></p>

<br>

## Backend Development : Python

- Exploratory Data analysis summary :
The movie database used was from kaggle which contained 46628 movies of  which the column titles were : 
```
Index(['id', 'title', 'tagline', 'description', 'genres', 'keywords', 'date',
       'collection', 'runtime', 'revenue', 'budget', 'director', 'cast',
       'production_companies', 'production_countries', 'popularity',
       'average_vote', 'num_votes', 'language', 'imdb_id', 'poster_url'],
      dtype='object')
```

The EDA analysis cleaned the database of duplicate full rows, imdb id, and titles. 5.41% / 2524 movies were without a genre and 31.9% / 14889 without an entry in keywords. These movies were not considered in the search. In the future , they will need to be incorporated into the recommendation system.

The word cloud and the find similar use NLP tools from the python package sklearn. 
Word cloud : countvectorizer 
Find similar : cosine_similarity

- Word cloud generation (Spontaneous market)
<p>

The word cloud generates by frequencies or occurrences of words per movie.
After importing CountVectorizor from sklearn, the code counts every word or bag of words per keyword per movie.
</p>

```
Overview of the Python code : (Pseudo-code)
import CountVectorizer from sklearn
counts = pd.DataFrame(count_matrix.toarray(),index=df.title,
                      columns=vectorizer.get_feature_names())
counts_transposed.sort_values(by=['sum'], axis=0, ascending=False)
```
<p>


</p>

<p align="center"><img width=100% src="https://github.com/himanshu20792/moviebuddy/blob/master/meta_data/word_cloud_graphic_readme.png"></p>

<p>

To avoid the keywords to be split like 'woman director', the df was created with and underscore like 'woman director' to maintain the logical connection.

</p>

<p align="center"><img width=80% src="https://github.com/himanshu20792/moviebuddy/blob/master/meta_data/Word_cloud_process_flow.bmp"></p>


- Find similar generation (Casual user)

<p>

The code with find similar searches for similar titles to the movies chosen by the user and assigns a cosine similarity score. The the resulting 20 movies are recommended.

</p>

```
Overview of the Python code : (Pseudo-code)
import cosine_similarity from sklearn
for title in titles:
	idx.append(indices[indices == title].index[0])
user_pref_vector = tfidf_np_matrix[idx].mean(axis=0)
cosine_sim = cosine_similarity(tfidf_matrix,np.atleast_2d(user_pref_vector))
df_cosine_sim = pd.DataFrame(cosine_sim, columns=['sim_score'])
df_cosine_sim = df_cosine_sim.sort_values(by='sim_score',ascending=False)
```

<p align="center"><img width=80% src="https://github.com/himanshu20792/moviebuddy/blob/master/meta_data/findsimilar_process_flow.png"></p>


## Credits
- Andreas Mueller. Python Package. Retrieved from https://pypi.org/project/wordcloud/ 
- Yashar Deldjoo, Maurizio Ferrari Dacrema, Mihai Gabriel Constantin, Hamid Eghbal-zadeh, Stefano Cereda, Markus Schedl, Bogdan Ionescu & Paolo Cremonesi. Movie genome: alleviating new item cold start in movie recommendation [Internet]. User Modeling and User-Adapted Interaction 29,291-343; 2019. Availible from:https://doi.org/10.1007/s11257-019-09221-y.
- Weight and biases

## Contributing
Please take a look at the [contributing](https://github.com/himanshu20792/moviebuddy/blob/master/CONTRIBUTING.md) guidelines if you're interested in helping!
- Alan Wang
- Himanshu Agarwal
- Ty Schnettler

## GitHub Links
![Python](https://img.shields.io/badge/python-v3.7+-blue.svg)
![Dependencies](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)
[![GitHub Issues](https://img.shields.io/github/issues/hilsdsg3/movie-recommender.svg)](https://github.com/hilsdsg3/movie-recommender/issues)
![Contributions welcome](https://img.shields.io/badge/contributions-welcome-orange.svg)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)

