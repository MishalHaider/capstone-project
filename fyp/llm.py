"""The only place that talks to the AI. The 3 agents use ask_json().
USE_MOCK=1 (in .env or in the terminal) -> a FAKE AI is used: no key and no internet needed.
The fake AI is only for checking that the code runs; it is NOT a real detector."""
import json, os, re
from collections import Counter
from dotenv import load_dotenv

load_dotenv()
USE_MOCK = os.getenv("USE_MOCK") == "1"
_model = None


def _fake_answer(system, user):
    if "detection agent" in system:
        fails, missing = Counter(), Counter()
        for line in user.splitlines():
            ip = line.split(" ")[0]
            if "POST /login" in line and '" 401' in line:
                fails[ip] += 1
            if '" 404' in line:
                missing[ip] += 1
        out = [{"source_ip": ip, "activity_type": "BRUTE_FORCE", "severity": "HIGH", "confidence": 0.9, "reason": f"{n} failed logins"} for ip, n in fails.items() if n >= 10]
        out += [{"source_ip": ip, "activity_type": "WEB_PROBING", "severity": "MEDIUM", "confidence": 0.8, "reason": f"{n} not-found requests"} for ip, n in missing.items() if n >= 10]
        return json.dumps(out)
    if "investigator" in system:
        ip = re.search(r"'source_ip': '([^']+)'", user)[1]
        kind = re.search(r"'activity_type': '([^']+)'", user)[1]
        return json.dumps({"source_ip": ip, "threat_type": kind, "severity": "HIGH", "timeline": ["many requests in a short time"], "summary": "fake investigation"})
    report = eval(user)
    return json.dumps({"action_type": "BLOCK_IP", "target": report["source_ip"], "duration_seconds": 3600, "justification": "fake plan"})


def ask(system, user):
    if USE_MOCK:
        return _fake_answer(system, user)
    global _model
    if _model is None:
        from langchain_groq import ChatGroq
        _model = ChatGroq(model=os.getenv("MODEL_NAME", "llama-3.3-70b-versatile"), temperature=0)
    return _model.invoke([("system", system), ("human", user)]).content


def ask_json(system, user, retries=2):
    """Ask the AI and return its answer as Python data. Tries again if the answer is not valid JSON."""
    for _ in range(retries + 1):
        text = re.sub(r"```(?:json)?", "", ask(system, user))
        starts = sorted(i for i in (text.find("["), text.find("{")) if i != -1)
        for i in starts:
            j = text.rfind("]" if text[i] == "[" else "}")
            try:
                return json.loads(text[i:j + 1])
            except json.JSONDecodeError:
                pass
    raise ValueError("AI did not return valid JSON")
