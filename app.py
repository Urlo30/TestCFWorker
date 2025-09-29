import requests
headers = {
  "Accept" : "*/*",
  "Alt-Used" : "vixsrc.to",
  "Connection" : "keep-alive",
  "Host": "vixsrc.to",
  "Referer" : "https://vixsrc.to/",
  "Sec-Fetch-Dest" : "iframe",
  "Sec-Fetch-Mode" : "navigate",
  "Sec-Fetch-Site" : "cross-site",
  "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/133.0",
}
response = requests.get('https://vixsrc.to/movie/786892', headers = headers)
print(response.text)
print(response)
