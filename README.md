# AI for DevOps — Ep 6: Running Models Locally (Ollama) — *S2 finale*

Part of **SoftOps 360 · AI for DevOps (Hands-On)**.

You can't paste prod logs, secrets, or customer data into a public API — compliance and security forbid it. The answer: run the model **on your own machine**. Same code, zero per-token cost, and **your data never leaves.**

## One-time setup: install Ollama
1. Install: **https://ollama.com** (Windows / Mac / Linux)
2. Pull a model:
   ```bash
   ollama pull llama3.2:1b        # ~1.3 GB — fast on a CPU-only laptop (the scripts' default)
   # stronger machine (more RAM / a GPU)? →  ollama pull llama3.1   (8B, smarter but slower on CPU)
   ```
3. Ollama now serves an **OpenAI-compatible API** at `http://localhost:11434` — that's the whole trick.

## What you run
| File | Shows |
|---|---|
| `01_hello_local.py` | the same SDK pointed at `localhost` — runs offline |
| `02_cloud_or_local.py` | **one flag** flips cloud ↔ local; nothing else changes |
| `03_private_log.py` | parse a log containing a **secret**, fully on your machine |

## Setup (this folder)
1. `pip install -r requirements.txt`
2. (only for `02` cloud side) copy `.env.example` → `.env` with your Groq key
3. Make sure Ollama is running, then: `python 01_hello_local.py`

## When to go local (the Ops decision)
- **Private / regulated data** — prod logs, secrets, PII must not leave your network.
- **No per-token cost, no rate limits, works offline.**
- **Trade-off:** needs RAM/CPU (a GPU helps); local models are smaller/slower than frontier cloud ones — so use the Ep5 cheat-sheet: local for private data, cloud for the heaviest reasoning.

## The big lesson
**Privacy is a `base_url` change.** Because Ollama speaks the same OpenAI-compatible API, *everything* you built in Ep 1–5 (prompts, JSON, function calling) runs locally too. You choose, per task, whether the data is allowed to leave.

## 🎉 That completes S2 — Practical LLM Skills
You can now **call, prompt, structure, tool-call, choose, and self-host** LLMs — the full practical toolkit.

**Next → S3: Ops Applications** — we point all of this at real operations:
AI log triage → RAG over your runbooks → the **AI on-call agent** → and **safety & guardrails**.
