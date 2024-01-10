# 지역변수 전역변수
def foo():
    x=20
    print(x)

# 전역 변수
x = 10
# calling function
foo()
print(x)
#print(x) local variable x not allowed to access. Error

print(locals())

# 여기에는 입력을 대기하는 코드가 없어서 바로 종료되요