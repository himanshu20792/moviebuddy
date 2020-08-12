import math
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pylab import rcParams
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from .models import ContentRec as Movies

movies = Movies.objects.values('keywords')

def rec(title):
    return("hi")