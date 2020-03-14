import requests

# falls website benötigt wird hier ein Teil des Headers mitgesendet
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
}

with requests.Session() as s:
    url = "https://www.enigmagroup.org/login"
    r = s.get(url, headers=headers)
    # print(r.content)

# Datei nach Benutzung wieder verschlüsselt! -> ###
url2 = ('http://challenges.enigmagroup.org/programming/1/')
data = {'username': '#####', 'ip': '###.###.###.###'}
cookies = {'PHPSESSID': '###', 'mission': 'yes'}


r = requests.post(url2, cookies=cookies, headers=headers, data=data)
print(r.text)