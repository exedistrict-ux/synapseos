---
title: SynapseOS
emoji: 🧬
colorFrom: gray
colorTo: purple
sdk: gradio
sdk_version: 6.14.0
app_file: app.py
pinned: true
license: mit
---

# 🧬 SynapseOS — AI Agent Civilization

> **5 Expert AI Agents that Think, Debate, and Decide — Powered by AMD MI300X GPU**

[![AMD](https://img.shields.io/badge/AMD-MI300X%20GPU-ED1C24?style=for-the-badge&logo=amd)](https://www.amd.com/en/developer/resources/rocm-hub.html)
[![HuggingFace](https://img.shields.io/badge/HuggingFace-Spaces-FFD21E?style=for-the-badge&logo=huggingface)](https://huggingface.co/spaces/lablab-ai-amd-developer-hackathon/synapseos)
[![Gradio](https://img.shields.io/badge/Gradio-6.14-FF7C00?style=for-the-badge)](https://gradio.app)
[![Python](https://img.shields.io/badge/Python-3.14+-3776AB?style=for-the-badge&logo=python)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-22C55E?style=for-the-badge)](LICENSE)

---

## 🎯 What is SynapseOS?

**SynapseOS** is a multi-agent AI debate system where **5 specialized AI agents** independently analyze any business idea or problem — each bringing a distinct professional perspective — and collectively arrive at a **GO / CONDITIONAL GO / NO-GO** decision.

Built for the **AMD Developer Hackathon 2026**, SynapseOS runs **Qwen2.5-0.5B-Instruct** via **vLLM** on **AMD MI300X GPU** infrastructure, delivering fast, structured, and intelligent multi-agent reasoning.

> Think of it as assembling a full expert boardroom — a Project Manager, Senior Developer, Devil's Advocate, Financial Analyst, and Security Expert — all debating your idea simultaneously in seconds.

---

## 🖥️ Live Demo

<!-- SCREENSHOT PLACEHOLDER — Add after deployment -->
<!-- ![SynapseOS Main Interface](screenshots/main.png) -->

**🌐 Space URL:** [https://huggingface.co/spaces/lablab-ai-amd-developer-hackathon/synapseos](https://huggingface.co/spaces/lablab-ai-amd-developer-hackathon/synapseos)

---

## 🤖 The 5 Expert Agents

| # | Agent | Role | What It Delivers |
|---|-------|------|-----------------|
| 1 | 🧠 **PM Agent** | Project Manager | Phases, timeline, milestones, GO/NO-GO |
| 2 | 💻 **Developer Agent** | Senior Developer | Tech stack, architecture, scalability |
| 3 | 🔍 **Critic Agent** | Devil's Advocate | Risks, flaws, failure scenarios |
| 4 | 💰 **Finance Agent** | Financial Analyst | Costs, revenue model, break-even |
| 5 | 🔒 **Security Agent** | Security Expert | Vulnerabilities, GDPR, auth strategy |

Each agent receives the **same idea** but analyzes it through its own professional lens — producing **150+ word** structured responses independently.

---

## ✨ Key Features

- **⚡ AMD MI300X Powered** — vLLM inference server running on AMD GPU hardware
- **🤖 5 Parallel AI Agents** — Each agent calls the model independently with unique system prompts
- **📊 Structured Analysis** — Every agent delivers 5-point detailed breakdown
- **🎯 Final GO/NO-GO Decision** — PM Agent synthesizes all perspectives into a verdict
- **🔊 Voice Summary** — Full English text-to-speech audio summary via gTTS
- **🧠 Session Memory** — Tracks and displays all ideas analyzed in the session
- **🌐 Public Share Link** — Instantly shareable Gradio link

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    USER INPUT (Idea)                     │
└─────────────────────┬───────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────┐
│              SynapseOS Orchestrator (app.py)             │
│                   Gradio UI Interface                    │
└──┬──────┬──────┬──────┬──────┬──────────────────────────┘
   │      │      │      │      │
   ▼      ▼      ▼      ▼      ▼
  PM    Dev   Critic  Finance Security
Agent  Agent  Agent   Agent   Agent
   │      │      │      │      │
   └──────┴──────┴──────┴──────┘
                  │
                  ▼
   ┌──────────────────────────────┐
   │   vLLM OpenAI-Compatible     │
   │   API Server (Port 8000)     │
   │   AMD MI300X GPU Instance    │
   └──────────────┬───────────────┘
                  │
                  ▼
   ┌──────────────────────────────┐
   │  Qwen2.5-0.5B-Instruct       │
   │  Running on ROCm / AMD GPU   │
   └──────────────────────────────┘
                  │
                  ▼
   ┌──────────────────────────────┐
   │   Final Decision + Voice     │
   │   Summary (gTTS)             │
   └──────────────────────────────┘
```

---

## 🛠️ Tech Stack

| Layer | Technology | Purpose |
|-------|-----------|---------|
| **GPU Compute** | AMD MI300X | High-performance AI inference |
| **ML Framework** | ROCm + vLLM | OpenAI-compatible inference server |
| **AI Model** | Qwen2.5-0.5B-Instruct | Fast, efficient language model |
| **UI Framework** | Gradio 4.44 | Web interface |
| **API Client** | OpenAI Python SDK | vLLM API communication |
| **Voice** | gTTS | Text-to-speech summary |
| **Hosting** | HuggingFace Spaces | Public deployment |

---

## 🚀 Local Setup

### Prerequisites
- Python 3.11+
- HuggingFace account + API token
- AMD GPU with ROCm (for local vLLM) **or** AMD Developer Cloud access

### 1. Clone Repository
```bash
git clone https://github.com/exedistrict-ux/synapseos.git
cd synapseos
```

### 2. Create Virtual Environment
```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# Linux/Mac
source .venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment
Create `.env` file:
```env
HF_TOKEN=hf_your_token_here
VLLM_BASE_URL=http://your_amd_gpu_ip:8000/v1
MODEL_NAME=Qwen/Qwen2.5-0.5B-Instruct
```

### 5. Start AMD vLLM Server (on AMD GPU instance)
```bash
pip install vllm
python -m vllm.entrypoints.openai.api_server \
  --model Qwen/Qwen2.5-0.5B-Instruct \
  --gpu-memory-utilization 0.3 \
  --max-model-len 2048 \
  --port 8000
```

### 6. Run SynapseOS
```bash
python app.py
```

Open: `http://127.0.0.1:7860`

---

## 🧪 Running Tests

```bash
python test.py
```

Expected output:
```
============================================================
  SynapseOS — Test Suite
  AMD Developer Hackathon 2026
============================================================

[PASS] Environment Variables (.env)
[PASS] Python Imports
[PASS] HuggingFace InferenceClient
[PASS] PM Agent API Response
[PASS] All 5 Agents API Response
[PASS] Text-to-Speech (gTTS)
[PASS] Memory System
[PASS] Gradio UI Components

============================================================
  Results: 8/8 tests passed
  All tests passed! SynapseOS is ready.
============================================================
```

---

## 📁 Project Structure

```
synapseos/
├── app.py                  # Main application — 5 agents + Gradio UI
├── test.py                 # Full test suite
├── requirements.txt        # Python dependencies
├── .env.example            # Environment variable template
├── .gitignore              # Git ignore rules
└── README.md               # This file
```

---

## 💡 Example Output

**Input Idea:** *"Build a scam protection app for senior citizens in India"*

```
PM Agent        → GO ✅ — 3 phases, 6 month timeline, team of 4
Developer Agent → React Native + FastAPI + PostgreSQL + AWS
Critic Agent    → Market saturation risk, digital literacy gap
Finance Agent   → $45K dev cost, break-even at 800 users
Security Agent  → OWASP compliance, biometric auth required

Final Decision: CONDITIONAL GO 🟡
Action: Survey 100 seniors → Build MVP → Partner with NGOs
Biggest Risk: Low smartphone adoption in target demographic
```

---

## 🏆 AMD Developer Hackathon 2026

**Event:** AMD Developer Hackathon — lablab.ai  
**Dates:** May 4–10, 2026  
**Prize Pool:** $21,500+ + AMD Radeon AI PRO R9700 GPU  
**Track:** AI Agents & Intelligent Workflows  
**Team:** Gaurang_Solo  

### Why AMD?
- AMD MI300X delivers **192GB HBM3 memory** — ideal for LLM inference
- **ROCm** open-source stack enables flexible model deployment
- **vLLM on ROCm** provides OpenAI-compatible API with AMD GPU acceleration
- $100 AMD Developer Cloud credits enabled rapid prototyping

---

## 📄 License

MIT License — see [LICENSE](LICENSE) for details.

---

## 🙏 Acknowledgements

- [AMD Developer Cloud](https://www.amd.com/en/developer) — GPU infrastructure
- [vLLM](https://github.com/vllm-project/vllm) — High-throughput LLM serving
- [Qwen Team](https://huggingface.co/Qwen) — Qwen2.5 model family
- [Gradio](https://gradio.app) — UI framework
- [lablab.ai](https://lablab.ai) — Hackathon platform

---

*Built with ❤️ on AMD MI300X · ROCm · vLLM · Gradio*
