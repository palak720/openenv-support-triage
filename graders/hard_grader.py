
def grade(output, expected):
    """
    Check category, priority, team, response
    """
    try:
        score = 0.0

        if output.get("category") == expected.get("category"):
            score += 0.25

        if output.get("priority") == expected.get("priority"):
            score += 0.25

        if output.get("team") == expected.get("team"):
            score += 0.25

        if output.get("response") == expected.get("response"):
            score += 0.25

        return score
    except:
        return 0.0