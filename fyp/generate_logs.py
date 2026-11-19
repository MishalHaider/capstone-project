"""Logs generator: writes a fake web-server log (access.log style) with normal traffic and two attackers.
Run:  python generate_logs.py      -> creates access.log"""
import random
from datetime import datetime, timedelta

BAD_BRUTE, BAD_PROBE = "172.20.0.9", "172.20.0.10"      # the two attackers (we know the answer)
t = datetime(2026, 11, 13, 10, 0, 0)
BROWSER = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0"
lines = []


def add(ip, request, status, agent=BROWSER):
    global t
    t += timedelta(seconds=random.randint(0, 3))
    lines.append(f'{ip} - - [{t.strftime("%d/%b/%Y:%H:%M:%S +0000")}] "{request}" {status} 150 "-" "{agent}"')


for _ in range(40):                                      # normal visitors
    add(random.choice(["172.20.0.5", "172.20.0.6", "172.20.0.7"]), random.choice(["GET / HTTP/1.1", "GET /index.html HTTP/1.1"]), 200)
for _ in range(50):                                      # brute force: many failed logins
    add(BAD_BRUTE, "POST /login HTTP/1.1", 401)
for p in ["admin", ".env", "wp-login.php", "phpmyadmin", "backup.zip", "config.php", ".git/config", "shell.php"] * 3:
    add(BAD_PROBE, f"GET /{p} HTTP/1.1", 404, "Nmap Scripting Engine")   # probing: paths that do not exist
for _ in range(15):
    add("172.20.0.5", "GET / HTTP/1.1", 200)

open("access.log", "w").write("\n".join(lines) + "\n")
print(f"access.log written: {len(lines)} lines. Attackers: {BAD_BRUTE} (brute force), {BAD_PROBE} (probing)")
