import urllib.request
import json
from sys import argv

OPTIONS = ['--min', '--max']
BASE_URL = 'https://codeforces.com'

def parse_arguments():
    def phelp():
        print(f'{argv[0]} <HANDLE> [--min value] [--max value]')
        exit(1)

    if len(argv) < 2: phelp()
    arguments = dict()
    arguments['handle'] = argv[1]
    for i in range(2, len(argv) - 1, 2):
        if argv[i] not in OPTIONS: phelp()
        arguments[argv[i]] = int(argv[i + 1])
    return arguments

config = parse_arguments()
response = urllib.request.urlopen(f"{BASE_URL}/api/user.status?handle={config['handle']}")
print("Finished requesting")
response = json.loads(response.read().decode('utf-8'))
if response['status'] != 'OK':
    print("API request faild. Aborting...")
    exit(1)

for submission in response['result']:
    if 'rating' not in submission['problem']:
        continue
    if '--min' in config and submission['problem']['rating'] < config['--min']:
        continue
    if '--max' in config and submission['problem']['rating'] > config['--max']:
        continue
    contest = submission['problem']['contestId']
    sub_id = submission['id']
    print((submission['id'], submission['verdict'], submission['problem'],
        f"{BASE_URL}/contest/{contest}/{sub_id}"))
    
