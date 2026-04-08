
def easy_grade(action, gt):
    score = 0.0

    if action.get("category") == gt.get("category"):
        score = 1.0

    return score


def medium_grade(action, gt):
    score = 0.0

    if action.get("category") == gt.get("category"):
        score += 0.6

    if action.get("priority") == gt.get("priority"):
        score += 0.4

    return score


def hard_grade(action, gt):
    score = 0.0

    if action.get("category") == gt.get("category"):
        score += 0.3

    if action.get("priority") == gt.get("priority"):
        score += 0.3

    if action.get("assigned_team") == gt.get("assigned_team"):
        score += 0.2

    # safe response check
    response = action.get("response", "")

    if isinstance(response, str) and len(response) > 20:
        score += 0.2

    return min(score, 1.0)