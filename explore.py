import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st


@st.cache_data
def load_data():
    df=pd.read_csv("nutrtion_table_per_gram.csv")
    data=df.iloc[:,1:].drop("Energy (kJ) per gram",axis=1)
    return data
data=load_data()
def show_explore():
    st.title("Explore Important Nutrients")
    st.write(
        """ ### Distribution of Energy
"""
    )
    fig1,ax1=plt.subplots()
    sns.histplot(data.iloc[:,2],bins=50,ax=ax1)
    st.write("The outliers of energy is above 6 kcal per 1 gram of nutrient.")
    st.pyplot(fig1)

    st.write(
        """### A glance at the calories outliers
"""
    )
    cal=data.query("`Energy (kcal) per gram`>6").sort_values("Energy (kcal) per gram", ascending=False)
    fig2,ax2=plt.subplots()
    sns.barplot(cal,x="Food Name",y="Energy (kcal) per gram",hue="Category",ax=ax2)
    plt.xticks(rotation=90)
    st.write("The outliers are from Fats and Oils and Legumes, Nuts and Seeds")
    st.pyplot(fig2)


    st.write("""### Top Protein Categories
             """)
    aa=data.groupby("Category")["Protein (g) per gram"].mean().sort_values(ascending=False).reset_index()
    #plt.figure(figsize=(10,5))
    fig3,ax3=plt.subplots()
    sns.barplot(data=aa,x="Category",y="Protein (g) per gram",ax=ax3)
    plt.xticks(rotation=90)
    st.pyplot(fig3)

    st.write("""### Top Calcium Categories""")
    bb=data.groupby("Category")["Calcium (mg) per gram"].mean().sort_values(ascending=False).reset_index()
    fig4,ax4=plt.subplots()
    sns.barplot(data=bb,x="Category",y="Calcium (mg) per gram",ax=ax4)
    plt.xticks(rotation=90)
    st.pyplot(fig4)
    

    
    st.write("""### Top Vitamin A (RAE) per gram Categories""")
    cc=data.groupby("Category")["Vitamin A (RAE) per gram"].mean().sort_values(ascending=False).reset_index()
    fig5,ax5=plt.subplots()
    sns.barplot(data=cc,x="Category",y="Vitamin A (RAE) per gram",ax=ax5)
    plt.xticks(rotation=90)
    st.pyplot(fig5)

    st.write(""" ### The correlation between healthy nutrients and unhealthy nutrients""")
    st.write("Healthy nutrients tend to show up together, but not with unhealthy ones. Chances that consumers can eat good nutrients while avoiding bad ones are very possible")
    fig6,ax6=plt.subplots()
    cor=data[["Protein (g) per gram","Calcium (mg) per gram","Iron (mg) per gram","Vitamin A (RAE) per gram","Total Sugar (g) per gram","Saturated Fat (g) per gram","Sodium (mg) per gram"]].corr()
    sns.heatmap(cor,annot=True,ax=ax6)
    st.pyplot(fig6)