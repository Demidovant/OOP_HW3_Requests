import requests

URL = 'https://akabab.github.io/superhero-api/api/all.json'

response = requests.get(URL)
data = response.json()

names = ['Hulk', 'Captain America', 'Thanos']
print(max([(item['powerstats']['intelligence'], item['name']) for item in data if item['name'] in names])[1])



# max_ = data[-1]['powerstats']['intelligence']
# for item in data:
#     if item['name'] in names:
#         if item['powerstats']['intelligence'] > max_:
#             max_ = item['powerstats']['intelligence']
#             result = item['name']
# print(result)
