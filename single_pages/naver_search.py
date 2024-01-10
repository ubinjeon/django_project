import os
import sys
import urllib.request
client_id = "Your client id"
client_secret = "Your client secret pw"
encText = urllib.parse.quote("직업 체험관")
display = 5
start = 1
url = f"https://openapi.naver.com/v1/search/local?display={display}&start={start}&query=" + encText # JSON 결과
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # XML 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)