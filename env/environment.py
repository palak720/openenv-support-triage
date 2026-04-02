
from env.models import Observation, Action
from env.data import TICKETS

# import graders
from graders.easy_grader import grade as easy_grade
from graders.medium_grader import grade as medium_grade
from graders.hard_grader import grade as hard_grade


class SupportEnv:

    def __init__(self, task="easy"):
        self.index = 0
        self.done = False
        self.task = task

        # ground truth for evaluation
        self.ground_truth = [
            {
                "category": "billing",
                "priority": "high",
                "assigned_team": "payments"
            },
            {
                "category": "general",
                "priority": "low",
                "assigned_team": "support"
            },
            {
                "category": "technical",
                "priority": "high",
                "assigned_team": "engineering"
            }
        ]

    # 🔁 reset environment
    def reset(self):
        self.index = 0
        self.done = False
        return Observation(**TICKETS[self.index])

    # ▶️ step function (MAIN LOGIC)
    def step(self, action: Action):
        gt = self.ground_truth[self.index]

        # choose grader based on task
        if self.task == "easy":
            reward = easy_grade(action, gt)
        elif self.task == "medium":
            reward = medium_grade(action, gt)
        else:
            reward = hard_grade(action, gt)

        # move to next step
        self.index += 1

        # check if done
        if self.index >= len(TICKETS):
            self.done = True
            return None, reward, True, {}

        # next observation
        next_obs = Observation(**TICKETS[self.index])

        return next_obs, reward, False, {}

    # 📊 state tracking
    def state(self):
        return {
            "current_index": self.index,
            "done": self.done,
            "task": self.task
        }