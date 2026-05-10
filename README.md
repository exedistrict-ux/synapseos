# 🧬 SynapseOS — AI Agent Civilization

> **AMD Developer Hackathon 2026** | Built on HuggingFace Inference API | Powered by Qwen2.5-7B

[![Python](https://img.shields.io/badge/Python-3.14+-blue.svg)](https://python.org)
[![Gradio](https://img.shields.io/badge/Gradio-6.14+-orange.svg)](https://gradio.app)
[![HuggingFace](https://img.shields.io/badge/HuggingFace-Qwen2.5--7B-yellow.svg)](https://huggingface.co)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## What is SynapseOS?

**SynapseOS** is a multi-agent AI debate system where **5 expert AI agents** independently analyze any business idea or problem — each bringing a unique professional perspective. The result is a comprehensive, 360-degree analysis with a final GO/NO-GO decision and a voice summary.

Think of it as having a full expert team in your pocket — a PM, Developer, Critic, Financial Analyst, and Security Expert — all debating your idea simultaneously.

---

## Live Demo

<!-- ADD YOUR SCREENSHOT HERE AFTER DEPLOYMENT -->
<!-- ![SynapseOS Demo](screenshots/demo.png) -->

**Local URL:** `http://127.0.0.1:7860`  
**Public URL:** Available after running with `share=True`

---

## The 5 Agents

| Agent | Role | What It Analyzes |
|-------|------|-----------------|
| PM Agent | Project Manager | Phases, timeline, milestones, GO/NO-GO |
| Developer Agent | Senior Developer | Tech stack, architecture, scalability |
| Critic Agent | Devil's Advocate | Risks, flaws, failure scenarios |
| Finance Agent | Financial Analyst | Costs, revenue model, break-even |
| Security Agent | Security Expert | Vulnerabilities, GDPR, auth strategy |

---

## Features

- **5 AI Agents** — Each calls HuggingFace API independently
- **150+ word responses** — Detailed, structured analysis per agent
- **Final Decision** — PM Agent gives GO / CONDITIONAL GO / NO-GO
- **Voice Summary** — Text-to-speech summary of the full debate
- **Memory System** — Remembers all ideas analyzed in the session
- **Public Share Link** — Share your debate with anyone via Gradio

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| AI Model | Qwen/Qwen2.5-7B-Instruct (HuggingFace Free) |
| Agent Framework | Custom Multi-Agent Python System |
| UI | Gradio 4.x |
| Voice | gTTS (Google Text-to-Speech) |
| API Client | huggingface_hub InferenceClient |
| Compute | AMD MI300X (AMD Developer Cloud) |

---

## Installation

### Prerequisites
- Python 3.11+
- HuggingFace account (free)
- HuggingFace API token with **Write** permissions

### Setup

**1. Clone the repository**
```bash
git clone https://github.com/exedistrict-ux/synapseos.git
cd synapseos
```

**2. Create virtual environment**
```bash
python -m venv .venv
.venv\Scripts\activate   # Windows
source .venv/bin/activate  # Linux/Mac
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Set up environment variables**

Create a `.env` file in the root directory:
```env
HF_TOKEN=hf_your_token_here
```

Get your free token at: https://huggingface.co/settings/tokens

**5. Run the app**
```bash
python app.py
```

Open your browser at `http://127.0.0.1:7860`

---

## Running Tests

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

## Project Structure

```
synapseos/
├── app.py              # Main application
├── test.py             # Test suite
├── requirements.txt    # Python dependencies
├── .env                # Environment variables (not committed)
├── .env.example        # Example env file
├── .gitignore          # Git ignore rules
└── README.md           # This file
```

---

## How It Works

```
User Input (Idea)
       │
       ▼
┌─────────────────────────────────────────┐
│           SynapseOS Orchestrator        │
└─────────────────────────────────────────┘
       │
       ├──► PM Agent ──────► HuggingFace API (Qwen2.5-7B)
       │                          │
       ├──► Developer Agent ──► HuggingFace API (Qwen2.5-7B)
       │                          │
       ├──► Critic Agent ────► HuggingFace API (Qwen2.5-7B)
       │                          │
       ├──► Finance Agent ───► HuggingFace API (Qwen2.5-7B)
       │                          │
       └──► Security Agent ──► HuggingFace API (Qwen2.5-7B)
                                  │
                                  ▼
                        Final Decision (GO/NO-GO)
                                  │
                                  ▼
                        Voice Summary (gTTS)
```

---

## AMD Developer Cloud Deployment

This project is optimized for AMD MI300X GPU infrastructure.

```bash
# Deploy to HuggingFace Spaces (free hosting)
gradio deploy

# Or run with AMD Developer Cloud
# Set up your instance and run:
python app.py
```

---

## Screenshots

<!-- DEPLOYMENT SCREENSHOT -->
### Main Interface
<!-- ![Main Interface](screenshots/main.png) -->

### Agent Debate Results
<!-- ![Debate Results](screenshots/debate.png) -->

### Voice Summary
<!-- ![Voice Summary](screenshots/voice.png) -->

---

## Example Output

**Input:** "Build a scam protection app for senior citizens in India"

**PM Agent verdict:** GO  
**Action Items:**
1. Conduct pilot survey with senior citizens
2. Partner with local NGOs for validation
3. Develop MVP focusing on key scam detection features

**Biggest Risk:** Ensuring cultural sensitivity and addressing local scamming tactics

---

## Built With

- [Gradio](https://gradio.app) — UI framework
- [HuggingFace Hub](https://huggingface.co) — AI model API
- [Qwen2.5-7B-Instruct](https://huggingface.co/Qwen/Qwen2.5-7B-Instruct) — Language model
- [gTTS](https://gtts.readthedocs.io) — Text to speech
- [AMD Developer Cloud](https://www.amd.com/en/developer/ai-dev-program.html) — GPU compute

---

## Team

**Team Name:** My AMD Team  
**Hackathon:** AMD Developer Hackathon 2026  
**Platform:** lablab.ai

---

## License

MIT License — see [LICENSE](LICENSE) for details.

---

*Built with AMD MI300X GPU · HuggingFace Free Tier · Gradio*
