import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Load dataset 
file_path = "./data/Clean_Dataset.csv"  # Modify this based on your file location
df = pd.read_csv(file_path, encoding="cp949")

# Drop unnecessary columns
df = df.drop(columns=['Unnamed: 0'], errors='ignore')  # Ignore if column doesn't exist

# Compute Z-score manually
price_mean = df['price'].mean()
price_std = df['price'].std()
df['z_score'] = (df['price'] - price_mean) / price_std

# Set threshold for filtering (threshold = 2.5)
threshold = 7.5

# Filter out extreme values where abs(z-score) > threshold
df_filtered = df[np.abs(df['z_score']) <= threshold]

# Print before and after filtering
print(f"Original Data Size: {df.shape[0]}")
print(f"Filtered Data Size: {df_filtered.shape[0]}")
print(f"Data Filtered: {df.shape[0] - df_filtered.shape[0]}")

# Set figure size for better visualization
plt.figure(figsize=(14,8))

### **1️ Flight Price Distribution Before & After Filtering** ###
plt.subplot(2,2,1)
sns.histplot(df['price'], bins=50, kde=True, color='blue', label="Before Filtering")
sns.histplot(df_filtered['price'], bins=50, kde=True, color='red', label="After Filtering")
plt.title(f"Price Distribution Before and After Filtering (Z ≤ {threshold})")
plt.xlabel("Price")
plt.ylabel("Frequency")
plt.legend()

### **2️ Average Price by Airline** ###
plt.subplot(2,2,2)
sns.barplot(x=df_filtered.groupby('airline')['price'].mean().sort_values().index, 
            y=df_filtered.groupby('airline')['price'].mean().sort_values().values, 
            palette='coolwarm')
plt.xticks(rotation=90)
plt.title("Average Price by Airline (After Filtering)")
plt.xlabel("Airline")
plt.ylabel("Average Price")


plt.subplot(2,2,3)
sns.boxplot(x="departure_time", y="price", data=df_filtered, palette="coolwarm")
sns.stripplot(x="departure_time", y="price", data=df_filtered, color="black", size=2, jitter=True, alpha=0.5)
plt.xticks(rotation=45)
plt.title("Box + Strip Plot: Price vs Departure Time (After Filtering)")
plt.xlabel("Departure Time")
plt.ylabel("Price")

### **4️ Days Left vs. Price Trend** ###
plt.subplot(2,2,4)
sns.lineplot(x="days_left", y="price", data=df_filtered, color="red", ci=None)
plt.title("Ticket Price vs Days Left (After Filtering)")
plt.xlabel("Days Left")
plt.ylabel("Average Price")

plt.tight_layout()
plt.show()
