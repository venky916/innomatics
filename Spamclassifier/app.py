import streamlit as st
from pickle import load


st.title(":red[SPAM CLASSIFIER]	😎")

st.header("ENTER THE MESSAGE !!!")

message_input = st.text_area("label goes here")


nb_classifier = load(open('models/nb_model.pkl', 'rb'))
cv=load(open('models/cv.pkl', 'rb'))

if st.button('check'):
    b=[]
    var1=list(str(message_input))
    b.append(''.join(var1))
    predict=nb_classifier.predict(cv.transform(b))

    if predict==1:
        st.write('SPAM')
    else:
        st.write('HAM')



