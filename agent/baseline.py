
from env.environment import SupportEnv
from env.models import Action


def dummy_agent(observation):
    msg = observation.message.lower()

    if "payment" in msg:
        return Action(
            category="billing",
            priority="high",
            assigned_team="payments",
            response="We are checking your payment issue."
        )

    elif "password" in msg:
        return Action(
            category="general",
            priority="low",
            assigned_team="support",
            response="You can reset your password using the reset option."
        )

    else:
        return Action(
            category="technical",
            priority="high",
            assigned_team="engineering",
            response="Our engineering team is investigating the issue."
        )


def run(task="easy"):
    env = SupportEnv(task=task)

    obs = env.reset()
    total_reward = 0

    while True:
        print(f"\n🧾 Ticket: {obs.message}")

        action = dummy_agent(obs)

        print("🤖 Action:", action)

        obs, reward, done, _ = env.step(action)

        print("⭐ Reward:", reward)

        total_reward += reward

        if done:
            break

    print("\nFinal Score:", total_reward)


if __name__ == "__main__":
    run(task="easy")