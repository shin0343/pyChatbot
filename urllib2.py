# urlopen()을 이용한 파일 저장

import urllib.request

url = "https://t1.daumcdn.net/cfile/tistory/213B5437527F8C6311"

# 메모리에 다운로드
mem = urllib.request.urlopen(url).read()

save_img = "python.png"

# 파일로 저장
with open(save_img, mode="wb") as f:
    f.write(mem)
    print("File is saved")
