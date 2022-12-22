#Q1

name = 'Python is a case sensitive language'
#a
print(len('name'))

#b
print("name"[::-1])

#c
print(name[4:12])

#d
newname=name.replace("a case sensitive" , "object oriented")
print(newname)

#e 
j=name.index("h")
print('c')

#f
t=name.replace(" ","")
print(t)
t1=newname.replace(" ","")
print(t1)

#Q2

p= "Vinayak Pandey"
q= "22104012"
r= "Electrical"
s= "9.9"
print(f" Hey, {p} Here!\n",f"My SID is:{q}\n",f"I am from {r} department and my CGPA is {s}")


#Q3

a = 56
b = 10

#for 'a & b'
print("a & b =", a & b)

#for 'a | b'
print("a | b =", a | b)

#for 'a ^ b'
print("a ^ b =", a ^ b)

#for left shift
l=a<<2
m=b<<2
print(l,bin(l))
print(m,bin(m))

#for right shift
n=a>>2
o=b>>4
print(n,bin(n))
print(o,bin(o))

#Q4

i = int(input('enter first no:\n'))
j = int(input('enter second no:\n'))
k = int(input('enter third no:\n'))

if j>k:
    if i>j:
        print(i)
    else:
        print(j)
else:
    if i>k:
        print(i)
    else:
        print(k)

#Q5

v= str(input('enter string:'))
if "name" in v: 
    print("yes")
else:
    print("no")

#Q6

x = int(input("enter first side;\n"))
y = int(input("enter second side:\n"))
z = int(input("enter third side:\n"))
d = x+y
e = y+z
f = x+z
if d<z or e<x or f<y:
    print('no')
else:
    print('yes')


