n = int(input('Enter a number: '))
count = 0
rev = ''
while n > 0:
    rem = n % 2
    n = n // 2
    rev = str(rem)+rev
    count = count + 1

print('The binary number is', rev)
