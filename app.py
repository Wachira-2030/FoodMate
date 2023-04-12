import streamlit as st
import pandas as pd
import numpy as np
import pickle
from recipe_recommender import RecipeRecommender

# Unpickling the instance from the file
#with open('recommender.pickle', 'rb') as f:
 #   recommender = pickle.load(f)

#pickle_in = open("recommender.pkl")
#recommender = pickle.load(pickle_in)

df = pd.read_csv("cleaned_data.csv")

recommender = RecipeRecommender(df)

def app():
    st.title("Recipe Recommender")
    
    target_calories = st.slider("Select your target calories:", 0, 1000, 500, 10)
    
    num_recommendations = st.slider("Select the number of recommendations:", 1, 10, 5, 1)
    
    if st.button("Recommend"):
        recommendations = recommender.recommend(target_calories, num_recommendations)
        for i, recommendation in enumerate(recommendations):
            st.write(f"Recipe {i+1}")
            st.write(f"Name: {recommendation[0]}")
            st.write(f"Ingredients: {recommendation[1]}")
            st.write(f"Steps: {recommendation[2]}")

if __name__ == "__main__":
    app()
