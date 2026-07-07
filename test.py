from tools.knowledge_search import search_knowledge_base


ticket = """
Our production job started failing after a configuration change.
The service is returning 401 unauthorized errors.
We think it may be an authentication issue.
"""


results = search_knowledge_base(ticket)


for result in results:
    print("=" * 50)
    print("Category:", result["category"])
    print("Score:", result["score"])
    print("Matched:", result["matched_keywords"])
    print("Fix:", result["standard_fix"])