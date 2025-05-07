import streamlit as st
import joblib
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from autocorrect import Speller
from contractions import fix
from textacy.preprocessing.remove import accents
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer, WordNetLemmatizer
from sklearn.linear_model import SGDClassifier
