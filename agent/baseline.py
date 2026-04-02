
import os
from openai import OpenAI
from env.environment import SupportEnv
from env.models import Action

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def run():
    env = SupportEnv()
    obs = env.reset()

    total_reward = 0

    while True:
        prompt = f"""
        Ticket: {obs.message}
        Decide category, priority, team, response.
        """

        res = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )

        # naive parsing (baseline)
        action = Action(
            category="billing",
            priority="high",
            assigned_team="payments",
            response="We are looking into your issue."
        )

        obs, reward, done, _ = env.step(action)
        total_reward += reward

        if done:
            break

    print("Baseline Score:", total_reward)


if __name__ == "__main__":
    run()