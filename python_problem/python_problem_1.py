num=0
A=0
B=0
result=True
while result:
    while True:
        try:
            A=int(input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능): "))
            if 1<=A<=3:
                break
            else:
                A!=1 or A!=2 or A!=3
                print("1,2,3 중 하나를 입력하세요")
        except:
            print("정수를 입력하세요")


    for i in range(A):
        print(f"playerA : {num+i+1}")
        if (num+i+1)==31:
            result=False
            break
    num+=A
    if result==False:
        break

    while True:
        try:
            B=int(input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능): "))
            if 1<=B<=3:
                break
            else:
                B!=1 or B!=2 or B!=3
                print("1,2,3 중 하나를 입력하세요")
        except:
            print("정수를 입력하세요")
            
    for i in range(B):
        print(f"playerB : {num+i+1}")
        if (num+i+1)==31:
            result=False
            break
    num+=B
    if result==False:
        break

