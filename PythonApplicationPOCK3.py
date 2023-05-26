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




slovo = input('Enter the word: ')

eg=slovo.count('e') 

ag=slovo.count('a') 

ig=slovo.count('i') 

ug=slovo.count('u') 

og=slovo.count('o') 

schetglas=eg+ag+ig+ug+og 

print("Total vowels",schetglas) 

print("Total consonants",len(slovo)-schetglas)  

if (eg==0):

 print ("The vowel e in the word False")

else:

 print("e=",eg)

if (ug==0):

 print ("The vowel u in the word False")

else:

 print("u=",ug)

if (og==0):

 print ("The vowel o in the word False")

else:

 print("o=",og)

if (ag==0):

 print ("The vowel a in the word False")

else:

 print("a=",ag)

if (ig==0):

 print ("The vowel i in the word False")

else:

 print("i=",ig)




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