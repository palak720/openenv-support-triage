from graders.easy_grader import grade as easy_grader
from graders.medium_grader import grade as medium_grader
from graders.hard_grader import grade as hard_grader

grade_easy = easy_grader
grade_medium = medium_grader
grade_hard = hard_grader

GRADERS = {
    "easy": easy_grader,
    "support_triage_easy": easy_grader,
    "medium": medium_grader,
    "support_triage_medium": medium_grader,
    "hard": hard_grader,
    "support_triage_hard": hard_grader,
}

TASK_GRADER_PAIRS = [
    ("support_triage_easy", easy_grader),
    ("support_triage_medium", medium_grader),
    ("support_triage_hard", hard_grader),
]

__all__ = [
    "easy_grader",
    "medium_grader",
    "hard_grader",
    "grade_easy",
    "grade_medium",
    "grade_hard",
    "GRADERS",
    "TASK_GRADER_PAIRS",
]
