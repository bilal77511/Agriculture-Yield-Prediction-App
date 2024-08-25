# Import required libraries
import os
import streamlit as st
from groq import Groq

# Set your API key (replace 'your_groq_api_key_here' with the actual API key)
os.environ["GROQ_API_KEY"] = "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"

# Initialize the Groq client
client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

# Function to handle predictions
def predict_yield(climate_zone=None, region=None, yield_units=None, farm_size=None, fertilizer_rate=None, 
                  fertilizer_type=None, historical_weather=None, temperature=None, soil_moisture=None, 
                  soil_type=None, weather_condition=None, crop_type=None, irrigation_method=None, 
                  prediction_period=None, custom_prompt=None):
    try:
        if custom_prompt:
            prompt = custom_prompt
        else:
            # Construct the prompt for the model using individual inputs
            prompt = (
                f"Predict the agricultural yield for a farm in the {climate_zone} climate zone, "
                f"located in the {region} region. The farm size is {farm_size} acres, and the desired yield units are {yield_units}. "
                f"The fertilizer application rate is {fertilizer_rate} using {fertilizer_type}. Historical weather data indicates {historical_weather}. "
                f"The average temperature is {temperature} degrees, soil moisture levels are {soil_moisture}, and the soil type is {soil_type}. "
                f"The current weather condition is {weather_condition}. The crop type is {crop_type}, and the irrigation method used is {irrigation_method}. "
                f"The yield prediction period is {prediction_period}."
            )

        # Call the Groq API
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            model="llama3-8b-8192",
        )

        # Return the response
        return chat_completion.choices[0].message.content

    except Exception as e:
        return f"An error occurred during prediction: {e}"

# Streamlit Interface
st.title("Agricultural Yield Prediction App")
st.write("Predict agricultural yield based on various factors.")

# Sidebar for input method selection
st.sidebar.title("Input Method")
input_method = st.sidebar.radio("Choose input method:", ("Use Custom Prompt", "Use Parameters"))

if input_method == "Use Parameters":
    # Sidebar inputs for parameters
    st.sidebar.title("Input Parameters")
    climate_zone = st.sidebar.text_input("Climate Zone")
    region = st.sidebar.text_input("Region")
    yield_units = st.sidebar.text_input("Desired Yield Units (e.g., tons per acre, bushels per acre)")
    farm_size = st.sidebar.text_input("Farm Size (acres or hectares)")
    fertilizer_rate = st.sidebar.text_input("Fertilizer Application Rate")
    fertilizer_type = st.sidebar.text_input("Fertilizer Type")
    historical_weather = st.sidebar.text_input("Historical Weather Data")
    temperature = st.sidebar.text_input("Temperature (degrees)")
    soil_moisture = st.sidebar.text_input("Soil Moisture Levels")
    soil_type = st.sidebar.text_input("Soil Type")
    weather_condition = st.sidebar.text_input("Weather Condition")
    crop_type = st.sidebar.text_input("Crop Type")
    irrigation_method = st.sidebar.text_input("Irrigation Method")
    prediction_period = st.sidebar.text_input("Yield Prediction Period (e.g., weekly, monthly, seasonal)")
    custom_prompt = None

else:
    # Sidebar input for custom prompt
    st.sidebar.title("Custom Prompt")
    custom_prompt = st.sidebar.text_area("Enter your custom prompt here", value="Enter your prompt...")
    climate_zone = region = yield_units = farm_size = fertilizer_rate = fertilizer_type = historical_weather = None
    temperature = soil_moisture = soil_type = weather_condition = crop_type = irrigation_method = prediction_period = None

# Main page layout for buttons and output
col1, col2 = st.columns([1, 2])

# Clear button functionality
if col2.button("Clear"):
    st.rerun()

# Predict button and display result
if col1.button("Predict Yield"):
    prediction = predict_yield(climate_zone, region, yield_units, farm_size, fertilizer_rate, fertilizer_type,
                               historical_weather, temperature, soil_moisture, soil_type, weather_condition,
                               crop_type, irrigation_method, prediction_period, custom_prompt)
    st.write("Predicted Yield:", prediction)
