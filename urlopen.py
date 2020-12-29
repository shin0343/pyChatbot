import urllib.request

url = "https://www.example.com"

res = urllib.request.urlopen(url) # url open!

data = res.read()

#바이너리를 문자열로 변환
text = data.decode("utf-8")
print(text)
