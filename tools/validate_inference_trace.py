from pathlib import Path
import sys
import yaml

PATH = Path("test-vectors/governance/inference-trace.yaml")
ALLOWED_ROLES = {"advisory", "eligibility_input", "risk_input", "ranking_input", "classification_input", "fraud_signal", "other"}


def decide(case: dict) -> tuple[str, str | None]:
    trace = case["trace"]
    receipt = case["decision_receipt"]
    if not trace.get("version"):
        return "fail", "inference_version_missing"
    if not trace.get("input_sha256"):
        return "fail", "input_snapshot_missing"
    if trace.get("normative_role") not in ALLOWED_ROLES:
        return "fail", "inference_cannot_be_normative_rule"
    if trace.get("decision_ref") != receipt.get("receipt_id") or trace.get("trace_id") != receipt.get("inference_trace_ref"):
        return "fail", "decision_reference_mismatch"
    if trace.get("rulebook_id") != receipt.get("rulebook_id") or trace.get("rulebook_version") != receipt.get("rulebook_version"):
        return "fail", "rulebook_reference_mismatch"
    expected_digest = case.get("expected_artifact_digest")
    if expected_digest and trace.get("artifact_digest") != expected_digest:
        return "fail", "model_artifact_mismatch"
    expected_threshold = case.get("expected_threshold")
    if expected_threshold is not None and trace.get("threshold") != expected_threshold:
        return "fail", "threshold_mismatch"
    return "pass", None


def main() -> int:
    data = yaml.safe_load(PATH.read_text(encoding="utf-8"))
    failures = []
    for case in data["cases"]:
        status, reason = decide(case)
        expected_status = case["expected"]
        expected_reason = case.get("reason")
        if status != expected_status or reason != expected_reason:
            failures.append(f"{case['id']}: expected ({expected_status}, {expected_reason}), got ({status}, {reason})")
        else:
            print(f"PASS {case['id']}: {status}{' (' + reason + ')' if reason else ''}")
    if failures:
        for failure in failures:
            print(f"FAIL {failure}")
        return 2
    print(f"Inference traceability vectors OK: {len(data['cases'])} cases")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
