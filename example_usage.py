from client import AiFinancialCrimeTransactionPatternDetectorClient

def main():
    client = AiFinancialCrimeTransactionPatternDetectorClient()
    txns = [{"amount": 9850, "type": "cash_deposit", "day": i} for i in range(1, 10)]
    res = client.analyze_transactions(txns, "ACC-88234")
    print("Risk Score: " + str(res["risk_score"]) + "/100")
    print("Recommended Action: " + res["recommended_action"])
    print("Flagged Patterns:")
    for p in res["flagged_patterns"]:
        print("  [" + p["pattern"] + "] Confidence: " + str(p["confidence"]) + "% -- " + p["description"])
    print("")
    print("SAR Draft:")
    print(res["sar_draft"])

if __name__ == "__main__":
    main()
