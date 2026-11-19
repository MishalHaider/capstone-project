"""Agent 3 - Response Planner: proposes ONE action. It only proposes; it cannot run anything."""
from llm import ask_json

SYSTEM = """You are an incident response planner. You get an investigation report. Propose one action.
Answer ONLY with JSON:
{"action_type": "BLOCK_IP|UNBLOCK_IP|RATE_LIMIT_IP|NO_ACTION", "target": "ip address or null",
"duration_seconds": 3600, "justification": "one short sentence"}
Use NO_ACTION if the traffic looks benign."""


def plan(report):
    return ask_json(SYSTEM, str(report))
