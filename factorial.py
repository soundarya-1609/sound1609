s,k=map(int,input().split())
for number in range(s+1,k):
   sums = 0
   temp = num
   while temp > 0:
       digit = temp % 10
       sums += digit ** 3
       temp //= 10
   if number == sum:
       print(number,end=' ')
