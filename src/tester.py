import requests
import json


def main():
    response = requests.post('http://localhost:5000/points/', headers={'content-type': 'application/json'}, data=json.dumps({'a': 'b'}))
    if response.status_code != 200:
        print response.content

if __name__ == '__main__':
    main()