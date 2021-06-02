def factorial(n):
    number = 1
    for i in range(1, n + 1):
        number *= i
    return number


def find_probability(n, k):
    C = factorial(n) / (factorial(k) * factorial(n - k))
    return C


def find_stirling_number(k, n):
    s = 0
    for i in range(1, n + 1):
        s = (-1) ** (n-i) * find_probability(n, i) * i ** k
    return int(s / factorial(n))


def calc_bella_numbers(B):
    sum_s = 0
    for i in range(1, B + 1):
        sum_s += find_stirling_number(B, i)
    return sum_s


print('<----------------Стрилинг & Белл----------------->')
while True:
    answer = input('Число Стирлинга или Белл (с/в): ').lower()
    if answer == 'с':
        print('S(k,n)')
        answer1 = input('Число k: ')
        answer2 = input('Число n: ')

        if not answer1.isdigit() or not answer2.isdigit():
            continue
        print(find_stirling_number(int(answer1), int(answer2)))
    elif answer == 'в':
        print('B(n)')
        answer1 = input('Число n: ')

        if not answer1.isdigit():
            continue
        print(calc_bella_numbers(int(answer1)))
    else:
        print('Введите ’с’ или ’в’')
        continue
