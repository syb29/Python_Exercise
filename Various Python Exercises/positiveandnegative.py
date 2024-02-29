num_of_numbers = int(input('Enter number of numbers : '))
psum = 0
nsum = 0
count = 0

while count < num_of_numbers:
    n = int(input('Enter the number : '))

    if n > 0:
        psum = psum + n
    else:
        nsum = nsum + n
    count = count + 1
print('The sum of the positive numbers is', psum)
print('The sum of the negative numbers is', nsum)

