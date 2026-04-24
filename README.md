## Machine Learning–Assisted Media Optimization for Lipid Production in Rhodotorula pacifica

## Overview

This project presents a machine learning–based framework for optimizing fermentation media to improve lipid production in Rhodotorula pacifica. The study integrates Response Surface Methodology (RSM), multiple machine learning regression models, model validation using Leave-One-Out Cross Validation (LOOCV), SHAP-based model interpretation, and process optimization using predictive modeling.

The best-performing model was deployed as an interactive Streamlit web application that allows users to predict lipid production, perform batch predictions, and identify optimal fermentation conditions.

This project demonstrates an end-to-end workflow including experimental design, machine learning modeling, model interpretation, optimization, and application development.

<img width="1983" height="793" alt="ChatGPT Image Apr 18, 2026, 09_54_23 PM" src="https://github.com/user-attachments/assets/ca640863-fb92-4d19-862f-cbec5650e80c" />


## Fermentation Parameters Used

# The machine learning model predicts lipid production based on the following fermentation variables:

Variable	Description
Glucose (% w/v)	Carbon source concentration
Ammonium sulphate (% w/v)	Nitrogen source concentration
Initial pH	Initial fermentation pH
Cultivation time (h)	Fermentation duration

Output: Lipid titer (g/L)

Machine Learning Models Implemented

The following regression models were trained and evaluated:

# Model	Description
ElasticNet	Linear regression with regularization
Decision Tree	Non-linear regression tree model
Random Forest	Ensemble tree-based model
XGBoost	Gradient boosting regression model

Model selection was performed using Leave-One-Out Cross Validation (LOOCV), and XGBoost achieved the best performance.

Model Performance Comparison
Model	RMSE	R² (LOOCV)
ElasticNet	Higher	Lower
Decision Tree	Medium	Medium
Random Forest	Low	High
XGBoost	Lowest	Highest

The XGBoost model showed the best predictive performance and was selected as the final model.

# Model Evaluation Metrics

The models were evaluated using:

R² Score
Adjusted R²
Mean Squared Error (MSE)
Root Mean Squared Error (RMSE)
Mean Absolute Error (MAE)
Leave-One-Out Cross Validation (LOOCV)
Train–Test Validation
Residual Analysis

# SHAP Model Interpretation

SHAP (SHapley Additive Explanations) was used to interpret the machine learning model and determine the importance of fermentation variables on lipid production.

The following SHAP analyses were performed:

SHAP summary plot
SHAP beeswarm plot
Feature dependence plots
Feature importance ranking

This helped identify the most influential parameters affecting lipid production.

# Media Optimization

Fermentation media optimization was performed using the trained XGBoost model by searching across the parameter space and predicting lipid production.

# Optimization workflow:

Define parameter ranges
Generate parameter combinations
Predict lipid production using ML model
Rank media compositions
Select optimal fermentation conditions

The optimized media conditions were exported as ranked optimization tables.

# Streamlit Web Application

A Streamlit web application was developed to allow users to interact with the machine learning model.

Link : https://fermentation-rsm-ml-optimization-hyanopgulfgrgs7xun8ttq.streamlit.app/

The application provides:

Single prediction for lipid titer
Batch prediction using CSV upload
Fermentation media optimization
Ranked optimization results
Model figures and SHAP plots
Visualization of model performance

The application is designed for local deployment and demonstration purposes.

# Project Structure
fermentation-RSM-ml-optimization
│
├── app.py
├── requirements.txt
├── README.md
│
├── data/
│   ├── data.csv
│   ├── FullDataset_Predictions_XGBoost.csv
│   └── Ranked_Media_Optimisation_XGBoost.csv
│
├── figures/
│   ├── ACTUAL_vs_PREDICTED_TESTSET.jpeg
│   ├── Model_Comparison_LOOCV.jpeg
│   ├── SHAP_BEESWARM.jpeg
│   ├── SHAP_SUMMARY_BAR.jpeg
│   ├── DEP_GLUCOSE.jpeg
│   ├── DEP_AMMONIUM.jpeg
│   ├── DEP_PH.jpeg
│   └── DEP_TIME.jpeg
│
├── model/
│   ├── features.pkl
│   └── xgboost_lipid_model.pkl
│
└── notebook/
    └── Fermentation_optimisation.ipynb

# Installation and Running the Application (Local)

Clone the repository
git clone https://github.com/kirankumar88/fermentation-RSM-ml-optimization.git
cd fermentation-RSM-ml-optimization

# Install dependencies
pip install -r requirements.txt
Run the Streamlit application
streamlit run app.py

# The application will open in your browser at:

http://localhost:8501


# Workflow
Fermentation Experiments
        ↓
Response Surface Methodology (RSM)
        ↓
Machine Learning Models
        ↓
LOOCV Validation
        ↓
Hyperparameter Tuning
        ↓
Train-Test Validation
        ↓
SHAP Interpretation
        ↓
Media Optimization
        ↓
Streamlit Application
        ↓
Prediction and Optimization


# Project Scope and Intended Use

This project is developed as a research and educational prototype to demonstrate the application of machine learning techniques for fermentation media optimization and bioprocess modeling.

This system is not intended for industrial process control or clinical use. The results produced by this model should be experimentally validated before practical application.

The primary purpose of this project is to demonstrate:

Machine learning for fermentation optimization
Experimental design and predictive modeling
Model interpretation using SHAP
Process optimization using ML
Development of a machine learning application
End-to-end bioprocess optimization workflow
Future Improvements
Bayesian optimization
Genetic algorithm optimization
Multi-objective optimization
Integration with fermentation databases
Automated experiment recommendation
Web deployment


# Author

Kiran Kumar
Microbial Biotechnology | Bioinformatics | Machine Learning | Fermentation Optimization | Omics Analysis

# License

This project is intended for research and educational purposes.
