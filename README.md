<p align="center"><img width=80% src="https://github.com/himanshu20792/moviebuddy/blob/master/meta_data/logo.bmp"></p>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
![Python](https://img.shields.io/badge/python-v3.7+-blue.svg)
![Dependencies](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)
[![GitHub Issues](https://img.shields.io/github/issues/hilsdsg3/movie-recommender.svg)](https://github.com/hilsdsg3/movie-recommender/issues)
![Contributions welcome](https://img.shields.io/badge/contributions-welcome-orange.svg)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)

## MovieBuddy Features
- THE website for movie recommendations
- Home of the 1-click-recommendation
- Wide selection of over +44,000 movies
- Three different options of recommendations
- Minimizes the cold start problem

<p align="center"><img width=100% src="https://github.com/himanshu20792/moviebuddy/blob/master/meta_data/Homepage_picture.bmp"></p>

<br>

### Details
The goal of the website is to give a variety of ways to recommend movies. The MovieBuddy website also has three levels of interaction starting from the homepage.
One of the team goals was to reduce the amount of clicks to get to the recommendations. The MovieBuddy recommends from a vast array of movies, over 44,000 movies with unique keyword and genre preferences.

The Word Cloud button leads to a word cloud that uses keyword search. On the Word Cloud page one click get you to the first recommendations. Once one word is selected from the word cloud, the recommendations appear. Currently , the team is improving the website for enhanced functionality like regenerating word cloud for other recommendations.

The Movie Preferences button leads to a page where selections of three genres with the ability to select like movies in each genre. This portion of the website would recommend after only three clicks. This page is currently under construction.

<p align="center"><img width=100% src="https://github.com/hilsdsg3/movie-recommender/blob/master/meta_data/Organization_website.bmp"></p>
<br>

## Development

- Word cloud generation
The word cloud generates by frequencies or occurrences of words, then normalizes the occurence values and displays them as with a graphic.       
"frequencies = sorted(frequencies.items(), key=itemgetter(1), reverse=True)""

The word cloud is generated with python and displayed with Django framework. We are currently investigating alternate methods to display.

<p align="center"><img width=80% src="https://github.com/hilsdsg3/movie-recommender/blob/master/meta_data/Word_cloud_process_flow.bmp"></p>
## Live Demo

## Disclaimer

## Credits
- Wordcloud package inventor
- Cold start problem article

## Contributing
Please take a look at the [contributing](https://github.com/hilsdsg3/movie-recommender/blob/master/CONTRIBUTING.md) guidelines if you're interested in helping!
- Alan Wang
- Himanshu Agarwal
- Ty Schnettler

#### Pending Features
- Word cloud additional features
