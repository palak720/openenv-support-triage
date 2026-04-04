
import os
import json
from datetime import datetime

from env.environment import SupportEnv
from env.models import Action

# 🧠 Memory
memory = []

# 📊 Logs
log_data = []


# 🤖 Smart Rule-Based Agent (Advanced)
def smart_agent(observation):
    msg = observation.message.lower()
    tier = observation.customer_tier.lower()

    category = "general"
    priority = "low"
    assigned_team = "support"
    response = "We are looking into your issue."

    # 🔍 Category detection
    if any(word in msg for word in ["payment", "refund", "charged", "billing"]):
        category = "billing"
        assigned_team = "payments"

    elif any(word in msg for word in ["crash", "error", "bug", "not working"]):
        category = "technical"
        assigned_team = "engineering"

    elif "password" in msg:
        category = "general"
        assigned_team = "support"

    # ⚡ Priority logic
    if tier == "premium":
        priority = "high"

    if "urgent" in msg or "immediately" in msg:
        priority = "high"

    # 🧠 Memory-based improvement
    if memory:
        last = memory[-1]
        if last["action"]["category"] == category:
            response = "Following up on a similar issue. We are prioritizing your case."

    # 💬 Response enhancement
    if category == "billing":
        response = "We apologize for the inconvenience. Our payments team is reviewing your issue and will resolve it जल्द."

    elif category == "technical":
        response = "Our engineering team is actively investigating the issue and will fix it as soon as possible."

    elif category == "general":
        response = "You can resolve this using our help section. Let us know if you need further assistance."

    return Action(
        category=category,
        priority=priority,
        assigned_team=assigned_team,
        response=response
    )


# ▶️ Run agent
def run(task="hard"):
    env = SupportEnv(task=task)

    obs = env.reset()
    total_reward = 0
    step_count = 0

    while True:
        print(f"\n🧾 Ticket: {obs.message}")

        action = smart_agent(obs)

        print("🤖 Action:", action)

        obs, reward, done, _ = env.step(action)

        print("⭐ Reward:", reward)

        # 🧠 Memory update
        memory.append({
            "ticket": obs.message if obs else "END",
            "action": action.dict()
        })

        # 📊 Logging
        log_data.append({
            "ticket": obs.message if obs else "END",
            "action": action.dict(),
            "reward": reward,
            "timestamp": str(datetime.now())
        })

        total_reward += reward
        step_count += 1

        if done:
            break

    # 📁 Save logs
    os.makedirs("logs", exist_ok=True)
    with open("logs/run_logs.json", "w") as f:
        json.dump(log_data, f, indent=2)

    # 🏆 Leaderboard
    leaderboard_file = "leaderboard.json"

    if os.path.exists(leaderboard_file):
        with open(leaderboard_file, "r") as f:
            leaderboard = json.load(f)
    else:
        leaderboard = []

    leaderboard.append({
        "task": task,
        "score": total_reward,
        "steps": step_count,
        "time": str(datetime.now())
    })

    with open(leaderboard_file, "w") as f:
        json.dump(leaderboard, f, indent=2)

    # 📈 Summary
    avg_score = total_reward / step_count

    print("\n======================")
    print(f"Task: {task}")
    print(f"Steps: {step_count}")
    print(f"Total Score: {total_reward}")
    print(f"Average Score: {avg_score}")
    print("======================\n")


if __name__ == "__main__":
    run(task="hard")