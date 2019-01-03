import webbrowser

# 모모랜드 모든 멤버들의 검색 페이지를 한번에 여는 코드
momo_land = ["나윤","혜빈","아인","낸시","주이","연우","제인","데이지","태하"]
for member in momo_land:
    url = "https://search.daum.net/search?q={}".format(member)
    webbrowser.open(url)