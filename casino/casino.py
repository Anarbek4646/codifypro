from random import choice, randint


def start(number, money):
    list_ = list(range(1,31))
    rand_num = choice(list_)
    if rand_num < number:
        return True
    else:
        return False
    

        