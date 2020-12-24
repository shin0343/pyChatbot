"""

[ beautifulsoup 사용 ]

HTML, XML 파일에서 데이터를 읽어내는 파이썬 라이브러리

"""

html_doc = """
<html><head><title>옛날 이야기</title></head>
<body>
<p calss="title"><b>옛날 이야기</b></p>

<p class="story">옛날 옛적에 세명의 자매가 있었습니다. 그들의 이름은
<a href="http://example.com/elsie" class="sister"id="link1">엘리제</a>,
<a href="http://example.com/lacie" class="sister"id="link2">레이시</a>,
<a href="http://example.com/tillie" class="sister"id="link3">타일리에</a> 이었습니다.

그들은 아주 가난하게 살았습니다.

<p class="story">...............</p>
"""

from bs4 import BeautifulSoup

# 생성자에서는 html_doc를 파싱하고, 그 결과를 BeautifulSoup 객체에 반환
soup = BeautifulSoup(html_doc,"html.parser") #BeautifulSoup 생성자

#print(soup.prettify()) #prettify함수는 Beautifulsoup에서 파싱 처리한 파서 트리를 유니코드로 리턴하는 함수

#soup 객체의 데이터 탐색
print(soup.title)
print(soup.title.name) #title의 이름
print(soup.title.string) #title의 내용 문자
print(soup.title.parent.name) #title 태그의 부모 태그의 이름
print(soup.p) #p 태그
#print(soup.p['class']) #p태그의 클래스

print(soup.a)
print("====================================")
print(soup.find_all('a')) #앵커 tag를 모두 찾음
print("====================================")
print(soup.find(id="link2")) #id가 link2인 것만 찾음

print("====================================")
for link in soup.find_all('a'): #a tag의 모든 href를 가져오기 위한 loop
    print(link.attrs['href']) #print(link.get('href'))
print(type(link.attrs))
print("====================================")

txt = soup.get_text() #태그들 모두 제거하고 텍스트만 가져옴
print(txt)

print(soup.head.title)
print(soup.head.title.string) #title의 문자열만 가져오기
print("------------------------------------")

p1 = soup.p
p2 = p1.next_sibling.next_sibling #sibling: 태그가 열리고 닫힐 때까지의 한 덩어리. next_sibling가 하나만 붙으면 엔터 하나
print(p2)
p3 = p2.previous_sibling
print(p3)
p4 = p3.previous_sibling
print(p4)
