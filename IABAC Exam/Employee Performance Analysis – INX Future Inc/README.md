# Employee Performance Analysis – INX Future Inc.

## 📌 Project Title
**Employee Performance Analysis – INX Future Inc.**

---

## 🎯 Project Objective
The main objective of this project is to analyze the factors affecting employee performance at INX Future Inc. and to build a machine learning model that predicts employee performance ratings.  
This system helps the Human Resources department make data-driven decisions related to talent management, performance appraisal, and employee retention strategies.

---

## 🛠 Technologies Used
- **Python:** Primary programming language.
- **Pandas & NumPy:** Data manipulation and numerical operations.
- **Matplotlib & Seaborn:** Data visualization and insight generation.
- **Scikit-Learn:** Building the Random Forest machine learning model and pipeline.
- **Django:** Developing the web application for model deployment.
- **HTML/CSS:** Front-end interface for user interaction.
- **SQLite:** Database used in the Django application.

---

## 📂 Project Execution Flow
To understand and run the project successfully, please follow the steps below in the given order.

---

### 🔹 Step 1: Exploratory Data Analysis (EDA)
- **File:**  
  `src/Data Processing/data_exploratory_analysis.ipynb`
- **Description:**  
  This notebook is the starting point of the project. It is used to understand the dataset structure, analyze distributions, identify missing values, detect outliers, and gain initial business insights related to employee performance.

---

### 🔹 Step 2: Visual Analysis
- **File:**  
  `src/visualization/visuals.ipynb`
- **Description:**  
  This notebook focuses on visualizing the data using charts and graphs. It helps in understanding relationships between different employee attributes such as age, experience, salary hike, and performance ratings.

---

### 🔹 Step 3: Data Preprocessing
- **File:**  
  `src/Data Processing/data_processing.ipynb`
- **Description:**  
  This notebook performs data cleaning and transformation tasks. It includes handling missing values, encoding categorical variables, scaling numerical features, and preparing the final dataset required for model training.

---

### 🔹 Step 4: Model Training and Pipeline Creation
- **File:**  
  `src/Data Processing/Pipeline.ipynb`
- **Description:**  
  This is the core machine learning notebook. A Random Forest Classifier is trained using a machine learning pipeline.  
  After training, the complete pipeline is saved as a `.pkl` file inside the `src/models/` directory for reuse during deployment.

- **Output Model File:**  
  `src/models/employee_performance_rf_pipeline.pkl`

---

### 🔹 Step 5: Web Application Deployment
- **Description:**  
  A Django-based web application has been developed to demonstrate the trained machine learning model.  
  The application takes employee-related inputs from the user (such as HR personnel) and predicts the employee performance rating in real time using the saved `.pkl` model.

---

## 🌐 Live Application Demo
The employee performance prediction system has been successfully deployed using Django on a free hosting platform.

**Live Demo URL:**  
https://iammilind.pythonanywhere.com

The application allows users to enter employee details and instantly view the predicted performance outcome.

---

## 📁 Project Structure Overview
- `data/` – Raw, processed, and external data resources  
- `src/` – Data processing, visualization, and model development notebooks  
- `models/` – Saved machine learning pipeline (`.pkl`)  
- `djangoapp/` – Django web application for deployment  
- `Project Summary/` – Project documentation, summary, and test cases  

---

## 📌 Notes
- This project demonstrates an **end-to-end data science lifecycle**, from data exploration to real-world deployment.
- The project is created for **IABAC Certified Data Scientist (CDS) evaluation**.
- Emphasis is placed on clarity, correctness, and practical implementation.

---

## ✅ Conclusion
This project showcases how machine learning can be effectively used to support HR decision-making by predicting employee performance. By combining data analysis, machine learning, and web deployment, the system provides a complete and practical solution aligned with real-world business needs.
