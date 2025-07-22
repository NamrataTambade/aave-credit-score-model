import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('wallet_scores.csv')
df['bucket'] = pd.cut(df['score'], bins=range(0, 1100, 100))
bucket_counts = df['bucket'].value_counts().sort_index()

bucket_counts.plot(kind='bar', color='skyblue', edgecolor='black')
plt.xlabel('Score Range')
plt.ylabel('Number of Wallets')
plt.title('Score Distribution')
plt.tight_layout()
plt.show()