import random

def guess_number_game():
    print("Добро пожаловать в игру 'Угадай число'!")
    while True:  # Внешний цикл для повторной игры
        # Генерируем случайное число от 1 до 100
        secret_number = random.randint(1, 100)
        attempts = 10  # Максимальное количество попыток

        print("Я загадал число от 1 до 100. У вас есть 10 попыток, чтобы его угадать.")

        # Основной цикл игры
        while attempts > 0:
            user_guess = input(f"У вас осталось {attempts} попыток. Введите ваше предположение (или 'выход' для завершения игры): ")

            if user_guess.lower() == 'выход':
                print("Вы вышли из игры. Спасибо за игру!")
                return  # Завершение работы функции и возврат в основную программу

            try:
                guess = int(user_guess)
                
                if guess < 1 or guess > 100:
                    print("Ошибка: Пожалуйста, введите число от 1 до 100.")
                    continue

                if guess < secret_number:
                    print("Слишком маленькое число. Попробуйте снова.")
                elif guess > secret_number:
                    print("Слишком большое число. Попробуйте снова.")
                else:
                    print(f"Поздравляем! Вы угадали число {secret_number}!")
                    break

                attempts -= 1  # Уменьшаем количество попыток

            except ValueError:
                print("Ошибка: Ввод должен быть целым числом.")
        
        if attempts == 0:
            print(f"К сожалению, вы исчерпали все попытки. Загаданное число было {secret_number}.")

        # Запрос на продолжение игры
        play_again = input("Хотите сыграть еще раз? (да/нет): ")
        if play_again.lower() != 'да':
            print("Спасибо за игру! До свидания!")
            break  # Выход из внешнего цикла

if __name__ == "__main__":
    guess_number_game()
