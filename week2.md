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
