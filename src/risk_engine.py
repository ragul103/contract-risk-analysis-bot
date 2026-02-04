def detect_risks(text):
    risks = []

    t = text.lower()

    if "terminate at any time" in t:
        risks.append("Unilateral Termination")

    if "indemnify" in t and "limit" not in t:
        risks.append("Unlimited Indemnity")

    if "non-compete" in t:
        risks.append("Non-Compete Clause")

    if "auto-renew" in t:
        risks.append("Auto Renewal")

    return risks
