import json
import os
from agent.models.knowledge import KnowledgeMatch

KB_PATH = "data/kb.json"


def load_knowledge_base():
    """
    Load knowledge base from JSON file.
    """
    with open(KB_PATH, "r") as file:
        data = json.load(file)
    return data["entries"]



def search_knowledge_base(ticket_text, top_k=2):
    """
    Search KB entries based on keyword matches.

    Args:
        ticket_text: Customer support ticket
        top_k: Number of results to return

    Returns:
        Ranked KB matches
    """

    entries = load_knowledge_base()
    ticket_text = ticket_text.lower()

    results = []


    for entry in entries:
        score = 0
        matched_keywords = []


        for keyword in entry["keywords"]:
            if keyword.lower() in ticket_text:
                score += 1
                matched_keywords.append(keyword)


        if score > 0:
            # results.append(
            #     {
            #         "id": entry["id"],
            #         "category": entry["category"],
            #         "score": score,
            #         "matched_keywords": matched_keywords,
            #         "likely_causes": entry["likely_causes"],
            #         "standard_fix": entry["standard_fix"],
            #         "severity_hint": entry["severity_hint"],
            #         "base_confidence": entry["base_confidence"]
            #     }
            # )
            results.append(
    KnowledgeMatch(
        id=entry["id"],
        category=entry["category"],
        score=score,
        matched_keywords=matched_keywords,
        likely_causes=entry["likely_causes"],
        standard_fix=entry["standard_fix"],
        severity_hint=entry["severity_hint"],
        base_confidence=entry["base_confidence"]
    )
)


    # highest matching entries first
    results.sort(
        key=lambda x: x.score,
        reverse=True
    )
    return results[:top_k]