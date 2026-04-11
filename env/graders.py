
def _field(action, name, default=None):
    if isinstance(action, dict):
        return action.get(name, default)
    return getattr(action, name, default)


def easy_grade(action, gt):
    if _field(action, "category") == gt.get("category"):
        return 0.9
    return 0.1


def medium_grade(action, gt):
    score = 0.2

    if _field(action, "category") == gt.get("category"):
        score += 0.35

    if _field(action, "priority") == gt.get("priority"):
        score += 0.35

    return score


def hard_grade(action, gt):
    score = 0.1

    if _field(action, "category") == gt.get("category"):
        score += 0.25

    if _field(action, "priority") == gt.get("priority"):
        score += 0.2

    if _field(action, "assigned_team") == gt.get("assigned_team"):
        score += 0.2

    response = _field(action, "response", "")
    if isinstance(response, str) and len(response.strip()) > 20:
        score += 0.15

    return min(score, 0.9)
