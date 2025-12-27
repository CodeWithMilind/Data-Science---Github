# Project Title
**Employee Performance Analysis – INX Future Inc.**

# Project Objective
The main objective of this project is to analyze the factors affecting employee performance at INX Future Inc. and to build a machine learning model that predicts employee performance ratings. This system aids the Human Resources department in making data-driven decisions regarding talent management, appraisals, and retention strategies.

# Technologies Used
- **Python:** Primary programming language.
- **Pandas & NumPy:** For data manipulation and numerical operations.
- **Matplotlib & Seaborn:** For data visualization and insights.
- **Scikit-Learn:** For building the Random Forest machine learning model and pipeline.
- **Django:** For developing the web application to deploy the model.
- **HTML/CSS:** For the front-end user interface of the web application.

# Project Execution Flow
To understand and run the project successfully, please follow the steps below in the given order:

### Step 1: Exploratory Data Analysis (EDA)
- **File:** `src/Data Processing/data_exploratory_analysis.ipynb`
- **Description:** This notebook is the starting point. It is used to perform initial data analysis to understand the structure of the dataset, check for missing values, and identify key patterns and correlations between features.

### Step 2: Visual Analysis
- **File:** `src/visualization/visuals.ipynb`
- **Description:** This file focuses on visualizing the data. It generates various charts and graphs to derive deeper insights into how different factors (like age, department, and salary hike) impact employee performance.

### Step 3: Data Preprocessing
- **File:** `src/Data Processing/data_processing.ipynb`
- **Description:** This notebook handles the cleaning and transformation of data. It performs tasks such as encoding categorical variables (converting text to numbers), handling any remaining data issues, and preparing the final dataset for model training.

### Step 4: Model Training and Pipeline
- **File:** `src/Data Processing/Pipeline.ipynb`
- **Description:** This is the core modeling file. It trains the Random Forest Classifier using a machine learning pipeline. After training, the model is saved as a `.pkl` file (serialized object) inside the `src/models/` directory for future use.

### Step 5: Web Application Deployment
- **Description:** A Django-based web application has been developed to demonstrate the model's capabilities. It uses the saved `.pkl` model file to take inputs from a user (HR Manager) and predict the performance rating of an employee in real-time.
- **Note:** The application is designed to be hosted on a free platform, and a public link will be provided for easy access and demonstration purposes.
