# Q 1
a=input("Enter a string to be reversed:")
print(a[-1::-1])

# Q 2

a=int(input("Enter the lower bound of the range:"))
b=int(input("Enter the upper bound of the range:"))
c=int(input("Enter the number to divisible with:"))
for i in range (a,b):
    if i%c==0:
        if i!=0:   #creating a fail safe for zero
            print(i, end=" ")
        else:
            continue

# Q 3

from math import sqrt
a=int(input("Enter the first side of the triangle:"))
b=int(input("Enter the second side of the triangle:"))
c=int(input("Enter the third side of the triangle:"))
#checking the validity of the triangle
if a<=b+c and b<=a+c and c<=a+b:
    print("Triangle is possible")
else:
    print("The Triangle is not possible")
    exit()
#finding semiparameter
s=(a+b+c)/2
# finding the area of the triangle using herons formula
area=sqrt(s*(s-a)*(s-b)*(s-c))
print("The area of the triangle by using herons formula is",area)

# Q 4

a=int(input("Enter the number of rows:"))
i=0
for i in range (0,a):
    for j in range (0,i+1):
        print("* ", end="")
    print("\r")
for i in range (a,0,-1):
    for j in range (i+1,0,-1):
        print("* ", end="")
    print("\r")

# Q 5

#we will procede with the ascii approach
#as we know ascii of A is 65 and ascii of Z in 90
ascii_no=65
a=int(input("Enter the number of rows:"))
for i in range (0,a):
    for j in range(0,i+1):
        print(chr(ascii_no),end="")
        if ascii_no<90:
            ascii_no +=1
        else:
            ascii_no=65
    print("\r")

# Q 6

a=int(input("Enter the lower bound of the range:"))
b=int(input("Enter the upper bound for the range:"))

for number in range(a,b+1):
    if number>1:
        for i in range (2,number):
            if number%i==0:
                break
        else:
            print(number)

# Q 7

for i in range (1,500):
    if i%7==0:
        if i%11==0:
            print(i)

# Q 8

i = 0
list_1 = []
while i < 10:
    a = int((input("Enter a number:")))
    list_1.append(a)
    i += 1

print("Question A----")
for i in list_1:
    if i < 0:
        continue
    if i > 0:
        print(i, end=" , ")
print("These are Positive numbers in the input numbers")
print("\r")

print("Question B----")
for i in list_1:
    if i > 0:
        continue
    if i < 0:
        print(i, end=" , ")
print("These are Negative numbers in the input numbers")
print("\r")

list_even = []
list_odd = []
for i in list_1:
    if i % 2 == 0:
        list_even.append(i)
    else:
        list_odd.append(i)
print("Question C----")
print("Odd numbers in the input numbers are", list_odd)
print("\r")
print("Question D----")
print("Even numbers in the input numbers are", list_even)
print("\r")
print("Question E----")
dic_1 = {}
for i in list_1:
    dic_1.update({i: list_1.count(i)})
print("The number of occurances of any number are", dic_1)

# Q9

a=input("Input the string:")

dict_1= dict()
Split_txt = str.split(a)

for t in Split_txt:
	if t in dict_1:
		dict_1[t] += 1
	else:
		dict_1[t] = 1

print(dict_1)