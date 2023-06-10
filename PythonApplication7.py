
n=int(input("Enter the number of list items: "))

spisok = list(map(int, input().split()))[:n]

e=set(spisok)

print(len(e))




a=set(input().split())

b=set(input().split())

print (len(a.intersection(b)))



used = set()
for i in input().split():
    n = int(i)
    if n in used:
        print('YES')
    else:
        print('NO')
        used.add(n)