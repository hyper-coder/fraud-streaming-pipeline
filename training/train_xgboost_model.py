#---------------------------------------------------------------
# XGBoost (Baseline)
# Think of XGBoost like asking a group of people to help you make 
# a decision — but you ask them one at a time, and each person learns 
# from the mistakes of the previous ones.
# The first person makes a rough guess.
# The second person looks at what the first missed and improves it.
# The third person focuses on what the first two still got wrong.
# And so on.
#
# Each person is like a small decision tree. 
# Individually, they’re weak, but Together, they become powerful.  
# (Like a team that learns from each other’s mistakes)
#
# That’s how XGBoost works — it builds a smart team of decision-makers.
#
# May 2025 
# Srikanth Devarajan, Hands on - Learning from home :) 
#---------------------------------------------------------------

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report, accuracy_score
from xgboost import XGBClassifier
import joblib

# Step 1: Load dataset
df = pd.read_csv("data/smart_fraud_dataset.csv")

# Step 2: Features and label
X = df.drop(columns=['fraud_label', 'customer_id'])  # Drop target and ID
y = df['fraud_label']

# Step 3: Calculate class imbalance ratio
neg_count = (y == 0).sum()
pos_count = (y == 1).sum()
scale_ratio = neg_count / pos_count
print(f"Class Imbalance Ratio: scale_pos_weight = {scale_ratio:.2f}")

# Step 4: Preprocessing
categorical_cols = ['merchant_category', 'merchant_country', 'payment_method']
numeric_cols = [col for col in X.columns if col not in categorical_cols]

preprocessor = ColumnTransformer([
    ('num', StandardScaler(), numeric_cols),
    ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_cols)
])

# Step 5: XGBoost with scale_pos_weight
xgb_model = XGBClassifier(
    use_label_encoder=False,
    eval_metric='logloss',
    scale_pos_weight=scale_ratio,
    random_state=42
)

# Step 6: Pipeline
pipeline = Pipeline([
    ('preprocessor', preprocessor),
    ('classifier', xgb_model)
])

# Step 7: Split & Train
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, stratify=y, random_state=42
)

pipeline.fit(X_train, y_train)

# Step 8: Evaluation
y_pred = pipeline.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# Step 9: Save the model
joblib.dump(pipeline, "models/xgboost_fraud_model.pkl")
print("XGBoost model saved: models/xgboost_fraud_model.pkl")


# Happy Ending 