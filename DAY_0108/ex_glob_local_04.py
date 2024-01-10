# ---------------------------------------------------------------
# Notice! even tho it's not global variable if it's list, tuple, set, dict
# 함수의 매개변수로 전달 후 원소값 변경시 모두 적용됨!
# ==> 해결 => 깊은 복사 deepcopy로 복사본 전달 필요!
# ---------------------------------------------------------------
def one(number):
    # 지역 변수
    print(number)

def datas(nums, value):
    #nums : 리스트
    #value : 정수
    nums[-1]=1004
    value = 'happy'
    print(nums, value, sep=' - ')

# 전역 변수 선언 --------------------------------------------------------------
value = "Good"
dataList = [11,22,33]
num = 7

# 함수 호출 -----------------------------------------------------------------------
one(num)

datas(dataList, value)

print(f'value : {value}, dataList : {dataList}, num : {num}')