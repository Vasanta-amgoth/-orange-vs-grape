**Orange vs Grapefruit Prediction**



**Orange vs Grapefruit Predictor**
This project uses a machine learning model to classify citrus fruits as either **orange** or **grapefruit** based on their physical characteristics. Built with **Streamlit**, this web application provides a user-friendly interface for predicting fruit type based on user input.



**Key Features:**
- **User-Friendly Interface:** Built with Streamlit for easy interaction.
- **Machine Learning Model:** Utilizes a pre-trained **Random Forest classifier**.
- **Predictive Inputs:**
  - Diameter (in cm)
  - Weight (in grams)
  - RGB color values (red, green, blue)
- **Real-Time Prediction:** Instant classification of the fruit upon input.



**How to Use:**
1. Input the fruit's diameter, weight, and RGB color values.
2. Click the **"Predict Fruit"** button.
3. The app displays the predicted fruit: **Orange** or **Grapefruit**.



**Files:**
- `orange_vs_grapefruit_streamlit.py`: Streamlit-based script to deploy the app.
- `citrus_pred.pkl`: Pre-trained machine learning model (Random Forest).


**Technologies Used:**
- **Python**
- **Streamlit** (for UI)
- **Joblib** (for loading the model)
- **NumPy** (for data processing)



 **Setup Instructions:**
1. Clone the repository.
2. Ensure you have Python and the necessary dependencies installed.
3. Run the app using the command:
   streamlit run orange_vs_grapefruit_streamlit.py
4. Access the app in your browser



**Future Improvements:**
- Add more fruit types for classification.
- Enhance the model with additional features for better accuracy.

