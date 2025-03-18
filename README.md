# 🌤 Weather Trend Forecasting using LSTM & Prophet  

## 🚀 Project Overview  
This project analyzes global weather trends using **LSTM (Deep Learning)** and **Facebook Prophet** for time series forecasting. The goal is to predict temperature changes and identify seasonal patterns using advanced AI models.  

## 📂 Dataset  
- **Source:** [Kaggle - Global Weather Repository](https://www.kaggle.com/datasets/nelgiriyewithana/global-weather-repository/code)  
- **Size:** 58,853 records  
- **Features:** Temperature, humidity, wind speed, air quality, etc.  

## 📊 Methodology  
1️⃣ **Data Preprocessing**  
   - Converted `last_updated` to **datetime format**  
   - Handled **missing values & outliers**  
   - Normalized data using **MinMaxScaler**  

2️⃣ **Exploratory Data Analysis (EDA)**  
   - Visualized temperature trends over time  
   - Identified correlations between weather features  
   - Detected anomalies in weather patterns  

3️⃣ **Forecasting Models**  
   - ✅ **LSTM (Deep Learning):** Captures long-term dependencies for accurate forecasting  
   - ✅ **Prophet (Explainability):** Auto-detects trends & seasonality in data  

4️⃣ **Model Evaluation**  
   - **Mean Absolute Error (MAE):** 42.76  
   - **Root Mean Squared Error (RMSE):** 47.57  
   - **Performance Comparison:** LSTM vs Prophet  

---

## 📌 Key Findings  
📉 **Temperature Trends:** Seasonal fluctuations observed across regions  
📈 **LSTM Model:** Achieved high accuracy with optimized layers  
📊 **Prophet Analysis:** Identified clear seasonal trends in weather data  

## 💡 Future Improvements  
🔹 Fine-tune hyperparameters for even better accuracy  
🔹 Integrate real-time weather data APIs for live forecasting  
🔹 Extend analysis to predict extreme weather events  

---

## 📁 Files in This Repository  
📜 `weather_forecasting.ipynb` → Jupyter Notebook with complete analysis  
📜 `README.md` → Project documentation (this file)  
📜 `forecast_results.csv` → Predicted temperature trends  
📜 `requirements.txt` → List of dependencies for easy setup  

---

## 🛠️ Technologies Used  
✅ **Python, TensorFlow, Keras, Pandas, Matplotlib**  
✅ **LSTM, Prophet, ARIMA, MinMaxScaler, Seaborn**  

---

## **📌 How to Run This Project**  
1️⃣ **Clone the Repository**  
```bash
git clone https://github.com/saiteja-muthyala/-Weather-Trend-Forecasting.git
cd -Weather-Trend-Forecasting
```
2️⃣ **Install Dependencies**
```bash
pip install -r requirements.txt

```
3️⃣ **Run the Jupyter Notebook**
```
bash
jupyter notebook
```
📬 **Contact**
📧 **Email**: tejasai48548012@gmail.com
🔗 **GitHub**: saiteja-muthyala
