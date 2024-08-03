import requests
import json
import sys

# from WebScraping.bs_select_opponent import get_opponents
# from bs_xpath_opponent import get_opponents
from wiki_fighters import get_opponents,get_fighter_info, get_opponents_with_info


if len(sys.argv) == 1:
    raise Exception("missing argument ...")

target = sys.argv[1]
url = sys.argv[2]
output = sys.argv[3]

handler = None
if target == 'ops':
    handler = get_opponents
elif target == 'ops+info':
    handler = get_opponents_with_info
elif target == 'info':
    handler = get_fighter_info

response = requests.get(url)

results = handler(response.text)
results = json.dumps(results)

with open(f'{output}.json', 'w', encoding='utf-8') as f:
    f.write(results)








# opponents = get_opponents(response.text)
# print(opponents) 
# opponents_json = json.dumps(opponents)
# print(opponents_json)
# with open('khabib_opponents.json', 'w', encoding='utf-8') as f:
#     f.write(opponents_json)