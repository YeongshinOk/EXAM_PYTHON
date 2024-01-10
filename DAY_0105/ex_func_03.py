# -------------------------------------------------------------
# 다양한 함수의 형태 - (2) 반환값 없는 함수
#
# - 함수 생성 문법
#
#
# -------------------------------------------------------------
# 함수기능 : 2개의 정수를 덧셈 후 출력해주는 기능
# 함수이름 : addTwo
# 매개변수 : x, y
# 반 환 값 : 없음
# ---------------------------------------------------------------------
def addTwo(x, y):
    value = x + y
    print(f'{x} + {y} = {value}')

# 함수 사용 즉 함수 호출 ===============================================
addTwo(10, 3)

# 함수 호출 시에 매개변수 갯수와 동일하게 데이터 전달해야 함!
# ERROR
# addTwo(1, 3, 2)
# addTwo(10)


# ----------------------------------------------------------------------------------
# 함수 기능 : 영어 단어를 입력 받아서 모두 대문자로 변환 해주는 기능
# 함수 이름 : convertCase
# 매개 변수 : word
# 반 환 값 : 없음 ==> 아무 일을 안하게 됨
# ----------------------------------------------------------------------------------
def convertCase(word):
    word = word.upper()

# ----------------------------------------------------------------------------------
# 함수 기능 : 시퀀스 객체의 모든 원소를 대문자로 변환 해주는 기능
# 함수 이름 : convertCase2
# 매개 변수 : str 타입의 원소로 구성된 list
# 반 환 값 : 없음
# ----------------------------------------------------------------------------------
def convertCase2(dataList):
    for idx in range(len(dataList)):
        dataList[idx] = dataList[idx].upper()

    # for idx, data in enumerate(dataList):
    #     dataList[idx] = data.upper()
# 함수 사용 즉, 함수 호출 -----------------------------------------------------------------
datas = ['Apple', 'Banana', 'Mango']

print(f'[BF] {datas}')

convertCase(datas)

print(f'[BF] {datas}')
for data in datas:
    print(data, data.upper())

for idx in range(len(datas)):
    datas[idx] = datas[idx].upper()

for idx, data in enumerate(datas):
    datas[idx] = data.upper()

print(datas)