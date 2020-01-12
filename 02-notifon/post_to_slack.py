# coding: utf-8
import requests
url = '' #replace with slack webhook
data = {"text": "Hello World"}
requests.post(url, json=data)
