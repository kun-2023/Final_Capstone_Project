import streamlit as st
import numpy as np
import pickle

def load_model():
    with open("saved_steps.pkl","rb") as file:
        data=pickle.load(file)
    return data


data=load_model()
regressor=data["model"]
scaler=data["scaler"]

def show_regression():
    st.title("Calculate the amount of calories you are about to consume.")
    st.write("""### Select the amount of each nutrient in the food item of 100 grams""")

    monounsaturated_fat=st.slider("Monounsaturated Fat (g)",0.00,73.00,0.00)
    polyunsaturated_fat=st.slider("Polyunsaturated Fat (g)",0.00,71.00,0.00)
    saturated_fat=st.slider("Saturated Fat (g)",0.00,50.00,0.00)
    carbohydrate=st.slider("Carbohydrate (g)",0.00,130.00,0.00)
    magnesium=st.slider("Magnesium (mg)",0.00,550.00,0.00)
    phosphorus=st.slider("Phosphorus (mg)",0.00,1400.00,0.00)

    healthy_fats=monounsaturated_fat+polyunsaturated_fat

    ok=st.button("Calculate the amount of calories in this food of 100 grams")
    if ok:
        X=np.array([[saturated_fat,healthy_fats,carbohydrate,magnesium,phosphorus]])
        X=scaler.transform(X)
        X=X.astype("float")

        calorie=regressor.predict(X)
        calorie=np.round(calorie,2)
        if calorie>333.00:
            st.subheader(f"The estimated calories is {calorie}.")
            st.warning("This food has a calroies of above 75 percentile. It's too much calories")
        elif calorie>191.00:
            st.subheader(f"The estimated calories is {calorie}.")
            st.info(f"The calorie is above 50 percentile.Maintain this level")
        else:
            st.subheader(f"The estimated calories is {calorie}.")
            st.success("It's a low calorie food. You are eating right")