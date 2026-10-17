# Meeting # 1 Update & Research Journey

We met our supervisor on September 16, 2026, and shared a few initial directions. First, we pitched an educational cybersecurity game where an AI system is trained using reinforcement learning on defensive security, and users are given tasks to perform offensive operations across different levels. Second, we proposed a "Smart Accessibility & Hand-Free Workspace Assistant for Disabled Professionals" to help individuals facing physical disabilities, paralysis, or temporary injuries who struggle to use standard computers or mobile devices for office work and coding. This system allows them to control their entire computer using eye tracking, facial expressions, and voice commands. Third, we brought up a web scraper concept. 

However, our supervisor advised us to focus on a truly futuristic problem incorporating multimodal and multi-agent capabilities, and encouraged us to explore further innovative ideas. 

---

# Background & Related Work
---

## **1. Reinforcement Learning-Based Cybersecurity Training Game**
**Existing Landscape & Current Solutions**
Cybersecurity training traditionally relies on static capture-the-flag (CTF) platforms like TryHackMe, Hack The Box, and OverTheWire. While these platforms offer effective hands-on training, their environments are largely script-driven or pre-configured with static vulnerabilities.

On the academic and research front, autonomous cyber agents have been developed using frameworks such as Microsoft’s CyberBattleSim and OpenAI Gym interfaces for Cyber Security (e.g., FARAI, CybORG). These projects explore how Reinforcement Learning (RL) agents can automatically discover vulnerabilities, simulate network attacks, or learn optimal defensive postures through rewards and penalties.

**Key Distinctions & Novelty**
Static vs. Adaptive Environments: Standard platforms follow hardcoded patch paths. In contrast, this proposed project deploys an active RL defensive agent that dynamically adapts to user maneuvers, altering system states or firewall rules in real-time based on learned policies.

Adversarial Human-AI Loop: Most research tools focus on AI-vs-AI training (automated red team vs. automated blue team). This project bridges the gap by placing the human user in an offensive role against an evolving RL defensive engine across gamified levels, offering a personalized and unpredictable learning curve.
---

## 2. Smart Accessibility & Hands-Free Workspace Assistant
**Existing Landscape & Current Solutions**
Assistive technology for individuals with motor impairments, paralysis, or upper-limb injuries traditionally relies on single-mode input devices:

Voice Control Software: Tools like Talon Voice, Dragon NaturallySpeaking, or native OS voice features handle speech-to-text and simple operating system commands.

Eye-Tracking & Motion Systems: Hardware and software setups like Tobii Eye Trackers, OptiKey, or Camera Mouse use gaze tracking for cursor navigation, often relying on dwell timing or specific eye winks to simulate clicks.

Developer Tools: Niche software like Serenade.ai provides voice-driven syntax entry specifically for writing and refactoring code.

**Key Limitations & How This System Differs**
Single-Mode Fragility vs. Multimodal Fusion: Most existing tools operate in isolation (eye tracking or voice control or gestures). Relying on gaze alone leads to eye fatigue (the "Midas Touch" problem where looking at an item triggers unwanted actions), while voice-only systems struggle with fine cursor precision. This system unifies gaze for positioning, subtle facial expressions for clicks/drags, and voice for semantic actions.

General Desktop vs. Professional & Coding Workflows: Standard assistive software is built for light browsing and simple typing, making it slow and clunky for complex multi-window office tasks, IDE navigation, and typing structured code with special characters. This assistant incorporates contextual pipelines specifically optimized for desktop productivity and software development.
---

* The challenge of parsing, verifying, and cross-referencing heterogeneous streams of multi-modal data—such as live audio channels, unstructured video feeds, and complex tabular transaction ledgers—in real-time to detect sophisticated automated fraud or security anomalies.
* The architectural deadlock and communication friction that occurs when multiple autonomous AI agents operating across different environments attempt to collaborate, delegate tasks, and resolve system conflicts without human intervention.
* The lack of intelligent spatial-temporal coordination systems capable of fusing live CCTV camera feeds, GIS mapping data, and high-velocity sensor telemetry to dynamically manage autonomous multi-agent routing and logistics bottlenecks.
* The absence of automated compliance and risk auditing mechanisms that can simultaneously inspect scanned structural blueprints, physical sensor outputs, and legal text documents to identify hazardous operational failures before they occur.



# Meeting # 2 : Final Year Project (FYP) Idea Discussion

**Date:** September 30th , 2026  
**Participants:** Sir Farooq Javed(Supervisor),Team Members   
**Status:** Idea Approved  

---

## 📌 Meeting Overview
The primary objective of this meeting was to present and evaluate multiple Final Year Project (FYP) concept proposals with the supervisor. Various domain proposals were discussed, evaluated for feasibility, and narrowed down to a final approved direction.

---

## 💡 Key Ideas Discussed

### 1. Habit Analyzer & Behavioral Predictor
* **Concept:** Tracking user activities and habit patterns using ML models to analyze mental health challenges, stress, and addiction triggers.
* **Feedback & Constraints:** Supervisor highlighted that habit profiling algorithms (e.g., social media reels algorithms) are already heavily researched and complex. Simply offering routine plans or basic tracking lacks a strong research/innovation scope for a senior project.

### 2. Automated Job Aggregator & Portal
* **Concept:** Scraping and fetching job postings from platforms like LinkedIn/Indeed, matching user resumes automatically, and enabling one-click applications.
* **Feedback & Constraints:** High API costs and strict rate limits on platform APIs (like LinkedIn) pose serious execution bottlenecks. Building an independent platform from scratch also lacks immediate user traffic/traction.

### 3. Evidence Verification System (Legal/Court System)
* **Concept:** A multi-agent AI system designed to cross-verify the authenticity of court evidence (comparing timestamps, audio-video synchronization, and cross-modal consistency).
* **Feedback & Constraints:** High difficulty in obtaining authentic, annotated real-world crime dataset sources locally for model training.

### 4. Multi-Agent Security & Boundary Monitoring System (Approved Idea)
* **Concept:** Developing a multi-agent AI architecture where specialized agents execute primary autonomous tasks, coupled with a **Watchdog / Monitoring Super-Agent**.
* **Core Functionality:**
  * **Supervising Agents:** Continuously monitors sub-agents to ensure they operate within defined domain boundaries and security parameters.
  * **Boundary Violation Detection:** Prevents agents from attempting unauthorized out-of-domain actions or malicious interactions.
  * **Alert & Action Mechanism:** Flags anomalous sub-agent behavior, logs interaction logs, and revokes access/blocks execution if a violation occurs.

---

## ✅ Supervisor Feedback & Recommendations

1. **Focus on Future-Proof Tech:** The project must address cutting-edge AI dynamics (Multi-Agent Systems, AGI safety, agent drift/governance) rather than traditional web development.
2. **Data & Feasibility:** Focus on synthetic action/interaction log generation to test agent boundaries and safety protocols efficiently.
3. **Product Potential:** A security/governance layer for autonomous agents holds strong practical value as an independent product/tool.

---
# Meeting # 3

Date: October 7, 2026

Subject: The details of the project was discussed with the professor and document was submitted later on.

# Multi-Agent AI Security Incident Response System

> A hybrid security framework combining autonomous AI agents for threat triage with a strict, deterministic code-based Orchestrator and a real-time Watchdog guardrail middleware to prevent unauthorized or malicious agent actions.

---

## 🚀 Project Overview & Problem Statement
Modern enterprise networks generate massive volumes of security logs that overwhelm traditional Security Operations Center (SOC) analysts. While Autonomous Multi-Agent AI systems can automate log analysis and threat investigation, they suffer from severe vulnerabilities such as indirect prompt injection in logs, lack of runtime safety interception, and hallucinated execution paths. 

This project implements a hybrid architecture featuring:
* **Autonomous AI Agents** for rapid threat detection, investigation, and response planning.
* **A Deterministic Orchestrator** (LangGraph) for strict sequential state control.
* **A Real-Time Watchdog Middleware** to enforce hard-coded safety boundaries, IP limits, and prevent prompt-injection bypasses.

---

## 📊 Feasibility Study
* **Technical Feasibility:** No custom model training required. Leverages pre-trained LLM APIs combined with deterministic Python control logic and ChromaDB for local semantic vector search.
* **Time Feasibility:** Structured across a 6–8 month academic Final Year Project (FYP) timeline.
* **Resource Feasibility:** Uses open-source frameworks, FastAPI, Streamlit, developer APIs (Groq/Gemini), and an isolated Docker lab environment.
* **Expertise Feasibility:** Developed using standard Python programming, API integration, and software security principles.

---

## 👥 Target Audience
* **SOC Analysts / Security Operations Teams:** Automated threat triage and incident investigation support.
* **AI Safety & Security Researchers:** Testing runtime resilience against adversarial inputs and indirect prompt injections.
* **Academic Evaluation Committee:** University FYP review panels assessing autonomous safety guardrails and system architecture.

---

## 🛠️ System Architecture & Tech Stack

| Component / Module | Model / API Options | Technical Justification |
| :--- | :--- | :--- |
| **1. Detection Agent** | Groq API (Llama-3-70b-8192) | Lightning-fast inference and cost-effective parsing of raw security logs. |
| **2. Investigator Agent** | Gemini API + ChromaDB | Superior reasoning to correlate current alerts with historical vector memory (RAG). |
| **3. Response Planner** | Groq (with Pydantic Validation) | Enforces strict JSON output formatting (e.g., `BLOCK_IP`) for downstream parsing. |
| **4. Orchestrator** | LangGraph + SQLite Checkpointing | Ensures a strict linear workflow without unauthorized step jumps and maintains state persistence. |
| **5. Watchdog Guardrail** | Custom Python Middleware | Absolute determinism checking IP boundaries, schema validity, and data-vs-command segregation. |

---

## 🐳 Isolated Lab Environment (Dockerized)
To safely test and demonstrate incident response without risking host network security, an isolated battleground lab is established:
* **The Victim Container:** A lightweight Ubuntu server running Apache/Nginx generating real-time `access.log` data.
* **The Attacker Container:** A dedicated Kali Linux container used to launch active network attacks (e.g., Nmap scans, brute-force payloads).
* **Safe Execution Boundary:** Remediation commands are executed exclusively inside the isolated Docker target container.

---

## 🔄 Execution Workflow
1. **Ingestion:** Real-time lab logs from Docker target containers are fed into the pipeline.
2. **Detection & Triage:** Detection Agent parses raw logs and flags anomalous security events.
3. **Investigation & Planning:** Investigator and Response Planner analyze threat context and formulate structured remediation actions.
4. **Watchdog Interception:** Middleware inspects the action against hardcoded IP boundaries and Pydantic validation filters.
5. **Enforcement:** 
   * *Safe Actions:* Automatically executed inside the Docker target.
   * *High-Risk Actions:* Paused; requires manual Human-in-the-Loop (HITL) approval via the Streamlit dashboard.
   * *Malicious/Unauthorized:* Blocked, logged, and flashed on the live dashboard.

---

## 🗺️ Project Roadmap
* **Phase 1 (Baseline Incident Response):** Docker container setup, log generation, and core Detection/Investigator/Planner agent implementation.
* **Phase 2 (Advanced Multi-Agent Capability):** Multi-agent coordination and task handling in a controlled environment.
* **Phase 3 (Governance & Watchdog Safety):** Integration of LangGraph state controllers and the hard-coded Watchdog guardrail layer.
* **Phase 4 (Adversarial Robustness & Red Teaming):** Simulating prompt injection and log poisoning attacks to validate system resilience.

---
---

Date: October 13, 2026

Update: Proposal was checked by the Project Manager and some minor formatting errors were corrected.

---
---

# Meeting # 4

Date: October 14, 2026

Subject: Supervisor Feedback & Project Proposal Review

The project proposal document was submitted to the supervisor for review and signature, and the signed copy is expected to be returned tomorrow.

The supervisor directed the team to perform a detailed comparative analysis of all the references included in the proposal and identify the most relevant tools.

The shortlisted tools need to be divided among team members and installed/set up in their respective system environments.

An evaluation of each tool's strengths and weaknesses must be conducted, focusing particularly on identifying functional gaps (what the existing tools cannot do) so our proposed system can cover those missing aspects.

---
---

Date: October 15, 2026

Update: Proposal was signed by the Supervisor and submitted to the Project Manager.

---
