#libraries
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
from sentiment_analysis_spanish import sentiment_analysis
import pandas as pd
import numpy as np

from math import sin
from time import time

#source code
sentiment = sentiment_analysis.SentimentAnalysisSpanish()
data_cleansing = []
analyzed_data = []


tiempo_inicial = time() 

print ('Reading data...')
df = pd.read_csv("data/data-test.csv")
file = open(“testfile.text”, “r”) 
text = file.read() 
art_pron = text.split(",")

print ('Removing articles and pronouns...')
for row in df.message:
    for art in art_pron:
        row = row.replace(' ' +art+' ',' ')
    data_cleansing.append(row)

print ('Sentiment analysis...')
for data in data_cleansing:
    analyzed_data.append([data,sentiment.sentiment(data)])

print('Saving data...')
res = pd.DataFrame(analyzed_data,
    columns = ["message","sentiment"]) 

print ('exporting data...')
res.to_csv (r'data\data-test-analyzed.csv', index = False, header=True)

tiempo_final = time() 
tiempo_ejecucion = tiempo_final - tiempo_inicial
print ('Run time: ',tiempo_ejecucion)