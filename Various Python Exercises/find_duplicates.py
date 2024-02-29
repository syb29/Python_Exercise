li = ['a', 'b', 'c', 'd', 'b', 'a']
counter = []
for alpha in li:

    if li.count(alpha) > 1:
        if alpha not in counter:
            counter.append(alpha)
print(counter)



