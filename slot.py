from random import randint
from decouple import config




def casino():
    balance = config('MY_MONEY', cast=int)
    print('Добро пожаловать в казино Royal!!!')
    print(f' Ваш текущий баланс составляет - {balance}')
    rand = randint(1, 30)
    while True:
        slot = int(input('Выберите слот от 1 до 30 на который хотите сделать ставку: '))
        if slot == 0:
            ostatok = abs(balance - 1000)
            if ostatok > 1000:
                print(f'вы в плюсе на {ostatok} сом')
            elif ostatok < 1000:
                print(f' вы в минусе на {ostatok} coм')
                break

        stavka = int(input('Сделайте вашу ставку: '))

        if slot == rand:
            stavka *= 2 + balance
            print(f'вы удвоили вышу ставку!!! ваш текущий баланс {balance} сом')
        else:
            balance -= stavka
            print(f' вы проиграли ставку(( ваш текущий баланс {balance} cом ')

        print('Хотите ли вы сыграть еще, если да - то делаете ставку, если нет - то нажмите на 0: ')


