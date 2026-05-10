Hugging Face's logo
Hugging Face
Models
Datasets
Spaces
Buckets
new
Docs
Enterprise
Pricing


Spaces:
lablab-ai-amd-developer-hackathon
/
synapseos


like
0

Logs
App
Files
Community
Settings
synapseos/
README.md
Metadata UI
license


title

SynapseOS
sdk


Gradio
emoji


+ Add Emoji
colorFrom


gray
colorTo


purple
pinned

thumbnail

No file chosen
short_description


164
165
166
167
168
169
170
171
172
173
174
175
176
177
178
179
180
181
182
183
184
185
186
187
188
189
190
191
192
193
194
195
196
197
198
199
200
201
202
203
204
205
206
207
208
209
210
211
212
213
214
215
216
217
218
219
220
221
222
223
224
225
226
227
228
229
230
231
232
233
234
235
236
237
238
239
240
241
242
243
244
245
246
247
248
249
250
251
252
253
254
255
256
257
258
259
260
261
262
263
264
265
266
267
268
269
270
271
272
273
274
275
⌄
⌄
⌄
⌄
⌄
⌄
⌄
⌄
⌄
⌄
⌄
⌄
⌄
⌄
---
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
Commit directly to the
main
branch
Open as a pull request to the
main
branch
Commit changes
Upload images, audio, and videos by dragging in the text input, pasting, or clicking here.
