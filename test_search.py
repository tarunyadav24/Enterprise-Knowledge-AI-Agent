from mcp_server.search import search_enterprise_documents

results = search_enterprise_documents("leave policy")

print("\n===== SEARCH RESULTS =====\n")

for i, doc in enumerate(results, start=1):
    print(f"Document {i}")
    print(doc)
    print("-" * 50)