# Project Report: Sales Prediction Using Python and Machine Learning

## 1. Abstract
This project presents a machine learning-based sales prediction system that estimates product sales based on advertising expenditure. Using a dataset of TV, Radio, and Newspaper advertising budgets, multiple regression models are implemented and evaluated. The system highlights the relationship between marketing channels and sales to support business forecasting.

## 2. Introduction
Sales prediction is crucial for businesses to allocate marketing budgets efficiently. This project investigates the relationship between advertising and sales using Machine Learning, providing an automated, data-driven approach to forecasting sales instead of relying on manual estimations.

## 3. Problem Statement
Manually predicting sales based on various marketing campaigns is complex and prone to errors. A data-driven prediction system is required to accurately model how advertising budgets distributed across TV, Radio, and Newspaper affect overall product sales.

## 4. Objectives
* Analyze the Advertising dataset.
* Understand the correlation between advertising channels and sales.
* Train a machine learning regression model to predict sales.
* Evaluate the model's accuracy.
* Develop an interactive prediction interface.

## 5. Dataset Description
The `Advertising.csv` dataset contains ~200 records with the following columns:
* **Unnamed: 0**: Index identifier (removed during cleaning)
* **TV**: Advertising expenditure on TV
* **Radio**: Advertising expenditure on Radio
* **Newspaper**: Advertising expenditure on Newspaper
* **Sales**: Product sales (Target variable)

## 6. Data Preprocessing
* **Missing values**: Checked and handled (none found).
* **Duplicates**: Checked and removed (none found).
* **Data cleaning**: Dropped the unnecessary `Unnamed: 0` index column.
* **Feature selection**: TV, Radio, and Newspaper were selected as input features (X), and Sales as the target (Y).

## 7. Exploratory Data Analysis
Histograms and scatter plots were plotted to understand the distribution of spending. 
* A strong linear relationship was observed between TV advertising and Sales. 
* The correlation matrix highlighted that TV has the strongest correlation with Sales (0.78), followed by Radio (0.58), and Newspaper (0.23).

## 8. Methodology
Data Collection -> Data Preprocessing -> Exploratory Data Analysis (EDA) -> Feature Selection -> Train-Test Split (80/20) -> Model Training -> Evaluation -> Prediction.

## 9. Machine Learning Algorithm
* **Multiple Linear Regression**: Fits a linear equation to the data by assigning weights (coefficients) to each advertising channel.
* **Decision Tree Regression**: Splits the data into branches based on feature values to make predictions.
* **Random Forest Regression**: Uses an ensemble of decision trees to improve prediction accuracy and reduce overfitting.

## 10. Experimental Results
Example performance for Linear Regression (approximate):
* **MAE**: 1.46
* **MSE**: 3.17
* **RMSE**: 1.78
* **R² Score**: 0.89

Random Forest generally yielded a higher R² Score (~0.97) on this dataset, indicating better handling of complex, non-linear relationships.

## 11. Advertising Impact Analysis
The regression coefficients showed that holding other factors constant, an increase in Radio advertising budget has a strong positive effect on sales per unit of budget. TV also significantly drives total sales due to larger typical budgets.

## 12. Applications
* Marketing budget planning
* Sales forecasting
* Advertising optimization
* Business decision-making
* Campaign performance analysis

## 13. Advantages
* Easy to implement and interpret
* Data-driven predictions
* Helps efficiently allocate advertising budgets
* Reduces manual estimation
* Supports objective business decisions

## 14. Limitations
* Dataset is relatively small (~200 records).
* Only three advertising channels are included.
* No customer demographics or time-series/seasonality information.
* Historical correlation/regression does not strictly prove that advertising causes sales.

## 15. Future Scope
* Train on larger real-world datasets.
* Incorporate time-series forecasting to account for seasonal trends.
* Implement Deep Learning models for complex feature extraction.
* Integrate into real-time business dashboards and automated marketing recommendations.

## 16. Conclusion
Machine learning provides a robust method to predict sales from advertising expenditure. By leveraging Multiple Linear Regression and Random Forest algorithms, businesses can make informed decisions to optimize their marketing budgets and maximize sales revenue.

## 17. References
* Python documentation
* Pandas, NumPy, Matplotlib, Seaborn libraries
* Scikit-learn (Machine Learning in Python)
* ISLR (Introduction to Statistical Learning) - Dataset Source
