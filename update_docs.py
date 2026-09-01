import os
import requests

api_key = os.environ["API_KEY"]

with open("test_query.sql", "r") as f:
    sql_code = f.read()

prompt = f"Write clear documentation in markdown explaining what this SQL query does. Only return the markdown, nothing else.\n\nSQL:\n{sql_code}"

response = requests.post(
    "https://openrouter.ai/api/v1/chat/completions",
    headers={
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    },
    json={
        "model": "openai/gpt-3.5-turbo",
        "messages": [{"role": "user", "content": prompt}]
    }
)

doc_text = response.json()["choices"][0]["message"]["content"]

with open("test_query.md", "w") as f:
    f.write(doc_text)

print("Done! test_query.md has been updated.")
