#---------------------------------------------------------------
# Logistic Regression (Baseline)
# When building a real fraud detection system, it’s tempting to 
# jump straight to complex models like Random Forest  or XGBoost. 
# But in practice, starting with a simple model like 
# logistic regression is often the smartest move.
#
# May 2025 
# Srikanth Devarajan, Hands on - Learning from home :) 
#---------------------------------------------------------------

# the Tariff tax free imports
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
import joblib

# -- modeling Starts -- 

# Step 1: Load data
df = pd.read_csv("data/smart_fraud_dataset.csv")

# Step 2: Define features and label
X = df.drop(columns=['fraud_label', 'customer_id'])
y = df['fraud_label']

# Step 3: Separate column types
categorical_cols = ['merchant_category', 'merchant_country', 'payment_method']
numeric_cols = [col for col in X.columns if col not in categorical_cols]

# Step 4: Build preprocessing pipeline
preprocessor = ColumnTransformer([
    ('num', StandardScaler(), numeric_cols),
    ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_cols)
])

# Step 5: Combine preprocessing + model
pipeline = Pipeline([
    ('preprocessor', preprocessor),
    ('classifier', LogisticRegression(class_weight='balanced', max_iter=500))
])

# Step 6: Split into train and test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y
)

# Step 7: Train the model
pipeline.fit(X_train, y_train)

# Step 8: Evaluate the model
y_pred = pipeline.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# Step 9: Save the model
joblib.dump(pipeline, "models/logistic_fraud_model.pkl")



# Happy Ending 

