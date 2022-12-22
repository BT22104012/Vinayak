#Q1

num1=int(input("first number"))
num2=int(input("second number"))
num3=int(input("third number"))
average=(num1+num2+num3)/3 
print('the average of numbers {0}, {1}, {2} is {3}'.format(num1,num2,num3, average)) 

#Q2

gross_income=int(input('enter your income'))
standard_deduction = 10000
dependent_deduction = 3000
tax_rate = 0.2
dependent = int (input('enter the number of dependents'))
tax_income = gross_income - standard_deduction - (dependent_deduction*dependent)
tax = tax_income*tax_rate
print('The income tax of person is', tax)

#Q3

num1=int(input("enter no. of seconds"))
minutes=num1//60
seconds=num1%60
print("no. of minutes:", minutes , "no. of seconds:" , seconds)

#Q4

num1=int(25)
num2=int('25')
num3=int(25.0)
sum=num1+num2+num3
print(sum)

#Q5

from math import *
for i in range(0, 360, 15):
    print(i, '---', round(sin(i), 4), round(cos(i),4))