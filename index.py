import os
import sys
import src.config.config
import src.controllers.methods as m
from time import time

# Properties
initial_time = 0
df = ""
file = ""
text = ""
art_pron = ""
data_cleansing = []
analyzed_data = []
dirname = os.path.dirname(os.path.abspath(__file__))

def start_time():
    initial_time = time()
    print("Start time: ", initial_time)

def end_time():
    final_time = time() 
    run_time = final_time - initial_time
    print("End time: ", final_time)
    print ('Run time: ', run_time)

def main():
    try:
        start_time()

        print('Reading data...')

        # read files
        response = m.read_files()
        df = response[0]
        file = response[1]
        text = response[2]
        art_pron = response[3]

        print('Removing articles and pronouns...')
        data_cleansing = m.remove_stopwords(df, art_pron)

        print('Sentiment analysis...')
        analyzed_data = m.sentiment_analysis(data_cleansing)

        print('Saving data...')
        if(analyzed_data != []):
            m.save_data(analyzed_data)
    except:
        print("An exception ocurred", sys.exc_info()[0])
    finally:
        #if(file != None):
        #    file.close()
        end_time()
        print("Analysis finished")

if __name__ == "__main__":
    main()