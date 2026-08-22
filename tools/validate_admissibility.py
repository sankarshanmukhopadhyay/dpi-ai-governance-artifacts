from datetime import datetime
from pathlib import Path
import yaml

PATH=Path('test-vectors/trust/interinstitutional-admissibility.yaml')

def dt(value):
    if isinstance(value, datetime): return value
    return datetime.fromisoformat(str(value).replace('Z','+00:00'))

def decide(case):
    p,r=case['profile'],case['request']
    if not r.get('authentic'): return 'reject','evidence_not_authentic'
    if p.get('status')=='revoked': return 'reject','admissibility_revoked'
    if p.get('status')=='suspended': return 'reject','admissibility_suspended'
    at=dt(r['at'])
    if at < dt(p['not_before']): return 'reject','admissibility_not_yet_valid'
    if at > dt(p['not_after']): return 'reject','admissibility_expired'
    pairs=[('upstream_authority','upstream_authority_mismatch'),('output_type','output_type_not_admissible'),('relying_institution','relying_institution_mismatch'),('downstream_decision','downstream_decision_not_admissible')]
    for key,reason in pairs:
        if r.get(key)!=p.get(key): return 'reject',reason
    if r.get('purpose')!=p.get('purpose'): return 'reject','purpose_not_admissible'
    if r.get('jurisdiction')!=p.get('jurisdiction'): return 'reject','jurisdiction_not_admissible'
    missing=set(p.get('conditions',[]))-set(r.get('conditions_met',[]))
    if missing: return 'reject','assurance_condition_missing'
    return 'admit',None

def main():
    data=yaml.safe_load(PATH.read_text())
    failures=[]
    for case in data['cases']:
        got=decide(case); exp=(case['expected'],case.get('reason'))
        print(case['id'],got)
        if got!=exp: failures.append(f"{case['id']}: expected {exp}, got {got}")
    if failures:
        [print('FAIL',x) for x in failures]; return 2
    print(f"Admissibility vectors OK: {len(data['cases'])} cases"); return 0
if __name__=='__main__': raise SystemExit(main())
