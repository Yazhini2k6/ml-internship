import pandas as pd
from feature_preparation import preprocessor
from model_training import decision_tree_model

# Gets names of all processed the Features
feature_names = preprocessor.get_feature_names_out()

# Gets feature importance from the Decision Tree
importance = decision_tree_model.feature_importances_

# Create a table of features and their importance
feature_importance = pd.DataFrame({
    "Feature": feature_names,
    "Importance": importance
})

# Sorts the features by importance
feature_importance = feature_importance.sort_values(by="Importance",ascending=False)

# Displays the top 15 influential features
print("\nTop 15 Most Influential Features:")
print(feature_importance.head(15).to_string(index=False))
