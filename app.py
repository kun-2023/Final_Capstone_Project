import streamlit as st
from regression import show_regression
from classification import show_classification
from explore import show_explore

page=st.sidebar.selectbox("Explore, Regression or Classification",("Explore","Regression","Classification"))

if page=="Regression":
    show_regression()
elif page=="Explore":
    show_explore()
else:
    show_classification()