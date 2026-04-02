
def grade(action, ground_truth):
    score = 0.0

    if action.category == ground_truth["category"]:
        score += 0.5

    if action.priority == ground_truth["priority"]:
        score += 0.5

    return score