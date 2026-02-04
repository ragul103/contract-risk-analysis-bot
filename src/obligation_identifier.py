def identify_obligations(text):
    obligations = []
    rights = []
    prohibitions = []

    sentences = text.split(".")

    for s in sentences:
        s_lower = s.lower()

        if "shall not" in s_lower or "must not" in s_lower:
            prohibitions.append(s.strip())

        elif "shall" in s_lower or "must" in s_lower:
            obligations.append(s.strip())

        elif "may" in s_lower:
            rights.append(s.strip())

    return {
        "obligations": obligations,
        "rights": rights,
        "prohibitions": prohibitions
    }
