# 🌾 Agricultural Yield Prediction App

Welcome to the **Agricultural Yield Prediction App**! This application leverages the power of the [**Granite-3B**](https://huggingface.co/ibm-granite/granite-3b-code-base) to predict agricultural yield based on various factors such as climate zone, region, soil type, and more. The app is built with **Streamlit**, providing an interactive and user-friendly interface for making predictions.

## 🚀 Demo

👉 [**Try the live demo here!**](https://huggingface.co/spaces/Abbas0786/Agricultural-Yield-Prediction)

## 📋 Features

- 🌎 **Climate Zone and Region:** Specify the climate zone and region of your farm to get tailored predictions.
- 🌱 **Soil and Crop Type:** Input soil type and crop variety to enhance prediction accuracy.
- 🌧️ **Weather Conditions:** Include historical weather data, current weather conditions, and soil moisture levels.
- 💧 **Irrigation and Fertilization:** Specify irrigation methods and fertilizer details.
- 🖊️ **Custom Prompts:** Use custom prompts for personalized predictions.
- 📊 **Yield Units and Prediction Period:** Define the units for yield (e.g., tons per acre) and the prediction period (e.g., weekly, monthly).

## 🛠️ Technologies Used

- **Streamlit:** A framework for building interactive web apps with Python.
- **IBM API:** Used for generating yield predictions using the Granite-3b-code-base model.
- **Python:** Backend logic and API integration.
- **.env File:** For secure API key management.

## 📦 Installation

Follow these steps to set up the app on your local machine:

1. **Clone the repository:**

    ```bash
    https://github.com/bilal77511/Agriculture-Yield-Prediction-App.git
    ```

2. **Navigate to the project directory:**

    ```bash
    cd agricultural-yield-prediction-app
    ```

3. **Install the required Python packages:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up your API key:**

    .env.example file is provided to add secrets. Add your own IBM_API_KEY, IBM_URL and PROJECT_ID  
   ***Dont forget to rename .env.example to .env after addding your own IBM_API_KEY, IBM_URL and PROJECT_ID***

6. **Run the app:**

    ```bash
    streamlit run app.py
    ```

## 🖥️ How to Use

1. **Open the app using the demo link provided above or run it locally using Streamlit.**
2. **Choose the input method:** Use a custom prompt or fill in parameters for a structured input.
3. **Enter the required details:** Depending on your chosen method, fill in climate zone, region, soil type, weather conditions, and other relevant fields.
4. **Click the "Predict Yield" button** to generate the yield prediction.
5. **Clear inputs** using the "Clear" button if you want to start over.

## 📷 Screenshot

![Agricultural Yield Prediction App](https://raw.githubusercontent.com/mj-awad17/Agriculture-Yield-Prediction-App/main/image.jpg)

## 🔑 API Key Setup

To use this app, you need a Groq API key:

1. Sign up on [IBM](https://cloud.ibm.com/) to get your API key.
2. Replace `"your_ibm_api_key_here"` in the script with your actual API key.
3. You can find the end point from the watson documntation or here is an example endpoint "https://us-south.ml.cloud.ibm.com"
4. You can find project id in your project settings.

## 📝 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.


## 🌟 Acknowledgements

- Thanks to [IBM-Watsonai](https://ibm.com/) challange for providing the API for yield prediction.
- Thanks to the [Streamlit](https://streamlit.io/) team for creating such an intuitive tool for building web apps.

## 📬 Contact

For any questions or feedback, please feel free to reach us!

- [Muhammad Jawad](https://www.linkedin.com/in/muhammad-jawad-86507b201/)
- [Muhammad Bilal](https://www.linkedin.com/in/muhammad-bilal-a75782280/)
- [Ghulam Abbas](https://www.linkedin.com/in/ghulam-abbas-310b7a302/)
- [Alisha Ashraf](https://www.linkedin.com/in/alisha-ashraf-b73404301/)
- [Hamid Raza](https://www.linkedin.com/in/hamid-raza-302baa286/)
