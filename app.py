import streamlit as st
import requests

'''
# Classify text regarding if it is AI written or not
'''

st.markdown('''
Just put in the text
''')

'''## Put in the text you want to investigate:'''

text_input = st.text_input('Text to analyze', 'This is a text that is way to short to identify reliably.')



url = 'https://aiwrittentextidentifier-l2scua5wbq-ey.a.run.app/predict'

params = {
    "text_input": text_input
}

r = requests.get(url, params=params)
print(r.json())
proba = r.json()["Probability"]
prediction = r.json()["Prediction"]

if st.button('Show Prediction'):
    # print is visible in the server output, not in the page
    print('Show prediction button clicked!')
    if proba > 0.5:
        st.write(f'With a probability of {round(proba, 3)} the text you put in is AI written.')
    else:
        st.write(f'With a probability of {round(1-proba,3 )} the text you put in is not AI written.')
    #st.write('Further clicks are not visible but are executed')
else:
    st.write('Click to show the Prediction!')
