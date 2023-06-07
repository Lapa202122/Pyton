
print(*[int(input()) for _ in range(int(input()))][::-1])






def rcr(a):
    res = [a[-1]]
    res += a[:n-1]
    return res
 
n = int(input('n = '))
lst = [x for x in input().split()]
print(*rcr(lst))








m = int(input())
n = int(input())
a =[]
for _ in range(n):
    a.append(int(input()))
    
print((2 * min(a) <= m) + len([x for x in a if x + min(a) > m]))