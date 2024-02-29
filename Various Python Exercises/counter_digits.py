# from typing import Union, Any

number = int(input('Please input a number: '))
m = number
counter = 0
addition = 0
rev = 0
while number > 0:
    r = number % 10
    number = number//10
    addition = addition + r
    rev = rev * 10 + r
    counter += 1
if m == rev:
    print('The number is palindrome')
else:
    print('The number is not palindrome')

print('The number of digits are ', counter)
print('The sum of the digit is ', addition)
print('Reversed number is ', rev)


