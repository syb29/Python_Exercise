D = open("C:/Users/syb29/OneDrive/Desktop/parts.txt").read().strip()

lines=len(D.split('\n'))
for l in range(lines):
    for line in D.split('\n'):
       for index,element in enumerate(line):
           print(index,element)
           if element.isdigit() and element in ''









