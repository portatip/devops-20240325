# Система математичеческих вычислений!
Cостоит  из **двух** *компонентов*
1. Решение квадратных уравнений
2. Сложение

Запуск приложений

`python3 kvur.py`

`python3 plus.py`

Пример кода:


```python3
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
```
