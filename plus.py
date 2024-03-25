print('Вас приветствует система сложения чисел!')
print("Для сложения введите a и b в виде чисел!")
bad_data = True
while bad_data == True:
    try:
        a = int(input("Введите a: "))
        b = int(input("Введите b: "))
        bad_data = False
    except ValueError:
        print('Данные не верны!')
    except ZeroDivisionError:
        print('На ноль делить нельзя!')
    except:
        print('Какая-то ошибка!')
print(f'Сумма {a} и {b} равна {a + b}.')