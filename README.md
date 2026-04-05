
---
title: OpenEnv Support Triage
emoji: 🤖
colorFrom: blue
colorTo: green
sdk: docker
app_file: app.py
pinned: false
---

# 🚀 AI Customer Support Triage Environment (OpenEnv)

## 🌐 Live Demo
👉 https://palakguptaaa-openenv-support-triage.hf.space  
👉 Swagger API Docs: https://palakguptaaa-openenv-support-triage.hf.space/docs  

## GitHub Repositery
https://github.com/palak720/openenv-support-triage

---

## 📌 Overview

This project simulates a **real-world customer support system** where an AI agent classifies, prioritizes, and responds to incoming support tickets.

It follows the **OpenEnv standard**, allowing agents to interact using:

- `reset()`
- `step()`
- `state()`

---

## 🎯 Problem Statement

Companies receive thousands of support tickets daily.

Manual triage:
- ❌ slow
- ❌ inconsistent
- ❌ expensive

---

## 💡 Solution

We built an **AI-powered triage environment** where:

- Tickets are simulated
- An agent makes decisions
- A scoring system evaluates performance

---

## 🧠 Features

- ✅ Real-world simulation (support tickets)
- ✅ OpenEnv-compliant API
- ✅ Multi-task evaluation (easy → medium → hard)
- ✅ Deterministic graders (0.0–1.0 scoring)
- ✅ Memory-based agent reasoning
- ✅ Logging system (run_logs.json)
- ✅ Leaderboard tracking
- ✅ Fully Dockerized deployment
- ✅ Live deployed on Hugging Face Spaces

---

## ⚙️ Environment Design

### 📥 Observation Space

| Field | Type |
|------|-----|
| ticket_id | string |
| message | string |
| customer_tier | string |
| timestamp | string |

---

### 📤 Action Space

| Field | Type |
|------|-----|
| category | string |
| priority | string |
| assigned_team | string |
| response | string |

---

## 🧪 Tasks

| Task | Description |
|------|------------|
| Easy | Predict ticket category |
| Medium | Category + priority |
| Hard | Full triage (category + priority + response) |

---

## 📊 Reward System

- Continuous score: **0.0 → 1.0**
- Partial credit for correct decisions
- Penalizes incorrect classification
- Rewards meaningful responses

---

## 🤖 Agent Design

### Current Implementation:
- Rule-based intelligent agent
- Memory-enhanced decisions
- Fallback-safe logic

### Optional:
- LLM-based agent (OpenAI integration supported)

---

## 🔄 API Endpoints

| Endpoint | Method | Description |
|---------|--------|------------|
| `/` | GET | Health check |
| `/reset` | POST | Reset environment |
| `/step` | POST | Take action |
| `/state` | GET | Get current state |

---

## ▶️ Run Locally

```bash
git clone <repo>
cd openenv-support-triage

pip install -r requirements.txt
uvicorn app:app --reload

## 🐳 Run with Docker

docker build -t openenv .
docker run -p 8000:8000 openenv

📁 Project Structure
openenv-support-triage/
│
├── env/              # environment logic
├── agent/            # agent implementations
├── graders/          # scoring system
├── tasks/            # task definitions
├── logs/             # run logs
│
├── app.py            # FastAPI app
├── Dockerfile
├── requirements.txt
├── openenv.yaml
├── leaderboard.json
├── README.md


## 📈 Sample Output
Ticket: Payment failed but money deducted
Action: billing, high, payments team
Reward: 0.9


## 🏆 Results
Average Score (Hard Task): ~0.8
Demonstrates intelligent decision-making
Robust evaluation system


##🚀 Future Improvements
🔹 Frontend dashboard (React)
🔹 Real LLM integration
🔹 Multi-agent comparison
🔹 Analytics visualization


##🧠 Key Learnings
Environment design for AI agents
Reward shaping techniques
API-based agent interaction
Deployment with Docker + Hugging Face

