#libraries
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
from sentiment_analysis_spanish import sentiment_analysis
import pandas as pd
import numpy as np

from math import sin
from time import time

#source code
initial_time = time() 

sentiment = sentiment_analysis.SentimentAnalysisSpanish()
data_cleansing = []
analyzed_data = []

print ('Reading data...')
df = pd.read_csv("data/data-test.csv")

file = open("data/list_art_pron.txt","r",encoding="utf-8") 
text = file.read()
art_pron = text.split(",")

print ('Removing articles and pronouns...')
for row in df.message:
    for art in art_pron:
        row = row.replace(' ' +art+ ' ',' ')
    data_cleansing.append(row)

print ('Sentiment analysis...')
for data in data_cleansing:
    analyzed_data.append([data,sentiment.sentiment(data)])

print('Saving data...')
res = pd.DataFrame(analyzed_data,
    columns = ["message","sentiment"]) 

print ('exporting data...')
res.to_csv (r'data\data-test-analyzed.csv', index = False, header=True)

file.close()

final_time = time() 
run_time = final_time - initial_time
print ('Run time: ',run_time)