# -------------------------------------------------------------
# 다양한 함수의 형태 - (1) 기본
# -------------------------------------------------------------
# 함수기능 : 팩토리얼을 계산 후 계산 결과를 반환해주는 기능
#           팩토리얼이란? 3! = 3 * 2 * 1
# 함수이름 : factorial
# 매개변수 : x
# 반 환 값 : 계산 결과
# ---------------------------------------------------------------------
def factorial(x):
    value = 1   #결과 저장 변수
    if x:
        for i in range(x, 0, -1): value *= i
            # value = value * i
            # value *= i
    return value

print(factorial(5))
# -------------------------------------------------------------
# 함수기능 : 팩토리얼을 계산 후 계산 결과를 아래와 같은 형태로 반환해주는 기능
#           팩토리얼이란? 3! = 3 * 2 * 1
# 함수이름 : factorial2
# 매개변수 : x
# 반 환 값 : 계산 문자열
# ---------------------------------------------------------------------
def factorial2(x):
    strRet = f'{x}! = '
    intRet = 1
    if x:
        for n in range(x, 0, -1):
            intRet = intRet * n
            strRet = strRet + str(n)  # + '*' if n!= 1 else ' = '
            strRet = strRet + (' * ' if n != 1 else ' = ')
            #print(strRet, intRet)

    return strRet + str(intRet)

print(factorial2(10))