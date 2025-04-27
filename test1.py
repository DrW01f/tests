"""
Даны две строки строчных латинских символов: строка J и строка S. Символы, входящие в строку J, — «драгоценности»,
входящие в строку S — «камни». Нужно определить, какое количество символов из S одновременно являются «драгоценностями».
Проще говоря, нужно проверить, какое количество символов из S входит в J.
Это разминочная задача, к которой мы размещаем готовые решения. Она очень простая и нужна для того, чтобы вы могли
познакомиться с нашей автоматической системой проверки решений. Ввод и вывод осуществляется через файлы, либо через
 потоки ввода-вывода, как вам удобнее.
ввод:      вывод:
ab              4
aabbccd
"""
#
# def sum_in_text():
#     with open("input.txt", "r", encoding="UTF-8") as f:
#         j = f.readline().strip()
#         s = f.readline().strip()
#         result = 0
#         for ch in s:
#             if ch in j:
#                 result += 1
#     with open("output.txt", "w", encoding="UTF-8") as f:
#         result = str(result)
#         f.write(result)
#
#
# sum_in_text()

"""
Даны два числа A и B. Вам нужно вычислить их сумму A+B. В этой задаче вам нужно читать из стандартного ввода и выводить
 ответ в стандартный вывод
Ввод: 2 2      Вывод: 4
"""

# def sum_():
#     data = input().split(" ")
#     return int(data[0]) + int(data[1])
#
# print(sum_())

"""
Даны три натуральных числа. Возможно ли построить треугольник с такими сторонами? Если это возможно, выведите строку 
YES, иначе выведите строку NO.
Треугольник — это три точки, не лежащие на одной прямой.
"""
#
# def is_triangle():
#     a, b, c = int(input()), int(input()), int(input())
#     if c >= a and c >= b:
#         if c < a + b:
#             print("YES")
#         else:
#             print("NO")
#     elif b >= a and b >= c:
#         if b < a + c:
#             print("YES")
#         else:
#             print("NO")
#     elif a >= c and a >= b:
#         if a < c + b:
#             print("YES")
#         else:
#             print("NO")

"""
Вам дан словарь, состоящий из пар слов. Каждое слово является синонимом к парному ему слову. Все слова в словаре 
различны. Для одного данного слова определите его синоним.
Формат ввода
Программа получает на вход количество пар синонимов N. Далее следует N строк, каждая строка содержит ровно два 
слова-синонима. После этого следует одно слово.
Формат вывода
Программа должна вывести синоним к данному слову.
Ввод                Вывод
3                       Bye
Hello Hi
Bye Goodbye
List Array
Goodbye
"""

# def synonyms():
#
#     count = int(input())
#     res = []
#     for i in range(count):
#         inputs = input()
#         res.append((inputs.split()[0], inputs.split()[1]))
#     key = input()
#     for word in res:
#         if key in word:
#             if key == word[0]:
#                 print(word[1])
#             else:
#                 print(word[0])


"""
В новой программе OpenCalculator появилась новая возможность – можно настроить, какие кнопки отображаются, а 
какие – нет. Если кнопка не отображается на экране, то ввести соответствующую цифру с клавиатуры или копированием из 
другой программы нельзя. Петя настроил калькулятор так, что он отображает только кнопки с цифрами x, y, z. Напишите 
программу, определяющую, сможет ли Петя ввести число N, а если нет, то какое минимальное количество кнопок надо 
дополнительно отобразить на экране для его ввода.
Формат ввода
Сначала вводятся три различных числа из диапазона от 0 до 9: x, y и z (числа разделяются пробелами). Далее вводится 
целое неотрицательное число N, которое Петя хочет ввести в калькулятор. Число N не превышает 10000.
Формат вывода
Выведите, какое минимальное количество кнопок должно быть добавлено для того, чтобы можно было ввести число N 
(если число может быть введено с помощью уже имеющихся кнопок, выведите 0)
Ввод:       Вывод:
1 2 3           0
1123

5 7 3           2
123
"""

# def how_many():
#     counts = []
#     numbers = input()
#     counts.extend([numbers.split()[0], numbers.split()[1], numbers.split()[2]])
#     res = set(input())
#     print(sum(1 for i in res if i not in counts))
#
# how_many()

"""
Во входном файле (вы можете читать данные из файла input.txt) записан текст. Словом считается последовательность 
непробельных символов идущих подряд, слова разделены одним или большим числом пробелов или символами конца строки. 
Для каждого слова из этого текста подсчитайте, сколько раз оно встречалось в этом тексте ранее.
Формат ввода
Вводится текст.
Формат вывода
Выведите ответ на задачу.
Ввод                        Вывод:
one two one tho three           0 0 1 0 0 
"""

# def count_words():
#     with open("input.txt", "r", encoding="UTF-8") as f:
#         text = []
#         for line in f:
#             text.extend(line.strip(" \n").split())
#         res = {}
#         for word in text:
#             res[word] = res.get(word, 0) + 1 if word in res.keys() else 0
#             print(res[word], end=" ")

"""
Напишите программу, которая находит в массиве элемент, самый близкий по величине к данному числу.
Формат ввода
В первой строке задается одно натуральное число N, не превосходящее 1000 — размер массива. Во второй строке содержатся 
N чисел — элементы массива, целые числа, не превосходящие по модулю 1000. В третьей строке вводится одно целое число 
x, не превосходящее по модулю 1000.
Формат вывода
Вывести значение элемента массива, ближайшее к x. Если таких чисел несколько, выведите любое из них.
Ввод:           вывод:
5                   5
1 2 3 4 5
6
"""

# def nearest_number():
#     _ = int(input())
#     numbers = []
#     numbers.extend(map(int, input().split()))
#     target = int(input())
#     res = {number: abs(target - number) for number in numbers}
#     print(min(res, key=res.get))


"""
В данном массиве из n целых чисел найдите три числа, произведение которых максимально.
Формат ввода
В единственной строке расположено 3<n10**5
Формат вывода
Выведите три элемента массива, дающих наибольшее произведение, в любом порядке.
"""

#
# def max_of_three():
#     numbers = list(map(int, input().split()))
#
#     # res = sorted(numbers, key=lambda x: abs(x),reverse=True)
#     # print(*res[0:3])
#
#     if len(numbers) == 3:
#         print(*numbers)
#     else:
#         first_number = numbers[0]
#         if abs(numbers[1]) >= abs(first_number):
#             second_number, first_number = first_number, numbers[1]  # порядок присвоения?
#         else:
#             second_number = numbers[1]
#         if abs(numbers[2]) >= abs(first_number):
#             # first_number, second_number, third_number = numbers[2], first_number, second_number
#             third_number, second_number,  first_number = second_number, first_number, numbers[2]
#         elif abs(numbers[2]) >= abs(second_number):
#             # second_number, third_number = numbers[2], second_number
#             third_number,  second_number = second_number, numbers[2]
#         else:
#             third_number = numbers[2]
#
#         for i in range(3, len(numbers)):
#             if abs(first_number) <= abs(numbers[i]):
#                 third_number, second_number, first_number = second_number, first_number, numbers[i]
#             elif abs(second_number) <= abs(numbers[i]):
#                 third_number, second_number = second_number, numbers[i]
#             elif abs(third_number) <= abs(numbers[i]):
#                 third_number = numbers[i]
#         print(first_number, second_number, third_number)
#
#           выдает ошибки на закрытых тестах
#
# max_of_three()

#https://contest.yandex.ru/contest/50668/problems/B/
"""
Через тернии к клиенту
Известная компания Тындекс идёт в ногу со временем — с началом активных космических перелётов в компании открылся 
сервис Тындекс.Ракетакси: пользователю необходимо лишь указать координаты начала и конца перелёта, после чего за ним 
вылетит персональная ракета.
По сути любой заказ можно описать в виде событий четырёх типов:
A (accepted) - заказ принят в работу (ракета вылетела за клиентом);
B (boarding) - клиент сел в ракету;
S (success) - заказ успешно завершён (клиент вышел на планете назначения);
C (cancelled) - заказ отменён.
Все происходящие с ракетами события отправляются на сервера, где сразу логируются. Вот только из-за проблем со связью 
(метеоритные потоки, вспышки на звездах и т.д.) отправка событий иногда затягивается, из-за чего записи в получившемся 
логе могут идти не по порядку.
Гарантируется, что все описанные в логе события задают один из следующих сценариев:
A - B - S
A - B - C
A - C
Вам, как главному аналитику (и по совместительству главному программисту) ракетопарка, необходимо исследовать лог за 
прошедший год и определить для каждой ракеты суммарное время движения (в минутах) в течение заказов.
В каждый момент времени ракета выполняет только один заказ. Будем считать, что каждая ракета в каждый момент времени:
или стоит на месте в ожидании заказа,
или перемещается по космосу, выполняя заказ.
Движение начинается после принятия заказа и завершается после отмены или завершения заказа. За одну минуту не может 
произойти несколько событий, связанных с одной и той же ракетой.
14 21 30 3632 A 
14 23 52 3632 B     2ч 22м
15 0 5 3632 C       + 13м
50 7 25 3632 A
50 7 26 3632 C      +1

                    120 + 22 +13 +1
"""

# def time_finder():
#     count = int(input())
#     if count == 0:
#         print(0)
#     logs = {}
#     diff_time = 0
#     for i in range(count):
#         text = input().split()
#         logs.setdefault(str(text[3]), []).append([list(map(int, text[0:3])), text[4]])
#
#     for k in sorted(logs.keys(), reverse=True):
#
#         logs[k] = sorted(logs[k])
#
#         for i in range(0, len(logs[k]) - 1):
#             if logs[k][i + 1][1] != "A":
#                 diff_time += (logs[k][i + 1][0][0] * 24 * 60 + logs[k][i + 1][0][1] * 60 + logs[k][i + 1][0][2]) - \
#                              (logs[k][i][0][0] * 24 * 60 + logs[k][i][0][1] * 60 + logs[k][i][0][2])
#             else:
#                 continue
#         print(diff_time, end=" ")
#         diff_time = 0
#
# #Ошибка на закрытых тестах
#
# time_finder()

#https://contest.yandex.ru/contest/50668/problems/D/
# def water():
#     count_order = int(input())
#     orders = [list(map(int, input().split())) for _ in range(count_order)]
#
#     count_tasks = int(input())
#     for i in range(count_tasks):
#         task = list(map(int, input().split()))
#         if task[2] == 1:
#             # coast = [sum(orders[j][2] for j in range(count_order) if task[0] <= orders[j][0] <= task[1])]
#             print(*[sum(orders[j][2] for j in range(count_order) if task[0] <= orders[j][0] <= task[1])], end=" ")
#         else:
#             # total_time = [sum((orders[k][1] - orders[k][0]) for k in range(count_order) if task[0] <= orders[k][1] <=
#             #                   task[1])]
#             print(*[sum((orders[k][1] - orders[k][0]) for k in range(count_order) if task[0] <= orders[k][1] <=
#                               task[1])], end=" ")
#
#       считает дольше 10 секунд
# water()


# def code_names():
#     count = int(input())
#     for person in range(count):
#         person = input().split(",")
#         alpha = len(set((person[0] + person[1] + person[2])))
#         date = sum(int(i) for i in person[3]) + sum(int(j) for j in person[4])
#         first_alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.index(person[0][0].upper()) + 1
#         res = hex(alpha + date * 64 + first_alpha * 256).upper()
#         print(res[-3:].upper() if len(res) > 2 else res.zfill(3).upper(), end=" ")

# import math
#
#
# def how_many_sleep():
#     n, m, x, y = list(map(int, input().split()))
#     house = []
#     count = 0  # кол-во частей окна
#     for i in range(n * x):
#         house.append(input().upper())
#     # print(house)
#     res = 0
#
#     for lvl in range(m * y, y):  # шаг для перехода по квартирам
#         for weigh in range(n * x, x):  # идем по этажам сверху вниз
#
#             for h in range(x):  # цикл поиска на 1 квартиру
#                 for w in range(y):
#                     if house[x][y] == "X":
#                         count += 1
#
#             if (x * y / 2) >= 0.5:
#                 res += 1
#             count = 0
#             continue
#         continue
#     print(res)
#     # неправильный ответ
#
#
# how_many_sleep()



def code():
    #               2       3       4     5      6      7       8       9
    # dict_secret = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
    # зашифровка слов и поиск их в общем щифре с последующем тсключением этой подстроки из общей части??
    dict_secrets = {"A": 2, "B": 22, "C": 222, "D": 3, "E": 33, "F": 333, "G": 4, "H": 44, "I": 444, "J": 5, "K": 55, \
                    "L": 555, "M": 6, "N": 66, "O": 666, "P": 7, "Q": 77, "R": 777, "S": 7777, "T": 8, "U": 88, \
                    "V": 888, "W": 9, "X": 99, "Y": 999, "Z": 9999}
    code_numbers = input()
    # 443355555566696667775553
    dict_words = []
    count = int(input())
    for i in range(count):
        dict_words.append(input().upper())
    # long = 0
    # res = ""

    # for i in range(1, len(code_numbers) - 1):
    #     if code_numbers[i] == code_numbers[i - 1]:
    #         if long < 2 or (code_numbers[i] == "7" or code_numbers[i] == "9" and long < 3):
    #             long += 1
    #         else:
    #             res += dict_secret[int(code_numbers[i - 1]) - 2][long]
    #             print(1, res, int(code_numbers[i - 1]), long)
    #             long = 0
    #             res = ""
    #     else:
    #         res += dict_secret[int(code_numbers[i - 1]) - 2][long]
    #         print(2, res, int(code_numbers[i - 1]), long)
    #         long = 0
    #         res = ""

        #     print(dict_secret[int(code_numbers[i - 1]) - 2], long)
        #     if long < 3 or (code_numbers[i] == "7" or code_numbers[i] == "9" and long < 4):
        #         long += 1
        #     else:
        #         res += dict_secret[int(code_numbers[i - 1]) - 2][long]
        #         long = 0
        #         res = ""
        # else:
        #     res += dict_secret[int(code_numbers[i - 1]) - 2][long]
        #     long = 0
        #     res = ""
        # print(res)

        # if code_numbers[i] != code_numbers[i - 1] or \
        #         ((code_numbers[i] == "7" or code_numbers[i] == "9" and long > 3) or long <= 3):
        #     res += dict_secret[int(code_numbers[i - 1]) - 2][long]
        #     long = 0
        #
        # else:
        #     long += 1
        # print(res)
            # if code_numbers[i] == "7" or code_numbers[i] == "9":
            #     long += 1
            # elif long < 3:
            #     long += 1
            # else:
            #     res += dict_secret[int(code_numbers[i - 1]) - 2][long]
            #     long = 0
            #
            # print(res)
        # res = ""

    # dict_words = sorted(dict_words, key=lambda x: len(x), reverse=True)  # сортировка по длине чтобы убрать подстроки
    # выбирать слова удалением части строки для избежания повторов?
    # for word in dict_words:
    #     res = ""
    #     for ch in word:
    #         res += str(dict_secrets[ch])
    #     if res in code_words:
    #         print(word, end=" ")
    #         code_words = code_words[:code_words.index(res)] + code_words[code_words.index(res) + len(word):]

#Неправильное решение
code()


#https://coderun.yandex.ru/selections/quickstart/problems/gcd-and-lcm
