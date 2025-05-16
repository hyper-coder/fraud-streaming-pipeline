import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ----------------------------------------
# Step 1: Load the dataset
# ----------------------------------------
df = pd.read_csv("smart_fraud_dataset.csv")

# ----------------------------------------
# Step 2: Print shape and preview records
# ----------------------------------------
print("Dataset shape:", df.shape)
print("\nSample records:\n", df.head())

# ----------------------------------------
# Step 3: Check fraud label distribution
# ----------------------------------------
fraud_counts = df['fraud_label'].value_counts()
print("\nFraud label distribution:\n", fraud_counts)

# ----------------------------------------
# Step 4: Plot transaction amount distribution
# ----------------------------------------
plt.figure(figsize=(10, 5))
sns.histplot(data=df, x='transaction_amount', hue='fraud_label', bins=50, kde=True)
plt.title('Transaction Amount Distribution by Fraud Label')
plt.xlabel('Transaction Amount')
plt.ylabel('Frequency')
plt.legend(title='Fraud Label', labels=['Legit (0)', 'Fraud (1)'])
plt.tight_layout()
plt.savefig("eda_amount_distribution.png")
plt.close()

# ----------------------------------------
# Step 5: Fraud rate by merchant country
# ----------------------------------------
fraud_by_country = df.groupby('merchant_country')['fraud_label'].mean().sort_values(ascending=False)
print("\nFraud rate by merchant_country:\n", fraud_by_country)

# ----------------------------------------
# Step 6: Correlation heatmap (numeric only)
# ----------------------------------------
numeric_df = df.select_dtypes(include=['float64', 'int64'])
corr_matrix = numeric_df.corr()



plt.figure(figsize=(12, 8))
sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap='coolwarm')
plt.title('Correlation Heatmap of Numeric Features')
plt.tight_layout()
plt.savefig("eda_correlation_heatmap.png")
plt.close()