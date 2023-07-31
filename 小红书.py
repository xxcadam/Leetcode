import requests
from bs4 import BeautifulSoup

proxy = {
    'http': 'http://127.0.0.1:7890',
    'https': 'http://127.0.0.1:7890'
}

url = 'https://www.xiaohongshu.com/users'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'
}

response = requests.get(url, headers=headers, proxies=proxy)
soup = BeautifulSoup(response.text, 'lxml')

bloggers = soup.find_all('div', class_='user-item')

top_bloggers = []
for blogger in bloggers:
    id = blogger['data-userid']
    nickname = blogger.find('p', class_='name').text
    fans_count = int(blogger.find('p', class_='fans-num').text)

    top_bloggers.append({
        'id': id,
        'nickname': nickname,
        'fans_count': fans_count
    })

top_bloggers = sorted(top_bloggers, key=lambda x: x['fans_count'], reverse=True)[:10]

for blogger in top_bloggers:
    print(f'ID: {blogger["id"]}')
    print(f'Nickname: {blogger["nickname"]}')
    print(f'Fans: {blogger["fans_count"]}')
    print('-' * 30)