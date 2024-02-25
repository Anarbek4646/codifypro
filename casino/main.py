from decouple import config 
from casino import start
start_money = config("MY_MONEY", default=1000, cast=int)

class Player:
    def __init__(self, name):
        self.__name = name
        self.__bank = config("MY_MONEY", default=1000, cast=int)

    @property
    def name(self):
        return self.__name
    
    @property
    def money(self):
        return self.__bank.get_balance()
    

def create_player():
    player_name = input('Enter your name: ')
    






def num_check():
    while True:
        print([i for i in range(1, 31)])
        number = int(input('Выберите число: '))
        
        if number < 1 or number > 30:
            print("Ошибка: Выберите число от 1 до 30")
            continue
        else:
            return number
        
        

def stavka_check():
    while True:
        money = int(input('Введите ставку: '))
        
        if money <= 0:
            print("Ошибка: Неверная ставка")
            continue
        elif money > start_money:
            print("Ошибка: Недостаточно денег")
            continue
        else:
            return money


while start_money and True:
    
    number = num_check()
    money = stavka_check()
        
    print('Удачи!')

    if start(number, money):
        start_money +=  money * 2
        print('u win: ', money*2, '$')
    else:
        start_money -= money
        print('_______________')
        print('_____U LOSE____')
        print('_______________')

    print('money have: ',start_money,'$')

    quest = input('again? y or no: ')
    if quest == 'no':
        break
    else: continue
