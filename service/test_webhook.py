import requests

url = "https://milonthis.app.n8n.cloud/webhook-test/ai-email-writer"

payload = {
    "recipient": "housemilon23@gmail.com",
    "subject": "Project Meeting",
    "prompt": "Write a professional email requesting a meeting next week."
}

response = requests.post(url, json=payload)

print("Status:", response.status_code)
print("Response:", response.text)