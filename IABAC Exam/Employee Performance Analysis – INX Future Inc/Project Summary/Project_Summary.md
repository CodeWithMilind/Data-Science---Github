# 📊 Project Summary: Employee Performance Analysis

## 1. Project Title
**Employee Performance Analysis – INX Future Inc.**

---

## 2. Business Problem Statement
INX Future Inc., a leading organization in data analytics and automation solutions, faces challenges in managing employee performance effectively. The existing performance evaluation process relies heavily on subjective assessments, which may introduce bias and inconsistency.

To overcome this limitation, the organization aims to adopt a data-driven approach to identify key factors influencing employee performance and to predict performance ratings objectively. This approach supports fair appraisals, improved workforce planning, and targeted talent management strategies.

---

## 3. Objective of the Project
The primary objective of this project is to develop a machine learning–based system that predicts employee performance ratings (on a scale of 1 to 4) using demographic, professional, and workplace-related attributes.

This system assists the Human Resources department in identifying high-performing employees, employees requiring improvement, and opportunities to enhance retention and productivity.

---

## 4. Dataset Description
- **Source:** INX Future Inc. internal employee dataset (Excel format)
- **Dataset Size:** 1200 employee records with 28 features
- **Feature Types:**
  - **Categorical Features:** Gender, Education Background, Marital Status, Department, Job Role, Business Travel Frequency, Overtime
  - **Numerical Features:** Age, Distance From Home, Hourly Rate, Total Work Experience, Years at Company, Years with Current Manager, etc.
- **Target Variable:**  
  - **Performance Rating**
    - 1 – Low  
    - 2 – Good  
    - 3 – Excellent  
    - 4 – Outstanding  

---

## 5. Exploratory Data Analysis (EDA)
Exploratory Data Analysis was conducted to understand data distribution, patterns, and relationships. Key insights include:

- Performance varies significantly across departments such as Sales, Development, HR, and Finance.
- Higher Environment Satisfaction and Job Satisfaction levels are associated with better performance ratings.
- Employees receiving higher salary hike percentages tend to perform better.
- Better work-life balance contributes positively to employee performance.
- Years in the current role and years with the current manager indicate employee stability and performance.

---

## 6. Data Preprocessing Steps
The following preprocessing steps were applied to prepare the dataset for modeling:

- **Data Cleaning:** Verified missing values and removed duplicates where necessary.
- **Feature Removal:** Dropped `EmpNumber` as it is a unique identifier with no predictive value. Removed `Attrition` to prevent data leakage.
- **Encoding Techniques:**
  - Manual encoding for ordinal variables such as Education Background, Business Travel Frequency, Gender, and Overtime.
  - Frequency encoding for high-cardinality categorical variables like Job Role and Department.
- **Scaling:** Feature scaling was not applied, as Random Forest models are invariant to feature scaling.

---

## 7. Feature Selection Approach
A subset of **8 high-impact features** was selected to build a robust and interpretable model.

### Selected Features
- Age  
- Distance From Home  
- EmpEnvironmentSatisfaction  
- EmpJobSatisfaction  
- EmpJobInvolvement  
- EmpLastSalaryHikePercent  
- TrainingTimesLastYear  
- OverTime  

### Justification
- **Business Relevance:** These features are directly actionable and influence employee motivation and productivity.
- **Model-Based Importance:** Random Forest feature importance analysis highlighted these variables as major contributors.
- **Model Simplicity:** Reducing the feature count minimizes noise, avoids overfitting, and simplifies deployment.

---

## 8. Model Selection and Justification
- **Chosen Model:** Random Forest Classifier

### Reasons for Selection
- High predictive accuracy through ensemble learning
- Ability to capture non-linear relationships
- Robustness against overfitting
- Effective handling of class imbalance

---

## 9. Model Pipeline and Training Process
A Scikit-Learn `Pipeline` was implemented to maintain consistency between training and inference.

- **Pipeline Workflow:**
  1. Input of selected features
  2. Random Forest Classifier (`n_estimators = 200`)
- **Data Split:** 80% training and 20% testing
- **Model Persistence:** The trained pipeline was saved as  
  `employee_performance_rf_pipeline.pkl`

---

## 10. Model Evaluation Metrics
The model was evaluated using standard classification metrics:

- **Accuracy:** Overall correctness of predictions
- **Precision:** Reliability of predicted classes
- **Recall:** Ability to identify all relevant performance categories
- **F1-Score:** Balanced metric combining precision and recall

---

## 11. Deployment Overview
The trained model was deployed using a **Django-based web application**.

- HTML-based form for user input
- Django backend loads the saved pickle model
- Real-time prediction of employee performance

**Live Application URL:**  
https://iammilind.pythonanywhere.com

---

## 12. Sample Input and Output Explanation
**Sample Input:**
- Age: 30  
- Distance From Home: 5 km  
- Environment Satisfaction: High  
- Job Satisfaction: Very High  
- Job Involvement: High  
- Last Salary Hike: 15%  
- Training Times Last Year: 3  
- OverTime: No  

**Predicted Output:**
- **Performance Rating:** 3 (Excellent)

Sample input and output screenshots are available in the `data/external` folder.

---

## 13. Business Impact
- Enables data-driven performance evaluations
- Supports employee retention and targeted training programs
- Reduces bias in appraisal processes

---

## 14. Limitations of the Current System
- Limited dataset size may restrict generalization
- Behavioral and psychometric factors are not included
- Model retraining is not automated

---

## 15. Future Enhancements
- Periodic retraining with new appraisal data
- Inclusion of textual feedback analysis
- Cloud-based deployment for enterprise scalability
- Interactive dashboards for HR analytics

---

## 16. Conclusion
This project demonstrates how machine learning can transform HR decision-making. By predicting employee performance accurately, INX Future Inc. can implement fairer evaluations, improve workforce productivity, and drive organizational growth.
