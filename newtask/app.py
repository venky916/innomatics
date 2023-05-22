import streamlit as st
import pandas as pd
import os
from pickle import load


# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_PATH_1 = os.path.join(FILE_DIR,"car_price_prediction.csv.csv")

df=pd.read_csv(DATA_PATH_1)

Levy	 = st.number_input(label="Levy	")
Prod_year = st.number_input(label="Prod. year")
Enginevolume = st.number_input(label="Engine volume")
Mileage = st.number_input(label="Mileage")
Cylinders = st.number_input(label="Cylinders")
Doors = st.number_input(label="Doors")
Airbags = st.number_input(label="Airbags")

val1 = st.selectbox(
    'Manufacturer',
    (df["Manufacturer"].unique()))

val2 = st.selectbox(
    'Category',
    (df["Category"].unique()))

val3 = st.selectbox(
    'Leather interior',
    (df["Leather interior"].unique()))

val4 = st.selectbox(
    'Fuel type',
    (df["Fuel type"].unique()))

val5 = st.selectbox(
    'Gear box type',
    (df["Gear box type"].unique()))

val6 = st.selectbox(
    'Drive wheels',
    (df["Drive wheels"].unique()))

val7 = st.selectbox(
    'Wheel',
    (df["Wheel"].unique()))

val8 = st.selectbox(
    'Color',
    (df["Color"].unique()))
