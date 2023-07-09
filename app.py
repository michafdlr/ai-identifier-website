import streamlit as st
import requests
import pandas as pd

st.sidebar.image('Logo2.png', use_column_width=True)

'''
# The AI Written Text Identifier
'''

st.markdown('''Identify whether a text is AI-generated. This app is built to help
            you determine if a given text is written by a human or an AI language model.''')

st.markdown(''':orange[*For reliable predictions, the minimum length of the text should be around 300 characters*].
            The model accuracy is approximately 98.5% when analyzing sufficiently long texts.''')

'''## Please enter the text you want to analyze:'''

demo_df = pd.read_csv('demo_data.csv')

def get_text():
    sample = demo_df.sample(n=1)
    return sample['text'].values[0], sample['AI'].values[0]

if "default" not in st.session_state and "ai" not in st.session_state:
    st.session_state["default"] = "Put your text here"
    st.session_state["ai"] = "None"

text_input = st.text_area('Text to analyze', value=st.session_state["default"], key="txt", height=500)

if st.sidebar.button('Use Demo Text'):
    st.session_state["default"], st.session_state["ai"] = get_text()
    st.experimental_rerun()
else:
    st.sidebar.write('Click to use Demo Text!')

url = 'https://aiwrittentextidentifier-l2scua5wbq-ey.a.run.app/predict'

params = {
    "text_input": text_input
}

r = requests.get(url, params=params)
print(r.json())
proba = r.json()["Probability"]
# prediction = r.json()["Prediction"]
length = len(text_input)

if st.sidebar.button('Show Prediction'):
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
    st.sidebar.write('Click to show the Prediction!')

# if st.checkbox("Show real classification"):
#     st.write(f"The real classification is: {st.session_state['ai']}")
# else:
#     st.write("Check to show the real classification")
