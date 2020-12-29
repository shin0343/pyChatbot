"""

urlopen 함수는 urllib.request 포함되어 있는 함수
: HTTP를 통해 웹서버에 데이터를 얻어올 때 많이 사용하는 함수

urlopen(url, [, data, [, timeout]])

 - url: 열고자 하는 URL 문자열
 - data: POST 방식으로 전송 시에 서버로 업로드할 폼 데이터
 - timeout: 타임아웃 시간

urlopen()에서 지원되는 메소드
    urlopen().read([nbytes]): nbyte의 데이터를 바이트 문자열로 읽음
    urlopen().readline(): 한 줄의 텍스트를 바이크 문자열로 읽음
    urlopen().info(): URL에 연관된 메타 정보를 담은 매핑 객체를 반환
    urlopen().getcode(): HTTP 응답 코드를 정수로 반환 (정상응답: 200, not found: 404)
    urlopen().close(): 연결을 닫는다
    
"""

import urllib.request

url = "http://www.naver.com"
u = urllib.request.urlopen(url)

print(u.read())

print(u.info())
