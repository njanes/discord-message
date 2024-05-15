import requests

# URL of Discord channel to send message
url = "https://discord.com/api/v9/channels/123456789/messages"

# Message content
payload = {"content": "Hello world"}

# User token (DO NOT SHARE YOUR TOKEN)
headers = {
    "Authorization": "RbU5MGQgeHJRYzOfWzNzc5MzM4.G50WUq.yU_r5dEWL45H-FJeWCLzZRNGM1nDFM7YlPTodfu"
}

# Post request
res = requests.post(url, payload, headers=headers)
