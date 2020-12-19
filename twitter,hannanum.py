# Twitter 객체의 pos()메소드 이용
# pos(분석할 문장, norm옵션, stem옵션)

from konlpy.tag import Twitter

twitter = Twitter() #트위터 객체 생성
wordList = twitter.pos("친구가 집에 놀러왔다",norm=True,stem=True)
print(wordList)
