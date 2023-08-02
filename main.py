import requests
from bs4 import BeautifulSoup

SEARCH_TERM = 'water bottle'
url = f"https://www.google.com/search?q={SEARCH_TERM}" #&oq=data&aqs=chrome..69i57j69i59j69i61l2j69i60j69i65l3.1002j0j7&sourceid=chrome&ie=UTF-8"

payload = {}
headers = {
#  'Cookie': '1P_JAR=2023-08-02-02; AEC=Ad49MVGDfA6GmEF6RmLQeey-Iafz74BOiSGVxUInEz1xhKkVkOfquusIrA; NID=511=fLgu1tp8L2NIPrA5C4V1XOhtMfSXgt8gvilioHr_7Ae_9K7Rmde6KcVUzEj_pUkN_qBszAsxzHxnKRnSfOhUloRwvJaoQboHfHxMAhXNVPw2tt9uO7TQrwK6I1mOdcoWki-GF_ltQnhbBro68daY0HTEgY1f14NFE_sYsu7OpGU'
}

response = requests.request("GET", url, headers=headers, data=payload)

soup = BeautifulSoup(response.text,'lxml')

results = soup.find_all('div',class_='Gx5Zad fP1Qef xpd EtOod pkphOe')
print(len(results))

for result in results:
    link = result.find('a').get('href')
    print(link)
    description = result.find('div',class_='BNeawe s3v9rd AP7Wnd').get_text().strip()
    print(description)


