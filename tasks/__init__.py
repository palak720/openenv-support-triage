from tasks.easy_task import TASK as EASY_TASK
from tasks.medium_task import TASK as MEDIUM_TASK
from tasks.hard_task import TASK as HARD_TASK

# Used by platform (IMPORTANT)
TASKS = [
    {
        "id": "support_triage_easy",
        "task_id": "easy",
        "name": "easy",
        "difficulty": "easy",
        "description": "Classify the support ticket category correctly.",
        "grader": "graders.easy_grader:grade",
        "graders": ["graders.easy_grader:grade"],
        "reward_range": [0.0, 1.0],
    },
    {
        "id": "support_triage_medium",
        "task_id": "medium",
        "name": "medium",
        "difficulty": "medium",
        "description": "Classify the support ticket category and priority.",
        "grader": "graders.medium_grader:grade",
        "graders": ["graders.medium_grader:grade"],
        "reward_range": [0.0, 1.0],
    },
    {
        "id": "support_triage_hard",
        "task_id": "hard",
        "name": "hard",
        "difficulty": "hard",
        "description": "Predict category, priority, assigned team, and response quality.",
        "grader": "graders.hard_grader:grade",
        "graders": ["graders.hard_grader:grade"],
        "reward_range": [0.0, 1.0],
    },
]

# Optional (local use)
PYTHON_TASKS = [
    {
        "id": "support_triage_easy",
        "grader": EASY_TASK["grader"],
    },
    {
        "id": "support_triage_medium",
        "grader": MEDIUM_TASK["grader"],
    },
    {
        "id": "support_triage_hard",
        "grader": HARD_TASK["grader"],
    },
]