n = int(input())
if n > 0:
    if n % 2 == 0:
        print('Positive even number')
    else:
        print('Positive odd number')
elif n < 0:
    if n % 2 == 0:
        print('Negative even number')
    else:
        print('Negative odd number')
else:
    print('Zero number')





slovo = input('Enter the word : ')
if "a" in slovo or "e" in slovo or "i" in slovo or "o" in slovo or "u" in slovo:
 print ("a -", slovo.count('a'), "| e -", slovo.count('e'), "| i -", slovo.count('i'), "| o -", slovo.count('o'), "| u -", slovo.count('u'))
else:
 print ("Folse")




summa=int(input("Minimum investment amount - "))

maikl=int(input("How many dollars does Michael have - "))

ivan=int(input("How many dollars does Ivan have - "))

if (maikl>=summa) and (ivan>=summa):

 print(2)

elif (maikl>=summa) and (ivan<=summa):

 print("Mike")

elif (maikl<=summa) and (ivan>=summa):

 print("Ivan")

elif (maikl<=summa) and (ivan<=summa) and ((maikl+ivan)>=summa):

 print(1)

elif (maikl<=summa) and (ivan<=summa) and ((maikl+ivan)<=summa):

 print(0)