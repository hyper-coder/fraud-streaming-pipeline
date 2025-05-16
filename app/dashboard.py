
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
#
#
#
# May 2025 
# Srikanth Devarajan, Hands on - Learning from home :) 
#---------------------------------------------------------------


#Free imports no duty :) 
from flask import Flask, render_template
import json
import os

app = Flask(__name__)


#landing page:
@app.route("/")
def home():
    transactions = []

    try:
        #read the verdicts
        if os.path.exists("verdicts.jsonl"):
            with open("verdicts.jsonl", "r", encoding="utf-8") as f:
                # Read full file safely
                lines = list(f)

            # Remove empty lines
            lines = [line.strip() for line in lines if line.strip()]

            # Get last 50 complete lines and parse as JSON
            transactions = [json.loads(line) for line in lines[-300:]]
            
        else:
            print("⚠️ verdicts.jsonl file not found.")
    except Exception as e:
        print(f"🔥 Error loading data: {e}")
        transactions = []
    #rendering the template. 
    return render_template("dashboard.html", transactions=transactions)

if __name__ == "__main__":
    app.run(debug=True)



# DISCLAIMER: THIS PROJECT IS PROVIDED FOR DEMONSTRATION PURPOSES ONLY.  
# IT USES SYNTHETIC DATA AND SIMPLIFIED ASSUMPTIONS NOT SUITABLE FOR PRODUCTION USE.  
# ALL MODELS, CODE, AND OUTPUTS ARE SHARED AS-IS, WITHOUT ANY WARRANTY OR GUARANTEE OF ACCURACY.  
# USE AT YOUR OWN RISK.