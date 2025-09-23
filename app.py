import streamlit as st
import pickle

# Load trained model
model = pickle.load(open("model.pkl", "rb"))

st.title("🚢 Titanic Survival Prediction")

# User inputs
pclass = st.selectbox("Passenger Class (1 = First, 2 = Second, 3 = Third)", [1, 2, 3])
sex = st.selectbox("Sex", ["male", "female"])
age = st.slider("Age", 0, 80, 25)
sibsp = st.number_input("Number of Siblings/Spouses Aboard", 0, 10, 0)
parch = st.number_input("Number of Parents/Children Aboard", 0, 10, 0)
fare = st.number_input("Ticket Fare", 0.0, 600.0, 32.0)
embarked = st.selectbox("Port of Embarkation", ["C", "Q", "S"])

# Convert categorical values to numeric (like during training)
sex = 1 if sex == "female" else 0
embarked_map = {"C": 0, "Q": 1, "S": 2}
embarked = embarked_map[embarked]

features = [[pclass, sex, age, sibsp, parch, fare, embarked]]

# Prediction
if st.button("Predict"):
    prediction = model.predict(features)
    if prediction[0] == 1:
        st.success("🎉 This passenger would have SURVIVED!")
    else:
        st.error("💀 This passenger would NOT have survived.")
