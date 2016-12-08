import requests
with open('dataset_3378_3.txt', 'r') as i_url:
	url = i_url.readline().strip()


while True:
	r = requests.get(url)
	url = "https://stepic.org/media/attachments/course67/3.6.3/" + r.text
	if "We" in url:
		data = r.text
		break

print(data)