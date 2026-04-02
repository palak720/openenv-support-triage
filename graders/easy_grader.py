
def grade(action, ground_truth):
    if action.category == ground_truth["category"]:
        return 1.0
    return 0.0