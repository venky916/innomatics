import streamlit as st
from matplotlib import image
import pandas as pd
import plotly.express as px
import os

# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")

IMAGE_PATH = os.path.join(dir_of_interest, "images", "no_smoking.webp")
DATA_PATH = os.path.join(dir_of_interest, "data", "tips.csv")

st.title("Dashboard - Smoking Data")

img = image.imread(IMAGE_PATH)
st.image(img,use_column_width="auto")

df = pd.read_csv(DATA_PATH)
st.dataframe(df)

fig_1 = px.histogram(df, x="sex", color="sex")
st.plotly_chart(fig_1)

fig_2=px.histogram(df, x="smoker",y="total_bill" ,color="smoker")
st.plotly_chart(fig_2)

fig_3= px.histogram(df, x="sex", y="total_bill", color="sex", pattern_shape="smoker")
st.plotly_chart(fig_3)
