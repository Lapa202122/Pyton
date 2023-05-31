repeats = int(input('Enter the number of numbers: '))
count = 0
 
for i in range(repeats):
    num = int(input('Enter an integer: '))
    count += (lambda x: 1 if x == 0 else 0)(num)  
 
print(count)






x = int(input('x = '))

a=0

for b in range(1, x+1):

 if x%b==0:

  a=a+1

print(a)



a=int(input('a = '))

b=int(input('b = '))

for i in range(a, b + 1):

 if i % 2 == 0:

  print(i, end=' ')