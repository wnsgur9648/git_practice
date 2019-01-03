import webbrowser

# 모모랜드 모든 멤버들의 검색 페이지를 한번에 여는 코드
# momo_land = ["나윤","혜빈","아인","낸시","주이","연우","제인","데이지","태하"]
# for member in momo_land:
#     url = "https://search.daum.net/search?q={}".format(member)
#     webbrowser.open(url)

# 사용자의 입력을 받아서 검색하기
keyword = input("검색어를 입력해 주세요 : ")
url = "https://search.daum.net/search?q={}".format(keyword)
webbrowser.open(url)