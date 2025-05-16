
#---------------------------------------------------------------
# Producer Service
# Generates transaction data and pushes into a Kafka Topic
# 
#
#
# May 2025 
# Srikanth Devarajan, Hands on - Learning from home :) 
#
#
#---------------------------------------------------------------


import random
import json
import time
from datetime import datetime, timedelta
from kafka import KafkaProducer

# Kafka producer setup
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Category definitions
merchant_categories = ['groceries', 'electronics', 'travel', 'fashion', 'food', 'digital_services']
countries = ['US', 'UK', 'IN', 'DE', 'BR']
payment_methods = ['online', 'POS', 'mobile_wallet', 'contactless']

category_ranges = {
    'groceries': (10, 300),
    'electronics': (100, 5000),
    'travel': (200, 8000),
    'fashion': (20, 1500),
    'food': (5, 200),
    'digital_services': (5, 300)
}

category_currency = {
    'US': 'USD',
    'UK': 'GBP',
    'IN': 'INR',
    'DE': 'EUR',
    'BR': 'BRL'
}

transaction_id = 10000

while True:
    is_fraud = random.random() < 0.2
    merchant_category = random.choice(merchant_categories)
    merchant_country = random.choice(countries)
    currency = category_currency[merchant_country]
    simulated_time = datetime.now() - timedelta(minutes=random.randint(0, 1440))

    if is_fraud:
        data = {
            "transaction_id": f"T{transaction_id}",
            "transaction_amount": round(random.uniform(15000, 30000), 2),
            "merchant_category": "digital_services",
            "merchant_country": "RU",
            "currency": "RUB",
            "payment_method": "online",
            "timestamp": simulated_time.strftime("%Y-%m-%d %H:%M:%S"),
            "transaction_hour": simulated_time.hour,
            "is_weekend": int(simulated_time.weekday() >= 5),
            "account_age_days": random.randint(1, 10),
            "avg_txn_amount_30d": round(random.uniform(10, 50), 2),
            "txn_count_24h": random.randint(8, 20),
            "is_new_merchant": 1,
            "geo_distance_km": round(random.uniform(100, 800), 2),
            "ip_change": 1,
            "device_trusted": 0,
            "is_high_risk_country": 1,
            "velocity_score": random.randint(8, 10)
        }
    else:
        amount = round(random.uniform(*category_ranges[merchant_category]), 2)
        data = {
            "transaction_id": f"T{transaction_id}",
            "transaction_amount": amount,
            "merchant_category": merchant_category,
            "merchant_country": merchant_country,
            "currency": currency,
            "payment_method": random.choice(payment_methods),
            "timestamp": simulated_time.strftime("%Y-%m-%d %H:%M:%S"),
            "transaction_hour": simulated_time.hour,
            "is_weekend": int(simulated_time.weekday() >= 5),
            "account_age_days": random.randint(30, 3000),
            "avg_txn_amount_30d": round(amount * random.uniform(0.5, 1.5), 2),
            "txn_count_24h": random.randint(1, 5),
            "is_new_merchant": random.choice([0, 1]),
            "geo_distance_km": round(random.uniform(1, 100), 2),
            "ip_change": random.choice([0, 1]),
            "device_trusted": random.choice([0, 1]),
            "is_high_risk_country": random.choice([0, 1]),
            "velocity_score": random.randint(0, 7)
        }

    producer.send('transactions', value=data)
    print(f"[SENT] {data['transaction_id']} | {data['timestamp']} | {data['currency']} {data['transaction_amount']} | Fraud: {is_fraud}")
    transaction_id += 1
    time.sleep(5)



# Happy Ending :) 



# DISCLAIMER: THIS PROJECT IS PROVIDED FOR DEMONSTRATION PURPOSES ONLY.  
# IT USES SYNTHETIC DATA AND SIMPLIFIED ASSUMPTIONS NOT SUITABLE FOR PRODUCTION USE.  
# ALL MODELS, CODE, AND OUTPUTS ARE SHARED AS-IS, WITHOUT ANY WARRANTY OR GUARANTEE OF ACCURACY.  
# USE AT YOUR OWN RISK.