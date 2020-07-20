import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pathlib
import requests
import re
import openpyxl
import xlsxwriter 

MOVIE_DATASET_FILE = 'movie_dataset.csv'
POST_PROCESSED_FILE = 'post_prcssd_datafile.csv'
movie_list = ''
vectorizer = CountVectorizer()

def prep_db(file,file_type):
    '''
    This module reads and prepares the db : cleans,
    deletes the columns with 'Unnamed' values,
    fills NaN values
    input : 
    file # the movieset file
    file type # csv file type
    output :
    df # read movie set dataframe 
    '''
    if file_type == 'csv':
        df = pd.read_csv(file, sep=',', dtype=str) # Read CSV File    
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
    df = df.fillna('') # clean the data - get rid of NaN
    df = df.astype(str) # change the default data type to string
    return(df)

def combine_row_text(features,df):
    '''
    This module combines and sets the case to lower
    args :
    input : 
    features # list of database columns to search in the movies database
    df # pandas dataframe
    output : counts # dataframe
    '''
    df['comb'] = ''
    for feature  in features:
        df['comb']= df['comb'].str.cat(df[feature].copy(), sep =' ')
    df['comb'] = df['comb'].str.lower()
    return(df)

def highest_count_words(df):
    '''
    This module takes as input the imported movie dataset 
    Also this function counts the words and
    sets the columns in decreasing order
    args :
    input : df # pandas dataframe of the pandas dataframe
    output : counts # dataframe of the counted objects
    '''
    
    count_matrix = vectorizer.fit_transform(df.comb)
    counts = pd.DataFrame(count_matrix.toarray(),
                      index=df.title,
                      columns=vectorizer.get_feature_names())
    return(counts)

def find_delete_columns(counts,character,char): 
    '''
    This sub-module is run off of the delete columns mega
    and deletes the unwanted columns of words
    args :
    input : 
    counts # dataframe of column of counted words
    character # regex code for the particular character(s)
    char # the unwanted character(s) that I want deleted
    output :
    counts # dataframe without the unwanted characters
    '''
    t = 0 # column counter
    n = 1
    orig = len(counts.columns)
    print(' ')
    print(' ')
    print(f'Original column count is {len(counts.columns)}')
    print(f'removing {char} columns .... ')
    for i in counts.columns:
        if t == (n * 1000):
            # print(str(round(t/len(counts.columns)*100,0))+'%')
            n +=1
        t+=1
        if re.findall(character, i):
            del counts[i]
    print(f'after deleting the unwanted word -{char}-, the list is {len(counts.columns)} long')
    print(f'Reduction effectiveness : {str(round((1-(len(counts.columns)/orig))*100,0))} %')
    return(counts)

def delete_columns_mega(counts):                   
    '''
    This module calls the sub module and controls the deletion of unwanted columns
    input : 
    counts # dataframe of column of counted words
    output :
    counts # dataframe without the unwanted characters    
    '''
    counts = find_delete_columns(counts, '\d', 'any numeric')
    counts = find_delete_columns(counts, '[\uac00-\ud7a3]', 'Korean characters')
    counts = find_delete_columns(counts, '[\u4e00-\u9FFF]', 'Chinese characters')
    counts = find_delete_columns(counts, '[\u0900-\u097F]',' Indian characters')
    counts = find_delete_columns(counts, '[\u0627-\u064a]',' Arabic characters')
    counts = find_delete_columns(counts, '[\u0400-\u04FF]',' Russian characters')
    counts = find_delete_columns(counts, '[\u0E00-\u0E7F]',' Thai characters')
    counts = find_delete_columns(counts, '[\u3040-\u309F]',' Japanese Hiragana characters')
    counts = find_delete_columns(counts, '[\u3040-\u30FF]',' Japanese Katagana characters')
    counts = find_delete_columns(counts, '(^has$)',' has')
    counts = find_delete_columns(counts, '(^time$)',' time')
    counts = find_delete_columns(counts, '(^never$)',' never')
    counts = find_delete_columns(counts, '(^director$)',' director')
    counts = find_delete_columns(counts, '(^john$)',' john')
    counts = find_delete_columns(counts, '(^and$)',' and')
    counts = find_delete_columns(counts, '(^will$)',' will')
    counts = find_delete_columns(counts, '(^you$)',' you')
    counts = find_delete_columns(counts, '(^they$)',' they')
    counts = find_delete_columns(counts, '(^is$)',' is')
    counts = find_delete_columns(counts, '(^film$)',' film')
    counts = find_delete_columns(counts, '(^it$)',' it')
    counts = find_delete_columns(counts, '(^one$)',' one')
    counts = find_delete_columns(counts, '(^its-?$)',' it,its')
    counts = find_delete_columns(counts, '(^of$)',' of')
    counts = find_delete_columns(counts, '(^on$)',' on')
    counts = find_delete_columns(counts, '(^for$)',' for')
    counts = find_delete_columns(counts, '(^the$)',' the')
    counts = find_delete_columns(counts, '(^to$)',' to')
    counts = find_delete_columns(counts, '(^your-?$)',' you,your')
    counts = find_delete_columns(counts, '(^new$)',' new')
    counts = find_delete_columns(counts, '(^man$)',' man')
    counts = find_delete_columns(counts, '(^woman$)',' woman')
    counts = find_delete_columns(counts, '(^no$)',' no')
    counts = find_delete_columns(counts, '(^his$)',' his')
    counts = find_delete_columns(counts, '(^he$)',' he')
    counts = find_delete_columns(counts, '(^hers$)',' hers')
    counts = find_delete_columns(counts, '(^can$)',' can')
    counts = find_delete_columns(counts, '(^all$)',' all')
    counts = find_delete_columns(counts, '(^from$)',' from')
    counts = find_delete_columns(counts, '(^are$)',' are')
    counts = find_delete_columns(counts, '(^there$)',' there')
    counts = find_delete_columns(counts, '(^an$)',' an')
    counts = find_delete_columns(counts, '(^with$)',' with')
    counts = find_delete_columns(counts, '(^in$)',' in')
    counts = find_delete_columns(counts, '(^be$)',' be')
    counts = find_delete_columns(counts, '(^what$)',' what')
    return (counts)

def most_frequent_words(counts,POST_PROCESSED_FILE):
    '''
    This function prepares the most frequent words of the 
    specific movie's selection types and ouputs to a csv
    input : 
    counts # dataframe of column of counted words
    output :
    counts_transposed # column transferred to rows
    and saved to a csv
    '''
    counts_transposed = counts.T
    counts_transposed['sum'] = counts_transposed.sum(axis=1)
    cols = counts_transposed.columns.tolist()
    cols = cols[-1:] + cols[:-1]
    counts_transposed = counts_transposed[cols]
    counts_transposed = counts_transposed.sort_values(by=['sum'], axis=0, ascending=False)
    counts_transposed.to_csv(POST_PROCESSED_FILE, sep=',', encoding='utf-8')
    return(counts_transposed)


# Imports the csv database
df = prep_db(MOVIE_DATASET_FILE,'csv')

print('The selection types are : ')
print(df.columns)

# combine the needed colums data into one string
df = combine_row_text(['title', 'director', 'tagline', 'genres', 'keywords'], df)

# calculates the frequency of words
counts = highest_count_words(df)

# This function cleans the database of unwanted words like "the , an , other lanaguage characters, etc)  
counts = delete_columns_mega(counts)


# This function prepares the most frequent words of the specific movie's selection types and ouputs a csv 
counts_T = most_frequent_words(counts,POST_PROCESSED_FILE)