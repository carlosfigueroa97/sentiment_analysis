import sys
import src.config.urls as urls
import pandas as pd
import numpy as np
from sentiment_analysis_spanish import sentiment_analysis as s_a

# Initialize variables
sentiment = s_a.SentimentAnalysisSpanish()

def read_files():
    try:
        df = pd.read_csv(urls.url_csv)
        file = open(urls.url_stopword,"r",encoding="utf-8") 
        text = file.read()
        art_pron = text.split(",")
        
        return [df, file, text, art_pron]
    except:
        print("An exception ocurred in method read_files", sys.exc_info()[0])

def remove_stopwords(df, art_pron):
    try:
        data_cleansing = []

        for row in df.message:
            for art in art_pron:
                row = row.replace(' ' +art+ ' ',' ')
            data_cleansing.append(row)

        return data_cleansing
    except:
        print("An exception ocurred in method remove_stopwords", sys.exc_info()[0])

def sentiment_analysis(data_cleansing):
    try:
        analyzed_data = []

        for data in data_cleansing:
            analyzed_data.append([data,sentiment.sentiment(data)])

        return analyzed_data
    except:
        print("An exception ocurred in method sentiment_analysis", sys.exc_info()[0])

def save_data(analyzed_data):
    try:
        res = pd.DataFrame(analyzed_data, columns = ["message","sentiment"])
        print ('Please wait, exporting data...')
        res.to_csv (urls.url_csv_analyzed, index = False, header=True)
    except:
        print("An exception ocurred in method save_data", sys.exc_info()[0])