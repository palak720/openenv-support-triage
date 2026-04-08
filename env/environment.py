
from env.models import Observation
from env.graders import easy_grade, medium_grade, hard_grade
from env.data import TICKETS, GROUND_TRUTH


class SupportEnv:   
    def __init__(self, task="easy"):
        self.index = 0
        self.done = False
        self.task = task

        self.tickets = TICKETS
        self.ground_truth = GROUND_TRUTH

    def reset(self):
        self.index = 0
        self.done = False

        # ⚠️ convert to dict (VERY IMPORTANT)
        return Observation(**self.tickets[self.index]).dict()

    def state(self):
        return {
            "index": self.index,
            "done": self.done,
            "task": self.task
        }

    def step(self, action):
        gt = self.ground_truth[self.index]

        if self.task == "easy":
            reward = easy_grade(action, gt)
        elif self.task == "medium":
            reward = medium_grade(action, gt)
        else:
            reward = hard_grade(action, gt)

        self.index += 1

        if self.index >= len(self.tickets):
            self.done = True
            return {}, float(reward), True, {}

        return (
            Observation(**self.tickets[self.index]).dict(),
            float(reward),
            False,
            {}
        )