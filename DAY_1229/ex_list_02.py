# ----------------------------------------------------
# 다양한 리스트 생성
# ----------------------------------------------------
# 실수 데이터로 구성된 리스트 생성
floatNums = [4.,35,3.5,6.3,5.01]

# str 데이터로 구성된 리스트 생성
strNums = ['44','55','98']

# bool 데이터로 구성된 리스트 생성
boolNums = [False,False,True,True,True]

# 다양한 데이터 타이븡로 구성된 리스트 생성
data = ['100', 98, False,7,12,'Apple',True]

# 빈 리스트 생성
nums = []

# 리스트 안에 리스트 데이터로 구성된 리스트 생성
nums = [10,20,30,['A','B'],100,200]

# 리스트의 요소 출력
print(f'nums[0] => {nums[0]}')
print(f'nums[1] => {nums[1]}')
print(f'nums[2] => {nums[2]}')
print(f'nums[3] => {nums[3]}')
print(f'nums[4] => {nums[4]}')
print(f'nums[5] => {nums[5]}')


print(f'nums[0] => {nums[0]}, {type(nums[0])}')
print(f'nums[1] => {nums[1]}, {type(nums[1])}')
print(f'nums[2] => {nums[2]}, {type(nums[2])}')
print(f'nums[3] => {nums[3]}, {type(nums[3])}')
print(f'nums[4] => {nums[4]}, {type(nums[4])}')
print(f'nums[5] => {nums[5]}, {type(nums[5])}')

# 리스트 안의 리스트 인덱싱해서 꺼내오기
print(f'nums[3] => {nums[3][1]}')
print(f'nums[3] => {nums[3][1]}, {type(nums[3][1])}')

data2 = [[[1,2,3]]]
print(data2)
print(data2[0])
print(data2[0][0])
print(data2[0][0][0])
