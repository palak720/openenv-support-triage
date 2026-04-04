
# 🚀 AI Customer Support Triage Environment (OpenEnv)

## 📌 Overview
This project simulates a real-world customer support system where an AI agent classifies and responds to incoming support tickets.

It follows the OpenEnv standard with step/reset/state APIs and supports multi-task evaluation.

---

## 🎯 Features

- Real-world simulation (customer support triage)
- OpenEnv compliant API
- Multi-level tasks (easy → medium → hard)
- Deterministic graders (0.0–1.0 scoring)
- Memory-based agent reasoning
- Logging + leaderboard system
- Dockerized deployment

---

## 🧠 Environment Design

### Observation
- ticket_id
- message
- customer_tier
- timestamp

### Action
- category
- priority
- assigned_team
- response

---

## 🧪 Tasks

| Task | Description |
|------|------------|
| Easy | Predict category |
| Medium | Category + priority |
| Hard | Full triage |

---

## 📊 Reward System

- Partial scoring
- Penalizes incorrect classification
- Rewards meaningful responses

---

## 🤖 Agent

- Rule-based + memory-enhanced agent
- Supports LLM integration (optional)
- Safe fallback logic

---

## ▶️ Run Locally

```bash
pip install -r requirements.txt
uvicorn app:app --reload