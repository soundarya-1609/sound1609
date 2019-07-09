#mano
from itertools import combinations
sound,t=input().split()
t=int(t)
top=[]
van=len(sound)-t
fake=combinations(sound,van)
for i in list(fake):
  top.append("".join(i))
print(min(top))
