from deep_translator import GoogleTranslator
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import streamlit as st
import nltk

st.write('# Qual a sua opinião?')
user_input = st.text_input('Escreva aqui: ')
text_t = GoogleTranslator(source='pt', target='en').translate(user_input)

nltk.download('vader_lexicon')

analyzer = SentimentIntensityAnalyzer()
score = analyzer.polarity_scores(text_t)
    
if score['neu'] + score['neg'] > score['pos'] and score['neg'] != 0:
    st.write("### Sentimos muito :(")

elif (score['pos'] > score['neu'] or score['pos'] > score['neg']) and score['neg'] == 0:
    st.write('### Nós agradecemos!')    
    




