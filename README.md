# Real-Time Fraud Detection Pipeline (Learning Project)


##  Overview

Real-time fraud detection is a well-established need in banking and fintech. The challenge is not awareness, it’s execution. 
Many machine learning demos stop at offline CSV classification. This learning project goes a step further by building a full real-time fraud detection pipeline.

## What It Does

- Synthetic data generation  
- Supervised model training (Logistic Regression and XGBoost)  
- Trains two machine learning models: Logistic Regression and XGBoost
- A Kafka-based streaming infrastructure  
- Real-time scoring using both models  
- A live dashboard built with Flask
- Generates realistic synthetic transactions (both legitimate and fraudulent)
- Streams live transactions via Kafka
- Scores incoming transactions in real time
- Displays results in a live dashboard with model verdicts and fraud alerts

The goal is to simulate a working prototype that reflects real production behavior, using open tools and local development.

One of the biggest blockers in ML projects is access to regulated data. In most enterprise environments, data access takes time, often months. To keep progress moving, this project uses carefully crafted synthetic data to enable development and testing early, without waiting for full datasets.

This is a hands-on learning project designed to simulate a real-time machine learning pipeline. It focuses on end-to-end flow, from data to prediction to dashboard, using simple tools and synthetic data in a local environment.



## Tech Stack

- Python 3.9
- scikit-learn, XGBoost
- Apache Kafka
- Flask (for the UI)
- Bootstrap 5 (UI styling)
**

Srikanth Devarajan, Hands on - Learning from home :) 




 DISCLAIMER: THIS PROJECT IS PROVIDED FOR DEMONSTRATION PURPOSES ONLY.  
 IT USES SYNTHETIC DATA AND SIMPLIFIED ASSUMPTIONS NOT SUITABLE FOR PRODUCTION USE.  
 ALL MODELS, CODE, AND OUTPUTS ARE SHARED AS-IS, WITHOUT ANY WARRANTY OR GUARANTEE OF ACCURACY.  
 USE AT YOUR OWN RISK.
