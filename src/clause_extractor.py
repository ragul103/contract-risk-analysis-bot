import re

def extract_clauses(text):
    clauses = []
    pattern = re.split(r'\n(?=\d+\.|\bClause\b|\bSection\b)', text)

    for idx, block in enumerate(pattern):
        clauses.append({
            "clause_id": f"C{idx+1}",
            "text": block.strip()
        })

    return clauses
