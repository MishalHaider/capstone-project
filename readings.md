# Weekly Research Update
We spent this week researching real-world problems and shortlisted some project ideas for our multi-modal, multi-agent system. Below is each idea along with the background of the problem and how we'd solve it with multiple agents.
#### 1. Oversight for Autonomous AI Agents
##### Problem
AI agents are increasingly trusted to book flights, spend money, write and deploy code, and negotiate with other companies' agents. As they chain longer sequences of actions and interact with agents from other vendors, nobody watches them in real time. A bad decision, or two agents with conflicting actions, can cause damage before anyone notices.
##### Existing Work
- **LLM/agent observability tools** (e.g., LangSmith, Langfuse, Arize Phoenix) record traces, logs, latency, and cost.
- **Guardrail frameworks** (e.g., NeMo Guardrails, Guardrails AI, Llama Guard) filter unsafe inputs and outputs of a single model.
- **Interoperability protocols** (e.g., MCP, Google's A2A) let agents from different vendors talk to each other and use tools.
##### Limitations
- Observability tools mostly **log after the fact**. They help with debugging, not with stopping an action mid-way.
- Guardrails check **one model's text**, not a long chain of real-world actions (payments, deployments).
- Tools are usually **tied to one framework or vendor**, so cross-vendor agent interactions are invisible.
- Protocols enable communication but include **no oversight layer**. Nobody checks whether two agents' actions conflict.
- Human review does not scale once agents run continuously.
##### What We Add
Independent **watchdog agents** that sit outside the agents they monitor and:
- watch logs, screen activity, and transaction records **across vendors** in one place,
- detect **cross-agent conflicts** and risky action sequences (not just single bad outputs),
- work in **real time**, with graded responses: log, flag, pause for human approval, or block.
  
#### 2. Multimodal Evidence Verification for Courts
##### Problem
Courts face a growing flood of image, video, audio, and digital document evidence. Judges and lawyers rarely have the time or technical expertise to verify all of it, so manipulated or contradictory evidence can go unnoticed.
##### Existing Work
- **Deepfake/manipulation detectors** for images, video, and audio (commercial and research tools).
- **Digital forensics tools** for metadata analysis, error-level analysis, and audio forensics.
- **Provenance standards** such as C2PA / Content Credentials, which attach signed capture and edit history to media.
##### Limitations
- Most tools are **single-modality**. Each file is checked in isolation, so contradictions between evidence items are missed.
- Detectors often **generalize poorly** to new generation methods and return a bare score with little explanation.
- Provenance only works if the media was **signed at capture**. Most existing evidence has no such record.
- Outputs are technical and **not written for judges and lawyers**.
- Full manual forensic review is slow and expensive.
##### What We Add
- **Separate specialist agents** per evidence type (image, video, audio, documents).
- A **cross-modal consistency agent** that checks evidence against each other (e.g., does the audio timestamp match the video? do the metadata and document dates agree?).
- A **report agent** that gives plain-language findings with confidence levels and reasons.
- **Decision support only, never a verdict.** Humans stay in charge.

#### 3. AI Companion Dependency
##### Problem
AI companion apps are used daily by hundreds of millions of people, including isolated elderly people and teenagers. Studies suggest heavy, long-term use can deepen loneliness, and some users show dependency and withdrawal-like reactions when access is cut off. There is no early-warning system for unhealthy usage.
##### Existing Work
- **Research studies** linking heavy chatbot use with loneliness and emotional dependence, mostly using surveys and controlled experiments.
- **App-level safety features** such as usage/time reminders, parental controls, age gates, and crisis-keyword responses (introduced by some companion platforms).
- **General mental-health chatbots and wellbeing apps** that support users but are separate from the companion products.
##### Limitations
- Most findings come from **self-reported surveys**, not real-time behavior signals.
- Existing safeguards are **crude**: fixed time limits and keyword triggers miss gradual change.
- Nothing tracks a user's **trend over weeks or months** (rising late-night use, mood drift, withdrawal from real contacts).
- Interventions are often **one-size-fits-all or abrupt** (sudden cutoffs), which can worsen dependency and feel paternalistic.
- Escalation to real human support is rare and poorly defined.
##### What We Add
- Agents that read **sentiment, tone, and usage patterns over time**.
- A **coordinator agent** that picks a proportionate response: no action, a gentle nudge, suggesting offline connection, or alerting real support in serious cases.
- **User-respecting design:** transparent, user-controlled thresholds, privacy-preserving analysis, and no lecturing.
  
#### 4. Learned Helplessness from AI Tutors
##### Problem
Students increasingly ask AI tutors and homework helpers for answers instead of working through problems. Over time this risks weakening independent thinking, yet most tools cannot tell whether a student is genuinely learning or just copying.
##### Existing Work
- **Intelligent Tutoring Systems** (e.g., knowledge tracing, hint-based tutors) that model student mastery in structured domains.
- **LLM tutors with Socratic modes** (e.g., Khanmigo, "study mode" features) that are prompted to guide rather than give answers.
- **Learning analytics** dashboards tracking time spent, scores, and completion.
##### Limitations
- Classic ITS work well in **narrow, structured subjects** but do not handle open-ended LLM conversation.
- Socratic behavior in LLM tutors is mostly **prompt-based** and easy to bypass by simply insisting on the answer.
- Tools measure **engagement and correct answers**, not how much of the work was the student's own.
- There is no reliable check of **real understanding** versus answer extraction.
- Hint policies are **fixed**, not adapted to each student's current need.
##### What We Add
- A **contribution-tracking agent** estimating how much of the work is genuinely the student's own.
- An **understanding-check agent** that probes with follow-up and transfer questions.
- A **coordinator agent** that decides, per student and moment, whether to give a hint, ask a question, or back off so real learning happens.
#### References: ####
Along with our own discussion, we read a number of research papers on these topics and also gathered supporting content using AI tools like Claude, DeepSeek, and Gemini.

---
---
# Research Paper Review: Architecture Matters for Multi-Agent Security

**Paper Title:** Architecture Matters for Multi-Agent Security  
**Authors:** Ben Hagag, William L. Anderson, et al. (2026)  
**Topic Relevance:** Multi-Agent Governance, AI Safety, Watchdog Interceptor Systems  

---

## 📌 Executive Summary
This paper demonstrates that security risks in **Multi-Agent Systems (MAS)** are fundamentally different and more complex than in single-agent LLM systems. Traditional content moderation and prompt-filtering mechanisms fail in multi-agent workflows because the attack surface exists within **inter-agent interactions, task delegation patterns, and execution boundaries**, rather than at an individual prompt level.

The authors prove that **System Architecture** (Boundary Separation, Runtime Supervision, Access Control) is the only reliable method to secure multi-agent environments effectively.

---

## 💡 Key Insights & Takeaways

### 1. Single-Prompt Guardrails Fall Short
* Traditional single-prompt guardrails (such as input toxicity filters) cannot protect multi-agent architectures.
* Malicious intent rarely resides in a single input; instead, it propagates through normal, benign-looking messages shared across multiple sub-agents.

### 2. Cascading Failures & Privilege Escalation
* If a single sub-agent is compromised via indirect prompt injection, it can exploit other trusted sub-agents to execute high-privilege actions (Privilege Escalation).
* Complex multi-step task delegation often leads to **goal drift**, where an agent unknowingly crosses its designated domain boundaries.

### 3. Architecture as the Primary Defense Layer
* Relying purely on LLM alignment or prompt instructions is insufficient for security guarantees.
* System-level architectural controls (Guardrails, Sandboxing, Isolation) are required to provide deterministic safety enforcement.

### 4. Need for Runtime Isolation & Strict Boundaries
* Sub-agents must operate under the Principle of Least Privilege with minimal necessary capabilities.
* A dedicated **Interceptor / Monitoring Layer** must sit on the inter-agent communication channel to inspect and block unauthorized requests in real time.

---

## 🛠️ Relevance to Our FYP (Multi-Agent Watchdog System)

This research directly validates the core architecture of our Final Year Project:

1. **Watchdog Interceptor Justification:** Confirms that runtime execution oversight must happen at the inter-agent communication layer—the core function of our Watchdog Super-Agent.
2. **Boundary Enforcement:** Supports isolating sub-agents within domain-specific boundaries to prevent privilege escalation.
3. **Mitigating Drift & Exploitation:** Proves that real-time action interception and audit logging are necessary to prevent cascading agent compromises.

---

## 📝 Key Citation for FYP Report

> *"Security in multi-agent LLM architectures cannot be achieved through prompt engineering alone; it requires explicit structural boundaries, privilege isolation, and real-time execution oversight."* — **Hagag et al. (2026)**

---

### 2. Don't Make Models Guess Security and Safety: Symbolic Guardrails for Domain-Specific AI Agents

**Authors:** Yining Hong, Yining She, Eunsuk Kang, Christopher S. Timperley, Christian Kästner (Carnegie Mellon University)
**Reference:** arXiv:2604.15579, 2026
**Code:** https://github.com/hyn0027/agent-symbolic-guardrails

#### Problem
AI agents that call tools (APIs, databases, command line) are being used in business software such as airline support, healthcare and customer service. A single wrong tool call can be costly: a refund that breaks policy, a flight cancelled after it has already left, or a leaked patient record. Most current defences either train the model to behave (alignment, RLHF) or use a second LLM to judge the first one. Both are probabilistic, so they lower the risk but cannot guarantee that a bad action never happens.

#### Idea
The authors propose **symbolic guardrails**, which are normal software checks written in code and applied to tool calls. Examples are checking that a user owns a ticket before cancelling it, validating inputs against a schema, requiring authentication before any other tool runs, and using fixed confirmation prompts. If the check fails, the action is blocked no matter what the model "thinks".

#### What they did
The paper has three parts:

1. **Benchmark review.** They reviewed 80 agent security and safety benchmarks. 61% state no rules at all, 24% give only vague goals such as "don't do unsafe things", and only about 9% give rules that can actually be verified.
2. **Enforceability analysis.** On τ²-Bench (airline), CAR-bench (in-car assistant) and MedAgentBench (medical records), they checked which requirements could be enforced with code. About 74% could, and about 95% of those needed only simple checks such as API validation. Requirements about tone, hallucination, step-by-step procedures and common-sense judgement could not be enforced this way.
3. **Experiments.** They ran each benchmark with and without guardrails using GPT-4o and GPT-5.

| Benchmark | Rule violations without guardrails | With guardrails | Task success |
|---|---|---|---|
| τ²-Bench (GPT-4o) | 52% | 0% | 0.36 → 0.48 |
| τ²-Bench (GPT-5) | 20% | 0% | 0.68 → 0.70 |
| CAR-bench (GPT-5) | 21% | 0% | 0.59 → 0.72 |
| MedAgentBench (GPT-5) | 23% | 0% | 0.59 → 0.67 |

Guardrails did not hurt task success and often improved it. The authors suggest that when an action is blocked, the agent receives a clear error and tries a safer alternative.

#### Limitations
- Zero violations with guardrails is true by design, because violating calls are rejected. The useful comparison is the baseline violation rate and the change in task success.
- Only three benchmarks and two models were tested, with small samples (50 to 300 tasks) and one run each. Some utility gains are not statistically significant.
- The MedAgentBench policy was generated by an LLM, not written by practitioners.
- Multi-agent and multimodal systems were not tested.

#### Takeaway
If a rule can be written as code, enforce it in code instead of relying on the prompt, and use neural guardrails only for what code can't check.

---

### 3. Watch Out for Your Agents! Investigating Backdoor Threats to LLM-Based Agents

**Authors:** Wenkai Yang, Xiaohan Bi, Yankai Lin, Sishuo Chen, Jie Zhou, Xu Sun
**Reference:** NeurIPS 2024
**Code:** https://github.com/lancopku/agent-backdoor-attacks

#### Problem
A backdoor attack hides a trigger inside a model, usually by poisoning part of its training data. The model behaves normally until the trigger appears, and then it follows the attacker's goal. Earlier work studied this on plain LLMs that answer directly. Agents work in several steps (think, act, observe, repeat), so there are many more places to hide an attack. This paper is presented as the first systematic study of backdoors in LLM agents.

#### Three types of attack
The attacks are separated by where the trigger sits and where the damage appears. The example used is a shopping agent asked to buy sneakers.

| Attack | Trigger | What changes | Example |
|---|---|---|---|
| Query-Attack | In the user's request | Final result | The agent adds "adidas" to its search and only looks at Adidas products |
| Observation-Attack | In what the environment returns | Final result | If Adidas appears in the search results, the agent buys it even when better options exist |
| Thought-Attack | Anywhere | Only the intermediate steps | The task is done correctly, but the agent always uses an attacker-chosen tool |

Thought-Attack is the hardest to notice because the final answer is correct. The authors also point out that the trigger can be an everyday phrase, so normal users can set it off without knowing.

### Experiments
They used the WebShop task from AgentInstruct for Query and Observation attacks, and a subset of ToolBench (translation tasks, target tool "Translate_v3") for Thought-Attack. The base models were LLaMA2-7B variants, fully fine-tuned. Poisoned training examples were generated with GPT-4 and then manually filtered. The main metric was attack success rate (ASR).

#### Results
- **Query-Attack:** ASR rose from 37% to 100% as poisoning increased. About 50 poisoned samples, around 2.6% of the training data, were enough for 100%.
- **Observation-Attack:** ASR reached 78%. It is harder to learn a trigger buried in a long observation, but this attack kept normal performance better.
- **Thought-Attack:** The agent increasingly used the target tool while still completing the task correctly, and normal performance stayed close to the clean model.
- **Stealth:** On inputs without the trigger, backdoored agents showed the target behaviour only about 0.5% to 1% of the time.
- **Defence:** One existing defence (DAN) performed poorly, letting between 83% and 100% of poisoned samples through. The authors say better defences are needed.

#### Limitations
- Only small models (LLaMA2-7B) and the ReAct framework, with one task per attack type.
- No error bars or significance tests, and only one defence was tested.
- The attacker needs access to training data or fine-tuning, which matters mainly when using third-party models or datasets.

#### Takeaway
An agent can be compromised in its reasoning steps even when its final output looks fine. Be careful with third-party models and training data.

---

### How the papers connect
Paper 1 is about defence: stop trusting the model to follow rules and enforce them in code. Paper 2 is about attack: the model itself may be compromised through poisoned training. Both point to keeping important decisions outside the model.

### Relevance to our project
Our system uses a code-based orchestrator and watchdog around LLM agents (detection, investigation, response).
- Agents should only propose actions. The orchestrator runs the real tools after the watchdog approves (Paper 1).
- The watchdog should check every tool call and its parameters, not just the final answer, because of Thought-Attack (Paper 2).
- Logs, alerts and retrieved memory should be treated as untrusted input, since an attacker may control their content (Observation-Attack).
- High-impact actions should still need human approval.
