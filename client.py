class AiFinancialCrimeTransactionPatternDetectorClient:
    def analyze_transactions(self, transaction_sequence=None, account_id='ACC-77821'):
        transaction_sequence = transaction_sequence or []
        patterns = [
            {'pattern': 'STRUCTURING', 'description': 'Sub-threshold cash deposits.', 'confidence': 96.2},
            {'pattern': 'LAYERING', 'description': 'Rapid layering via shell entities.', 'confidence': 88.7}
        ]
        sar = 'SAR DRAFT -- Account: ' + account_id + ' | Suspected structuring and layering detected.'
        return {
            'risk_score': 94.1,
            'flagged_patterns': patterns,
            'sar_draft': sar,
            'recommended_action': 'FREEZE_AND_FILE_SAR'
        }
