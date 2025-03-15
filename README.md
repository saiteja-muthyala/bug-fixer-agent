# 🌤 Weather Trend Forecasting using LSTM & Prophet  

## 🚀 Project Overview  
This project analyzes global weather patterns using **LSTM (Deep Learning)** and **Facebook Prophet** for trend forecasting.  

## 📂 Dataset  
- **Source:** Kaggle - Global Weather Repository  
- **Size:** 58,853 records  
- **Features:** Temperature, humidity, wind speed, air quality, etc.  

## 📊 Methodology  
1️⃣ **Data Cleaning & Preprocessing**  
   - Converted `last_updated` to **datetime format**.  
   - Handled **missing values & outliers**.  
   - Normalized data using **MinMaxScaler**.  

2️⃣ **Exploratory Data Analysis (EDA)**  
   - Visualized temperature trends.  
   - Identified correlations between weather features.  
   - Detected anomalies in data.  

3️⃣ **Forecasting Models**  
   - ✅ **LSTM (Deep Learning)** → High-accuracy weather trend forecasting.  
   - ✅ **Prophet (Explainability)** → Auto-detects trends & seasonality.  

4️⃣ **Model Evaluation**  
   - **MAE (Mean Absolute Error):** XX.XX  
   - **RMSE (Root Mean Squared Error):** XX.XX  
   - **Performance comparison:** LSTM vs Prophet  

## 📌 Key Findings  
📉 **Temperature trends:** Found seasonal fluctuations across regions.  
📈 **LSTM model:** Achieved high accuracy with optimized layers.  
📊 **Prophet analysis:** Showed clear seasonal trends in weather data.  

## 💡 Future Improvements  
🔹 Tune hyperparameters further for better accuracy.  
🔹 Integrate real-time weather data APIs.  
🔹 Extend analysis to extreme weather event predictions.  

## 📁 Files in This Repo  
- `weather_forecasting.ipynb` → Jupyter Notebook with all steps.  
- `README.md` → This project documentation.  
- `forecast_results.csv` → Predicted temperature trends.  

## 🛠️ Technologies Used  
✅ **Python, TensorFlow, Keras, Pandas, Matplotlib**  
✅ **LSTM, Prophet, ARIMA, MinMaxScaler**  

---

## **📌 How to Run This Project**
1️⃣ **Clone the Repository**  
```bash
git clone https://github.com/yourusername/weather_forecasting.git
cd weather_forecasting
