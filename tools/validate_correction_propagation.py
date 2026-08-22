from pathlib import Path
import yaml

PATH=Path('test-vectors/redress/correction-propagation.yaml')

def decide(case):
    order,receipt=case['order'],case['receipt']
    if receipt.get('order_ref')!=order.get('order_id'): return 'fail','order_reference_mismatch'
    results={r['target_id']:r for r in receipt.get('target_results',[])}
    for target in order['targets']:
        if target['target_id'] not in results: return 'fail','target_missing_from_receipt'
    unresolved=[t for t in order['targets'] if t.get('mandatory') and results[t['target_id']]['status']!='completed']
    if unresolved and receipt.get('status')=='complete': return 'fail','unresolved_mandatory_target'
    if not unresolved and receipt.get('status')!='complete': return 'fail','completion_status_mismatch'
    return 'pass',None

def main():
    data=yaml.safe_load(PATH.read_text())
    failures=[]
    for case in data['cases']:
        got=decide(case); exp=(case['expected'],case.get('reason'))
        print(case['id'],got)
        if got!=exp: failures.append(f"{case['id']}: expected {exp}, got {got}")
    if failures:
        [print('FAIL',x) for x in failures]; return 2
    print(f"Correction propagation vectors OK: {len(data['cases'])} cases"); return 0
if __name__=='__main__': raise SystemExit(main())
