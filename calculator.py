def calculator(a, b, s):
    # a = float(input('a = '))
    # b = float(input('b = '))
    # s = input('Введите сивол:+,-,*,/')
    if s == '+':
        return a + b
    elif s == '-':
        return a - b
    elif s == '*':
        return a * b
    elif s == '/':
        if b == 0:
            return 'На ноль делить нельзя'
        else:
            return a / b
    else:
        return 'Неверный знак'

if __name__ == '__main__':
    calculator(3, 2, '*')