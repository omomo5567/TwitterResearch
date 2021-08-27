import urllib.request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

#なぜか開けないサイトあり。（error403）
url = input('>> ')
headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0"
        }

response = urllib.request.urlopen(url)
print('url:', response.geturl())
