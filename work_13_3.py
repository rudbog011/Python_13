import random
def is_valid(user_input, number):
    if user_input.isdigit():
        user_number = int(user_input)
        if user_number >= 1 and user_number <= number:
            return True
        else:
            return False
    else:
        return False
def is_valid_n(user_input):
    if user_input.isdigit():
        user_number = int(user_input)
        if user_number >= 1:
            return True
        else:
            return False
    else:
        return False
def query_game():
    print('Вы хотите продолжить игру? (Да/Нет)')
    answer = input()
    if answer.lower() == 'да':
        game()
    else:
        print('Ждём Вас ещё!')
def game():
    count = 0
    print('Добро пожаловать в игру "Угадай число".')
    while True:
        print('Введите правую границы для случайного выбора числа (от 1 до n):')
        number = input()
        if is_valid_n(number):
            number = int(number)
            break
        else:
            continue
    secret_number = random.randint(1, number)
    while True:
        print(secret_number, 'Введите число от 1 до', number)
        user_input = input()
        if not is_valid(user_input, number):
            continue
        else:
            user_number = int(user_input)
        count += 1
        if secret_number > user_number:
            print('Загаданное число больше, чем введенное вами число')
        elif secret_number < user_number:
            print('Загаданное число меньше, чем введенное вами число')
        else:
            print('УРА! Вы угадали загаданное число. Вы использовали: ', count, 'попыток для решения задачи')
            query_game()
            break
game()




