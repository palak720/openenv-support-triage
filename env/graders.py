
def easy_grade(action, gt):
    score = 0.0

    if action.category == gt["category"]:
        score = 1.0

    return score


def medium_grade(action, gt):
    score = 0.0

    if action.category == gt["category"]:
        score += 0.6

    if action.priority == gt["priority"]:
        score += 0.4

    return score


def hard_grade(action, gt):
    score = 0.0

    if action.category == gt["category"]:
        score += 0.3

    if action.priority == gt["priority"]:
        score += 0.3

    if action.assigned_team == gt["assigned_team"]:
        score += 0.2

    # response quality (simple heuristic)
    if len(action.response) > 20:
        score += 0.2

    return min(score, 1.0)