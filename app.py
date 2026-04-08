import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))



from fastapi import FastAPI
from pydantic import BaseModel
from env.environment import SupportEnv

app = FastAPI()

# Initialize environment
env = SupportEnv()


# -----------------------------
# Root API
# -----------------------------
@app.get("/")
def root():
    return {"message": "OpenEnv Support Triage API"}


# -----------------------------
# Request model
# -----------------------------
class ActionRequest(BaseModel):
    action: str


# -----------------------------
# RESET (MANDATORY - POST)
# -----------------------------
@app.post("/reset")
def reset():
    obs = env.reset()

    return {
        "observation": obs.__dict__,
        "reward": 0.0,
        "done": False,
        "info": {}
    }


# -----------------------------
# STEP (MANDATORY - POST)
# -----------------------------
@app.post("/step")
def step(request: ActionRequest):
    action = request.action

    obs, reward, done, info = env.step(action)

    return {
        "observation": obs.__dict__ if obs else None,
        "reward": float(reward),
        "done": bool(done),
        "info": info if info else {}
    }


# -----------------------------
# HEALTH CHECK (optional but good)
# -----------------------------
@app.get("/health")
def health():
    return {"status": "ok"}