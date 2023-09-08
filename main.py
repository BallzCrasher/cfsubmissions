import urllib.request
import json
import argparse

# pargin argments
parser = argparse.ArgumentParser()
parser.add_argument("handle", type=str, help='Codeforces user handle.')
parser.add_argument('--min', type=int, help='Min value of problem rating.')
parser.add_argument('--max', type=int, help='Max value of problem rating.')
parser.add_argument('--from', type=int, help='1-based index of the first submission to return.')
parser.add_argument('--count', type=int, help='Number of returned submissions.')
parser.add_argument('--show-unrated', type=bool, help='Show problems that does not have a rating tag.')
config = parser.parse_args().__dict__
config['BASE_URL'] = 'https://codeforces.com'

if __name__ == '__main__':
    # configuring API request
    url = f"{config['BASE_URL']}/api/user.status?handle={config['handle']}"
    if config['from']: 
        url += f"&from={config['from']}"
    if config['count']: 
        url += f"&count={config['count']}"
    header = { 
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    }
    request = urllib.request.Request(
        url,
        data = None,
        headers = header
    )

    # sending API request
    response = urllib.request.urlopen(request)
    print("Finished requesting")
    response = json.loads(response.read().decode('utf-8'))
    print("Finished reading request")
    if response['status'] != 'OK':
        print("API request failed. Aborting...")
        exit(1)

    config['response'] = response['result']
    import parser
    parser.run(config)
