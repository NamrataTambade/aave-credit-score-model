# DeFi Wallet Credit Scoring (Sample Project)

## 📌 Objective
Assign a credit score (0–1000) to each wallet using their Aave V2 transaction history.

## 🚀 How to Run

### 1. Run the scoring script
```bash
python wallet_credit_score.py
```

This will generate a `wallet_scores.csv` file.

### 2. Run the analysis script
```bash
python analysis.py
```

This will show a score distribution bar graph.

## 📁 Files
- `sample_user_transactions.json` — Dummy Aave V2-style data
- `wallet_credit_score.py` — Feature extraction + scoring logic
- `analysis.py` — Visualization of score distribution