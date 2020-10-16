# глобальные переменные
userChoice = 0      # переменная, которая хранит выбор пользователя
# Задание 1: вобъявить переменную, котоая будет хранить 15 значений
valuesArray = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15']

print('Меню:')
print('1. Вывести на экран все знаения')
print('2. Добавить значение')
print('3. Удалить значение')
print('4. Найти значение')
print('5. Отсортировать значения')
print('6. Выйти')
print('Введите опцию:')
userChoice = int(input())

# Задание 2: в цикле while создать ограничения для ввода опций таким образом, чтобы
# программа принимала только значения, из меню (1-6), в остальных случаях выдавала ошибку.

# Задание 3: Реализовать опцию 1 и 2 из списка меню.
while userChoice != 6:
    # Вывод ошибки, если userChoice больше или меньше 1 или 6
    if userChoice < 1 or userChoice > 6:
        print('Ошибка!')

    print('Введите опцию:', userChoice)

    print('Меню:')
    print('1. Вывести на экран все знаения')
    print('2. Добавить значение')
    print('3. Удалить значение')
    print('4. Найти значение')
    print('5. Отсортировать значения')
    print('6. Выйти')
    print('Введите опцию:')
    userChoice = int(input())

    # Реализуем функцию 1
    if userChoice == 1:
        for i in valuesArray:
            print(i)

    # Реализуем функцию 2
    if userChoice == 2:
        newValue = input('Введите новое значение: ')
        valuesArray.append(newValue)

    # Реализуем функцию 3
    if userChoice == 3:
        delValue = input('Введите значение на удаление: ')
        try:
            valuesArray.remove(delValue)
        except:
            print('Ошибка!')

    # Реализуем функцию 4
    if userChoice == 4:
        foundValue = input('Введите значение, которое надо найти: ')
        for i in valuesArray:
            if foundValue == i:
                print('Значение найдено: {}'.format(i))
                break
            else:
                pass

    # Реализуем функцию 5, но не указываем ключа, т.к его нет. Сортировка будет проводится так, как предписано в python
    if userChoice == 5:
        valuesArray.sort()