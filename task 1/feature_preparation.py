import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

# Loading the cleaned dataset
ds = pd.read_csv("../cleaned_dataset.csv")

# Displays number of rows and columns in the cleaned dataset
print("Cleaned dataset shape:", ds.shape)

# Removes columns that should not be used for prediction
remove_columns = columns_to_remove = ["Restaurant ID","Aggregate rating","Restaurant Name","Address","Locality Verbose","Rating color","Rating text"]
# Seperate the target column "Aggregate rating" from all other input columns
X = ds.drop(columns=remove_columns)
y = ds["Aggregate rating"]

# Display the input features and target column
print("\nFeatures:")
print(X.columns.tolist())
print("\nTarget:")
print("Aggregate rating")

# Identifys numerical and categorical columns
num_cols = X.select_dtypes(include="number").columns.tolist()
cat_cols = X.select_dtypes(include=["object", "str"]).columns.tolist()
print("\nNumerical features:")
print(num_cols)
print("\nCategorical features:")
print(cat_cols)

# Training and testind data splitting
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)
print("\nTraining data shape:", X_train.shape)
print("\nTesting data shape:", X_test.shape)

# Create an encoder for categorical columns
preprocessor = ColumnTransformer(transformers=[("categorical",OneHotEncoder(handle_unknown="ignore"),cat_cols)],remainder="passthrough")

# Fit the encoder using training data
X_train = preprocessor.fit_transform(X_train)

# Transform the testing data using the same encoder
X_test = preprocessor.transform(X_test)

# Display the final shapes
print("\nFinal training feature shape:", X_train.shape)
print("\nFinal testing feature shape:", X_test.shape)
print("\nFeature preparation completed successfully.")  
