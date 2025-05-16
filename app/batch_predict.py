

import pandas as pd
import joblib

# Step 1: Load the saved model
model = joblib.load("models/xgboost_fraud_model.pkl")
model2 = joblib.load("models/logistic_fraud_model.pkl")

# Step 2: Load the input CSV file
input_df = pd.read_csv("data/batch_input_sample.csv")

# Step 3: Separate out transaction IDs
txn_ids = input_df['transaction_id']
X = input_df.drop(columns=['transaction_id'])


# Step 4: Predict fraud probabilities and verdicts
probs = model.predict_proba(X)[:, 1]       # Probability of fraud
preds = (probs > 0.5).astype(int)          # Verdict: 1 = FRAUD, 0 = NOT FRAUD

# Step 4a - Second model
probs2 = model2.predict_proba(X)[:, 1]       # Probability of fraud
preds2 = (probs > 0.5).astype(int)          # Verdict: 1 = FRAUD, 0 = NOT FRAUD

# Step 5: Prepare final report with selected fields
report_df = pd.DataFrame({
    'Transaction ID': txn_ids,
    'Amount (USD)': X['transaction_amount'],
    'Merchant Country': X['merchant_country'],
    'Payment Method': X['payment_method'],
    'Velocity Score': X['velocity_score'],
    'IP Changed': X['ip_change'],
    'Fraud Risk Score': probs.round(2),
    'XGBoost-Model Verdict': ['FRAUD' if x == 1 else 'NOT FRAUD' for x in preds],
    'LR-Model Verdict': ['FRAUD' if x == 1 else 'NOT FRAUD' for x in preds2]
})

# Step 6: Save the report to CSV
report_df.to_csv("data/fraud_risk_report.csv", index=False)
print("✅ Fraud risk report generated: data/fraud_risk_report.csv")

# Happy Ending 


#DISCLAIMER: THIS PROJECT IS PROVIDED FOR DEMONSTRATION PURPOSES ONLY.  
#IT USES SYNTHETIC DATA AND SIMPLIFIED ASSUMPTIONS NOT SUITABLE FOR PRODUCTION USE.  
#ALL MODELS, CODE, AND OUTPUTS ARE SHARED AS-IS, WITHOUT ANY WARRANTY OR GUARANTEE OF ACCURACY.  
#USE AT YOUR OWN RISK.