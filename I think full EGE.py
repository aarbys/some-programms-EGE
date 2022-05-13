
# 27задание список
# Прототип на мусорные баки и кольцевую дорогу.
f = open('')
n = int(f.readline())
a = [int(i) for i in f]
price = [0] * n
for i in range(1, n):
    price[0] += min(i, n - i) * a[i]
cen = n // 2
minus = sum(a[:cen])
plus = sum(a[cen + n % 2:])
for i in range(1, n):
    plus = plus + a[i - 1] - a[(cen + n % 2) % n]
    minus = minus - a[i - 1] + a[cen]
    price[i] = price[i - 1] + plus - minus
    cen = (cen + 1) % n
print(price.index(min(price)) + 1)


# Прототип на макс последовательность кратную 71.
f = open('')
N = int(f.readline())
maxsumm = 0
minlen = 122222222222222222222222
S = 0
ost_sum = [10000000000000000] * 71  # Массив с минимальными суммами, гле индекс равен остатку от деления на 71
ost_ind = [-1] * 71
ost_sum[0] = 0
for i in range(N):
    x = int(f.readline())
    S += x
    P = S % 71
    if S - ost_sum[P] > maxsumm:
        maxsumm = S - ost_sum[P]
        minlen = i - ost_ind[P]
    elif S - ost_sum[P] == maxsumm:
        minlen = min(minlen, i - ost_ind[P])
    elif S < ost_sum[P]:
        ost_sum[P] = S
        ost_ind[P] = i
print(minlen)
f.close()


# Прототип пути
f = open("")
n = int(f.readline())
t = int(f.readline())
S_a = 0
S_b = t
S_b1 = 0
S_b2 = 0
for i in range(n):
    c = f.readline().split()
    a = int(c[0])
    b = int(c[1])
    S_a += a
    S_b1 = S_b + b
    S_b2 = S_a + t
    S_b = min(S_b1, S_b2)
print(S_b)


# Некратная сумма
f = open('27_N_summa.txt')
n = int((f.readline()))
ch = nch = ch2 = nch2 = 0
for i in range(n):
    x = int(f.readline())
    if x % 2 != 0:
        if x > nch2:
            if nch < x:
                nch2 = nch
                nch = x
            else:
                nch2 = x

    else:
        if x > ch2:
            if x > ch:
                ch2 = ch
                ch = x
            else:
                ch2 = x
print(max(nch2 + nch, ch2 + ch))


# Буферный массив на кратность 15
f = open("")
N = int(f.readline())
a = [int(f.readline()) for i in range(4)]
R, m, m15, m5, m3 = 0, 0, 0, 0, 0
for i in range(N - 4):
    if a[0] > m15 and a[0] % 15 == 0:
        m15 = a[0]
    if a[0] > m5 and a[0] % 5 == 0:
        m5 = a[0]
    if a[0] > m3 and a[0] % 3 == 0:
        m3 = a[0]
    m = max(m, a[0])
    x = int(f.readline())
    p = x * m15
    if x % 15 == 0:
        p = max(p, x * m)
    elif x % 5 == 0:
        p = max(p, x * m3)
    elif x % 3 == 0:
        p = max(p, x * m5)
    a.remove(a[0])
    a.append(x)
    R = max(R, p)
print(R)
f.close()


# Количество пар чисел НЕ кратное 6.
f = open('')
k6 = k2 = k3 = 0
N = int(f.readline())
for i in range(N):
    a = int(f.readline())
    if a % 6 == 0:
        k6 += 1
    elif a % 2 == 0:
        k2 += 1
    elif a % 3 == 0:
        k3 += 1
print(((n * n - 1) / 2) - (k2 * k3 + k6 * (n - k6) + k6 * (k6 - 1) / 2))
f.close()


# Прототип на выбор из троек максимальной суммы не кратной 79
f = open('')
n = int(f.readline())
s = 0
m = 20 ** 10000
for i in range(n):
    p = f.readline().split()
    x1 = int(p[0])
    x2 = int(p[1])
    x3 = int(p[2])
    s += max(x1, x2, x3)
    if max(x1, x2, x3) == x1:
        d1 = x1 - min(x2, x3)
        d2 = x1 - max(x2, x3)
    elif max(x1, x2, x3) == x2:
        d1 = x2 - min(x1, x3)
        d2 = x2 - max(x1, x3)
    else:
        d1 = x3 - min(x1, x2)
        d2 = x3 - max(x1, x2)
    if d1 % 79 != 0:
        m = min(m, d1)
    if d2 % 79 != 0:
        m = min(m, d2)
if s % 79 == 0:
    s = s - m
print(s)
f.close()


# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# БЛОК 26ых ЗАДАНИЙ!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


# Задача про сис.Админа.
# https://inf-ege.sdamgia.ru/problem?id=27423
f = open('26_sys_admin.txt')
k = f.readline().split()
S = int(k[0])
N = int(k[1])
a = [int(f.readline()) for i in range(N)]
a.sort()
tsumma = 0
kolvo = 0
maxfile = 0
for i in range(N):
    if tsumma + a[i] <= S:
        tsumma += a[i]
        kolvo += 1
        maxfile = max(maxfile, a[i])
    else:
        if tsumma + a[i] - maxfile <= S:
            tsumma = tsumma + a[i] - maxfile
            maxfile = a[i]
print(kolvo, maxfile)


# Прототип на скидки!!!
# https://inf-ege.sdamgia.ru/problem?id=29674
f = open('26_skidka.txt')
n = int(f.readline())
a = []
s = 0
for i in range(n):
    x = int(f.readline())
if x <= 50:
    s += x
else:
    a.append(x)
a.sort()
mid = len(a) // 2
withD = a[:mid]
withoutD = a[mid:]
s = s + sum(withoutD) + sum(withD) * 0.75
print(s, withD[-1])


# Прототип на грузы.
# https://inf-ege.sdamgia.ru/problem?id=33198
f = open('26_gryz.txt')
k = f.readline().split()
N = int(k[0])
M = int(k[1])
a = []
maxves = tsumma = kolvo = 0
for i in range(N):
    x = int(f.readline())
    if x >= 200 and x <= 210 and x + tsumma <= M:
        tsumma += x
        kolvo += 1
        maxves = max(maxves, x)
    else:
        a.append(x)
a.sort()
for i in range(len(a)):
    if a[i] + tsumma <= M:
        tsumma += a[i]
        kolvo += 1
        maxves = max(maxves, a[i])
    elif tsumma - a[i - 1] + a[i] <= M:
        tsumma += a[i] - a[i - 1]
        maxves = max(maxves, a[i])
print(kolvo, tsumma)
f.close()


# Задание на детали
# https://inf-ege.sdamgia.ru/problem?id=33771
f = open('26_details.txt')
str1 = f.readline().split()
N, M = int(str1[0]), int(str1[1])
a, b = [], []
for i in range(N):
    x = f.readline().split()
    x[0] = int(x[0])
    x[1] = int(x[1])
    if x[2] == 'B':
        b.append(x)
    else:
        a.append(x)
b.sort()
a.sort()
tsumma, kolvoa = 0, 0
for i in range(len(b)):
    if b[i][0] * b[i][1] + tsumma <= M:
        tsumma += b[i][0] * b[i][1]
    elif b[i][0] * b[i][1] + tsumma > M:
        for j in range(b[i][1] - 1, 0, -1):
            if b[i][0] * (b[i][1] - j) + tsumma <= M:
                tsumma = tsumma + (b[i][0] * (b[i][1] - j))
for i in range(len(a)):
    if a[i][0] * a[i][1] + tsumma <= M:
        tsumma += a[i][0] * a[i][1]
        kolvoa += a[i][1]
    elif a[i][0] * a[i][1] + tsumma > M:
        for j in range(a[i][1] - 1, 0, -1):
            if a[i][0] * j + tsumma <= M:
                kolvoa = kolvoa + j
                tsumma = tsumma + a[i][0] * j
                break
print(kolvoa, M - tsumma)
f.close()


# Прототип на места в кинотеатрах. Я предпочитаю решать в excel
# https://inf-ege.sdamgia.ru/problem?id=37161
f = open('26_kinoteatr.txt')
n = int(f.readline())
maxr, mesto, bileti = 0, 22 ** 2222, []
for i in range(n):
    k = f.readline().split()
    k[0] = int(k[0])
    k[1] = int(k[1])
    bileti.append(k)
bileti.sort()
ryad = 0
for i in range(n - 1):
    if bileti[i][0] != ryad:
        if bileti[i][0] != bileti[i + 1][0]:
            continue
        else:
            if bileti[i + 1][1] - bileti[i][1] - 1 == 2:
                maxr = max(maxr, bileti[i][0])
                mesto = bileti[i][1] + 1
                ryad = bileti[i][0]
print(maxr, mesto)
f.close()


# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# БЛОК 25ых ЗАДАНИЙ!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


# 25 задачи однотипны все, даже коды толком, будет 2 варианта всего
# https://inf-ege.sdamgia.ru/problem?id=27422
for i in range(174457, 174505 + 1):
    a = []
    for j in range(2, i // 2 + 1):
        if i % j == 0 and len(a) < 2:
            a.append(j)
        elif i % j == 0 and len(a) >= 2:
            a.append(11)
            break
    if len(a) == 2:
        print(*a)

# https://inf-ege.sdamgia.ru/problem?id=36038
k = 0
i = 452021 + 1
while k != 5:
    a = []
    for j in range(2, i // 2 + 1):
        if i % j == 0:
            a.append(j)
    if len(a) >= 2:
        M = a[0] + a[-1]
    if M % 7 == 3:
        print(i, M)
        k += 1
    i += 1


# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# БЛОК 24ых ЗАДАНИЙ!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


# Максимальная длина, где символ i =/=  символ i+1
# https://inf-ege.sdamgia.ru/problem?id=27421
f = open('24_easy.txt').readline()
maxlen = 1
tl = 1
for i in range(len(f) - 1):
    if f[i] != f[i + 1]:
        tl += 1
        maxlen = max(maxlen, tl)
    else:
        maxlen = max(maxlen, tl)
        tl = 1
print(maxlen)
f.close()


# Макс длина последовательности, состоящей из символов X
# https://inf-ege.sdamgia.ru/problem?id=27686
f = open('24_symbolX.txt').readline()
f = f.replace('Y', '*')
f = f.replace('Z', '*')
f = f.split('*')
print(len(max(f)))


# Прототип на несколько строк
# https://inf-ege.sdamgia.ru/problem?id=29672
f = open('24_a_lot_of_strings.txt')
kolvo_strok = 0
for i in f:
    if i.count('E') > i.count('A'):
        kolvo_strok += 1
print(kolvo_strok)
f.close()


# Подсёт самой популярной буквы после А
# https://inf-ege.sdamgia.ru/problem?id=33196
f = open('24_after_A.txt').readline()
massiv = [0] * 26
for i in range(len(f) - 1):
    if f[i] == 'A':
        massiv[ord(f[i + 1]) - 65] += 1
print(chr(massiv.index(max(massiv)) + 65))
#Примичание 65 потому что буква A по таблице UTF имеет номер 65
#А каждая следующая буква алфавита на 1 больше предыдушей


# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# БЛОК 23их ЗАДАНИЙ!!!!!
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


# Блок заданий самый простой, на моё мнение. Тут 1 вариант, но есть небольшое разнообразие, я его напишу.
# Так что я даже расписывать не буду ничего, просто укажу ссылки на задачи.
# https://inf-ege.sdamgia.ru/problem?id=11358
def f(c, e):
    if c == e:
        return 1
    elif c > e:
        return 0
    else:
        return f(c + 1, e) + f(c + 2, e) + f(c * 2, e)


print(f(3, 10) * f(10, 12))


# https://inf-ege.sdamgia.ru/problem?id=13418
def f(c, e):
    if c == e:
        return 1
    elif c > e or c == 26:
        return 0
    else:
        return f(c + 1, e) + f(c * 2 + 1, e)


print(f(1, 27))


# https://inf-ege.sdamgia.ru/problem?id=15117
def f(c, e):
    if c == e:
        return 1
    elif c > e or c == 15:
        return 0
    else:
        return f(c + 1, e) + f(c + 2, e)


print(f(3, 9) * f(9, 20))


# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# БЛОК Теория игр!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


# Я рекомендую не учить код а понять его.
# https://www.youtube.com/watch?v=bPuqNdSm3nM
# Вот, например, видео, в нём объяснение подробно этого кода.
# Я напишу с другими данными, адаптированными под задание


# https://inf-ege.sdamgia.ru/problem?id=27765
# https://inf-ege.sdamgia.ru/problem?id=27766
# https://inf-ege.sdamgia.ru/problem?id=27767


from functools import lru_cache


def moves(S):
    a, b = S
    return (a + 1, b), (a * 2, b), (a, b + 1), (a, b * 3)


@lru_cache(None)
def game(S):
    if sum(S) >= 69:
        return 'END'
    elif any(game(x) == 'END' for x in moves(S)):
        return 'Петя1'
    elif all(game(x) == 'Петя1' for x in moves(S)):
        return 'Ваня1'
    elif any(game(x) == 'Ваня1' for x in moves(S)):
        return 'Петя2'
    elif all(game(x) == 'Петя1' or game(x) == 'Петя2' for x in moves(S)):
        return 'Ваня2'
    elif any(game(x) == 'Петя1' for x in moves(S)):
        return 'Ваня1 После неуд.Хода пети'


for i in range(1, 59):
    S = 10, i
    print(i, game(S))


# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# БЛОК 17ых заданий!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


#Я напишу для парочки заданий код, которые мне покажутся наиболее интересными, остальное просить у Андрея

# https://inf-ege.sdamgia.ru/problem?id=37336
# Количество пар чисел, где хотя бы 1 из них кратно 3ем, и максимальная сумма. Пара - подряд идущие
f = open('17_1_iz_kr3.txt')
maxpara = -100000000000
kolvopar = 0
a = [int(i) for i in f]
for i in range(len(a) - 1):
    if (a[i] % 3 == 0) or (a[i + 1] % 3 == 0):
        kolvopar += 1
        maxpara = max(maxpara, a[i] + a[i + 1])
print(kolvopar,maxpara)
f.close()


#https://inf-ege.sdamgia.ru/problem?id=37337
# Количество пар, где остаток от деления на 160 различен и хотя бы 1 делится на 7.
# А затем максимальная сумма таких элементов
f = open('17_big.txt')
maxpar = -1000
kolvo = 0
a = [int(i) for i in f]
for i in range(len(a) - 1):
    for j in range(i + 1, len(a)):
        if ((a[i] % 160) != (a[j] % 160)) and ((a[i] % 7 == 0) or a[j] % 7 == 0):
            kolvo += 1
            maxpar = max(maxpar, a[j] + a[i])
print(kolvo, maxpar)
f.close()


# Задача из модуля MAXIMUM(Прекрасный центр)
# Весь текст задачи скопирую.
# В файле содержится последовательность целых чисел.
# Элементы последовательности могут принимать целые значения от –10 000 до 10 000 включительно.
# Определите количество пар последовательности, в которых хотя бы одно число кратно 7.
# А абсолютная разница элементов пары больше максимального элемента последовательности, кратного 7.
# Также укажите минимальную из сумм элементов таких пар.
# В ответе запиши количество пар, удовлетворяющих условию, и минимальную из сумм элементов таких пар.
# В данной задаче под парой подразумевается два идущих подряд элемента последовательности.
f = open('17_full.txt')
a = [int(i) for i in f]
maxkr7 = -1000000000
for i in range(len(a)):
    if a[i] % 7 == 0:
        maxkr7 = max(maxkr7, a[i])
k = 0
ms = 1000000000000000000
for i in range(len(a)-1):
    if (((a[i]%7==0) or (a[i+1]%7==0)) and (abs(a[i]-a[i+1])>maxkr7)):
        k+=1
        ms=min(a[i]+a[i+1],ms)
print(k,ms)
f.close()


# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# БЛОК 15ых заданий!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


# https://inf-ege.sdamgia.ru/problem?id=9804
# (x & 29 ≠ 0 → (x & 17 = 0 → x & А ≠ 0)) == 1
# Наименьшее, поэтому break будет в последнем if'e, вдь мы идём от 0 -> 9999
for A in range(10000):
    flag = True
    for x in range(10000):
        if ((x & 29 != 0) <= ((x & 17 == 0) <= (x & A != 0))) == 0:
            flag = False
            break
    if flag:
        print(A)
        break


# https://inf-ege.sdamgia.ru/problem?id=13745
# ((x ≤ 9) →(x ⋅ x ≤ A)) ⋀ ((y ⋅ y ≤ A) → (y ≤ 9))
for A in range(10000):
    flag = True
    for x in range(1000):
        for y in range(1000):
            if (((x <= 9) <= (x * x <= A)) and ((y * y <= A) <= (y <= 9))) == 0:
                flag = False
                break
        if not (flag):
            break
    if flag:
        print(A)


# https://inf-ege.sdamgia.ru/problem?id=8106
# ¬ДЕЛ(x, А) → (ДЕЛ(x, 6) → ¬ДЕЛ(x, 4))
for A in range(1, 10000):
    flag = True
    for x in range(1000):
        if (((x % A) != 0) <= (((x % 6) == 0) <= ((x % 4) != 0))) == 0:
            flag = False
            break
    if flag:
        print(A)


# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# БЛОК 14ых заданий!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


# https://inf-ege.sdamgia.ru/problem?id=7761
# Счётчик количества цифр 1 в двоичной записи
x = 4 ** 2020 + 2 ** 2017 - 15
k = 0
while x > 0:
    if x % 2 == 0:
        k += 1
    x = x // 2
print(k)


# https://inf-ege.sdamgia.ru/problem?id=2302
# Число 18 записали в системе счистления X, получилось 30. Какая СС?
x = 18
a=[3,0]
for i in range(2, 10):
    s = x
    b = []
    while s > 0:
        b.append(s % i)
        s = s//i
    b.reverse()
    if b == a:
        print(i)
        break


# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# БЛОК 2ых заданий!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


# https://inf-ege.sdamgia.ru/problem?id=17320
# ((x ∧ y) ∨ (y ∧ z)) ≡ ((x → w) ∧ (w → z)).
print('x,y,z,w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if ((x and y) or (y and z)) == ((x <= w) and (w <= z)):
                    print(x, y, z, w)
