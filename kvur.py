from math import sqrt

print("Вас приветствует система решения квадратных уранений!")
print("Для решения уравнения введите слудующие значения в виде числа!")
bad_data = True
while bad_data == True:
    try:
        a = int(input("Введите a: "))
        b = int(input("Введите b: "))
        c = int(input("Введите c: "))
        bad_data = False
    except ValueError:
        print('Данные не верны!')
    except ZeroDivisionError:
        print('На ноль делить нельзя!')
    except:
        print('Какая-то ошибка!')

D = b * b - (4 * a * c)
print(f'Дискриминант равен: {D}.')

if D > 0:
    d = sqrt(D)
    X1 = ((-b) + d) / (2 * a)
    X2 = ((-b) - d) / (2 * a)
    print(f"Перый корень уравнения равен {X1}, второй корень равен {X2}")
elif D == 0:
    X1 = (-b) / (2 * a)
    print("Корень уравнения равен {}".format(X1))
else:
    print('Уравнение не имеет корней!')
