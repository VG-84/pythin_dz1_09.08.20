# DZ1-1
name = input('Как к вам можно обращаться?')
age = input('Ваш возраст')
print('Привет', name, 'Вам действительно', age, "лет?")

# DZ1-2
time = int(input('Введите количество секунд'))
hour = time / 3600
min = time / 60
print(hour, ':', min, ':', time)

# DZ1-3
time = (input('Введите чсло'))
sum1 = time
sum11 = int(sum1)
sum2 = time + time
sum22 = int(sum2)
sum3 = time + time + time
sum33 = int(sum3)
sum4 = int(sum11 + sum22 + sum33)
print(sum4)

# DZ1-4
a = 679
b = []
while a > 10:
    b.append(a % 10)
    a //= 10
c = max(b)
print(c)

# DZ1-5
while True:
    rev = input('Выручка')
    if rev.isdigit():
        rev = int(rev)
        break
    print('Введите число')
while True:
    cost = input('Издержки')
    if cost.isdigit():
        cost = int(cost)
        break
    print('Введите число')
result = rev - cost
if result > 0:
    index = rev / cost
    print(f'{result} — выручка больше издержек на {index}')
    while True:
        state = input('Численность сотрудников фирмы?')
        if state.isdigit():
            state = int(state)
            break
        print('Введите число')
        ind_state = result / state
        print(f'Прибыль фирмы в расчете на одного сотрудника {ind_state}')
elif result < 0:
    index = rev / cost
    print(f'{result} — издержки больше выручки')

# DZ1-6
while True:
    a = input('Результат')
    if a.isdigit():
        a = int(a)
        break
    else:
        print('Введите число')
while True:
    b = input('Результат на день')
    if b.isdigit():
        b = int(b)
        break
    else:
        print('Введите число')

day = 1
ind = a
while ind <= b:
    ind *= 1.1
    day += 1
print(day)

