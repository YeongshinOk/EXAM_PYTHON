#Q1
home_city = "Ulsan"
blood_type = "B"
fav_season = "Spring"
height = 182
phone_num = "+82)10-9868-6358"
nationality = "Rep of Korea"

#Q2
mbti = 'INFP'
blood = 'A'
gender = 'M'
height = 171.7
weight = 77

print("[신상 정보]")
print('MBTI :',mbti,'   혈액형 :',blood, '    성별 :',gender)
print('몸무게 :',weight,'  키 :',height)

print("MBTI : %s    혈액형 : %s    성별 :  %s\n몸무게 : %d   키 : %f "%(mbti, blood, gender, weight, height))

print(f'MBTI : {mbti} \t 혈액형 : {blood} \t 성별 : {gender}\n몸무게 : {weight} \t 키 : {height}')

#Q3
favseason = input("좋아하는 계절은?")
print("당신은 %s을 좋아하는 군요!" %favseason)

Spring = input("봄은 영어로?")
print("봄은 영어로 Spring입니다.")



data_int = int(50)
data_float = float(0.91)
data_str = 'Winter'
data_bool = bool(False)

print(f'데이터 {data_int} => {type(data_int)} 타입')
print(f'데이터 {data_float} => {type(data_float)} 타입')
print(f'데이터 {data_str} => {type(data_str)} 타입')
print(f'데이터 {data_bool} => {type(data_bool)} 타입')

#Q4
#1번 heap
#2번 stack

#Q5
#1번 int
#2번 float
#3번 str
#4번 bool
#5번 2진법
#6번 8진법
#7번 16진법

#Q6
Length = float(input("직육면체 가로길이(cm) :"))
Width = float(input("직육면체 세로길이(cm) :"))
Height = float(input("직육면체 높이길이(cm) :"))

Area = Length*Width
Volume = Area*Height

print("직사각형 넓이 : %f\n직육면체 부피 : %f" %(Area,Volume))