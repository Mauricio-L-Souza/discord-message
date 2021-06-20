import time
import requests

header = {
    'authorization': 'Put your token here'}

# url must be like 'https://discord.com/api/v9/channels/123/messages'

# Work
work_payload = {'content': 'p!work'}
work_url = 'https://discord.com/api/v9/channels/{HERE YOUR CHANNEL ID}/messages'

# Bank payloads
deposit_payload = {'content': 'p!deposit all'}
withdraw_payload = {'content': 'p!withdraw 50'}

# Fishing
fish_payload = {'content': 'p!fish'}
buy_fishing_rod_payload = {'content': 'p!buy fishing rod'}
fishing_url = 'https://discord.com/api/v9/channels/{HERE YOUR CHANNEL ID}/messages'

# Global attributes
global_attr = {'fishing_count': 0}


def work():
    requests.post(work_url,
                  data=work_payload, headers=header)
    print('trabalhando!')
    time.sleep(1)
    requests.post(work_url,
                  data=deposit_payload, headers=header)
    print('depositando!')


def fish():
    time.sleep(2)
    if(global_attr['fishing_count'] > 5):
        requests.post(fishing_url,
                      data=withdraw_payload, headers=header)
        print('Retirado 50tao')
        time.sleep(1.5)
        requests.post(fishing_url,
                      data=buy_fishing_rod_payload, headers=header)
        print('comprando outra vara!')
        global_attr['fishing_count'] = 0
        return

    requests.post(fishing_url,
                  data=fish_payload, headers=header)
    global_attr['fishing_count'] = global_attr['fishing_count'] + 1
    print('pescando pela ' + str(global_attr['fishing_count']) + ' vez!')


while True:
    work()
    fish()
    time.sleep(310)
