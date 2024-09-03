import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://gremio.net')
except urllib.error.URLError:
    print('\033[31mERRO: site indisponivel\033[m')
else:
    print('Consegui acessar o site!')
