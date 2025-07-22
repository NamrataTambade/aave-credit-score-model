import json
import pandas as pd
from collections import defaultdict

def extract_features(data):
    features = defaultdict(lambda: {
        'num_tx': 0, 'num_deposit': 0, 'num_borrow': 0, 'num_repay': 0,
        'num_redeem': 0, 'num_liquidation': 0, 'volume_deposit': 0,
        'volume_borrow': 0, 'volume_repay': 0, 'volume_redeem': 0
    })

    for tx in data:
        wallet = tx['user']
        action = tx['action']
        amount = float(tx.get('amount', 0))
        features[wallet]['num_tx'] += 1

        if action == 'deposit':
            features[wallet]['num_deposit'] += 1
            features[wallet]['volume_deposit'] += amount
        elif action == 'borrow':
            features[wallet]['num_borrow'] += 1
            features[wallet]['volume_borrow'] += amount
        elif action == 'repay':
            features[wallet]['num_repay'] += 1
            features[wallet]['volume_repay'] += amount
        elif action == 'redeemunderlying':
            features[wallet]['num_redeem'] += 1
            features[wallet]['volume_redeem'] += amount
        elif action == 'liquidationcall':
            features[wallet]['num_liquidation'] += 1

    return pd.DataFrame.from_dict(features, orient='index')

def score_wallets(df):
    df['score'] = 1000
    df['score'] -= df['num_liquidation'] * 100
    df['score'] -= (df['num_borrow'] - df['num_repay']).clip(lower=0) * 10
    df['score'] -= (df['volume_borrow'] - df['volume_repay']).clip(lower=0) * 0.01
    df['score'] += df['volume_deposit'] * 0.005
    df['score'] = df['score'].clip(lower=0, upper=1000)
    return df[['score']]

def main():
    with open('sample_user_transactions.json') as f:
        data = json.load(f)

    features = extract_features(data)
    scores = score_wallets(features)
    scores.to_csv('wallet_scores.csv')
    print("✅ Scoring complete. Output saved to wallet_scores.csv")

if __name__ == "__main__":
    main()