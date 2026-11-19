"""Runs the three agents one after the other:  Detect -> Investigate -> Plan -> (simulated) Execute.
Every incident is saved in results.jsonl (one line each); the dashboard only READS that file.
Run:  python run.py"""
import json, time
from agents.detection_agent import detect
from agents.investigator_agent import investigate
from agents.planner_agent import plan


def run_pipeline(log_path="access.log", out_path="results.jsonl"):
    lines = open(log_path, encoding="utf-8").read().splitlines()
    alerts = detect(lines)
    print(f"Detection Agent: {len(alerts)} alert(s)")
    records = []
    for alert in alerts:
        print("\nALERT   :", alert)
        report = investigate(alert, lines)
        print("REPORT  :", report)
        action = plan(report)
        print("PLAN    :", action)
        print("EXECUTE : (simulated only)", action.get("action_type"), action.get("target"))
        records.append({"time": time.strftime("%Y-%m-%d %H:%M:%S"), "source_ip": alert.get("source_ip"),
                        "alert": alert, "report": report, "plan": action, "status": "SIMULATED"})
    with open(out_path, "w", encoding="utf-8") as f:           # one JSON object per line
        for r in records:
            f.write(json.dumps(r) + "\n")
    return records


if __name__ == "__main__":
    run_pipeline()
