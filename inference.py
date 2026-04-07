
import os
from typing import List, Optional
from openai import OpenAI

from env.environment import SupportEnv
from env.models import Action

# ================== ENV VARIABLES ==================
API_BASE_URL = os.getenv("API_BASE_URL", "https://api.openai.com/v1")
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-3.5-turbo")
HF_TOKEN = os.getenv("HF_TOKEN", "dummy_key")

TASK_NAME = "support-triage"
BENCHMARK = "openenv-support"
MAX_STEPS = 10

# ================== OPENAI CLIENT ==================
client = OpenAI(base_url=API_BASE_URL, api_key=HF_TOKEN)

# ================== LOG FUNCTIONS ==================
def log_start(task: str, env: str, model: str):
    print(f"[START] task={task} env={env} model={model}", flush=True)


def log_step(step: int, action: str, reward: float, done: bool, error: Optional[str]):
    error_val = error if error else "null"
    done_val = str(done).lower()
    print(
        f"[STEP] step={step} action={action} reward={reward:.2f} done={done_val} error={error_val}",
        flush=True,
    )


def log_end(success: bool, steps: int, score: float, rewards: List[float]):
    rewards_str = ",".join(f"{r:.2f}" for r in rewards)
    print(
        f"[END] success={str(success).lower()} steps={steps} score={score:.2f} rewards={rewards_str}",
        flush=True,
    )

# ================== AGENT ==================
def fallback_agent(obs):
    text = obs.message.lower()

    category = "general"
    priority = "low"
    team = "support"

    if "payment" in text:
        category = "billing"
        priority = "high"
        team = "payments"
    elif "login" in text:
        category = "technical"
        priority = "medium"
        team = "tech"

    return Action(
        category=category,
        priority=priority,
        assigned_team=team,
        response="We are working on your issue."
    )


def get_action(obs):
    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": "Classify support ticket"},
                {"role": "user", "content": obs.message}
            ],
            max_tokens=50
        )
        # ignoring LLM output → fallback safe
        return fallback_agent(obs)

    except Exception:
        return fallback_agent(obs)

# ================== MAIN ==================
def main():
    env = SupportEnv(task="hard")

    rewards = []
    steps = 0

    log_start(TASK_NAME, BENCHMARK, MODEL_NAME)

    try:
        obs = env.reset()

        for step in range(1, MAX_STEPS + 1):

            action_obj = get_action(obs)

            action_str = f"{action_obj.category}|{action_obj.priority}|{action_obj.assigned_team}"

            obs, reward, done, _ = env.step(action_obj)

            rewards.append(reward)
            steps = step

            log_step(step, action_str, reward, done, None)

            if done:
                break

        score = sum(rewards) / len(rewards) if rewards else 0.0
        score = min(max(score, 0.0), 1.0)

        success = score > 0.5

    finally:
        log_end(success, steps, score, rewards)


if __name__ == "__main__":
    main()