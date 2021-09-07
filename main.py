# http://localhost:9515/session

import requests
import json
# POST先URL
url = "http://localhost:9515/session"
head = {'Content-Type': 'application/json; charset=utf-8'}
payload = {'capabilities': {}}
r = requests.post(url, headers=head, data=json.dumps(payload))

print(r.text)
