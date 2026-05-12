import http.cookiejar
import re
import urllib.request

images = {
    'sma-labum.jpg': '164kO1YmE230y1tG40-fMW009L09OCyEm',
    'ibu-kampus.jpg': '1RIsw3VLPOvjDMhB1iAGl0tmXC94Fo1Av',
    'instrumen-bg.jpg': '1hOoFEulEiHcxVE_jz2WXqjY_rSefidTh',
}

cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
opener.addheaders = [('User-Agent', 'Mozilla/5.0')]

for filename, file_id in images.items():
    url = f'https://drive.google.com/uc?export=download&id={file_id}'
    print('Downloading', filename, 'from', url)
    try:
        response = opener.open(url)
        data = response.read()
        confirm_match = re.search(rb'name="confirm" value="(.+?)"', data)
        if confirm_match:
            confirm = confirm_match.group(1).decode('utf-8')
            url = f'https://drive.google.com/uc?export=download&confirm={confirm}&id={file_id}'
            response = opener.open(url)
            data = response.read()
        with open(filename, 'wb') as out:
            out.write(data)
        print('Saved', filename, len(data), 'bytes')
    except Exception as e:
        print('Failed', filename, e)
