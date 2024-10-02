import os
import streamlit as st
from ibm_watsonx_ai import Credentials
from ibm_watsonx_ai.foundation_models import ModelInference
from ibm_watsonx_ai.metanames import GenTextParamsMetaNames as GenParams
from ibm_watsonx_ai.foundation_models.utils.enums import ModelTypes, DecodingMethods
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Define a function to run Watson AI prediction
def run_watson_granite(user_input):
    # Initialize the model inference with environment variables
    model_inference = ModelInference(
        model_id="ibm/granite-13b-chat-v2",  # Replace with your desired model ID
        params={
            GenParams.DECODING_METHOD: DecodingMethods.GREEDY,
            GenParams.TEMPERATURE: 0.5,
            GenParams.MIN_NEW_TOKENS: 10,
            GenParams.MAX_NEW_TOKENS: 1024
        },
        credentials=Credentials(
            api_key=os.getenv("IBM_API_KEY"),
            url=os.getenv("IBM_URL")
        ),
        project_id=os.getenv("PROJECT_ID")
    )

    # Define the system's role with parameters
    system_prompt = (
        "\nYou have to predict the desired crop yield and best crop based on the mentioned parameters."
    )

    # Combine system prompt with user input
    complete_prompt = user_input + " " + system_prompt
    print(complete_prompt)
    
    # Generate response from the model
    response = model_inference.generate(complete_prompt)
    results = response.get('results', [])

    del model_inference

    # Extract the generated text from the response
    generated_texts = [item.get('generated_text') for item in results]

    return generated_texts

# Streamlit app
st.title("Agricultural Yield Prediction Tool")

st.write("""
*Agricultural Yield Prediction Tool* helps you estimate crop yields based on a variety of factors.
By entering your details, we generate predictions for your agricultural yield based on the data provided.
""")

# Sidebar inputs for agricultural details
st.sidebar.header("Enter Agricultural Details")

location = st.sidebar.text_input("Location (GPS coordinates, city, state, or zip code)")
crop_type = st.sidebar.text_input("Crop Type (e.g., corn, wheat, soybeans, etc.)")
farm_size = st.sidebar.number_input("Farm Size (acres or hectares)", min_value=0.1, step=0.1)
soil_type = st.sidebar.text_input("Soil Type (e.g., clay, silt, loam, etc.)")
historical_weather_data = st.sidebar.text_area("Historical Weather Data (temperature, precipitation, sunshine hours)")
climate_zone = st.sidebar.text_input("Climate Zone or Region")
weather_forecast_integration = st.sidebar.text_input("Weather Forecast Integration (optional)")
soil_moisture_levels = st.sidebar.number_input("Soil Moisture Levels (%)", min_value=0.0, max_value=100.0, step=0.1)
fertilizer_application = st.sidebar.text_input("Fertilizer Application Rates and Types")
irrigation_system = st.sidebar.text_input("Irrigation System Information (e.g., drip, sprinkler, flood)")
crop_variety = st.sidebar.text_input("Crop Variety and Planting Date")
pest_management = st.sidebar.text_input("Pest and Disease Management Practices")
yield_prediction_period = st.sidebar.selectbox("Yield Prediction Period", ["weekly", "monthly", "seasonal"])
desired_yield_units = st.sidebar.selectbox("Desired Yield Units", ["tons per acre", "bushels per acre"])

# Prediction button
if st.button("Predict Yield"):
    # Prepare user input for the LLM with more prompt engineering
    user_input = f"""
    Location: {location}
    Desired Crop: {crop_type}
    Farm Size: {farm_size} {desired_yield_units.split()[1]}
    Soil Type: {soil_type}
    Historical Weather Data: {historical_weather_data}
    Climate Zone: {climate_zone}
    Weather Forecast Integration: {weather_forecast_integration}
    Soil Moisture Levels: {soil_moisture_levels}%
    Fertilizer Application: {fertilizer_application}
    Irrigation System: {irrigation_system}
    Crop Variety: {crop_variety}
    Pest Management: {pest_management}
    Yield Prediction Period: {yield_prediction_period}
    """

    # Call the LLM function
    response = run_watson_granite(user_input)

    # Display the predicted yield
    generated_text = response[0]  # Assuming the first item is the response
    st.write(f"**Yield Prediction:** {generated_text}")

# Footer
st.markdown("Developed by Muhammad Bilal, Ghulam Abbas, Muhammad Jawad, Hamid Raza, and Alisha Ashraf")
