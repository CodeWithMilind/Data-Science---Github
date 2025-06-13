# 📊 Loan Approval Prediction Project

This project focuses on predicting whether a loan will be approved or not based on applicant details. It involves complete data cleaning, preprocessing, visualization, and implementation of multiple machine learning models like Logistic Regression, Linear Regression, and K-Nearest Neighbors.

---

## 📂 Project Structure

├── loan_approved.csv # Raw original dataset
├── FinalData.csv # Final cleaned and preprocessed dataset
├── practice.ipynb # Rough notebook for initial practice and testing
├── LogReg.ipynb # Logistic Regression model implementation
├── LinReg.ipynb # Linear Regression model (for learning/comparison)
├── KNN.ipynb # K-Nearest Neighbors model
├── README.md # Project documentation

---

## 📁 Dataset

### 📌 loan_approved.csv

Original dataset with raw information of loan applicants.

### 📌 FinalData.csv

This is the **final cleaned and preprocessed dataset**, created after:

- Handling missing values
- Encoding categorical variables
- Removing outliers
- Dropping unimportant features (like `Loan_Amount_Term`)
- Normalizing/transforming features (if needed)
- Performing data visualization to understand feature relationships

---

## ⚙️ Technologies & Libraries Used

- Python
- Pandas, NumPy
- Matplotlib, Seaborn
- Scikit-learn

---

## 📊 Exploratory Data Analysis (EDA)

- Heatmaps to check correlation
- Count plots and boxplots for visualizing distributions and outliers
- Relationship between target and important features like:
  - `Credit_History`
  - `LoanAmount`
  - `ApplicantIncome` & `CoapplicantIncome`

---

## 🤖 Models Implemented

### ✅ `LogReg.ipynb` — Logistic Regression

- Used for binary classification (Loan Approved or Not)
- Evaluation Metrics:
  - Accuracy
  - Precision, Recall, F1-score
  - Confusion Matrix

### ✅ `LinReg.ipynb` — Linear Regression

- Applied for educational comparison, not suitable for classification
- Helped understand numeric prediction concept

### ✅ `KNN.ipynb` — K-Nearest Neighbors

- Used for classification
- Compared performance with Logistic Regression

---

## 📈 Model Performance (Logistic Regression)

| Metric    | Value (Approx.)     |
| --------- | ------------------- |
| Accuracy  | 72%                 |
| Precision | 69–77% (class-wise) |
| Recall    | 64–80% (class-wise) |
| F1-score  | 70–74% (class-wise) |

---

## 🧠 Key Learnings

- Importance of feature selection in model performance
- Categorical encoding, outlier removal, and EDA improved accuracy
- Logistic Regression works well for binary classification tasks
- Learned how different models behave with the same dataset

---

## 🪄 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/codewithmilind/loan-approval-project.git
   cd loan-approval-project
   ```
