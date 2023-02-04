
#Q1
m=int(input("enter marks"))
if(m<25):
    print(" Grade F")
elif(m>=25 and m<45):
    print(" Grade E")
elif(m>=45 and m<50):
    print(" Grade D")
elif(m>=50 and m<60):
    print(" Grade C")
elif(m>=60 and m<80):
    print(" Grade B")
elif(m>=80):  
    print(" Grade A")

#Q2
year = int(input("Year = "))

if((year % 4 == 0 and year % 100 != 0) or year % 400 == 0):
	print(year, " is a leap year")
else:
	print(year, " is not a leap year")

#Q3
import random
import math

for i in range (1,11):
    num1 = random.randint(1,10)
    num2 = random.randint(1,10)
    print ("Question",i,":",num1,"*",num2,"=", end = " ")
    guess = int (input())
    answer = num1*num2
    if guess == answer:
        print ("Right!")
    else:
        print ("Wrong. The answer is: ",answer)


#Q4

for candy in range(200):
    if candy%5==2 and candy%6==3 and candy%7==2:
      print(candy)
