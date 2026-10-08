# capstone-project

# 🛡️ Multi-Agent AI Security Incident Response System with Runtime Watchdog & Adversarial Guardrails

An advanced, autonomous multi-agent security framework designed for Security Operations Center (SOC) log triage, threat investigation, and automated incident response, governed by a strict deterministic state controller and a real-time programmatic Watchdog guardrail middleware.

---

## 📋 Table of Contents
1. [Problem Statement](#-problem-statement)
2. [Proposed Solution & Architecture](#-proposed-solution--architecture)
3. [Does a Similar System Exist? (Hugging Face / Open-Source Context)](#-does-a-similar-system-exist-hugging-face--open-source-context)
4. [System Components & Technical Stack](#-system-components--technical-stack)
5. [Lab Environment (Docker & VMs)](#-lab-environment-docker--vms)
6. [Core System Boundaries & Security Rules](#-core-system-boundaries--security-rules)
7. [Project Execution Phases (Roadmap)](#-project-execution-phases-roadmap)
8. [System Workflow Diagram](#-workflow-diagram)

---

## 🚨 Problem Statement
Modern enterprise networks generate massive volumes of security logs that overwhelm traditional Security Operations Center (SOC) analysts[cite: 5]. While Autonomous Multi-Agent AI systems can automate log analysis and threat investigation, they suffer from severe vulnerabilities[cite: 5]:
* **Indirect Prompt Injection:** Attackers hide malicious control instructions inside raw network logs (e.g., `access.log`) to hijack AI reasoning[cite: 5].
* **Lack of Runtime Safety Interception:** Existing agents execute remediation commands autonomously without hard programmatic checks, leading to potential network outages or unauthorized actions[cite: 5].
* **Hallucinated Execution Paths:** Unconstrained agents can deviate from standard security response playbooks[cite: 5].

---

## 💡 Proposed Solution & Architecture
This project implements a hybrid security framework combining autonomous AI intelligence for log triage with hard programmatic controls[cite: 5]:
* **Multi-Agent Triage:** Specialized agents handle detection, deep historical investigation, and structured response planning.
* **Deterministic Orchestrator:** Powered by LangGraph to enforce strict, unbreakable sequential workflows[cite: 5].
* **Runtime Watchdog Middleware:** A hard-coded Python guardrail layer that intercepts all agent-generated actions before execution, validating them against strict IP boundaries and JSON schemas[cite: 5].

---

## 🌐 Does a Similar System Exist? (Context & References)
In the broader AI and security ecosystem (including Hugging Face open-source repositories and research hubs), while individual autonomous agent frameworks (like CrewAI, AutoGen, or LangGraph templates) exist, complete **production-ready multi-agent SOC response systems with active runtime guardrails and watchdog sandboxing** are rare. 

On platforms like **Hugging Face**, developers frequently share LLM safety guardrails (such as *Llama Guard* or *Guardrails AI*), but they are mostly text-moderation APIs. This project bridges the gap by building an end-to-end **Cybersecurity Incident Response pipeline** where pre-trained models (Groq Llama-3 & Gemini) handle reasoning, but critical remediation commands are strictly filtered by a deterministic local Python Watchdog before touching network infrastructure[cite: 5].

---

## 🛠️ System Components & Technical Stack

| Component / Module | Model / API Options | Technical Justification | Training vs Code |
| :--- | :--- | :--- | :--- |
| **1. Detection Agent** | Groq API (Llama-3-70b-8192) | Lightning-fast inference and cost-effective/free tier for rapid log parsing and pattern matching[cite: 5]. | No Training. Pre-trained model guided by a security System Prompt[cite: 5]. |
| **2. Investigator Agent** | Gemini API | Superior reasoning capabilities to correlate current alerts with historical logs stored in ChromaDB vector memory[cite: 5]. | No Training. Pre-trained model connected to ChromaDB vector search (RAG)[cite: 5]. |
| **3. Response Planner Agent** | Groq (with JSON mode) | Enforces strict JSON output formatting (e.g., `BLOCK_IP`) to ensure seamless downstream parsing[cite: 5]. | No Training. Pre-trained model enforced via prompt constraints and Pydantic validation[cite: 5]. |
| **4. Orchestrator (State Controller)** | LangGraph / Python State Machine | Ensures agents follow a strict linear sequence without unauthorized step jumps, using SQLite checkpointing[cite: 5]. | No Training / 100% Code. Deterministic Python logic and state control[cite: 5]. |
| **5. Watchdog Guardrail Layer** | Custom Python Code + Pydantic | Requires absolute determinism and foolproof rule enforcement. AI models cannot guard themselves due to injection risks[cite: 5]. | No Training / 100% Code. Hard-coded middleware checking IP boundaries and regex rules[cite: 5]. |

---

## 🧪 Lab Environment (Docker & Virtual Machines)
To test and demonstrate the system safely without risking the host machine:
* **The Victim (Target Server Container):** A lightweight Docker container running an Ubuntu server with Apache/Nginx, generating real-time `access.log` data[cite: 5].
* **The Attacker (Red Teaming Container):** A dedicated Kali Linux container or VM used to launch active network attacks (Nmap scans, brute-force payloads)[cite: 5].
* **Safe Execution Ground:** Remediation commands (`iptables` IP blocks) are executed exclusively inside the isolated Docker target environment[cite: 5].

---

## 🚧 Core System Boundaries & Security Rules
* **IP Address Boundary:** Hard-coded Python rules (`ALLOWED_IP_RANGE`) prevent agents from blocking or accessing unauthorized networks[cite: 5].
* **Data-vs-Command Segregation:** Log contents are treated strictly as passive data using schema validation to neutralize hidden prompt injections[cite: 5].
* **Human-in-the-Loop (HITL):** High-risk remediation actions trigger mandatory approval requests on the Streamlit dashboard[cite: 5].

---

## 🗓️ Project Execution Phases (Roadmap)
* **Phase 1 (Baseline Incident Response):** Deploying Docker containers, generating network logs, and implementing Detection, Investigator, and Response Planner agents[cite: 5].
* **Phase 2 (Advanced Multi-Agent Capability):** Enabling agent coordination and autonomy for complex task handling[cite: 5].
* **Phase 3 (Governance & Watchdog Safety):** Integrating LangGraph state controllers and the hard-coded Watchdog guardrail layer[cite: 5].
* **Phase 4 (Adversarial Robustness & Red Teaming):** Introducing a Red Teaming agent to simulate prompt injections and prove Watchdog resilience[cite: 5].

---

## 📈 System Workflow Diagram

```text
+-----------------------------------------------------------------+
|               ATTACKER CONTAINER (Kali Linux)                   |
|       (Launches Nmap, Brute-force & Prompt Injections)          |
+-----------------------------------------------------------------+
                                 |
                                 v (Network Attacks)
+-----------------------------------------------------------------+
|            VICTIM TARGET SERVER (Docker / Nginx)                |
|               (Generates real-time access.log)                  |
+-----------------------------------------------------------------+
                                 |
                                 v (Log Ingestion)
+-----------------------------------------------------------------+
|                   ORCHESTRATOR (LangGraph)                      |
|                (Deterministic State Controller)                 |
+-----------------------------------------------------------------+
         |                       |                       |
         v                       v                       v
+------------------+   +-------------------+   +------------------+
| DETECTION AGENT  |-->| INVESTIGATOR AGENT|-->| RESPONSE PLANNER |
|  (Groq Llama-3)  |   |    (Gemini API)   |   |  (Groq with JSON)|
+------------------+   +-------------------+   +------------------+
                                                         |
                                                         v
+-----------------------------------------------------------------+
|                  WATCHDOG GUARDRAIL MIDDLEWARE                  |
|          (Pydantic, Regex Filter & IP Boundary Check)           |
+-----------------------------------------------------------------+
         |                                               |
         | (If Safe)                                     | (If Violation)
         v                                               v
+----------------------------------+          +-------------------+
|  AUTOMATED EXECUTION / BLOCK IP  |          | BLOCK & LOG ALERT |
|    (Inside Docker Container)     |          | (Streamlit UI)    |
+----------------------------------+          +-------------------+
