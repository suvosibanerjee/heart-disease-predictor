import streamlit as st
import pickle
import numpy as np

# import the model
pipe = pickle.load(open('pipe.pkl','rb'))
df = pickle.load(open('df.pkl','rb'))

st.title("Heart Disease Predictor")

#age
age = st.number_input("Your age")

#sex
sex = st.selectbox('Sex',["Male","Female"])

#chest pain type
cp = st.selectbox('Chest pain type',[0,1,2,3])

#resting blood pressure
trestbps = st.number_input("Your resting blood pressure")

#Cholestrol
chol = st.number_input("Your Cholestrol")

#fasting blood sugar
fbs = st.selectbox('Is your fasting blood sugar greater than 120mg/dl',["Yes","No"])

#resting electrocardiographic results
restecg = st.selectbox('Resting ECG Results',[0,1,2])

#Max heart rate
thalach = st.number_input("Your max heart rate")

#exercise induced angina
exang = st.selectbox('Are you performing exercises including angina',["Yes","No"])

#oldpeak
oldpeak = st.number_input("Your old peak")

#the slope of the peak exercise ST segment
slope = st.selectbox('What is the slope of the peak exercise ST segment',[0,1,2])

#number of major vessels (0-3) colored by flourosopy
ca = st.selectbox('What is the number of major vessels (0-3) colored by flourosopy',[0,1,2,3])

#thal
thal = st.selectbox('What is your max heart rate achieved',["normal","fixed defect","reversable defect"])

if st.button('Predict'):
    # query
    if sex=="Male":
        sex = 1
    else:
        sex=0

    if fbs=="Yes":
        fbs=1
    else:
        fbs=0

    if exang =="Yes":
        exang =1
    else:
        exang=0

    if thal == "normal":
        thal=1
    elif thal =="fixed defect":
        thal=2
    else:
        thal=3

    query = np.array([age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal])

    query = query.reshape(1,13)
    disease = str(int(np.exp(pipe.predict(query)[0])))
    if disease:
        out = "You might have heart disease"
    else:
        out="You don't seem to have heart disease"
    st.title(out)
