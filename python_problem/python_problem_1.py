import random

num=0
result=True

def brGame(player):
    global num, result, loser
    while True:
        try:
            if player=='computer':
                player_num=random.randint(1,3)
            else:
                player_num=int(input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능): "))
            if 1<=player_num<=3:
                break
            else:
                player_num!=1 or player_num!=2 or player_num!=3
                print("1,2,3 중 하나를 입력하세요")
        except:
            print("정수를 입력하세요")


    for i in range(player_num):
        print(f"{player}  {num+i+1}")
        if (num+i+1)==31:
            result=False
            loser=player
            break
    num+=player_num

while result:
    brGame('computer')
    if result==False:
        break

    brGame('player')
    if result==False:
        break

if loser=='computer':
    print('player win!')
else:
    print('computer win!')

