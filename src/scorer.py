def score_risk(risks):
    if len(risks) == 0:
        return "Low"
    elif len(risks) <= 2:
        return "Medium"
    else:
        return "High"
