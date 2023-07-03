
print(*[int(input()) for _ in range(int(input()))][::-1])






def rcr(a):
    res = [a[-1]]
    res += a[:n-1]
    return res
 
n = int(input('n = '))
lst = [x for x in input().split()]
print(*rcr(lst))







m, n, c = int(input()), int(input()), 0
t = sorted([int(input()) for _ in range(n)], reverse = True)
if t[0] > m:
  print('The problem has no solution')
  exit()
while len(t):
  c += 1
  k = m - t.pop(0)
  for i in range(len(t)):
    if t[i] <= k:
      t.pop(i)
      break
print(c)
