
def grade(action, ground_truth):
    score = 0.0

    if action.category == ground_truth["category"]:
        score += 0.3

    if action.priority == ground_truth["priority"]:
        score += 0.2

    if action.assigned_team == ground_truth["assigned_team"]:
        score += 0.2

    # response quality check
    if action.response and len(action.response.strip()) > 30:
        score += 0.3

    return score