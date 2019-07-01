number=int(input())
sume=0
temp=number
while temp>0:
   digit=temp%10
   sume += digit**3
   temp//=10
if number==sume:
   print("yes")
else:
   print("no")
