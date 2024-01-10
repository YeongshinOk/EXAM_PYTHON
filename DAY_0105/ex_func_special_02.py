# -------------------------------------------------------------
# 다양한 함수의 형태 - 특별한 함수 (2)
# - 매개변수의 갯수를 유동적으로 가변으로 하는 함수
# - 키와 값의 덩어리 데이터
# - 형태 : def 함수명(*data):
# - 가변 인자 함수
# - 매개변수 갯수 : 0개 ~ N개
# - 호출 : 함수명(키1=값1)
# -       함수명(키1=값1, 키2=값2, 키3=값3)
#           함수명()
# -------------------------------------------------------------
#  aDict = {'name':"Hong",'age':10}
#  aDict.update(job='학생')
#  aDict.update(job='학생',birth='1112',blood='A')
#  print(aDict)
#  aDict.update(점수1=100, 점수2=100, 점수3=100, 점수4=3, 점수5=19)

# -----------------------------------------------------------------------
#       함수 기능 : 회원 가입 기능
#       함수 이름 : joinMember
#       매개 변수 : 이름, 전화 번호, 아이디, 이메일, 취미, 주소, 생일, ....
#       매개 변수 : 가변 + 데이터 정보 함께
#       매개 변수 : 키워드파라미터 **member
#       반 환 값 : '가입 완료 되었습니다.' str
# -----------------------------------------------------------------------
def joinMember(**member):
    # print(type(member))
    print(member)
    # 멤버 저장소에 멤버 추가하기
    # members.update(**member)
    # members.append(member)
    members[f'M{len(members)}']=member


# -----------------------------------------------------------------------------
# 함수 사용 즉 호출
# -----------------------------------------------------------------------------
# 가입된 회원들 저장 변수
members = {}
mList = []
print(f'BF : {members}')
print(f'BF : {mList}')

    # 회원가입 기능 함수 호출
joinMember(name='Hong')
joinMember(id='Hong84',phone='010')
joinMember(id='baby',blood='A')

print(f'AF : {members}')
print(f'AF : {mList}')
# m = {'name':'Hong','age':17}
# print(m.keys())
# print(m.values())
# print(m.items())

# -----------------------------------------------------------------------
#       함수 기능 : 회원 가입 기능
#       함수 이름 : joinMember2
#       매개 변수 : 필수 = > id, pw
#       매개 변수 : 선택 = > **option 이름, 전화 번호, 이메일, 취미, 주소, 생일, ....
#       매개 변수 : 가변 + 데이터 정보 함께
#       매개 변수 : 키워드파라미터 **member
#       반 환 값 : '가입 완료 되었습니다.' str
# -----------------------------------------------------------------------
def joinMember2(id,pw,**option):
    print('Ok')

members = {}
mList = []
print(f'BF : {members}')
print(f'BF : {mList}')

joinMember2('a','b')
joinMember2('h','w',phone='010', blood ='B')



joinMember(name='Hong')
joinMember(id='Hong84',phone='010')
joinMember(id='baby',blood='A')

# -----------------------------------------------------------------------
#       함수 기능 : 회원 가입 기능
#       함수 이름 : joinMember2
#       매개 변수 : 필수 = > id, pw, loc, gender
#       매개 변수 : 선택 = > **option 이름, 전화 번호, 이메일, 취미, 주소, 생일, ....
#       매개 변수 : 가변 + 데이터 정보 함께
#       매개 변수 : 키워드파라미터 **member
#       반 환 값 : '가입 완료 되었습니다.' str
# -----------------------------------------------------------------------
def joinMember3(id,pw,loc='내국인',gender='남자',**option):
    print(id,pw,loc,gender,option)

members = {}
mList = []
print(f'BF : {members}')
print(f'BF : {mList}')

joinMember3('a','b')
joinMember3('a','b',gender='여자')
joinMember3('h','w',phone='010', blood ='B')

print(f'AF : {members}')
print(f'AF : {mList}')

joinMember(name='Hong')
joinMember(id='Hong84',phone='010')
joinMember(id='baby',blood='A')