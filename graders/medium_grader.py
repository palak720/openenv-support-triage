
def grade(output, expected):
    """
    Check category + priority
    """
    try:
        score = 0.0

        if output.get("category") == expected.get("category"):
            score += 0.5

        if output.get("priority") == expected.get("priority"):
            score += 0.5

        return score
    except:
        return 0.0