# 연습문제
camile = {'health':575.6,'health_regen':1.7,'mana':338.8,'mana_regen':1.63,'melee':125,'attack_damage':60,'attack_speed':0.625,'armor':26,'magic_resistance':32.1,'movement_speed':340}

print(camile['health'])
print(camile['movement_speed'])

#심사문제
key = input("스테이터스 입력").split()
value = input("실수 입력").split()

for n in range(len(value)):
    value[n] = float(value[n])

statusDict=dict()
for k in range(len(key)):
    statusDict[key[k]]=value[k]
print(statusDict)




# value = map(float, value)
#
# statusDict=dict()
# for i in range(len(key)):
#     statusDict[key[i]]=value[i]
# print(statusDict)


# for n in range(len(value)):
#     value[n] = float(value[n])
#
# print(type(value[0]))
