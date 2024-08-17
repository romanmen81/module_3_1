# Глобальная переменная для подсчета вызовов
calls = 0

# Функция для подсчета вызовов
def count_calls():
    global calls
    calls += 1

# Функция, которая возвращает информацию о строке
def string_info(string):
    count_calls()
    return (len(string), string.upper(), string.lower())

# Функция, которая проверяет наличие строки в списке
def is_contains(string, list_to_search):
    count_calls()
    # Приводим строки к нижнему регистру для сравнения
    return string.lower() in (s.lower() for s in list_to_search)

# Примеры вызовов функций
print(string_info('Capybara'))  # Вывод: (8, 'CAPYBARA', 'capybara')
print(string_info('Armageddon')) # Вывод: (10, 'ARMAGEDDON', 'armageddon')
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Вывод: True
print(is_contains('cycle', ['recycling', 'cyclic']))   # Вывод: False

# Вывод числа вызовов
print(calls)  # Вывод: 4