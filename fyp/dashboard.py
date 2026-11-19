"""Dashboard (Streamlit). It only SHOWS what the agents saved in results.jsonl and what is in access.log.
Run:  streamlit run dashboard.py"""
import json, os, subprocess, sys
import streamlit as st

LOG, RESULTS = "access.log", "results.jsonl"
USE_MOCK = os.getenv("USE_MOCK") == "1"
if not USE_MOCK:
    try:
        from dotenv import load_dotenv; load_dotenv(); USE_MOCK = os.getenv("USE_MOCK") == "1"
    except ImportError:
        pass

st.set_page_config(page_title="Incident Response Dashboard", page_icon="🛡️", layout="wide")
st.title("🛡️ Multi-Agent Incident Response Dashboard")
st.caption("Baseline (Unprotected): agents only propose, actions are SIMULATED. No Watchdog yet.")


def read_lines():
    return open(LOG, encoding="utf-8").read().splitlines() if os.path.exists(LOG) else []


def read_results():
    if not os.path.exists(RESULTS):
        return []
    return [json.loads(l) for l in open(RESULTS, encoding="utf-8") if l.strip()]


with st.sidebar:
    st.header("Controls")
    if USE_MOCK:
        st.warning("Fake AI (USE_MOCK=1): only checks that the code runs.")
    else:
        st.success("Real AI (Groq)")
    if st.button("1. Generate sample logs", use_container_width=True):
        subprocess.run([sys.executable, "generate_logs.py"], check=False)
        st.toast("access.log created")
    if st.button("2. Run analysis", use_container_width=True, type="primary"):
        if not os.path.exists(LOG):
            st.error("No access.log yet. Press button 1 first.")
        else:
            try:
                from run import run_pipeline
                with st.spinner("Agents are working..."):
                    run_pipeline(LOG, RESULTS)
                st.toast("Analysis done")
            except Exception as e:
                st.error(f"Analysis failed: {e}")
    st.divider()
    st.caption("The dashboard does not decide anything. It shows the files the agents wrote.")

lines, results = read_lines(), read_results()
bad_ips = {r["source_ip"] for r in results}
c1, c2, c3 = st.columns(3)
c1.metric("Log lines", len(lines))
c2.metric("Alerts (suspicious IPs)", len(results))
c3.metric("Proposed blocks", sum(1 for r in results if r["plan"].get("action_type") == "BLOCK_IP"))

tab_inc, tab_log, tab_appr = st.tabs(["Incidents", "Logs", "Pending approvals"])

with tab_inc:
    if not results:
        st.info("No incidents yet. Use the buttons in the sidebar: 1) generate logs, 2) run analysis.")
    for r in results:
        a, rep, p = r["alert"], r["report"], r["plan"]
        sev = a.get("severity", "")
        icon = {"HIGH": "🔴", "MEDIUM": "🟠", "LOW": "🟡"}.get(sev, "⚪")
        with st.expander(f"{icon} {r['source_ip']}  |  {a.get('activity_type')}  |  severity {sev}  |  {r['time']}", expanded=True):
            x, y, z = st.columns(3)
            with x:
                st.markdown("**1. Detection Agent**")
                st.write(f"Type: {a.get('activity_type')}")
                st.write(f"Confidence: {a.get('confidence')}")
                st.write(a.get("reason", ""))
            with y:
                st.markdown("**2. Investigator Agent**")
                st.write(f"Threat: {rep.get('threat_type')}")
                for step in rep.get("timeline", []):
                    st.write(f"- {step}")
                st.write(rep.get("summary", ""))
            with z:
                st.markdown("**3. Response Planner**")
                st.write(f"Proposed: **{p.get('action_type')}** {p.get('target') or ''}")
                st.write(f"Duration: {p.get('duration_seconds')} s")
                st.write(p.get("justification", ""))
            st.caption(f"Executor status: {r['status']} (nothing was really blocked)")

with tab_log:
    st.write("Last 40 log lines. Suspicious IPs found by the agents are marked with 🔴.")
    for l in lines[-40:]:
        st.text(("🔴 " if l.split(" ")[0] in bad_ips else "    ") + l)
    if not lines:
        st.info("access.log is empty or missing.")

with tab_appr:
    st.info("Coming later (Phase 5): risky actions checked by the Watchdog will wait here for a human to Approve or Reject.")
    st.button("Approve", disabled=True)
    st.button("Reject", disabled=True)
