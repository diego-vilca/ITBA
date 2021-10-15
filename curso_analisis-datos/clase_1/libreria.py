import requests

def wget(url):
    '''Esta función nos ayuda a descargar archivos desde la web y no es necesaria para archivos locales
    '''
    r = requests.get(url, allow_redirects=True)
    with open('./Data/' + url[url.rfind('/') + 1::], 'wb') as f:
        f.write(r.content)
