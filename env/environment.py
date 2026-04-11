
try:
    from env.graders import grade_easy, grade_medium, grade_hard
except ImportError:
    from graders.easy_grader import grade as grade_easy
    from graders.medium_grader import grade as grade_medium
    from graders.hard_grader import grade as grade_hard

from env.data import TICKETS, GROUND_TRUTH


class SupportEnv:
    def __init__(self, task="easy"):
        self.task = task
        self.tickets = TICKETS
        self.ground_truth = GROUND_TRUTH
        self.index = 0
        self.done = False

    def reset(self):
        self.index = 0
        self.done = False

        ticket = self.tickets[0]

        return {
            "ticket_id": ticket.get("ticket_id", ""),
            "message": ticket.get("message", ""),
            "customer_tier": ticket.get("customer_tier", "")
        }

    def step(self, action):
        if self.done:
            return {}, 0.0, True, {}

        gt = self.ground_truth[self.index]

        if self.task == "easy":
            reward = grade_easy(action, gt)
        elif self.task == "medium":
            reward = grade_medium(action, gt)
        else:
            reward = grade_hard(action, gt)

        self.index += 1

        if self.index >= len(self.tickets):
            self.done = True
            return {}, float(reward), True, {}

        ticket = self.tickets[self.index]

        return (
            {
                "ticket_id": ticket.get("ticket_id", ""),
                "message": ticket.get("message", ""),
                "customer_tier": ticket.get("customer_tier", "")
            },
            float(reward),
            False,
            {}
        )