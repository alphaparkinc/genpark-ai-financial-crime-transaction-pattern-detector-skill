from client import AiFinancialCrimeTransactionPatternDetectorClient

def main():
    client = AiFinancialCrimeTransactionPatternDetectorClient()
    txns = [{"amount": 9850, "type": "cash_deposit", "day": i} for i in range(1, 10)]
    res = client.analyze_transactions(txns, "ACC-88234")
    print(f"Risk Score: {res['risk_score']}/100")
    print(f"Recommended Action: {res['recommended_action']}")
    print("Flagged Patterns:")
    for p in res["flagged_patterns"]:
        print(f"  [{p['pattern']}] Confidence: {p['confidence']}% — {p['description']}")
    print(f"
SAR Draft Preview:
{res['sar_draft'][:300]}...")

if __name__ == "__main__":
    main()
