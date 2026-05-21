import streamlit as st
import pickle
from sklearn import linear_model
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt  #static/data visualization library
#%matplotlib

df=pd.read_csv("home_price_loc.csv")

st.title("Home Price Prediction")

le=LabelEncoder()  #le encoder me kis chex ko cahnge kra h or khn

df["location"] = le.fit_transform(df["location"])

st.dataframe(df)

#dependent variable is price

#independent variable is area  & loaction

x=df.drop('price',axis='columns')
y=df.price

st.subheader("Dependent Variables that's in 2 Dimension")
st.dataframe(x)

st.subheader("Inependent Variables that's in series")
st.dataframe(y)


st.sidebar.header("DATASET INFORMATION")
st.sidebar.subheader("No# Area we have")
st.sidebar.info(df["area"].count())

model=linear_model.LinearRegression()
model.fit(x,y)

area=st.number_input("Enter area")
loc=st.selectbox("Enter location",le.classes_)   #le.classes me sari locations hyn

if loc:
    are=le.transform([loc])[0]   #transform le k andr qualittative data hai  jo transform krrh    
    predicted_price=model.predict([[area,are]])
    st.success(predicted_price[0])

   



