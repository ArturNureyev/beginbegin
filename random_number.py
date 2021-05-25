import random
def random_num(from_num, to_num):
    return random.randint(from_num, to_num)
secret_num = random_num(1, 100)
counter = 0
right_border = 100
print("Добро пожаловать в числовую угадайку")
def is_valid_num(users_num):
    if users_num.isdigit() and  0 < int(users_num) < right_border + 1:
        return True
    else:
        return False
while True:
    print("Введите число от 1 до", right_border, "(включительно)")
    num = input()
    counter += 1
    if is_valid_num(num) is False:
        print('А может введем корректное чило от 1 до', right_border)
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
            print("Вы угадали, поздравляем!\nВаше количество попыток:", counter)
            print("Если хотите сыграть еще, напишите 'да'")
            if input().lower() == "да":
                print("Если хотите расширить диапазон числа, напишите 'да'")
                if input().lower() == "да":
                    print("Введите крайнюю правую границу диапазона")
                    right_border = int(input())
                    secret_num = random_num(1, right_border)
                    counter = 0
                    continue
                else:
                    secret_num = random_num(1, 100)
                    counter = 0
                    continue
            else:
                break
print("Спасибо, что играли в числовую угадайку. Еще увидимся...")
