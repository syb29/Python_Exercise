text = input('Enter a sentence : ')
print(text[::-1])
num_of_numbers = int(input('Enter number of numbers: '))
count = 0
max = int(input('Enter a number: '))
while count < num_of_numbers-1:
    number = int(input('Enter a number: '))
    if number > max:
        max = number
    count = count + 1
print('The max number is', max)


