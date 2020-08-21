import requests


apiKey = ''
apiBase = 'https://financialmodelingprep.com/api/v3'

params = {'apikey': apiKey}

url = apiBase + '/profile/TD'

r = requests.get(
    url=url,
    params=params
)

data = r.json()

print(data)
