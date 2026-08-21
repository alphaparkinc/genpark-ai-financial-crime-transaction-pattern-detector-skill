from client import AiFinancialCrimeTransactionPatternDetectorClient

def main():
    client = AiFinancialCrimeTransactionPatternDetectorClient()
    txns = [{'amount': 9850, 'type': 'cash_deposit', 'day': i} for i in range(1, 10)]
    res = client.analyze_transactions(txns, 'ACC-88234')
    print('Risk Score: ' + str(res['risk_score']) + '/100')
    print('Action: ' + res['recommended_action'])
    print('SAR: ' + res['sar_draft'])
    print('Patterns:')
    for p in res['flagged_patterns']:
        print('  ' + p['pattern'] + ' (' + str(p['confidence']) + '%)')

if __name__ == '__main__':
    main()
