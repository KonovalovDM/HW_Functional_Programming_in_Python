# Рекурсивная функция, которая выводит только нечетные числа из переданного списка на консоль:

def print_odd_numbers(numbers):
    if not numbers:  # Базовый случай: если список пуст, заканчиваем рекурсию
        return
    if numbers[0] % 2 != 0:  # Проверяем, является ли число нечетным
        print(numbers[0])
    # Рекурсивный вызов для оставшейся части списка
    print_odd_numbers(numbers[1:])

# Пример использования
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print_odd_numbers(numbers)

print("\n")  # Отступ в две строки


# Рекурсивная функция для подсчета элементов в списке:

def count_elements(lst):
    # Базовый случай: если список пуст, возвращаем 0
    if not lst:
        return 0
    # Рекурсивный случай: убираем первый элемент и вызываем функцию для оставшегося списка
    return 1 + count_elements(lst[1:])

# Пример использования
my_list = [1, 2, 3, 4, 5]
print("Количество элементов в списке:", count_elements(my_list))

print("\n")  # Отступ в две строки


# Функция, которая при каждом следующем своем вызове выводит на консоль следующий элемент заданного списка.

def create_iterator(lst):
    # Инициализируем индекс
    index = -1

    def next_element():
        nonlocal index  # Даем доступ к переменной `index` из внешней области
        index += 1
        if index < len(lst):
            return lst[index]
        else:
            raise StopIteration("Список закончился!")

    return next_element


# Пример использования
my_list = [10, 20, 30, 40, 50]
iterator = create_iterator(my_list)

# Вызываем функцию несколько раз
print(iterator())  # 10
print(iterator())  # 20
print(iterator())  # 30
print(iterator())  # 40
print(iterator())  # 50

# Попробуем вызвать еще раз (будет исключение StopIteration)
# print(iterator())  # Это вызовет ошибку StopIteration