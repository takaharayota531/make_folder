import requests

data = [
  ('grant_type', 'refresh_token'),
  ('client_id', '465307590611-mum36vmrae32krvgkku24tttcthsj5vd.apps.googleusercontent.com'),
  ('client_secret', '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'),
  ('refresh_token', '1//0ePYZkBaR0y9CCgYIARAAGA4SNwF-L9IrLpzhdAC339hiNX16ojlMmhP3jTFcbSnx8n7RXuYT9e8v4ZSHo2eCnm8az5YJPDlkL2w'),
]

response = requests.post('https://accounts.google.com/o/oauth2/token', data=data)

json = response.json()
access_token = json['access_token']


headers = {
    'Authorization': 'Bearer ' + access_token,
}

response = requests.get('https://mybusiness.googleapis.com/v4/accounts', headers=headers)
json = response.json()

account_id = json['accounts'][0]['name'].replace('accounts/','')
