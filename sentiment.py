#from deep_translator import GoogleTranslator
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import streamlit as st
import nltk

st.write('### How do you feel?')
user_input = st.text_input('Type here (use one or two words): ')
#text_t = GoogleTranslator(source='pt', target='en').translate(user_input)

nltk.download('vader_lexicon')

analyzer = SentimentIntensityAnalyzer()
score = analyzer.polarity_scores(user_input)
    
if score['neu'] + score['neg'] > score['pos'] and score['neg'] != 0:
    st.write("### Sorry :(")

elif (score['pos'] > score['neu'] or score['pos'] > score['neg']) and score['neg'] == 0:
    st.write('### Awesome! :)')    
    




