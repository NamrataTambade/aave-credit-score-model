# Aave V2 Wallet Credit Score Model

This project assigns a **credit score between 0 and 1000** to wallets interacting with the Aave V2 protocol based on historical transaction-level behavior. The scores reflect the financial responsibility of wallets—where higher scores represent safe and trustworthy behavior, while lower scores flag potentially risky, exploitative, or bot-like patterns.

---

## 🚀 Objective

Develop a robust, automated scoring engine that:
- Ingests raw transaction-level data from Aave V2.
- Engineers relevant behavioral features per wallet.
- Assigns a credit score using a rule-based logic.
- Outputs a structured file with wallet addresses and their scores.

---

## 📂 Project Structure


---

## ⚙️ How It Works

1. **Data Loading**: Reads raw JSON of Aave V2 transactions.
2. **Wallet Grouping**: Aggregates all transactions per unique wallet.
3. **Feature Engineering**: Extracts behavioral signals like:
   - Number of deposits, borrows, repays, redemptions, liquidations
   - Activity span (in days)
   - Borrow-to-repay and deposit-to-redeem ratios
4. **Scoring**: Assigns a score between 0–1000 using rule-based logic:
   - Penalizes risky actions like liquidations.
   - Rewards responsible actions like timely repayments.
5. **Output**: Generates a CSV with wallet addresses and their scores.

---

## 🧠 Features Used

| Feature Name             | Description                                     |
|--------------------------|-------------------------------------------------|
| tx_count                 | Total number of transactions                    |
| deposit_count            | Number of deposit actions                       |
| borrow_count             | Number of borrow actions                        |
| repay_count              | Number of repay actions                         |
| liquidation_count        | Number of times wallet was liquidated          |
| active_days              | Time span between first and last transaction   |
| borrow_repay_ratio       | Ratio of repays to borrows                     |
| deposit_redeem_ratio     | Ratio of redeem to deposit actions             |

---

## 🧪 How to Run

### 🖥️ Requirements
- Python 3.8+
- pandas

### 🔧 Install dependencies
```bash
pip install -r requirements.txt

▶️ Run the scoring engine

python score_wallets.py --json user_transactions.json --out wallet_scores.csv



