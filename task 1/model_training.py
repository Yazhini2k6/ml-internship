from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from feature_preparation import X_train, X_test, y_train, y_test

# Create and train the Linear Regression model
linear_model = LinearRegression()
linear_model.fit(X_train, y_train)
print("Linear Regression model trained successfully.")

# Create and train the Decision Tree Regression model
decision_tree_model = DecisionTreeRegressor(random_state=42)
decision_tree_model.fit(X_train, y_train)
print("Decision Tree Regression model trained successfully.")

# Makes predictions using both models
linear_predictions = linear_model.predict(X_test)

decision_tree_predictions = decision_tree_model.predict(X_test)


# Displays a few predictions
print("\nFirst 10 Linear Regression predictions:")
print(linear_predictions[:10])

print("\nFirst 10 Decision Tree Regression predictions:")
print(decision_tree_predictions[:10])

print("\nModel training and prediction completed successfully.")
