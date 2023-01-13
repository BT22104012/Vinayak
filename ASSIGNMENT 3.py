#Q1 
string=str(input("Enter the string:"))
words = string.split() if "" in string else list(string)
counts = ()
for word in words:
    if word in counts:
        counts[word] +=1
    else:
        counts[word] = 1

print(counts)      

#Q2
import datetime
year = int(input("enter the year:"))
month = int(input("enter the month :"))
day = int(input("enter the day =:"))
if not (1 <=month <=12) or not (1 <= day <= 31) or not (1800<= year <=2025):
    print("invalid input date")
else : 
    input_date =datetime.datetime(year,month,day)
    next_date = input_date + datetime.timedelta(days=1)
    print("next date:", next_date.strftime("%Y-%m-%d"))
    

#Q3 . 
list1=list(map(int,input("Enter the numbers separated by space:").split()))
list2=[]
for e in list1:
    t=(e,e*e)
    list2.append(t)
print("\nList containing (n,n^2) is shown below:")
print(list2)



#Q4 


grade_point=int(input("Enter grade points:"))
dic={10:"Your grade is 'A+' and Outstanding performance.",
     9:"Your grade is 'A' and Excellent performance.",
     8:"Your grade is 'B+' and Very Good performance.",
     7:"Your grade is 'B' and Good performance.",
     6:"Your grade is 'C+' and Average performance.",
     5:"Your grade is 'C' and Below Average performance.",
     4:"Your grade is 'D' and Poor performance."}
#Applying Conditions for correct grade range
if 4<=grade_point<=10:
        statement=dic.get(grade_point)
        print(statement)
else:
       print("\nError\nPlease enter grade in range [4,10]")
       



#Q5 

string = "ABCDEFGHIJK"
j = 0
while len(string)-j*2 >= 1:
    print(" "*j, string[0 : len(string) - j*2])
    j += 1



#Q6 

repeat="Y"
dic={}
dic2={}
#List containing Y or N
liste=["Y","y","n","N"]
while repeat=="Y" or repeat=="y":
    
    name = str(input("Enter student name:"))
    sid = int(input("Enter student SID:"))
    if sid<0:
        print("\nError\nSID can't be negative\n")
    else:
       
        dic.update({sid: name})
        
        dic2.update({name:sid})
       
        repeat = str(input("Enter Y to continue or N to end:"))
    if repeat=="N" or repeat=="n":
        break
    elif (not (repeat in liste)):
        print("\nError\nPlease enter valid input['Y' or 'N']")
        repeat=str(input("\nEnter Y to continue or N to end:"))
print("\nQ.6(a)")
print("The Dictionary containing {'SID':'Name'} is shown below")
print(dic)
print("\nQ.6(b)")
list_k=sorted(dic2)
dic3={}
for ele in list_k:
    dic3.update({dic2.get(ele):ele})
print("The Dictionary after sorting according to name:")
print(dic3)

# c
#sorting according to SID
print("\nQ.6(c)")
sort_dic = sorted(dic)
dic4 = {}
for va in sort_dic:
    dic4.update({va: dic.get(va)})
print("The Dictionary after sorting according to SID:")
print(dic4)
# d
print("\nQ.6(d)")
# Taking input SID to be searched
enter_sid = int(input("Enter SID to get name of student:"))
# Searching for sid as key in dic
output_name = str(dic.get(enter_sid))
# printing name with key sid
print(f"Name of student with SID {enter_sid} is {output_name}.")





#Q7 Write a python program to print Fibonacci sequence also print average of the resultant Fibonacci series.

print("\nQuestion 7")

#input from user
n=int(input("Enter number of elements N in fibonacci series:\n[N must be positive Integer]: N="))
#printing error message when N<=0
if n<=0 :
    print("\nError\nNumber of elements in fibonacci series must be integer and greater than zero.")
#code for fibonacci series
else:
    #code for fibonacci series for first 2 elements
    if n == 1:
        print("\nThe fibonacci series with 1 element is shown below\n[1]")
        print("\nAverage of given fibonacci series is", 1)

    elif n == 2:
        print("\nThe fibonacci series with 2 element is shown below\n[1,1]")
        print("\nAverage of given fibonacci series is", 1)
    #General code for fibonacci for next N-2 elements
    else:
        # List of fibonacci elements with 1,1 as initial elements
        list1 = [1, 1]
        #Building logic to get fibonacci series
        a = 1
        b = 1
        # For loop
        for i in range(n - 2):
            s = a + b
            list1.append(s)
            a = b
            b = s
        # printing the final fibonacci series
        print(f"\nThe fibonacci series with {n} elements is shown below:")
        print(list1)
        # Finding average of fibonacci series
        sum = 0    #intial sum=0
        # finding sum of all elements in list1
        for num in list1:
            sum = sum + num
        average = (sum / n)
        # Till two decimal place
        two_decimal = "{:.2f}".format(average)
        # printing average
        print(f"\nAverage of given fibonacci series is {two_decimal}")



#Q8 Given the sets below, write python statement to:

        
print("\nQuestion 7")

#Given Sets
set1= {1, 2, 3, 4, 5}
set2= {2, 4, 6, 8}
set3= {1, 5, 9, 13, 17}
#printing the given sets
print(f"Set1= {set1}\nSet2= {set2}\nSet3= {set3}")
#a
print("\nQ.8(a)")
print("\nA new Set of all 'elements that are in Set1 and Set2 but not both' is:")
set_sym_dif=set1.symmetric_difference(set2)
print(set_sym_dif)
#b
#set1 Union set2
print("\nQ.8(b)")
print("\nA new set of all elements that are 'in only one of the three sets Set1,Set2 and Set3' is:")
set_u1=set1.union(set2)

#set1 Union set2 Union set3
set_uf=set_u1.union(set3)

#set1 intersection set2
set_i1=set1.intersection(set2)

#set1 intersection set2 intersection set3
set_if=set_i1.intersection(set3)

#set1 intersection set2
set_12=set1.intersection(set2)

#set2 intersection set3
set_23=set2.intersection(set3)

#set3 intersection set1
set_13=set1.intersection(set3)

#final required set
set_f1=set_uf-set_12-set_23-set_13
print(set_f1)
#c
print("\nQ.8(c)")
set_c1=set_12.union(set_23)
set_c2=set_c1.union(set_13)
set_final=set_c2-set_if
print("\nA new set of elements that are 'exactly in two of the sets Set1, Set2 and Set3' is:")
print(set_final)
#d
#forming a set containing values from 1 to 10
print("\nQ.8(d)")
set_d={1,2}
set_d.clear()
for i in range(1,11):
    set_d.add(i)
set_new=set_d-set1
#printing final set
print("\nA new set of all Integers in the 'range 1 to 10' that are 'not in Set1' is:")
print(set_new)
#e
print("\nQ.8(e)")
set_e=set_d-set_uf
print("\nA new set of all Integers in the range 1 to 10 that are not in Set1,Set2 and Set3.")
print(set_e)
