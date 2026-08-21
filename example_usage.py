from client import AiFinancialCrimeTransactionPatternDetectorClient

def main():
    client = AiFinancialCrimeTransactionPatternDetectorClient()
    txns = [{"amount": 9850, "type": "cash_deposit", "day": i} for i in range(1, 10)]
    res = client.analyze_transactions(txns, "ACC-88234")
    print("Risk Score: {}/100".format(res["risk_score"]))
    print("Recommended Action: {}".format(res["recommended_action"]))
    print("Flagged Patterns:")
    for p in res["flagged_patterns"]:
        print("  [{}] Confidence: {}% -- {}".format(p["pattern"], p["confidence"], p["description"]))
    print("")
    print("SAR Draft Preview:")
    print(res["sar_draft"][:300])

if __name__ == "__main__":
    main()
