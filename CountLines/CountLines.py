import requests
with open('dataset_3378_2.txt', 'r') as i_url:
	url = i_url.readline().strip()

r = requests.get(url)
lines = r.text.splitlines()
print(len(lines))