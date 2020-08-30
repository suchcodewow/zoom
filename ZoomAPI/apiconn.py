# print("HERRO")
import jwt
import http.client
import datetime
import json

api_key = 'vnUG13jKSleL8v0DeyNK8Q'
api_sec = 'ji4UmJQv603iQHn8hedwqpHjPjuCIH8MJy2V'

payload = {
    'iss': api_key,
    'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=2)
}

jwt_encoded = str(jwt.encode(payload, api_sec), 'utf-8')
# print(jwt_encoded)
conn = http.client.HTTPSConnection("api.zoom.us")
headers = {
    'authorization': "Bearer %s" % jwt_encoded,
    'content-type': "application/json"
}

conn.request("GET", "/v2/users?status=active", headers=headers)
res = conn.getresponse()

response_string = res.read().decode('utf-8')
response_obj = json.loads(response_string)
ZoomUserID = response_obj['users'][0]['id']
conn.request("GET", "/v2/users/%s/meetings" % ZoomUserID, headers=headers)
res = conn.getresponse()
response_string = res.read().decode('utf-8')
response_obj = json.loads(response_string)
print(response_obj)
