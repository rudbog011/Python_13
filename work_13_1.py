import random
count = 0
def is_valid(user_input):
    if user_input.isdigit():
        user_number = int(user_input)
        if user_number >= 1 and user_number <= 100:
            return True
        else:
            return False
    else:
        return False

secret_number = random.randint(1, 100)
print('Добро пожаловать в игру "Угадай число".')
while True:
    print('Введите число от 1 до 100')
    user_input = input()

    if not is_valid(user_input):
        continue
    else:
        user_number = int(user_input)
    count += 1
    if secret_number > user_number:
        print('Загаданное число больше, чем введенное вами число')
    elif secret_number < user_number:
        print('Загаданное число меньше, чем введенное вами число')
    else:
        print('УРА! Вы угадали загаданное число')
        break
print('Вы использовали: ', count, 'попыток для решения задачи. Спасибо за игру. Ждем вас ещё!')