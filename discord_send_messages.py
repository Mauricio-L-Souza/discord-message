import requests

header = {
    'authorization': 'Put your token here'}

# url must be like 'https://discord.com/api/v9/channels/123/messages'

url = 'https://discord.com/api/v9/channels/{HERE YOUR CHANNEL ID}/messages'
payload = {'content': 'Here your message'}

requests.post(url, data=payload, headers=header)
