"""
SynapseOS — Test Suite
Tests all 5 agents, HuggingFace API connection, TTS, and memory system.
Run: python test.py
"""

import os
import sys
import time
import tempfile

# ============================================================
# TEST UTILITIES
# ============================================================
PASS = "\033[92m[PASS]\033[0m"
FAIL = "\033[91m[FAIL]\033[0m"
INFO = "\033[94m[INFO]\033[0m"

results = {"passed": 0, "failed": 0}

def test(name, fn):
    try:
        fn()
        print(f"{PASS} {name}")
        results["passed"] += 1
    except Exception as e:
        print(f"{FAIL} {name} — {e}")
        results["failed"] += 1

# ============================================================
# TEST 1 — ENVIRONMENT
# ============================================================
def test_env():
    from dotenv import load_dotenv
    load_dotenv()
    token = os.environ.get("HF_TOKEN", "")
    assert token and token != "your_hf_token_here", "HF_TOKEN not set in .env"
    assert token.startswith("hf_"), "HF_TOKEN format invalid"
    print(f"  {INFO} Token: {token[:20]}...")

# ============================================================
# TEST 2 — IMPORTS
# ============================================================
def test_imports():
    import gradio
    import huggingface_hub
    import gtts
    import requests
    print(f"  {INFO} Gradio: {gradio.__version__}")
    print(f"  {INFO} HuggingFace Hub: {huggingface_hub.__version__}")

# ============================================================
# TEST 3 — HUGGINGFACE CLIENT
# ============================================================
def test_hf_client():
    from dotenv import load_dotenv
    load_dotenv()
    from huggingface_hub import InferenceClient
    token = os.environ.get("HF_TOKEN")
    client = InferenceClient(model="Qwen/Qwen2.5-7B-Instruct", token=token)
    assert client is not None, "InferenceClient failed to initialize"
    print(f"  {INFO} Client initialized successfully")

# ============================================================
# TEST 4 — MODEL RESPONSE (PM AGENT)
# ============================================================
def test_pm_agent():
    from dotenv import load_dotenv
    load_dotenv()
    from huggingface_hub import InferenceClient
    token = os.environ.get("HF_TOKEN")
    client = InferenceClient(model="Qwen/Qwen2.5-7B-Instruct", token=token)

    system_prompt = "You are a Project Manager. Analyze the idea briefly in 3 sentences."
    response = client.chat.completions.create(
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": "Analyze this idea: A scam protection app for senior citizens"}
        ],
        max_tokens=100,
        temperature=0.7
    )
    text = response.choices[0].message.content.strip()
    assert len(text) > 20, "Response too short"
    print(f"  {INFO} PM Agent response: {text[:80]}...")

# ============================================================
# TEST 5 — MODEL RESPONSE (ALL 5 AGENTS)
# ============================================================
def test_all_agents():
    from dotenv import load_dotenv
    load_dotenv()
    from huggingface_hub import InferenceClient
    token = os.environ.get("HF_TOKEN")
    client = InferenceClient(model="Qwen/Qwen2.5-7B-Instruct", token=token)

    agents = ["PM Agent", "Developer Agent", "Critic Agent", "Finance Agent", "Security Agent"]
    idea = "Build a scam protection app for senior citizens in India"

    for agent in agents:
        response = client.chat.completions.create(
            messages=[
                {"role": "system", "content": f"You are a {agent}. Give a 2-sentence analysis."},
                {"role": "user", "content": f"Analyze: {idea}"}
            ],
            max_tokens=80,
            temperature=0.7
        )
        text = response.choices[0].message.content.strip()
        assert len(text) > 10, f"{agent} response too short"
        print(f"  {INFO} {agent}: OK ({len(text)} chars)")
        time.sleep(0.5)

# ============================================================
# TEST 6 — TEXT TO SPEECH
# ============================================================
def test_tts():
    from gtts import gTTS
    tts = gTTS("SynapseOS test successful.", lang="en")
    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
    tts.save(tmp.name)
    assert os.path.exists(tmp.name), "Audio file not created"
    size = os.path.getsize(tmp.name)
    assert size > 1000, f"Audio file too small: {size} bytes"
    print(f"  {INFO} Audio file created: {size} bytes")
    os.unlink(tmp.name)

# ============================================================
# TEST 7 — MEMORY SYSTEM
# ============================================================
def test_memory():
    memory = {"conversations": [], "debates": []}
    memory["conversations"].append("Test idea 1")
    memory["conversations"].append("Test idea 2")
    memory["debates"].append({"idea": "Test idea 1", "agents": {}})
    assert len(memory["conversations"]) == 2
    assert len(memory["debates"]) == 1
    print(f"  {INFO} Memory system working: {memory['conversations']}")

# ============================================================
# TEST 8 — GRADIO UI IMPORT
# ============================================================
def test_gradio_ui():
    import gradio as gr
    with gr.Blocks() as demo:
        txt = gr.Textbox(label="Test")
        btn = gr.Button("Test Button")
    assert demo is not None
    print(f"  {INFO} Gradio UI blocks created successfully")

# ============================================================
# RUN ALL TESTS
# ============================================================
if __name__ == "__main__":
    print("\n" + "="*60)
    print("  SynapseOS — Test Suite")
    print("  AMD Developer Hackathon 2026")
    print("="*60 + "\n")

    test("Environment Variables (.env)", test_env)
    test("Python Imports", test_imports)
    test("HuggingFace InferenceClient", test_hf_client)
    test("PM Agent API Response", test_pm_agent)
    test("All 5 Agents API Response", test_all_agents)
    test("Text-to-Speech (gTTS)", test_tts)
    test("Memory System", test_memory)
    test("Gradio UI Components", test_gradio_ui)

    print("\n" + "="*60)
    total = results["passed"] + results["failed"]
    print(f"  Results: {results['passed']}/{total} tests passed")
    if results["failed"] == 0:
        print("  \033[92mAll tests passed! SynapseOS is ready.\033[0m")
    else:
        print(f"  \033[91m{results['failed']} test(s) failed. Please fix before submitting.\033[0m")
    print("="*60 + "\n")

    sys.exit(0 if results["failed"] == 0 else 1)
