# Najbardziej ogólny to none, czyli nic,
# Typ boolean – czyli tak albo nie, prawda albo fałsz, 0 albo 1
# Typ liczbowy – integer (typ całkowity) albo float (typ zmiennoprzecinkowy)
# Typ string – typ znakowy (jedna litera lub ciąg znaków)
# Kolekcja – lista, tupla, słownik
# Funkcja

# letters = ["a", "b", "c"]
# matrix = [[0, 1], [2, 3]]

# zeros = [0] * 10
# print(zeros)

# combined = matrix + letters
# print(combined)

# numbers = list(range(1, 20))

# print(numbers)

# chars = list("Hello World")

# print(len(chars))
    
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# first, second, *other = numbers
# print(first)
# print(other)

# # first = numbers[0]
# # second = numbers[0]
# third = numbers[0]


# letters = ["a", "b", "c"]
# print(letters.count("d"))
# if "d" in letters:
# print(letters.index("d"))

# numbers = [2, 34, 567, 12]
# # numbers.sort(reverse=True)
# print(sorted(numbers, reverse=True))
# print(numbers)


# items = [
#     ("Product1", 10),
#     ("Product2", 9),
#     ("Product3", 12),
# ]


# def sort_items(item):
#     return item[1]


# items.sort(key=lambda item: item[1])
# print(items)    


# prices = list(map(lambda item: item[1], items))
# print(prices)

# filtered = list(filter(lambda item: item[1] >= 10, items))
# print(filtered)


# prices = list(map(lambda item: item[1], items))
# prices = [item[1] for item in items]

# filtered = list(filter(lambda item: item[1] >= 10, items))
# filter = [item for item in items if item[1 >= 10]]

# list1 = [1, 2, 3]
# list2 = [10, 20, 30]

# # print(list(zip("abc", list1, list2)))

# # [(1, 10), (2, 20), (3, 30)]

# browsing_session = []
# browsing_session.append(1)
# browsing_session.append(2)
# browsing_session.append(3)
# print(browsing_session)
# last = browsing_session.pop()
# print(last)
# print(browsing_session)
# print("redirect", browsing_session[-1])

# Queues

from collections import deque
queue =  deque([])
queue.append(1)
queue.append(2)
queue.append(3)
queue.popleft()
print(queue)
if not queue:
    print("Empty")