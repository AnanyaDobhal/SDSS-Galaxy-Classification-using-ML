# 🌌 Sloan Digital Sky Survey (SDSS) Galaxy Classification using Machine Learning

[![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-Web%20Framework-black?logo=flask)](https://flask.palletsprojects.com/)
[![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Scikit--Learn-orange?logo=scikitlearn)](https://scikit-learn.org/)
[![Dataset](https://img.shields.io/badge/Dataset-Kaggle-blue?logo=kaggle)](https://www.kaggle.com/datasets/bryancimo/sdss-galaxy-classification-dr18)
[![License](https://img.shields.io/badge/License-MIT-green)]()

### 🧠 Category: Machine Learning  
**Skills Used:** Python | Flask | Data Visualization | Data Preprocessing | Machine Learning | HTML | TensorFlow  

---

## 🚀 Project Overview
This project aims to classify galaxies from the **Sloan Digital Sky Survey (SDSS)** dataset using various machine learning algorithms.  
It automates the classification of galaxies based on their photometric parameters and helps astronomers analyze galaxy morphology efficiently.  

The system is deployed as a **Flask web application**, allowing users to input photometric attributes and receive the predicted **galaxy class** instantly.

---

## 🪐 Objectives
- To automate galaxy classification using ML models.  
- To perform data preprocessing and handle imbalance using **SMOTE**.  
- To evaluate multiple models and deploy the best-performing one using **Flask**.  
- To provide an interactive web interface for real-time galaxy classification.  

---

## 🧩 Project Flow
1. **Prior Knowledge**  
   Understanding galaxy morphology, redshift, and photometric parameters.

2. **Data Collection & Preparation**  
   - Dataset: [SDSS Galaxy Classification DR18 | Kaggle](https://www.kaggle.com/datasets/bryancimo/sdss-galaxy-classification-dr18)  
   - Contains 100,000 galaxy records with multiple photometric parameters.

3. **Data Preprocessing**  
   - Handle missing values.  
   - Change data types (`Subclass` → int).  
   - Feature scaling using `StandardScaler`.  
   - Feature selection using **SelectKBest**.  
   - Class imbalance handled with **SMOTE**.  
   - Split data into **Train (80%)** and **Test (20%)**.

4. **Exploratory Data Analysis (EDA)**  
   - Descriptive statistics.  
   - Visual, univariate, bivariate & multivariate analysis.  
   - Outlier handling and feature correlation visualization.

5. **Model Building**  
   Trained and evaluated multiple models:
   - Decision Tree Classifier  
   - Random Forest Classifier ✅ *(Best Model)*  
   - Logistic Regression  

6. **Model Deployment**  
   - Best model (`RF.pkl`) saved using **Pickle**.  
   - Integrated with Flask for deployment.  
   - User inputs photometric values via web form → model predicts galaxy class.

---

## 🧠 Machine Learning Models

| Model | Accuracy | Remarks |
|--------|-----------|----------|
| Decision Tree | 0.81 | Moderate performance |
| Logistic Regression | 0.78 | Baseline model |
| **Random Forest** | **0.85 (Test)** | ✅ Best performing model |



---

## 📊 Key Insights
- Achieved **85% test accuracy** using Random Forest Classifier.  
- Model generalized well with good recall and balanced class performance.  
- Class imbalance successfully mitigated via **SMOTE**.  

---

## 🧰 Technologies Used
- **Programming Language:** Python  
- **Libraries:** NumPy, Pandas, Matplotlib, Seaborn, Scikit-learn, Imbalanced-learn  
- **Web Framework:** Flask  
- **Deployment:** Pickle model integration with Flask app  
- **Frontend:** HTML, CSS  

---

## 🌐 Web Application Overview

### 🔸 Input Form
Users can enter photometric parameters manually into the form as shown below:

| Columns | Input Example |
|----------|----------------|
| i | 16.813 |
| z | 16.59408 |
| modelFlux_z | 230.3376 |
| petroRad_g | 3.955328 |
| petroRad_r | 4.087168 |
| petroFlux_z | 201.0571 |
| petroR50_u | 1.613005 |
| petroR50_g | 1.766743 |
| petroR50_i | 1.74353 |
| petroR50_r | 1.784977 |

**→ Click "Submit"** to generate the predicted galaxy classification result.

---

## ⚙️ How to Run the Project

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/SDSS-Galaxy-Classification.git
   cd SDSS-Galaxy-Classification

2. **Run the Flask app**
   ```bash
  python app.py

3. **Open in browser**
   ```bash
   http://127.0.0.1:5000/

## 📁 Project Structure
   ```bash
SDSS-Galaxy-Classification/
│
├── static/
│   └── (images)
│
├── templates/
│   ├── index.html
│   └── output.html
|   └── home.html
│
├── model/
│   └── RF.pkl
│
├── app.py
|── README.md

