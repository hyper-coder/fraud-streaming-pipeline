
#---------------------------------------------------------------
# RiskOps UI  -- With dual model predictions. 
# A fraud analyst should be able to say
# “This transaction came from a new IP, outside the customer’s usual country, 
# with an unusually high amount. That does feel suspicious.”
# The UI is designed in the context of Ops person context and not in ML context
#
# They don’t need to know machine learning, but they do need to know what 
# the model is looking at — because they:
#	Investigate alerts
#	Make judgment calls on edge cases
#	Review false positives
#	Provide feedback to improve the model
#
#
# NOTE: 
#  This file is obsolete and provided for backward compatability
#  use Dashboard.py to trigger dashboard.html
#
#
#
# May 2025 
# Srikanth Devarajan, Hands on - Learning from home :) 
#---------------------------------------------------------------

#Tariff free imports :) 
from flask import Flask, render_template, request
import joblib
import numpy as np
import pandas as pd

app = Flask(__name__)

# Load both models
regression_model = joblib.load("models/logistic_fraud_model.pkl")
xgboost_model = joblib.load("models/xgboost_fraud_model.pkl")

# Define input feature order
feature_order = [
    'transaction_amount', 'merchant_category', 'merchant_country', 'payment_method',
    'transaction_hour', 'is_weekend', 'account_age_days', 'avg_txn_amount_30d',
    'txn_count_24h', 'is_new_merchant', 'geo_distance_km', 'ip_change',
    'device_trusted', 'is_high_risk_country', 'velocity_score'
]

@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        data = {}
        for feature in feature_order:
            val = request.form.get(feature)
            if feature in ['is_weekend', 'is_new_merchant', 'ip_change', 'device_trusted', 'is_high_risk_country']:
                data[feature] = int(val == '1')
            elif feature in ['transaction_hour', 'txn_count_24h', 'velocity_score', 'account_age_days']:
                data[feature] = int(val)
            elif feature in ['transaction_amount', 'avg_txn_amount_30d', 'geo_distance_km']:
                data[feature] = float(val)
            else:
                data[feature] = val  # categorical value

        input_df = pd.DataFrame([data])

        # Predict with both models
        reg_prob = regression_model.predict_proba(input_df)[0][1]
        xgb_prob = xgboost_model.predict_proba(input_df)[0][1]

        result = {
            "regression": {
                "name": "Basic Risk Engine",
                "score": round(reg_prob, 2),
                "verdict": "FRAUD" if reg_prob > 0.5 else "NOT FRAUD"
            },
            "xgboost": {
                "name": "Advanced Risk Engine",
                "score": round(xgb_prob, 2),
                "verdict": "FRAUD" if xgb_prob > 0.5 else "NOT FRAUD"
            }
        }

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)


# Happy Ending 


# DISCLAIMER: THIS PROJECT IS PROVIDED FOR DEMONSTRATION PURPOSES ONLY.  
# IT USES SYNTHETIC DATA AND SIMPLIFIED ASSUMPTIONS NOT SUITABLE FOR PRODUCTION USE.  
# ALL MODELS, CODE, AND OUTPUTS ARE SHARED AS-IS, WITHOUT ANY WARRANTY OR GUARANTEE OF ACCURACY.  
# USE AT YOUR OWN RISK.