import streamlit as st
import requests

'''
# Identify if a text is AI written or not
'''

st.markdown('''
This app is build to help you identify if a text is AI written or not.
The minimum length of the text should be :red[around 300 characters in order to give you a reliable prediction].

The accuracy of the model is about 98.5% if you put in a text that is appropriately long.
''')

'''## Put in the text you want to investigate:'''

text_input = st.text_area('Text to analyze', 'This is a text that is way to short to identify reliably. You can make better predictions if you put in a text that is at least 300 characters long.',
                          height=500
                          )



url = 'https://aiwrittentextidentifier-l2scua5wbq-ey.a.run.app/predict'

params = {
    "text_input": text_input
}

r = requests.get(url, params=params)
print(r.json())
proba = r.json()["Probability"]
# prediction = r.json()["Prediction"]
length = len(text_input)

if st.button('Show Prediction'):
    # print is visible in the server output, not in the page
    print('Show prediction button clicked!')
    if length < 300:
        st.write(f":orange[❗️Attention:] Your text is {length} characters long and therefore shorter than 300 characters. Be careful with the prediction.")
    else:
        st.write(f"Your text is {length} characters long. The prediction should be reliable.")
    if proba > 0.5:
        st.write(f'With a probability of **{round(proba*100, 2)}%** the text you put in is :red[AI written].')
    else:
        st.write(f'With a probability of **{round(100-proba*100,2 )}%** the text you put in is :green[*not* AI written].')
    #st.write('Further clicks are not visible but are executed')
else:
    st.write('Click to show the Prediction!')
