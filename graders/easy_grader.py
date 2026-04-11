
def grade(output, expected):
    """
    Check if predicted category matches expected category
    """
    try:
        return 1.0 if output.get("category") == expected.get("category") else 0.0
    except:
        return 0.0