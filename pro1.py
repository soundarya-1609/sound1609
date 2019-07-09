santhosh = int(input())
dafney=[]
for i in range(0,santhosh):
 lan=input()
 dafney.append(lan)
thissss=[]
for i in zip(*dafney):
 if(i.count(i[0])==len(i)):
  thissss.append(i[0])
 
 else:
  break
print(''.join(thissss))
