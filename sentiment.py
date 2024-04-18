from deep_translator import GoogleTranslator
import streamlit as st
import nltk

st.write('# Qual a sua opinião?')
user_input = st.text_input('Escreva aqui: ')
text_t = GoogleTranslator(source='pt', target='en').translate(user_input)

nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()
score = analyzer.polarity_scores(text_t)
    

if score['neu'] + score['neg'] > score['pos'] or (score['compound'] < 0.1 and score['compound'] > 0):
    st.write("### I'm sorry :(")

elif (score['pos'] > score['neu'] or score['pos'] > score['neg']) and score['neg'] == 0:
    st.write('### Thanks!')


#st.write(score)    
    




