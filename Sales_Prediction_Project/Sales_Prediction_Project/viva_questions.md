# Viva Questions & Answers: Sales Prediction Project

**1. What is the main objective of this project?**
**Ans:** To build a machine learning model that predicts product sales based on advertising expenditure on TV, Radio, and Newspaper.

**2. Which machine learning algorithm is primarily used in this project?**
**Ans:** Multiple Linear Regression is primarily used, as we are predicting a continuous target variable based on multiple input features.

**3. What is the difference between Simple and Multiple Linear Regression?**
**Ans:** Simple Linear Regression uses one independent variable to predict a dependent variable. Multiple Linear Regression uses two or more independent variables (e.g., TV, Radio, Newspaper).

**4. Why did we drop the `Unnamed: 0` column?**
**Ans:** It is just an index or row identifier and carries no predictive information for sales. Including it could negatively affect the model or simply add noise.

**5. What is the purpose of the Train-Test Split?**
**Ans:** To evaluate how well our model generalizes to new, unseen data. We train the model on the training set (80%) and evaluate its performance on the testing set (20%).

**6. What does the R² (R-squared) score indicate?**
**Ans:** It represents the proportion of variance in the dependent variable (Sales) that can be explained by the independent variables. A score closer to 1 (or 100%) indicates a better fit.

**7. Which advertising channel has the strongest correlation with Sales?**
**Ans:** Based on the correlation heatmap, TV advertising has the strongest correlation with Sales (approx 0.78).

**8. What is Mean Absolute Error (MAE) and Root Mean Squared Error (RMSE)?**
**Ans:** 
* MAE measures the average magnitude of errors in predictions, without considering their direction.
* RMSE is the square root of the average squared errors. It penalizes larger errors more heavily than MAE.

**9. Can we say that high TV advertising *causes* high sales based on this model?**
**Ans:** No. Regression and correlation measure the strength of association, not causation. Other hidden factors could be influencing both variables.

**10. How does Random Forest improve upon Linear Regression in this dataset?**
**Ans:** Random Forest can capture non-linear relationships and interactions between features (e.g., spending on both TV and Radio simultaneously might boost sales more than the sum of their individual effects), which Linear Regression cannot model easily without explicit interaction terms.
