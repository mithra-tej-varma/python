lista = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
listb = ['1','2','3','4','5','6','7','8','9','0']
listc = ['!','@',"#","$","%","^","&","*",'>','<']
listd = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
print("PASSword generator:")
import random as rm
char = ''
up_char=int(input("How many uppercase do you want: "))
low_char=int(input("How many lowercase do you want: "))
digits=int(input("How many digits do you want: "))
special_characters=int(input("How many special characters do you want: "))
for i in range(up_char):
    n=rm.randint(0,25)
    char+=listd[n]
for i in range(low_char):
    n=rm.randint(0,25)
    char+=lista[n]
for i in range(special_characters):
    n=rm.randint(0,9)
    char+=listc[n]
for i in range(digits):
    n=rm.randint(0,9)
    char+=listb[n]
print(f"Your password is : {char}")