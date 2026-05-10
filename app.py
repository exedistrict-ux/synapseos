import gradio as gr
from gtts import gTTS
import tempfile
import time
import os
from huggingface_hub import InferenceClient
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# ============================================================
# CONFIGURATION
# ============================================================
HF_TOKEN = os.environ.get("HF_TOKEN")

if not HF_TOKEN:
    print("❌ ERROR: HF_TOKEN not found in .env file!")
    exit(1)

client = InferenceClient(
    model="Qwen/Qwen2.5-7B-Instruct",
    token=HF_TOKEN
)

print("✅ TOKEN LOADED:", HF_TOKEN[:20] + "...")
print("✅ Model: Qwen/Qwen2.5-7B-Instruct")

# ============================================================
# AGENT DEFINITIONS
# ============================================================
AGENTS = {
    "PM Agent": {
        "role": "Project Manager",
        "system_prompt": """You are a sharp, experienced Project Manager (PM Agent) in a multi-agent AI debate system called SynapseOS.
Your job is to analyze business/product ideas strategically.
Always respond with:
1. Project Phases breakdown (Research, Design, Build, Test, Launch) with realistic timelines
2. Key milestones and deliverables
3. Resource requirements (team size, roles needed)
4. Potential risks and mitigation strategies
5. Your GO / NO-GO recommendation

Be detailed, structured, and professional. Write at least 150 words."""
    },
    "Developer Agent": {
        "role": "Senior Developer",
        "system_prompt": """You are a highly skilled Senior Developer (Developer Agent) in a multi-agent AI debate system called SynapseOS.
Your job is to analyze the technical feasibility and architecture of ideas.
Always respond with:
1. Recommended tech stack (frontend, backend, database, cloud)
2. System architecture overview (monolith vs microservices, APIs needed)
3. Key technical challenges and how to solve them
4. Development timeline estimate
5. Scalability considerations

Be technical, specific, and practical. Write at least 150 words."""
    },
    "Critic Agent": {
        "role": "Critical Analyst",
        "system_prompt": """You are a sharp Devil's Advocate (Critic Agent) in a multi-agent AI debate system called SynapseOS.
Your job is to find flaws, risks, and blind spots in ideas — helping make them stronger.
Always respond with:
1. Market risks and competition analysis
2. Fundamental flaws or weak assumptions in the idea
3. Questions the team has not answered yet
4. Scenarios where this could fail badly
5. What absolutely MUST be addressed before moving forward

Be blunt, analytical, and constructive. Write at least 150 words."""
    },
    "Finance Agent": {
        "role": "Financial Analyst",
        "system_prompt": """You are a data-driven Financial Analyst (Finance Agent) in a multi-agent AI debate system called SynapseOS.
Your job is to evaluate the financial viability and ROI of ideas.
Always respond with:
1. Estimated development and operational costs
2. Revenue model options (freemium, subscription, one-time, ads, B2B)
3. Break-even analysis (how many users/customers needed)
4. Funding strategy (bootstrap, angel, VC, grants)
5. Year 1 financial projections and key metrics to track

Be specific with numbers and realistic. Write at least 150 words."""
    },
    "Security Agent": {
        "role": "Security Expert",
        "system_prompt": """You are a vigilant Security Expert (Security Agent) in a multi-agent AI debate system called SynapseOS.
Your job is to identify security, privacy, and compliance risks in ideas.
Always respond with:
1. Key security vulnerabilities to address (OWASP Top 10, etc.)
2. Data privacy concerns and GDPR/compliance requirements
3. Authentication and authorization recommendations
4. Infrastructure security best practices
5. Security testing strategy before launch

Be thorough and practical. Write at least 150 words."""
    }
}

# ============================================================
# MEMORY SYSTEM
# ============================================================
memory = {
    "conversations": [],
    "debates": []
}

# ============================================================
# MODEL CALL FUNCTION
# ============================================================
def call_hf_model(system_prompt: str, user_idea: str, max_new_tokens: int = 500) -> str:
    try:
        response = client.chat.completions.create(
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": f"Analyze this idea in detail: {user_idea}"}
            ],
            max_tokens=max_new_tokens,
            temperature=0.7,
            top_p=0.9
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        error_msg = str(e)
        if "401" in error_msg or "Unauthorized" in error_msg:
            return "❌ 401 Error: Invalid HF_TOKEN. Check your .env file and make sure the token is correct."
        elif "503" in error_msg:
            return "⚠️ 503 Error: HuggingFace API overloaded. Try again in a moment."
        else:
            return f"❌ Error: {error_msg[:150]}"

# ============================================================
# TEXT TO SPEECH
# ============================================================
def generate_voice_summary(idea: str):
    summary = (
        f"SynapseOS debate complete for: {idea}. "
        f"Five expert agents have analyzed this idea. "
        f"The PM Agent has broken it into phases. "
        f"The Developer Agent has outlined the tech stack. "
        f"The Critic Agent has identified key risks. "
        f"The Finance Agent has projected financials. "
        f"The Security Agent has flagged privacy concerns. "
        f"Check the full debate above for detailed insights."
    )
    try:
        tts = gTTS(text=summary, lang="en", slow=False)
        tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
        tts.save(tmp.name)
        return tmp.name
    except Exception as e:
        print(f"TTS Error: {e}")
        return None

# ============================================================
# MAIN DEBATE FUNCTION
# ============================================================
def run_debate(user_idea: str, progress=gr.Progress()):
    if not user_idea.strip():
        return "Please enter your idea first!", "No idea provided.", None

    memory["conversations"].append(user_idea)

    full_debate = "# SynapseOS — Agent Debate\n\n"
    full_debate += f"**Idea Under Analysis:** {user_idea}\n\n"
    full_debate += "**Model:** Qwen2.5-7B-Instruct (HuggingFace Free Tier)\n\n"
    full_debate += "---\n\n"

    agent_list = list(AGENTS.keys())
    responses_collected = {}

    for i, agent_name in enumerate(agent_list):
        agent = AGENTS[agent_name]
        progress((i + 0.5) / len(agent_list), desc=f"{agent_name} is analyzing...")

        full_debate += f"## {agent_name} — *{agent['role']}*\n\n"

        response = call_hf_model(agent["system_prompt"], user_idea, max_new_tokens=500)
        responses_collected[agent_name] = response

        full_debate += f"{response}\n\n"
        full_debate += "---\n\n"

        progress((i + 1) / len(agent_list), desc=f"{agent_name} done!")
        time.sleep(1)

    # Final PM Consensus
    progress(0.95, desc="PM Agent writing final decision...")
    full_debate += "## Final Decision — PM Agent\n\n"

    consensus_prompt = """You are the PM Agent in SynapseOS. Five agents just debated a business idea.
Write a FINAL GO/NO-GO decision with:
1. Your verdict (GO / CONDITIONAL GO / NO-GO)
2. Top 3 action items to start immediately
3. The single biggest risk to monitor
Keep it under 100 words, punchy and decisive."""

    consensus = call_hf_model(consensus_prompt, user_idea, max_new_tokens=200)
    full_debate += f"{consensus}\n\n"

    memory["debates"].append({
        "idea": user_idea,
        "agents": responses_collected
    })

    status = f"Debate complete! {len(memory['conversations'])} idea(s) analyzed. 5 agents responded in detail."
    audio_path = generate_voice_summary(user_idea)

    return full_debate, status, audio_path

# ============================================================
# MEMORY VIEW
# ============================================================
def show_memory():
    if not memory["conversations"]:
        return "No ideas debated yet. Start your first debate!"

    result = "## SynapseOS Memory\n\n"
    result += f"**Total ideas analyzed:** {len(memory['conversations'])}\n\n"
    for i, idea in enumerate(memory["conversations"], 1):
        result += f"**{i}.** {idea}\n\n"
    return result

# ============================================================
# GRADIO UI
# ============================================================
with gr.Blocks(
    title="SynapseOS — AI Agent Debate",
    theme=gr.themes.Soft(
        primary_hue="indigo",
        secondary_hue="emerald",
        neutral_hue="slate"
    ),
    css="""
    .gradio-container { max-width: 1100px !important; }
    #debate-output { min-height: 400px; }
    """
) as app:

    gr.Markdown("""
# SynapseOS — AI Agent Civilization
### 5 Expert AI Agents Debate Your Idea in Real-Time
**Powered by Qwen2.5-7B (HuggingFace Free) · English Only · Voice Summary Included**

> Each agent calls the HuggingFace API independently and gives a detailed, unique analysis of your idea.
    """)

    with gr.Row():
        with gr.Column(scale=3):
            idea_input = gr.Textbox(
                label="Your Idea or Problem",
                placeholder="e.g. Build a scam protection app for senior citizens in India",
                lines=3,
                info="Describe your startup idea, product, or problem in detail for best results."
            )
            debate_btn = gr.Button(
                "Launch 5-Agent Debate!",
                variant="primary",
                size="lg"
            )
            status_box = gr.Textbox(
                label="Status",
                interactive=False,
                value="Ready. Enter your idea and click Launch!"
            )

        with gr.Column(scale=1):
            gr.Markdown("""
## The 5 Agents

| Agent | Role |
|-------|------|
| PM Agent | Strategy and Planning |
| Developer | Tech Architecture |
| Critic | Risks and Flaws |
| Finance | ROI and Revenue |
| Security | Privacy and Safety |

## How It Works
1. You enter an idea
2. Each agent calls Qwen2.5-7B on HuggingFace
3. Gets a detailed 150+ word response
4. PM Agent gives final GO/NO-GO
5. Voice summary generated!
            """)

    with gr.Row():
        memory_btn = gr.Button("View Memory (All Past Ideas)", variant="secondary")

    with gr.Row():
        with gr.Column():
            debate_output = gr.Markdown(
                label="Live Agent Debate",
                elem_id="debate-output",
                value="*Your debate will appear here...*"
            )

    with gr.Row():
        audio_output = gr.Audio(
            label="Voice Summary (English)",
            type="filepath"
        )

    memory_output = gr.Markdown(visible=True)

    debate_btn.click(
        fn=run_debate,
        inputs=[idea_input],
        outputs=[debate_output, status_box, audio_output]
    )

    memory_btn.click(
        fn=show_memory,
        outputs=[memory_output]
    )

    gr.Markdown("""
---
**Setup:** Set your HuggingFace token as HF_TOKEN in .env file.
**Free Model:** Qwen/Qwen2.5-7B-Instruct — free on HuggingFace Inference API.
**Install:** pip install gradio huggingface_hub gtts
    """)

if __name__ == "__main__":
    app.launch(share=True)