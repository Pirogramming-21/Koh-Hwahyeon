print('Hello, Django girls!')

#문자열
print("Ola".upper())
print(len("Ola"))

#변수, print()함수
name='Hwahyeon'
print(name)

name='Maria'
print(name)

#리스트
lottery=[2,42,12,19,30,59]
print(len(lottery))

lottery.sort()
print(lottery)

lottery.reverse()
print(lottery)

print(lottery[0])
print(lottery[5])

lottery.pop(0)
print(lottery)

#딕셔너리
participant = {'name': 'Hwahyeon', 'country': 'Poland', 'favorite_numbers': [7, 42, 92]}
print(participant['name'])

participant['favorite_language']='Python'
print(len(participant))

participant.pop('favorite_numbers')
print(participant)

participant['country']='Korea'
print(participant)

#비교하기
print(5>2)
print(3<1)
print(5>2*2)
print(1==1)
print(5!=2)
print(6>=12/2)
print(3<=2)

print(6>2 and 2<3)
print(3>2 and 2<1)
print(3>2 or 2<1)

#Boolean
a=True
print(a)

a=2>4
print(a)


#If...elif...else
if 3>2:
    print('It works!')

if 5>2:
    print('5 is indeed greater than 2')
else: 
    print('5 is not greater than2')

name='Hwahyeon'
if name=='Hwahyeon':
    print('Hey Hwahyeon!')
elif name=='Jisoo':
    print('Hey Jisoo!')
else:
    print('Hey anonymous!')

volume=57
if volume<20:
    print("It's kinda quiet.")
elif 20 <= volume < 40:
    print("It's nice for background music")
elif 40 <= volume < 60:
    print("Perfect, I can hear all the details")
elif 60 <= volume < 80:
    print("Nice for parties")
elif 80 <= volume < 100:
    print("A bit loud!")
else:
    print("My ears are hurting! :(")

#주석
#volume 값을 바꿔보세요
if volume <20 or volume > 80:
    volume=50
    print("That's better!")

#나만의 함수 만들기
def hi():
    print('Hi there!')
    print('How are you?')

hi()

def hi(name):
    if name=='Hwahyeon':
        print('Hi Hwahyeon!')
    elif name=='suzy':
        print('Hi suzy!')
    else:
        print('Hi anonymous!')

hi('suzy')
hi('jennie')

def hi(name):
    print('Hi '+name+'!')

hi('jiwon')

#for문
def hi(name):
    print('Hi '+name+'!')

girls=['Rachel','Monica', 'Phoebe','Ola']

hi('Rachel')
hi('Monica')
hi('Phoebe')
hi('Ola')

for name in girls:
    hi(name)

person={'name':'Ola', 'height':155, 'favorite_language':'Python'}

for element in person:
    print(element)

for element in person.values():
    print(element)

for key, value in person.items():
    print('Person\'s '+str(key)+' is '+str(value))

for number in range(1,11):
    print(number)

for i in range(1,6):
    print(i)