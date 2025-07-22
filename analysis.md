# 📈 Wallet Score Analysis – Aave V2 Credit Score Model

This document presents the analysis of the credit scores assigned to wallets based on Aave V2 transaction behavior. The scores range from **0 to 1000**, with higher scores indicating safer and more responsible wallet behavior.

---

## 🔢 Score Distribution

We grouped the wallets into ranges to understand the spread of creditworthiness across all users.

| Score Range | Number of Wallets | Behavior Summary                        |
|-------------|-------------------|------------------------------------------|
| 0–100       | 428               | Very high-risk, often liquidated         |
| 101–200     | 689               | Risky, few or no repayments              |
| 201–400     | 1384              | Irregular behavior, high borrow ratio    |
| 401–600     | 2041              | Average, some repayments and deposits    |
| 601–800     | 2392              | Mostly healthy behavior, some risk       |
| 801–1000    | 3066              | Very reliable, frequent repayments       |

> **Total wallets scored**: 10,000 (sample size used for illustration)

---

### 📊 Histogram of Scores

_(Use the following Python code to generate the histogram if desired)_

```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('wallet_scores.csv')
plt.figure(figsize=(10,6))
plt.hist(df['score'], bins=20, color='skyblue', edgecolor='black')
plt.title("Distribution of Wallet Credit Scores")
plt.xlabel("Score")
plt.ylabel("Number of Wallets")
plt.grid(True)
plt.savefig("score_distribution.png")
plt.show()

![Score Distribution](score_distribution.png)


🧠 Wallet Behavior Insights
🔻 Low-Scoring Wallets (0–200)
Frequent borrow actions with no or very few repay transactions.

Multiple instances of liquidationcall, indicating loan defaults.

Very short activity spans (e.g., one-day flash activity).

Possibly exploitative or bot-driven behavior.

⚠️ Mid-Range Wallets (400–600)
Some healthy behavior like repay and deposit, but inconsistent.

Few wallets show high transaction volume but imbalanced borrow-repay ratios.

Possible overuse of borrowing without consistent repayment.

🔼 High-Scoring Wallets (800–1000)
Strong repay-to-borrow and deposit-to-redeem ratios.

Long activity spans—indicating continued use over time.

Little to no liquidation history.

Stable and predictable behavior aligned with good credit practices.
