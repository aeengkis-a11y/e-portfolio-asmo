import urllib.request

urls = [
    'https://drive.google.com/uc?id=1RLLPJ0cdY_p94a54kbtLKJgw0Ff_qQI1',
    'https://drive.google.com/uc?id=1ej9ct-DJiihUhCkkeWzGoPkMMebbCa21',
    'https://drive.google.com/uc?id=1wIcDJf4wzc4KCL5Ps-UeoWYGQj7nU_np',
    'https://drive.google.com/uc?id=1L4uNLOgHMcACE0Oe1XtQHw6g5uWxGuEt'
]

for u in urls:
    print('URL:', u)
    req = urllib.request.Request(u, method='HEAD', headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            print('Status:', r.status)
            print('Content-Type:', r.getheader('Content-Type'))
            print('Location:', r.getheader('Location'))
    except Exception as e:
        print('ERROR:', e)
    print('---')
