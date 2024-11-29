import streamlit as st
import numpy as np
import pickle



def load_model():
    with open("classification.pkl","rb") as file:
        data=pickle.load(file)
    return data


data=load_model()
classifier=data["model"]
scaler=data["scaler"]


def show_classification():
    st.title("See which category your food belongs to?")
    st.write("""### Select the amount of each nutrient in this item of 100 grams""")


    energy=st.slider("Energy (kcal)",0.00,917.00,0.00)
    protein=st.slider("Protein (g)",0.00,100.00,0.00)
    sugar=st.slider("Total Sugar (g)",0.00,100.00,0.00)
    cholesterol=st.slider("Cholesterol (mg)",0.00,1190.00,0.00)
    monounsaturated_fat=st.slider("Monounsaturated Fat (g)",0.00,73.00,0.00)
    polyunsaturated_fat=st.slider("Polyunsaturated Fat (g)",0.00,71.00,0.00)
    saturated_fat=st.slider("Saturated Fat (g)",0.00,50.00,0.00)
    fiber=st.slider("Total Dietary Fiber")
    #carbohydrate=st.slider("Carbohydrate (g)",0.00,130.00,0.00)
    #magnesium=st.slider("Magnesium (mg)",0.00,550.00,0.00)
    #phosphorus=st.slider("Phosphorus (mg)",0.00,1400.00,0.00)

    healthy_fats=monounsaturated_fat+polyunsaturated_fat

    ok=st.button("Calculate the amount of calories in this food of 100 grams")
    if ok:
        X=np.array([[healthy_fats,energy,protein,sugar,saturated_fat,cholesterol,fiber]])
        X=scaler.transform(X)
        X=X.astype("float")

        cluster=classifier.predict(X)
        if cluster=="High energy and fat":
            st.subheader(f"The food item belongs to the {cluster} group")
            st.warning("Watch out for the calories and fats")
        elif cluster=="High on Protein and cholesterol":
            st.subheader(f"The food item belongs to the {cluster} group")
            st.warning("Get the protein, but watch out for the cholesterols")
        elif cluster=="High on sugar and minerals":
            st.subheader(f"The food item belongs to the {cluster} group")
            st.warning("if there's too much sugar in it, I feel for your teeth")
        else:
            st.subheader(f"The food item belongs to the {cluster} group")
            st.success("Everything is in good balane, but you add some more proteins and minerals!!!")
        