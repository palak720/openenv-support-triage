
from env.graders import easy_grade, medium_grade, hard_grade
from env.data import TICKETS, GROUND_TRUTH


class SupportEnv:
    def __init__(self, task="easy"):
        self.task = task
        self.tickets = TICKETS
        self.ground_truth = GROUND_TRUTH
        self.index = 0
        self.done = False

    # 🔁 RESET FUNCTION
    def reset(self):
        self.index = 0
        self.done = False

        ticket = self.tickets[self.index]

        # ✅ ALWAYS return simple dict (NO Pydantic, NO class)
        return {
            "ticket": ticket.get("ticket", "")
        }

    # 📊 STATE (optional but good)
    def state(self):
        return {
            "index": self.index,
            "done": self.done,
            "task": self.task
        }

    # ▶️ STEP FUNCTION
    def step(self, action):
        # Safety check
        if self.done:
            return {}, 0.0, True, {}

        gt = self.ground_truth[self.index]

        # 🔥 grader selection
        if self.task == "easy":
            reward = easy_grade(action, gt)
        elif self.task == "medium":
            reward = medium_grade(action, gt)
        else:
            reward = hard_grade(action, gt)

        # move next
        self.index += 1

        # end condition
        if self.index >= len(self.tickets):
            self.done = True
            return {}, float(reward), True, {}

        ticket = self.tickets[self.index]

        return (
            {
        "ticket_id": ticket.get("ticket_id"),
        "message": ticket.get("message"),
        "customer_tier": ticket.get("customer_tier")
    },
            float(reward),
            False,
            {}
        )