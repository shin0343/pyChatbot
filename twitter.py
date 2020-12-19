# Twitter 객체의 pos()메소드 이용
# pos(분석할 문장, norm옵션, stem옵션)

from konlpy.tag import Twitter

twitter = Twitter() #트위터 객체 생성
wordList = twitter.pos("친구가 집에 놀러왔다",norm=True,stem=True)
print(wordList)


# 한나눔(Hannanum) 분석기
from konlpy.tag import Hannanum
hannanum = Hannanum()

# analyze() 메소드는 가독성이 떨어진다!
wordList = hannanum.analyze(u'롯데마트의 흑마늘 양념 치킨이 논란이 되고 있다')
print(wordList)

# morphs() 는 한 줄에 구분되는 형태소를 출력. 품사정보 X
wordList = hannanum.morphs(u'롯데마트의 흑마늘 양념 치킨이 논란이 되고 있다')
print(wordList)

nounList = hannanum.nouns(u'다람쥐는 새 쳇바퀴에 타고 싶다')
print(hannanum.pos(u'웃으면 더 행복합니다')
