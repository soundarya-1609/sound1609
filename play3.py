n = int(input())
nums = list(map(int,input().split()))
temps = []
for i in range(n):
    if nums[i] == i:
        temps.append(nums[i])
if len(temps) == 0:
    print(-1)
else:
    for i in sorted(temps):
        print(i,end=' ')
