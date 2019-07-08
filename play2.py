no = int(input())
nums = sorted(input().split(), reverse=True)
temps = ''
for i in nums:
    temps+= i
print(int(temps))
