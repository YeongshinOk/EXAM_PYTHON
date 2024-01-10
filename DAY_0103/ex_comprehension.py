# ------------------------------------------------------------------
# 컴프리헨션 (Comprehension)
# - List Comprehension, Dict Comprehension, Set Comprehension
# ------------------------------------------------------------------
# [실습] aList의 원소 값을 제곱한 값을 원소로 가지는 bList 생성하세요.
aList = [1,2,3,4]

# 일반적 for 방식
bList =[]
for a in aList:
    bList.append(a**2)

print(f'aList => {aList}')
print(f'bList => {bList}')

# 컴프리헨션 방식
cList = [a**2 for a in aList]
print(f'cList => {cList}')

# [실습] aList의 원소 값 중에서 짝수인 데이터만 제곱한 값을 원소로 가지는 bList 생성하세요.
# 일반적 for 방식
bList = []
for a in aList:
    if not a%2:
        bList.append(a**2)

print(f'aList => {aList}')
print(f'bList => {bList}')

# 컴프리헨션 방식
clist2 = [a**2 for a in aList if not a%2]
#        ----- -------------- ----------
#         (3)       (1)          (2)
# (2)에서 True인 경우만 (3) 실행
print(f'cList2 => {clist2}')


# [실습3] aList의 원소 값 중에서 짝수인 데이터는 제곱, 홀수인 데이터는 그대로
# 저장한 bList3 생성하세요.
bList3 = []
for a in aList:
    if not a%2:
        bList3.append(a**2)
    else:
        bList3.append(a)
print(f'aList => {aList}\nbList3 => {bList3}')

clist3 = [a**2 for a in aList if not a%2 else a for a in aList]

print(f'cList3 => {clist3}')

clist3 = {a:a**2 for a in aList if not a%2 else a for a in aList}

print(f'cList3 => {clist3}')
