from sklearn.metrics import mean_squared_error, r2_score
from model_training import (y_test,linear_predictions,decision_tree_predictions)

# Linear Regression metrics
linear_mse = mean_squared_error(y_test,linear_predictions)

linear_r2 = r2_score(y_test,linear_predictions)

# Decision Tree Regression metrics
decision_tree_mse = mean_squared_error(y_test,decision_tree_predictions)
decision_tree_r2 = r2_score(y_test,decision_tree_predictions)

# Linear Regression results
print("\nLinear Regression Results:")
print("Mean Squared Error:", linear_mse)
print("R² Score:", linear_r2)

# Decision Tree Regression results
print("\nDecision Tree Regression Results:")
print("Mean Squared Error:", decision_tree_mse)
print("R² Score:", decision_tree_r2)

# Displays actual and predicted values
print("\nFirst 10 Actual Ratings:")
print(y_test.iloc[:10].values)
print("\nFirst 10 Linear Regression Predictions:")
print(linear_predictions[:10])
print("\nFirst 10 Decision Tree Predictions:")
print(decision_tree_predictions[:10])
