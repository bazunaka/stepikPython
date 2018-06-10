'''Паша очень любит кататься на общественном транспорте, а получая билет, сразу
проверяет, счастливый ли ему попался. Билет считается счастливым, если сумма
первых трех цифр совпадает с суммой последних трех цифр номера билета.

Однако Паша очень плохо считает в уме, поэтому попросил вас написать программу,
которая проверит равенство сумм и выведет "Счастливый", если суммы совпадают, и
"Обычный", если суммы различны.

На вход программе подаётся строка из шести цифр.

Выводить нужно только слово "Счастливый" или "Обычный", с большой буквы.'''

a = int(input())
left, right = a//1000, a%1000
L1, L2, L3 = left//100, left%100//10, left%10
r1, r2, r3 = right//100, right%100//10, right%10

if L1+L2+L3 == r1+r2+r3:
    print("Счастливый")
else:
    print("Обычный")
