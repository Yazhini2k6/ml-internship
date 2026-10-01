# Restaurant Rating Prediction
 
A machine learning project that predicts a restaurant's **Aggregate Rating** from attributes such as location, cuisine, cost, available services, price range, and customer votes. It covers the complete ML workflow: data exploration → preprocessing → feature preparation → model training → evaluation → feature analysis.
 
> Developed as **Task 1** of a Machine Learning internship by **Gunayazhini**.
 
---
 
## Table of Contents
 
- [Dataset](#dataset)
- [Project Structure](#project-structure)
- [Workflow](#workflow)
- [Results](#results)
- [Installation](#installation)
- [Usage](#usage)
- [Key Takeaways](#key-takeaways)
 
---
 
## Dataset
 
| Item | Details |
|---|---|
| Records | 9,551 |
| Columns | 21 |
| Target variable | `Aggregate rating` |
| Train / test split | 80% / 20% (7,640 / 1,911 records) |
| Random seed | 42 |
 
**Columns excluded from the input features**
 
| Column(s) | Reason |
|---|---|
| `Restaurant ID` | Identifier, not a meaningful predictor |
| `Restaurant Name`, `Address`, `Locality Verbose` | Unsuitable for prediction |
| `Rating color`, `Rating text` | Directly derived from the rating (**data leakage**) |
 
---
 
## Project Structure
 
```
restaurant-rating-prediction/
├── dataset.csv                      # Original dataset
├── cleaned_dataset.csv              # Output of preprocessing.py
├── requirements.txt                 # Python dependencies
├── README.md
├── Task_1_Restaurant_Rating_Prediction_Internship_Report.docx
└── src/
    ├── data_exploration.py          # Inspect structure, types, missing/duplicate values
    ├── preprocessing.py             # Clean data and save cleaned_dataset.csv
    ├── feature_preparation.py       # Feature/target selection, split, one-hot encoding
    ├── model_training.py            # Train Linear Regression & Decision Tree
    ├── model_evaluation.py          # Compute MSE and R²
    └── feature_analysis.py          # Decision Tree feature importance
```
 
---
 
## Workflow
 
1. **Data Exploration** – Shape, column names, data types, numerical/categorical columns, statistical summary, unique values, missing values, and duplicates.
2. **Preprocessing** – No duplicate rows were found. The 9 missing values in `Cuisines` were filled with `"Unknown"`, and the result was saved as `cleaned_dataset.csv`.
3. **Feature Preparation** – Dropped unsuitable columns, split the data 80/20, and applied **One-Hot Encoding** to categorical features. The encoder is fitted on the training data only to avoid leakage. The 14 input features expand to **2,770** encoded features.
4. **Model Training** – Two regression models:
   - **Linear Regression** – baseline model
   - **Decision Tree Regressor** – captures non-linear relationships
5. **Model Evaluation** – Mean Squared Error (MSE) and R² Score on the test set.
6. **Feature Analysis** – Feature importances from the trained Decision Tree.
 
---
 
## Results
 
### Model Performance
 
| Model | MSE ↓ | R² Score ↑ |
|---|---|---|
| Linear Regression | 1.199810 | 0.472868 |
| **Decision Tree Regression** | **0.154055** | **0.932316** |
 
### Top Features (Decision Tree)
 
| Rank | Feature | Importance |
|---|---|---|
| 1 | Votes | 0.943772 |
| 2 | Longitude | 0.015546 |
| 3 | Latitude | 0.009172 |
| 4 | Average Cost for two | 0.004545 |
| 5 | Currency – Brazilian Real (R$) | 0.000810 |
| 6 | Cuisines – North Indian | 0.000570 |
| 7 | Price range | 0.000534 |
 
> **Note:** Feature importance shows how the Decision Tree used each feature, not that a feature *causes* a higher or lower rating.
 
---
 
## Installation
 
```bash
# Clone the repository
git clone https://github.com/<your-username>/restaurant-rating-prediction.git
cd restaurant-rating-prediction
 
# (Optional) create a virtual environment
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
 
# Install dependencies
pip install -r requirements.txt
```
 
---
 
## Usage
 
The scripts use relative paths (`../dataset.csv`), so run them **from inside the `src/` folder**, in this order:
 
```bash
cd src
 
python data_exploration.py      # 1. Explore the raw data
python preprocessing.py         # 2. Clean data -> ../cleaned_dataset.csv
python feature_preparation.py   # 3. Prepare features and train/test split
python model_training.py        # 4. Train both models
python model_evaluation.py      # 5. Print MSE and R²
python feature_analysis.py      # 6. Print top 15 feature importances
```
 
Later scripts import from earlier ones (for example, `model_evaluation.py` imports from `model_training.py`), so running a later script also executes the stages it depends on.
 
---
 
## Key Takeaways
 
- The Decision Tree clearly outperformed the Linear Regression baseline (R² ≈ 0.93 vs ≈ 0.47), suggesting non-linear relationships between the features and the rating.
- `Votes` is by far the most influential feature, accounting for roughly 94% of the Decision Tree's total importance.
- Excluding `Rating color` and `Rating text` prevented data leakage and kept the evaluation honest.
 
---
 
## Author
 
**Gunayazhini**
