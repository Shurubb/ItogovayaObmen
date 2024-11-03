import requests
import json
import pprint

obmen = requests.get('https://open.er-api.com/v6/latest/USD')
result = json.loads(obmen.text)
ob = pprint.PrettyPrinter(indent=4)
ob.pprint(result)
