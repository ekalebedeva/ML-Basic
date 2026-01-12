# Задача 1. Написать программу, которая получает на вход строку и возвращает словарь, где:#
# ключи — символы из этой строки;
# значения — сколько раз каждый символ встречается в строке.


text = input("Введите строку: ")
char_count = {}
for char in text:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1
print("Словарь с количеством символов:", char_count)

# Задача 2. Дана строка текста (или введённая через консоль). Программа должна вернуть новую строку, в которой порядок слов будет обратным.

text = input("Введите строку: ")
words = text.split()
reversed_words = words[::-1]
reversed_text = ' '.join(reversed_words)
print("Строка с обратным порядком слов:", reversed_text)

# Задача 3. Написать программу, которая удаляет из списка все дубликаты, сохранив исходный порядок элементов.

original_list = [1, 2, 3, 2, 4, 1, 5, 3, 3]
unique_list = []
for item in original_list:
    if item not in unique_list:
        unique_list.append(item)
print("Список без дубликатов:", unique_list)

# Задача 4. Даны три (или больше) списка с объектами. Программа должна создать новый список, содержащий все уникальные элементы — каждый объект встречается только один раз.

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
list3 = [6, 7, 8, 1]
combined = list1 + list2 + list3
unique_set = set(combined)
unique_list = list(unique_set)
print("Список с уникальными элементами:", unique_list)

# Задача 5. Дана строка текста (или введённая через консоль). Программа должна вернуть словарь с четырьмя ключами:
# "гласные",
# "согласные",
# "цифры",
# "пунктуация".
# Значения — количество символов каждого типа в строке.


text = input("Введите строку: ")
vowels = "аеёиоуыэюяАЕЁИОУЫЭЮЯaeiouAEIOU"
consonants = "бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩbcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
digits = "0123456789"
punctuation = ".,!?;:-—()[]{}'\" "
counts = {
    "гласные": 0,
    "согласные": 0,
    "цифры": 0,
    "пунктуация": 0
}
for char in text:
    if char in vowels:
        counts["гласные"] += 1
    elif char in consonants:
        counts["согласные"] += 1
    elif char in digits:
        counts["цифры"] += 1
    elif char in punctuation:
        counts["пунктуация"] += 1
print("Результат анализа строки:")
for key, value in counts.items():
    print(f"{key}: {value}")
