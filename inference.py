
import os
import requests
import json
from env.environment import SupportEnv
from env.models import Action

# Load env variables
API_BASE_URL = os.getenv("API_BASE_URL")
MODEL_NAME = os.getenv("MODEL_NAME")
HF_TOKEN = os.getenv("HF_TOKEN")

# fallback agent (no API dependency)
def fallback_agent(observation):
    text = observation.message.lower()

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
        response="We are looking into your issue."
    )

# Optional API call (safe fallback)
def get_action(observation):
    try:
        headers = {
            "Authorization": f"Bearer {HF_TOKEN}",
            "Content-Type": "application/json"
        }

        payload = {
            "model": MODEL_NAME,
            "messages": [
                {"role": "user", "content": observation.message}
            ]
        }

        response = requests.post(
            f"{API_BASE_URL}/chat/completions",
            headers=headers,
            json=payload,
            timeout=5
        )

        if response.status_code == 200:
            return fallback_agent(observation)
        else:
            return fallback_agent(observation)

    except:
        return fallback_agent(observation)


def run(task="easy"):
    env = SupportEnv(task=task)

    print("[START]")
    total_reward = 0

    obs = env.reset()
    step_num = 0

    while True:
        action = get_action(obs)

        obs, reward, done, _ = env.step(action)

        total_reward += reward

        print(f"[STEP] step={step_num}, category={action.category}, priority={action.priority}, reward={reward}")

        step_num += 1

        if done:
            break

    print(f"[END] total_reward={total_reward}")


if __name__ == "__main__":
    run("easy")