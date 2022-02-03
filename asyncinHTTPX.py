from urllib import response
from wsgiref import headers
from aiohttp import request
import requests
import httpx


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'

}

url = 'Https://httpbin.org/headers'

r = requests.get(url, headers=headers)
print(r.text)


r = httpx.get(url, headers=headers)
print(r.text)
