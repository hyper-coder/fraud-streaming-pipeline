
#---------------------------------------------------------------
# Consumer Model  Service
# Reads from Kafka, predicts fraud and saves it into a local Log
# 
#
#
# May 2025 
# Srikanth Devarajan, Hands on - Learning from home :) 
#
#
#---------------------------------------------------------------



# Tax free Imports
import json
import pandas as pd
from kafka import KafkaConsumer
import joblib
from datetime import datetime

# Load models
log_model = joblib.load("models/logistic_fraud_model.pkl")
xgb_model = joblib.load("models/xgboost_fraud_model.pkl")

# Kafka setup
consumer = KafkaConsumer(
    'transactions',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda m: json.loads(m.decode('utf-8')),
    auto_offset_reset='latest',   # Only read new messages
    enable_auto_commit=True,
    group_id='fraud-dashboard-v2'  # Change to reset consumption point
)

print("🟢 Listening for Kafka transactions...")

for message in consumer:
    txn = message.value

    # Convert to DataFrame
    df = pd.DataFrame([txn])
    X = df  # Pass full data to pipeline

    # Predict
    log_pred = log_model.predict(X)[0]
    xgb_pred = xgb_model.predict(X)[0]

    # Add verdicts
    txn["LogisticRegression"] = "FRAUD" if log_pred == 1 else "NOT FRAUD"
    txn["XGBoost"] = "FRAUD" if xgb_pred == 1 else "NOT FRAUD"
    txn["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S") 

    # Write to verdicts.jsonl
    with open("verdicts.jsonl", "a", encoding="utf-8") as f:
        f.write(json.dumps(txn) + "\n")
        f.flush()

    print(f"📨 T{txn['transaction_id']} → Log: {txn['LogisticRegression']} | XGB: {txn['XGBoost']}")


# Happy Ending :)

# DISCLAIMER: THIS PROJECT IS PROVIDED FOR DEMONSTRATION PURPOSES ONLY.  
# IT USES SYNTHETIC DATA AND SIMPLIFIED ASSUMPTIONS NOT SUITABLE FOR PRODUCTION USE.  
# ALL MODELS, CODE, AND OUTPUTS ARE SHARED AS-IS, WITHOUT ANY WARRANTY OR GUARANTEE OF ACCURACY.  
# USE AT YOUR OWN RISK.