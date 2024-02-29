with open("C:/Users/syb29/OneDrive/Desktop/aoc.txt", "r") as file:
    lines = []

    # Iterate over the lines of the file
    for line in file:
        # Remove the newline character at the end of the line
        line = line.strip()

        # Append the line to the list
        lines.append(line)
print(lines)
li = []
mu = []
for i in lines:
    val=''
    for a in range(len(i)):
       if i[a].isdigit():
           val += i[a]
       else:
            for ind, va in enumerate(['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']):
                if i[a:].startswith(va):
                    val += str(ind+1)




    li.append(val)
    mu.append(val)
    print(li)





lin=[]

am = ''
bm = ''
for b in li:
    if len(b) >= 2:
        am = int(b[::len(b) - 1])
        lin.append(am)

    elif len(b) == 1:
        bm = int(b[0]+b[0])
        lin.append(bm)


print(lin)
total = sum(lin)
print(total)












