# 🚀 SynapseOS — Local Ollama Setup

## What Changed?
✅ **No more API errors!**  
✅ **Local deployment** — runs on your machine  
✅ **No API keys needed**  
✅ **Completely free**  

## Quick Start (5 minutes)

### Step 1: Install Ollama
1. Go to https://ollama.ai
2. Download for your OS (Windows, Mac, Linux)
3. Install it

### Step 2: Pull a Model (do THIS first)
Open PowerShell/Terminal and run ONE of these:

```powershell
# Recommended - Fast & Lightweight (2.3 GB)
ollama pull mistral

# Slower but better - More capable (7 GB)
ollama pull llama2

# Chat-optimized (4.2 GB)
ollama pull neural-chat
```

**This downloads the model** (~2-7 GB depending on choice)

### Step 3: Start Ollama Server
Keep a PowerShell/Terminal window running:
```powershell
ollama serve
```

You should see:
```
2026-05-10 12:34:56 Listening on [::]:11434
```

**LEAVE THIS RUNNING!**

### Step 4: Run SynapseOS
In a NEW PowerShell/Terminal window:
```powershell
cd c:\Users\GB\Desktop\synapse
python app.py
```

You should see:
```
🚀 Local Ollama API: http://localhost:11434/api/generate
📦 Model: mistral
Running on local URL:  http://127.0.0.1:7860
```

**Done!** Open http://127.0.0.1:7860 in your browser

## Available Models

| Model | Size | Speed | Quality | Command |
|-------|------|-------|---------|---------|
| **mistral** | 2.3 GB | ⚡⚡⚡ | Good | `ollama pull mistral` |
| **llama2** | 7 GB | ⚡ | Excellent | `ollama pull llama2` |
| **neural-chat** | 4.2 GB | ⚡⚡ | Good | `ollama pull neural-chat` |

## Change the Model

Edit [app.py](app.py) line ~21:
```python
MODEL_NAME = "mistral"  # Change to "llama2", "neural-chat", etc.
```

Then restart the app.

## Troubleshooting

### ❌ Error: "Cannot connect to Ollama"
- Make sure `ollama serve` is running in another window
- Check http://localhost:11434 is accessible
- Restart Ollama

### ❌ Model takes forever to respond
- First run is slow (loading model into memory)
- Subsequent requests are faster
- Close other apps to free up RAM

### ❌ Out of memory?
- Try `mistral` (smallest)
- Close other apps
- Reduce `num_predict` in app.py

### ❌ Want to switch models?
```powershell
ollama pull llama2  # Download new model
# Edit app.py line ~21: MODEL_NAME = "llama2"
# Restart app.py
```

## System Requirements

- **RAM:** At least 4 GB free (8 GB recommended)
- **Disk:** 3-10 GB depending on model
- **CPU:** Any modern processor works
- **GPU:** Optional (Ollama auto-uses if available)

## Performance Tips

1. **Close heavy apps** (Chrome with many tabs, Photoshop, etc.)
2. **Use Mistral** for fast responses
3. **First run is slowest** (loading model from disk)
4. **Keep Ollama running** in background

---

✨ **Enjoy SynapseOS!** Now with zero API errors, zero latency, and zero costs!
