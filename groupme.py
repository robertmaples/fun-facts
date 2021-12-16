import requests
import time
import yaml

with open("config.yaml", 'r') as yamlfile:
    config = yaml.load(yamlfile, Loader=yaml.FullLoader)

    access_token = config['access-token']
    group_id = config['group-id']
    text_file_path = config['text-file-path']
    sleep_time = config['sleep-time']

    split = []
    with open(text_file_path) as f:
        text = f.read()
        split = text.splitlines()

    base_url = "https://api.groupme.com/v3"

    params = {'token': access_token}
    num = 1
    for s in split:
        num += 1
        body = {
            "message": {
                "source_guid": f"{num}",
                "text": s}}
        group = requests.post(
            f"{base_url}/groups/{group_id}/messages", params=params, json=body)
        print(group.json())
        time.sleep(sleep_time)
