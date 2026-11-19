"""Agent 2 - Investigator: looks at all log lines of one flagged IP and writes a short report."""
from llm import ask_json

SYSTEM = """You are a security investigator. You get an alert and all log lines of one IP address.
Answer ONLY with JSON:
{"source_ip": "...", "threat_type": "BRUTE_FORCE|WEB_PROBING|PORT_SCAN|OTHER|BENIGN", "severity": "LOW|MEDIUM|HIGH",
"timeline": ["short step 1", "short step 2"], "summary": "one or two sentences"}"""


def investigate(alert, log_lines):
    ip = alert["source_ip"]
    its_lines = [l for l in log_lines if l.startswith(ip + " ")][:30]    # simple log lookup
    user = f"ALERT: {alert}\n\nLOG LINES OF {ip}:\n" + "\n".join(its_lines)
    return ask_json(SYSTEM, user)
