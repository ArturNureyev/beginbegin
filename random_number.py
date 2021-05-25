import random
def random_num(from_num, to_num):
    return random.randint(from_num, to_num)
secret_num = random_num(1, 100)
print("Добро пожаловать в числовую угадайку")
def is_valid_num(users_num):
    if users_num.isdigit() and  0 < int(users_num) < 101:
        return True
    else:
        return False
while True:
    print("Веедите число от 1 до 100(включительно)")
    num = input()
    if is_valid_num(num) is False:
        print('А может введем корректное чило от 1 до 100?')
        continue
    else:
        num = int(num)
        if num < secret_num:
            print("Ваше число меньше загаданного, попробуйте еще разок")
            continue
        elif num > secret_num:
            print("Ваше число больше загаданного, попробуйте еще разок")
            continue
        elif num == secret_num:
            print("Вы угадали, поздравляем!")
            break
print("Спасибо, что играли в числовую угадайку. Еще увидимся...")