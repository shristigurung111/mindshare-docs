import os
import requests

api_key = os.environ["ANTHROPIC_API_KEY"]

with open("test_query.sql", "r") as f:
    sql_code = f.read()

prompt = "Write clear documentation in markdown explaining what this SQL query does. Only return the markdown, nothing else.\n\nSQL:\n" + sql_code

response = requests.post(
    "https://api.anthropic.com/v1/messages",
    headers={
        "x-api-key": api_key,
        "anthropic-version": "2023-06-01",
        "content-type": "application/json"
    },
    json={
        "model": "claude-sonnet-4-5",
        "max_tokens": 1000,
        "messages": [{"role": "user", "content": prompt}]
    }
)

data = response.json()
doc_text = data["content"][0]["text"]

with open("test_query.md", "w") as f:
    f.write(doc_text)

print("Done! test_query.md has been updated.")