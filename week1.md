# Week 1 Update & Research Journey

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
