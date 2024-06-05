
import streamlit as st
import pickle
import pandas as pd

# Loading the saved model, scaler, label encoder, and SOPs
model = pickle.load(open('model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))
label_encoder = pickle.load(open('label_encoder_y.pkl', 'rb'))
sops = pickle.load(open('sops.pkl', 'rb'))

# Streamlit app
st.title('Machine Failure Prediction')
st.write("Enter the parameters to predict machine failure:")

def main():
    air_temperature = st.slider("Air temperature", 295, 305)
    process_temperature = st.slider("Process temperature", 306, 314)
    rotational_speed = st.slider("Rotational speed", 1168, 2886)
    torque = st.slider("Torque", 3.8, 76.6)
    tool_wear = st.slider("Tool wear", 0, 253)
    type = st.selectbox("Type", ["L", "M", "H"])

    if st.button("Predict"):
        mapping = {'L': 0, 'M': 1, 'H': 2}
        input_data = pd.DataFrame({
            'Type': [mapping[type]],
            'Air temperature [K]': [air_temperature],
            'Process temperature [K]': [process_temperature],
            'Rotational speed [rpm]': [rotational_speed],
            'Torque [Nm]': [torque],
            'Tool wear [min]': [tool_wear],
            'Power': [torque * rotational_speed]
        })

        # Normalize the inputs using the saved scaler
        input_data_scaled = scaler.transform(input_data)

        # Predict
        prediction = model.predict(input_data_scaled)
        prediction_proba = model.predict_proba(input_data_scaled)

        prediction_label = label_encoder.inverse_transform(prediction)[0]
        prediction_proba_dict = {label_encoder.inverse_transform([i])[0]: proba for i, proba in enumerate(prediction_proba[0])}

        st.write(f"Prediction: {prediction_label}")
        st.write("Prediction probabilities:")
        st.write(prediction_proba_dict)

        st.write("Standard Operating Procedure:")
        st.write(sops[prediction_label])

        if prediction_label != "No Failure":
            st.write("Action: Need maintenance")
        else:
            st.write("Action: No action required")

if __name__ == "__main__":
    main()
