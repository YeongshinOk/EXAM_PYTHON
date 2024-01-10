# ---------------------------------------------------------------------
# 함수 (Function)
# - 특정 기능을 구현하기 위한 코드 묶음을 의미
# - 자주 사용되는 기능을 함수로 구현함
# - 함수 생성 문법
#   def 함수이름(매개변수1, 매개변수2, ..., 매개변수):
#       실행코드
#       실행코드
#       return 리턴값 <---- 반환값, 결과값
# ---------------------------------------------------------------------
# 함수기능 : 2개의 숫자의 합계를 계산 후 결과를 반환해 주는 기능
# 함수이름 : addTwo
# 매개변수 : x , y
# 반 환 값 : 합계
# ---------------------------------------------------------------------
def addTwo(x, y):
    value = x + y
    return value


# ---------------------------------------------------------------------
# 함수기능 : 2개의 숫자의 곱셈을 계산 후 결과를 반환해 주는 기능
# 함수이름 : mulTwo
# 매개변수 : x , y
# 반 환 값 : 곱셈 결과
# ---------------------------------------------------------------------
def mulTwo(x, y):
    value = x * y
    return  value

# ---------------------------------------------------------------------
# 함수 사용 => 함수 호출 (Calling)
# - 방법 : 함수이름(데이터, 데이터 ...)
# ---------------------------------------------------------------------
print(addTwo(10, 3))
addTwo(5,2)
addTwo(-7,4)
