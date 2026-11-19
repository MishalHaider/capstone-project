"""Agent 1 - Detection: reads log lines and says which IPs look suspicious. It only flags, it never acts."""
import re
from collections import Counter, defaultdict
from llm import ask_json

SYSTEM = """You are a security detection agent for a web server.
You get a short summary of the access log, one line per IP address. Find IP addresses that behave suspiciously:
- BRUTE_FORCE: many failed logins (POST /login with status 401) from one IP
- WEB_PROBING: many requests to paths that do not exist (404) or to admin/config files
- PORT_SCAN: one IP touching many different services
Normal visitors must NOT be flagged.
Answer ONLY with a JSON list. Each item:
{"source_ip": "...", "activity_type": "BRUTE_FORCE|WEB_PROBING|PORT_SCAN|OTHER", "severity": "LOW|MEDIUM|HIGH", "confidence": 0.0-1.0, "reason": "short reason"}
If nothing is suspicious answer []."""


LINE = re.compile(r'^(\S+) .*?"(\S+) (\S+) [^"]*" (\d{3}) .*"([^"]*)"$')


def summarize(log_lines):
    """Shrink the log to one short line per IP (the AI has a size limit per minute).
    The AI still decides what is suspicious; we only count things."""
    ips = defaultdict(lambda: {"n": 0, "status": Counter(), "paths": Counter(), "login_401": 0, "agent": ""})
    for line in log_lines:
        m = LINE.match(line)
        if not m:
            continue
        ip, method, path, status, agent = m.groups()
        d = ips[ip]
        d["n"] += 1
        d["status"][status] += 1
        d["paths"][path] += 1
        d["agent"] = agent[:40]
        if method == "POST" and path == "/login" and status == "401":
            d["login_401"] += 1
    out = []
    for ip, d in ips.items():
        top = ",".join(f"{p}:{c}" for p, c in d["paths"].most_common(4))
        st = ",".join(f"{k}:{v}" for k, v in sorted(d["status"].items()))
        out.append(f"ip={ip} requests={d['n']} failed_logins_401={d['login_401']} "
                   f"not_found_404={d['status'].get('404', 0)} distinct_paths={len(d['paths'])} "
                   f"status=[{st}] top_paths=[{top}] agent=\"{d['agent']}\"")
    return out


def detect(log_lines):
    alerts = ask_json(SYSTEM, "\n".join(summarize(log_lines)))
    return alerts if isinstance(alerts, list) else [alerts]