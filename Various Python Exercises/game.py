D = open("C:/Users/syb29/OneDrive/Desktop/game.txt").read().strip()
ans = 0
for line in D.split('\n'):
  game,parts= line.split(': ')
  _id=int(game.split(' ')[1])
  r,g,b = 0,0,0

  for part in parts.split('; '):
    for cubes in part.split(', '):
      num,color = cubes.split(' ')
      num=int(num)
      if color=='red':
        r=max(r,num)
      if color=='green':
        g=max(g,num)
      if color=='blue':
        b=max(b,num)
  ans+=r*g*b


print(ans)


  









