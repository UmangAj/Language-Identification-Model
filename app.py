import streamlit as st
import pickle
import numpy as np
import pandas as pd
import logging

try:
	
	model = pickle.load(open('model.pkl', 'rb'))
	df = pickle.load(open('df.pkl', 'rb'))

	st.title('Language Identification Model')
	st.write('#### Enter the sentence that you want to detect the language:')

	if st.button('Languages available'):
		languages_available = df['language'].unique().reshape(3,7)
		st.dataframe(languages_available)

	user_sentence = st.text_area('', label_visibility="collapsed")
	user_sentence_array = np.array([user_sentence])
	result = model.predict(user_sentence_array)[0]

	if st.button('Predict'):
		if not user_sentence_array:
			st.warning('Please enter a sentence.')
		else:
			st.write('#### Detected language:',  result)

except Exception as e:
	st.error("This service is currently unavailable. Please try again later.")
	

