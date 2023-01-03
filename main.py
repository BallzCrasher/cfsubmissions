import urllib.request
import json
import argparse
BASE_URL = 'https://codeforces.com'

# pargin argments
parser = argparse.ArgumentParser()
parser.add_argument("handle", type=str, help="handle of the user")
parser.add_argument('--min', type=int, help='min value of problem rating')
parser.add_argument('--max', type=int, help='max value of problem rating')
config = parser.parse_args().__dict__

#sending API request
response = urllib.request.urlopen(f"{BASE_URL}/api/user.status?handle={config['handle']}")
print("Finished requesting")
response = json.loads(response.read().decode('utf-8'))
if response['status'] != 'OK':
    print("API request faild. Aborting...")
    exit(1)

#parsing response
for submission in response['result']:
    if 'rating' not in submission['problem']:
        continue
    if config['--min'] and submission['problem']['rating'] < config['--min']:
        continue
    if config['--max'] and submission['problem']['rating'] > config['--max']:
        continue
    contest = submission['problem']['contestId']
    sub_id = submission['id']
    print((submission['id'], submission['verdict'], submission['problem'],
        f"{BASE_URL}/contest/{contest}/submission/{sub_id}"))
    
