# Real-Time Fraud Detection Pipeline (Demo Project)

This project demonstrates a full-stack, real-time fraud detection system using synthetic data, machine learning models, and Kafka streaming — all built and tested locally.

## 📌 What It Does

- Generates realistic synthetic transactions (both legitimate and fraudulent)
- Trains two machine learning models: Logistic Regression and XGBoost
- Streams live transactions via Kafka
- Scores incoming transactions in real time
- Displays results in a live dashboard with model verdicts and fraud alerts

## 🛠 Tech Stack

- Python 3.9
- scikit-learn, XGBoost
- Apache Kafka
- Flask (for the UI)
- Bootstrap 5 (UI styling)
