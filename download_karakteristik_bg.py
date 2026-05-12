import http.cookiejar
import re
import urllib.request

cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
opener.addheaders = [('User-Agent', 'Mozilla/5.0')]

filename = 'karakteristik-bg.jpg'
file_id = '1HHwVS2uVa79ULSN8MUfiwoml-XULh2WM'
url = f'https://drive.google.com/uc?export=download&id={file_id}'
print('Downloading', filename, 'from', url)

response = opener.open(url)
data = response.read()
confirm_match = re.search(rb'name="confirm" value="(.+?)"', data)
if confirm_match:
    confirm = confirm_match.group(1).decode('utf-8')
    url = f'https://drive.google.com/uc?export=download&confirm={confirm}&id={file_id}'
    print('Confirming with', confirm)
    response = opener.open(url)
    data = response.read()

with open(filename, 'wb') as out:
    out.write(data)

print('Saved', filename, len(data), 'bytes')
