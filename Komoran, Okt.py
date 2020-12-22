# KoNLPy 패키지에 있는 분석기(형태소/POS태그 작성기)

"""

Hannanum Class
    - analyze(구문): 구문 분석
    - morph(구문): 형태소 분석
    - nouns(구문): 명사 추출
    - pos(구문, 옵션)

Kkma Class (꼬꼬마 클래스라 명명)
    - morph(구문): 형태소 분석
    - nouns(구문): 명사 추출
    - pos(구문, 옵션)

Komoran Class
    - morph(구문): 형태소 분석
    - nouns(구문): 명사 추출
    - pos(구문, 옵션)

OKt Class : 기존의 Twitter 클래스가 OKt로 이름 변경됨(v5.0 이후)
    - morph(구문): 형태소 분석
    - nouns(구문): 명사 추출
    - pos(구문, 옵션)
    - phrases(): phrase(어구) 추출

"""

# Komoran 사용

"""

    품사(POS: Part Of Speech) 태그

    NN(명사): NNP(고유명사), NNG(일반명사)
    VV(동사), VCN(부정지정사, 형용사)
    
"""

#from konlpy.tag import Komoran

#komoran = Komoran(userdic='dic.txt') # userdic: 사용자 정의 사전 경로명. dic.txt 내의 품사 구분은 Tab키로 구분!

#wordList = komoran.morphs(u'와우 코모란도 오픈소스가 되었습니다')

#wordList = komoran.nouns(u'오픈소스에 관심 많은 멋진 개발자님들!')

#wordList = komoran.pos(u'코모란. 혹시 바람과 함께 사라지다 아시나요?')
#print(wordList)


# OKt Class 사용

from konlpy.tag import OKt # Twitter클래스와 같은 클래스

okt = Okt()

wordList = okt.morphs(u'단독 입찰보다 복수 입찰의 경우')
wordList = okt.nouns(u'단독 입찰보다 복수 입찰의 경우')
wordList = okt.phrases(u'단독 입찰보다 복수 입찰의 경우')
wordList = okt.pos(u'단독 입찰보다 복수 입찰의 경우')
print(wordList)

wordList = okt.pos(u'이것도 되나욬ㅋㅋㅋ') # 아무 옵션 없음
wordList = okt.pos(u'이것도 되나욬ㅋㅋㅋ',norm=True) # norm옵션을 True로 하면 잘못된 표기법 구분해줌
wordList = okt.pos(u'이것도 되나욬ㅋㅋㅋ',norm=True) # stem옵션을 True로 하면 잘못된 표기법의 정확한 표기법까지 제시해줌
print(wordList)

