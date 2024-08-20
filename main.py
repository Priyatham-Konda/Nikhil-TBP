import streamlit as st
import joblib
import pandas as pd

st.set_page_config(
    page_title="Main Page",
    page_icon="👋",
)

# Custom CSS to increase font size and change font style
st.markdown("""
<style>
    .big-font {
        font-size: 300%;
        font-style: san-serif; /* Change font style here */
    }
</style>
""", unsafe_allow_html=True)

model = joblib.load('random_forest_model.pkl')
request = {
    "MEAN_RR": [885.1578],
    "MEDIAN_RR": [853.7637],
    "SDRR": [140.9727412],
    "pNN25": [11.13333333],
    "pNN50": [0.533333333],
    "HR": [69.49995211]
}

# data = request.json
df = pd.DataFrame(request)
predictions = model.predict(df)
print(predictions)
st.markdown('<p class="big-font">Predictions: {}</p>'.format(predictions.tolist()[0]), unsafe_allow_html=True)