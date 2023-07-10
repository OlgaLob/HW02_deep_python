# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. Программа должна
# возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.

import fractions


def gcd(x, y):
    if x > y:
        tmp = y
    else:
        tmp = x
    for i in range(1, tmp + 1):
        if x % i == 0 and y % i == 0:
            gcd = i
    return gcd


fr1 = input('Введите первую дробь: ')
fr2 = input('Введите вторую дробь: ')

numerator1 = int(fr1[0])
denominator1 = int(fr1[2])

numerator2 = int(fr2[0])
denominator2 = int(fr2[2])

numerator_sum = numerator1 * denominator2 + numerator2 * denominator1
denominator_sum = denominator1 * denominator2
gcd_sum = gcd(numerator_sum, denominator_sum)


numerator_mult = numerator1 * numerator2
denominator_mult = denominator1 * denominator2
gcd_mult = gcd(numerator_mult, denominator_mult)

f1 = fractions.Fraction(numerator1, denominator1)
f2 = fractions.Fraction(numerator2, denominator2)

print(f'Произведение дробей {fr1} и {fr2} равно {int(numerator_mult / gcd_mult)}/{int(denominator_mult / gcd_mult)}')
print(f'Произведение дробей {fr1} и {fr2} с применением модуля "fractions" равно {f1 * f2}')
print(f'Сумма дробей {fr1} и {fr2} равна {int(numerator_sum / gcd_sum)}/{int(denominator_sum / gcd_sum)}')
print(f'Сумма дробей {fr1} и {fr2} с применением модуля "fractions" равна {f1+f2}')
