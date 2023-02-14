
## 시작 정수와 끝 정수를 입력받아서
## 그 사이에 있는 정수 중에서
## 3으로 나누어 떨어지고 10으로는 나누어 떨어지지 않는 정수를 프린트하고
## 그 합계를 구한다


###### Version 1: while #######

시작 = int( input("시작 정수를 입력하세요: ") )
끝 = int( input("끝 정수를 입력하세요: ") )

i = 시작
합계 = 0
출력 = ""

while i <= 끝 :

    if (i % 3 == 0) and (i % 10 != 0) :
        출력 = 출력 + " "+ str(i)
        합계 = 합계 + i

    i = i +1

print( 출력 )
print("합계 = ", 합계)


###### Version 2: while - continue #######


시작 = int( input("시작 정수를 입력하세요: ") )
끝 = int( input("끝 정수를 입력하세요: ") )

i = 시작
합계 = 0
출력 = ""

while i <= 끝 :

    if i % 10 == 0 :
        i = i + 1
        continue

    if i % 3 == 0 :
        출력 = 출력 + " "+ str(i)
        합계 = 합계 + i

    i = i +1

print( 출력 )
print("합계 = ", 합계)


###### Version 3: while - break #######


시작 = int( input("시작 정수를 입력하세요: ") )
끝 = int( input("끝 정수를 입력하세요: ") )

i = 시작
합계 = 0
출력 = ""

while True :

    if (i % 3 == 0) and (i % 10 != 0) :
        출력 = 출력 + " "+ str(i)
        합계 = 합계 + i

    i = i +1

    if i > 끝 :
        break

print( 출력 )
print("합계 = ", 합계)


###### Version 4: for - range #######


시작 = int( input("시작 정수를 입력하세요: ") )
끝 = int( input("끝 정수를 입력하세요: ") )

합계 = 0
출력 = ""

for i in range(시작, 끝+1) :

    if (i % 3 == 0) and (i % 10 != 0) :
        출력 = 출력 + " "+ str(i)
        합계 = 합계 + i

print( 출력 )
print("합계 = ", 합계)


###### Version 5: for - range - continue #######


시작 = int( input("시작 정수를 입력하세요: ") )
끝 = int( input("끝 정수를 입력하세요: ") )

합계 = 0
출력 = ""

for i in range(시작, 끝+1) :

    if i % 10 == 0 :
        continue

    if i % 3 == 0 :
        출력 = 출력 + " "+ str(i)
        합계 = 합계 + i

print( 출력 )
print("합계 = ", 합계)


###### Version 6: for - range(A,B, step) #######


시작 = int( input("시작 정수를 입력하세요: ") )
끝 = int( input("끝 정수를 입력하세요: ") )

합계 = 0
출력 = ""


if 시작 % 3 == 0 :
    실제시작 = 시작
else :
    몫 = 시작 // 3
    실제시작 = 3* (몫+1)


while True :
    if 시작 % 3 == 0 :
        break
    시작 = 시작 +1

for i in range(시작, 끝+1, 3) :

    if i % 10 == 0 :
        continue

    if i % 3 == 0 :
        출력 = 출력 + " "+ str(i)
        합계 = 합계 + i

print( 출력 )
print("합계 = ", 합계)