num=0
while True:
    try:
        num=int(input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능): "))
        if 1<=num<=3:
            break
        else:
            num!=1 or num!=2 or num!=3
            print("1,2,3 중 하나를 입력하세요")
    except:
        print("정수를 입력하세요")


for i in range(num):
    print(f"playerA : {i+1}")
A=num

while True:
    try:
        num=int(input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능): "))
        if 1<=num<=3:
            break
        else:
            num!=1 or num!=2 or num!=3
            print("1,2,3 중 하나를 입력하세요")
    except:
        print("정수를 입력하세요")
        
for i in range(num):
    print(f"playerB : {A+i+1}")

