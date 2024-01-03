result = list(range(2,101,2))
print(result)

# int ==> str 형변환 ----------------------------------------------
# result[0] = str(result[0]) 반복

# ----------------------------------------------------------------
# 시퀀스 데이터 타입에서 원소/요소를 하나씩 빼서 반복코드 수행 => for in 반복문
# ----------------------------------------------------------------
strNum=''
for num in result:
    strNum = strNum + str(num)
print(f'strNum => {type(strNum)} {strNum}')

# --------------------------------------------------------
# 리스트 안에 모든 원소를 str 타입으로 변환해서 저장
# --------------------------------------------------------
# 데이터의 인덱스 범위 => 0 ~ len(data)-1
print(f'[Before] result => {result}')

for idx in range(len(result)):
    result[idx] = str(result[idx])
print(f'[After] result => {result}')