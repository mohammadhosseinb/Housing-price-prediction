# 🏠 DelTAX — Tehran House Price Prediction

DelTAX is a Python-based machine learning project for estimating residential property prices in **Tehran**.

The project collects real estate listings from **Divar** using Selenium, cleans and stores the collected data in a **MySQL database**, and then uses a **Random Forest Regression** model to estimate the price of a property based on its characteristics.

The model predicts the **estimated price per square meter**, which is then used to calculate the estimated total price of the property.

---

## 🎯 Project Goal

The main goal of this project is to build an end-to-end pipeline that can help estimate the market price of a house based on its characteristics.

Instead of requiring the user to manually calculate the total estimated price, the project takes the property information as input and returns:

* Estimated price per square meter
* Estimated total property price

---

## 🔄 Project Pipeline

The project consists of three main stages:

```text
             Divar
               │
               ▼
       Selenium Web Scraping
               │
               ▼
        Data Collection
               │
               ▼
        Data Cleaning
               │
               ▼
          MySQL Database
               │
               ▼
       Data Preparation
               │
               ▼
    Random Forest Regression
               │
               ▼
     Estimated Price / m²
               │
               ▼
      Total Estimated Price
```

The three Python files are designed to be executed in this order:

```text
deltax_web.py
      ↓
deltax_database.py
      ↓
deltax_home.py
```

---

## 🕷️ 1. Web Scraping — `deltax_web.py`

The first stage collects real estate listings from **Divar** using Selenium.

The scraper is designed for listings in **Tehran** and can collect approximately **1,000+ property listings**, depending on the amount of available data.

The collected information includes property characteristics such as:

* Property price
* Area
* Number of rooms
* Construction year
* Elevator
* Parking
* Storage room
* Neighborhood
* Other relevant listing information

Selenium is used to automate the process of navigating through the listings and collecting the required information.

---

## 🧹 2. Data Cleaning & Database — `deltax_database.py`

After collecting the data, the next stage processes and cleans the dataset.

Real-world scraped data can contain incorrect, incomplete, or unrealistic values. Therefore, the collected listings are cleaned before being used for machine learning.

Examples include removing listings with unrealistic or invalid prices.

After preprocessing, the cleaned data is stored in a **MySQL database**.

This makes the data easier to manage and allows the machine learning stage to work with structured and cleaned data.

---

## 🤖 3. Machine Learning — `deltax_home.py`

The final stage uses **Scikit-learn** to build a house price prediction model.

The machine learning algorithm used in this project is:

**Random Forest Regression**

The target variable is:

```text
Price per Square Meter
```

Instead of directly predicting the total price of a property, the model estimates the price per square meter.

The total estimated price can then be calculated as:

```text
Estimated Total Price
=
Predicted Price per m² × Property Area
```

This approach also makes the prediction easier to interpret.

---

## 📥 Model Inputs

The prediction model uses the following property characteristics:

| Feature           | Description                     |
| ----------------- | ------------------------------- |
| Area              | Property area in square meters  |
| Rooms             | Number of rooms                 |
| Construction Year | Year the property was built     |
| Elevator          | `0` = No, `1` = Yes             |
| Parking           | `0` = No, `1` = Yes             |
| Storage           | `0` = No, `1` = Yes             |
| Neighborhood      | Property neighborhood in Tehran |

Example:

```text
Area: 100 m²
Rooms: 2
Construction Year: 1398
Elevator: 1
Parking: 1
Storage: 1
Neighborhood: ...
```

The model then estimates the price per square meter and calculates the approximate total property price.

---

## 🧠 Technologies Used

* **Python**
* **Selenium**
* **MySQL**
* **Scikit-learn**
* **Pandas**
* **NumPy**
* **Random Forest Regression**

---

## 📁 Project Structure

```text
Housing-price-prediction/
│
├── deltax_web.py
├── deltax_database.py
├── deltax_home.py
├── README.md
└── requirements.txt
```

### `deltax_web.py`

Collects Tehran real estate listings from Divar using Selenium.

### `deltax_database.py`

Cleans the collected data and stores it in MySQL.

### `deltax_home.py`

Loads the prepared data, trains the Random Forest regression model, and estimates property prices.

---

## 🚀 How It Works

Run the project in the following order:

### 1. Collect the data

```bash
python deltax_web.py
```

This starts the scraping process and collects property listings from Divar.

### 2. Process and store the data

```bash
python deltax_database.py
```

The collected data is cleaned and stored in MySQL.

### 3. Predict the property price

```bash
python deltax_home.py
```

The machine learning model uses the prepared dataset to estimate the price per square meter and the total estimated price.

---

## 📊 Prediction Example

A user can provide information such as:

```text
Area: 100 m²
Rooms: 2
Construction Year: 1398
Elevator: 1
Parking: 1
Storage: 1
Neighborhood: ...
```

The model returns an estimated price per square meter.

The total estimated property price is then calculated automatically:

```text
Estimated Price per m² × Area
=
Estimated Total Property Price
```

---

## ⚠️ Limitations

This project is intended as a **personal machine learning project and educational implementation**.

The predicted price should be considered an estimation rather than a guaranteed market price.

Real estate prices can be affected by many factors, including:

* Exact location
* Street and building position
* Property condition
* Renovation quality
* Floor
* View
* Building age
* Market conditions
* Listing accuracy

Additionally, the model is trained using scraped listing data, and listing prices may differ from actual transaction prices.

---

## 🔮 Future Improvements

Possible improvements for future versions include:

* Collecting a larger dataset
* Adding more Tehran neighborhoods
* Adding more property features
* Comparing Random Forest with other regression algorithms
* Hyperparameter tuning
* Improving data preprocessing
* Adding model evaluation metrics
* Building a simple web interface for price prediction
* Automating the complete data collection and training pipeline

---

## 📌 Project Purpose

This project was developed as a personal **Machine Learning / Data Science project** to practice building an end-to-end machine learning pipeline using real-world data.

It demonstrates the integration of:

```text
Web Scraping
     +
Data Cleaning
     +
Database Management
     +
Machine Learning
     =
End-to-End Prediction System
```

---

## 👨‍💻 Author

**Mohammad Hossein**

This project was developed for educational and portfolio purposes.
