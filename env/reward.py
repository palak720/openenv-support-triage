
def compute_reward(action, ground_truth):
    score = 0.0

    if action.category == ground_truth["category"]:
        score += 0.3
    if action.priority == ground_truth["priority"]:
        score += 0.2
    if action.assigned_team == ground_truth["assigned_team"]:
        score += 0.2
    if len(action.response) > 20:
        score += 0.2

    # penalty
    if action.response == "":
        score -= 0.2

    return min(max(score, 0.0), 1.0)