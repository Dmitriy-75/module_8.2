def personal_sum(numbers):
    y = ()
    result = 0
    incorrect_data = 0
    for i in numbers:
        try:
            result += i
        except TypeError:
            incorrect_data += 1
            print(f'Некорректный тип данных для подсчёта суммы - {i}')
    y += result, incorrect_data
    return y


def calculate_average(number):
    len_ = 0
    try:
        z = personal_sum(number)
        for i in number:
            if type(i) is not str:
                len_ += 1
        avr = z[0] / len_
    except TypeError:
        print('В numbers записан некорректный тип данных.')
        avr = None
    except ZeroDivisionError:
        avr = 0
    return avr


print(f'Результат 1: {calculate_average("1, 2, 3")}')  # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}')  # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Всё должно работать



