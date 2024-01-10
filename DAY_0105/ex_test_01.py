# -----------------------------------------------------------------------
# [실습] 2개의 정수를 입력 받은 후 4칙 연산 수행 결과를 반환하는 기능의
#       함수를 정의해 주세요.
#       함수이름 : fourCalc
#       매개변수 : n1, n2
#       반환결과 : 4칙 연산 결과
# -----------------------------------------------------------------------
def fourCalc(n1, n2):
    return n1+n2, n1-n2, n1*n2, n1/n2 if n2 else '0으로 나눌 수 없음'

print(fourCalc(10,3))
print(fourCalc(10,0))
    # n1, n2 = map(int, input().split())
    #
    # plus = n1 + n2
    # minus = n1 - n2
    # times = n1 * n2
    # divide = n1 / n2

    # return plus, minus, times, divide


# -----------------------------------------------------------------------
# [실습] 문자열을 16진수 코드값으로 변환 후 반환하는 함수를 정의해 주세요.
#       함수이름 : getConde
#       매개변수 : message
#       반환결과 : str
# -----------------------------------------------------------------------
def getCode(message):
    ret=''
    for msg in message:
        ret += hex(ord(msg)) + ' '
    return ret

print(getCode('Good Luck'))