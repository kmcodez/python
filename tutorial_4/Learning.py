# Sample Calculation
"""
a=25
b=25
c=a+b
print("total :",c)
type(a)
a=45
print(type(a))
print(id(a))
print(id(b))
"""

# keywords
"""
import keyword
print(keyword.kwlist)
"""

# Getting string input statement
"""
name=input("Enter Name: ")
print(type(name))
print(name)
"""

# Getting integer input statement
"""
a=input("Enter The Value of A : ")
b=input("Enter The Value of B : ")
c=a+b
print(c)
"""

"""
a=int(input("Enter The Value of A : "))
b=int(input("Enter The Value of B : "))
c=a+b
print(c)
print(type(a))
print(type(b))
print(type(c))
"""

# Getting Float input statement
"""
a=float(input("Enter The Value of A : "))
b=float(input("Enter The Value of B : "))
c=a+b
print(c)
print(type(a))
print(type(b))
print(type(c))
"""

# Multiple Values in Single line
# Split option
"""
name1,name2,name3=input("Enter 3 Names : ").split()
print("Name 1 : ",name1)
print("Name 2 : ",name2)
print("Name 3 : ",name3)
"""
# Split with comma
"""
name1,name2,name3=input("Enter 3 Names : ").split(',')
print("Name 1 : ",name1)
print("Name 2 : ",name2)
print("Name 3 : ",name3)
"""

# Multiple line string input
"""
a= " Bhagwan Das Jangade, who held a position as general manager
 of National Highways and Infrastructure Development Corporation Ltd, 
 has been booked under the Prevention of Corruption Act"
print(type(a))
print(a)
"""

# List object
"""
para=[]
print(type(para))
"""

# List objects integers type
"""
para=[25,50,90]
print(para[0])
print(para[1])
print(para[2])
"""

# List objects join type
"""
para=["kumar","kavi","kiruthik"]
print('|'.join(para))
"""

# List objects
"""
para=[]
print("Enter a Para : ")

while True:
    line=input()
    if line:
        para.append(line)
    else:
        break
print(para)
output='\n'.join(para)
print(output)
"""

# Type Casting
"""
a = 10
print(a)
print(type(a))
"""
# Giving a value, it gives class type as int
# change a = 10 as a = 10.0, now
"""
a = 10.0
print(a)
print(type(a))
#now it shows class as float
#now how to change as float to int
b=int(a)
print(b)
print(type(b))
#now change float to int
"""
# Type casting
"""
a = input("Enter The Value of A : ")
b = input("Enter The Value of B : ")
c = a+b
print("Total : " + c)
"""
#this method only gives result of adding number as 2550
#because this is string
#so how convert string to int
"""
a = int(input("Enter The Value of A : "))
b = int(input("Enter The Value of B : "))
c = a+b
print("Total : " , c)
#now good but still using + instead of comma shows as conceate error
"""
# Another method of above formula
"""
a = int(input("Enter The Value of A : "))
b = int(input("Enter The Value of B : "))
c = a+b
print("Total : " + str(c))
"""

"""
# String and String Function
s = "kiruthik Varshan"
print(s)
print(type(s))
# now how to change all the letters to upper case
print(s.upper())
# now how to change all the letters to smaller case
print(s.lower())
# now change to capitalize the first letter for sentence
print(s.capitalize())
# now change to capitalize the first letter for every word
print(s.title())
# calculate how many letter or particular word
print(s.count("i"))
# check the finishing letter or word
print(s.endswith("n"))
# find the index whether place
print(s.find("r"))
# find the index whether place multiple letter
print(s.find("r", 3))
# replace the particular letter wholr paragraph
print(s.replace("r", "5"))
# check all the lettera are upper or lower
a = "kavi1234"
print(a.isupper())
print(a.islower())
# above line modify below manner
print("Is Upper : ",a.isupper())
print("IS Lower : ",a.islower())
# this above should be given comma
# this method useing, output is super
# find the sentence alpha numeric
print("IS Alpha Numeric : ",a.isalnum())
# find the sentence alpha numeric
print("IS Alpha : ",a.isalpha())
# find the sentence alpha numeric
print("IS Numeric : ",a.isnumeric())
# how to split the lines \n
a = "kumar\nkavi\nkiruthik"
print(a)
# splitlines with a bracket
print(a.splitlines())
# if want to split with \n
print(a.splitlines(True))
# split the line using empty spaces
b = "Kiruthi is good talented kind person"
print(b.split(" "))
# split the line using comma
c = "Kiruthi,is,good,talented,kind,person"
print(c.split(","))
# count total length of sentence including empty spaces
d = "            kavi                    "
print(len(d))
# count only letter of sentence including empty spaces
print(len(d.strip()))
# remove left side empty spaces and count the total length
print(len(d.lstrip()))
# remove right side empty spaces and count the total length
print(len(d.rstrip()))
# Partition the date
e = "22-09-2021"
print(e.partition("-"))
"""

# String Manipulation
"""
    S   a   m   p   l   e
    0   1   2   3   4   5   
   -6  -5  -4  -3  -2  -1
"""
"""
# There are called string slicing
s = "sample"
print(s)
# Print particular letter in a word or a para
print(s[0:2])
# Print starting to particular point
print(s[:5])
# Print reverse starting point to particular point
print(s[1:])
# Print last letter of the word
print(s[-1])
# Print between letter of the word
print(s[-4:-1])
# Print omit the last letter of the word
print(s[:-1])
# Print all letter reversely (use double semi column
print(s[::-1])
"""

# Arithmetic operators
"""
+	Addition
-	Subtraction
*	Multiplication
/	Division
%	Modulus
**	Exponentiation
//	Floor division
"""
"""
a=123
b=10
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(3**5)
"""

# Arithmetic Assignment operators
"""
=   Assignment
+=	Addition
-=	Subtraction
*=	Multiplication
/=	Division
%=	Modulus
**=	Exponentiation
//=	Floor division
"""

"""
a = 125
print(a) # Just print equation of a
a += 10  # This means a = a+10 (Addtion A A O)
print(a)
a -= 10  # This means a = a-10 (Subtraction A A O)
print(a)
a *= 10  # This means a = a*10 (Multipilication A A O)
print(a)
a /= 10  # This means a = a/10 (Division A A O)
print(a)
a %= 10  # This means a = a%10 (Modules A A O)
print(a)
a **= 10  # This means a = a**10 (Exponentiation A A O)
print(a)
a //= 10  # This means a = a//10 (Floor Division A A O)
print(a)
"""

# Comparion operators or Relational operators
"""
==	Equal
!=	Not equal
>	Greater than
<	Less than
>=	Greater than or equal to
<=	Less than or equal to

"""
"""
a=15
b=10
print(a == b) # a value and b value are equal so result is true
              # a value and b value are not equal so result is false
print(a != b) # a value and b value are not equal, result is true
              # a value and b value are equal, result is false
print(a > b)  # a value is big b value is small, result is ture
              # a value is small b value is big, result is false
print(a < b)  # a value is small b value is big, result is true
              # a value is big b value is small, result is false
print(a >= b) # a value is big b value is small or a and b value
              # is same, result is ture
              # a value is small b value is big, result is false
print(a <= b) # a value is small b value is big or a and b value
              # is same, result is true
              # a value is big b value is small, result is false
"""

# Logical operators
"""
and
or
not
"""
"""
a = 25
print(a >= 10 and a <= 20)
print(a >= 10 or a <= 20)
print(not(a >= 10 and a <= 20)) # this is opposit for 1st equation
"""

#Bitwise operators
"""
& 	AND
|	OR
^	XOR
~ 	NOT
<<	Zero fill left shift
>>	Signed right shift
"""
"""
a = 25
b = 45
print(a&b)
print(a|b)
print(a^b)
print(~a)
print(a<<2)
print(a>>2)
"""

# IF Statement
"""
Write a program to check the given number is Even No or Odd No
"""
"""
n=int(input("Enter the number : "))
if n%2==0:
    print(n," is Even number")
else:
    print(n, " is Odd number")
"""

# IF Else Statement
"""
Write a program to check Vote eligibility by enter his/her name and age
"""
"""
name = input("Enter Your Name : ")
age = int(input("Enter Your Age : "))
if age >= 18:
    print(name,"age is ",age," Eligible for Vote.")
else:
    print(name, "age is ", age, " Not Eligible for Vote.")
"""

# Elif Statement
"""
Days       Rs
0        No Fine
1-5      Rs 0.5
5-10     Rs 1
10-30    Rs 5
>30      Membership Cancel

This is for a library, book readers takes a book, use the period of 1 month,
then return the book. Who one return the book after 1 month period, they should
be fined.
"""
"""
days = int(input("Enter the delayed days : "))
if (days == 0):
    print("Good No Fine")
elif (days >= 1 and days <= 5):
    print("Fine Amount : ", days * 0.5)
elif (days > 5 and days <= 10):
    print("Fine Amount : ", days * 1)
elif (days > 10 and days <= 30):
    print("Fine Amount : ", days * 5)
elif (days > 30):
    print("Membership Cancel")
"""

# Nested If Statement
"""
 3Marks as input
 Total
 Average
 result
 If pass Grade
          Marks     Grade
        90 - 100      A
        80 -  89      B
        70 -  79      C
          Else        D
"""
"""
m1 = int(input("Enter Mark - 1 : "))
m2 = int(input("Enter Mark - 2 : "))
m3 = int(input("Enter Mark - 3 : "))
total = m1 + m2 + m3
average = total / 3.0
print("Total   : ", total)
print("average : ", average)
if m1 >= 35 and m2 >= 35 and m3 >= 35:
    print("Result  :  Pass")
    if average >= 90 and average <= 100:
        print("Grade : A")
    elif average >= 80 and average <= 89:
        print("Grade : B")
    elif average >= 70 and average <= 79:
        print("Grade : C")
    else:
        print("Grade : D")
else:
    print("Result :  Fail")
    print("Grade  :  No Grade")
"""

# While Loop Statement
"""
1. While Loop
2. For Loop
"""
"""
i = 1
while i <= 10:
    print(i)
    i += 1
# You need to print some value continuosuly use this
"""
"""
n = 40
i = 2
while i <= n:
    print(i)
    i += 2
"""
# Continue Statement
"""
i = 1
while i <= 20:
    if i%2==0:
        i=i+1
        continue;
    print(i)
    i += 1
# Using this module it shows a result as omit if statement no print other nos
"""

# Break Statement
"""
i = 1
while i <= 20:
    if i==7:
        break
    print(i)
    i += 1
# Using this module for break the particular end
"""

# Range
"""
1-5   =>1,2,3,4,5
0-5   =>2,4
range(5)  => 0,1,2,3,4
range(2,5)  =>
"""
"""
a=list(range(5))
print(a)

# Or directly to use print input
# The range is works in n-1 formula and stats with whats given or 0

print(list(range(5))) # This formula works in starting with 0 and close in n-1
print(list(range(2,5))) # This formula works in starting with 2 and close in n-1
print(list(range(0,20,2))) # This formula works in starting with 2 and close in n-1 and shows even no
print(list(range(1,20,2))) # This formula works in starting with 1 and close in n-1 and shows odd no
"""

# For Loop
"""
for i in range(10):
    print(i)
for i in range(3,10):
    print(i)
for i in range(0,25,2):
    print(i)
for i in range(1,25,2):
    print(i)

for i in range(5):
    a = int(input("Enter a Number : "))
    b = int(input("Enter a Number : "))
    c = a+b
    print(c)
# This for loop used for works with n no of repeated works
"""

# Nested For Loop
"""
*
**
***
****
*****

*****
****
***
**
*

ABCDE
ABCDE
ABCDE
ABCDE
ABCDE

abcde
abcde
abcde
abcde
abcde


A - Z     => 65-90
a - z     => 97-122
"""
"""
for i in range(6):
    for j in range(i):
        print("*",end="")
    print("")
# If you need continue n time of repeat statement use this formula and need this type
# reversal formula should change range od first for loop
print("----------------------------") # This is for sepration code, dont consider
for i in range(5,0,-1): # Should see the range
    for j in range(i):
        print("*",end="")
    print("")
print("----------------------------") # This is for sepration code, dont consider
# if use capital alphapetic letters
for i in range(65,70,1):
    for j in range(65,70,1):
        print(chr(j),end="") # why chr function use here, bcoz change no to chrecter
    print("")
# In range function directly to use nos, special chrs but do not use alp letters,
# so, we use nos from 65 to 90 for capital A to Z and 97 to 122 for small a to z
print("----------------------------") # This is for sepration code, dont consider
# id use small alphapetic letters
for i in range(97,102,1):
    for j in range(97,102,1):
        print(chr(j),end="")
    print("")
"""

# While else & For Else
# While Else Statement
"""
i = 1
while i <= 5:
    print(i)
    i += 1
# first run this above statement result shown to 1 to 5
# Then given else statement below
else:
    print("While Loop Completed")
# now shown the result as fully run the statment and else statement
# after while statement have any break, else statement not shown, see below
i = 1
while i <= 5:
    if(i==4):
        break
    print(i)
    i += 1
else:
    print("While Loop Completed")
# Now run the statement else statement not shown the console

# For Else Statement
for i in range(1,21):
    print(i)
# first run this above statement result shown to 1 to 20
# Then given else statement below
else:
    print("For Loop Completed")
# now shown the result as fully run the statment and else statement
# after for statement have any break, else statement not shown, see below
for i in range(1,21):
    if i==5:
        break
    print(i)
else:
    print("For Loop Completed")
# Now run the statement else statement not shown the console
"""

# Lists
"""
Sequence Type
Mutable
a[5]
a={1,2,3,4,5}
a[0]
"""
"""
a=[1,2,3,4,5]
print(a)
print(type(a))
a[0]=100 # Change a particular list
print(a)
print(a[1])
print(a[-1])
print(a[0:3])
print(a[2:])
print(a[:3])
print("-------------------")
a = [1, True, 'Kavi', 2.5, [15,78,42,63]]
print(a)
print(type(a))
print(a[0],", The Class Type is : ", type(a[0]))
print(a[1],", The Class Type is : ", type(a[1]))
print(a[2],", The Class Type is : ", type(a[2]))
print(a[3],", The Class Type is : ", type(a[3]))
print(a[4],", The Class Type is : ", type(a[4]))
print(a[4][3]) # Find the nested list type
print("-------------------")
a = [10, 25 , 35, 45]
print(a)
a.clear() # Clear the whole list
print(a)
print("-------------------")
a=[11,22,33,44,55,66,77,88,99]
b = a.copy() # call the copy function from a to b
print(b)
print("-------------------")
a = [10,25,35,25,45,25,35,55,25]
print(a.count(25)) # Count the Elements the particular value
print(a.index(25)) # This is the particular value where to be places
print(len(a)) # Total length of particular list
print(max(a)) # Find the maximize value
print(min(a)) # Find the Minimum Value
a.pop(0) # Remove Element using index
print(a)
print("-------------------")
a = [10,25,35,25,45,25,35,55,25]
a.remove(25) # remove the value, which value comes first
print(a)
print("-------------------")
names=["Ram"] # Only list type
print(names)
names.append("Kumar")
names.append("Kavi")
names.append("Kiruthik") # Those above add one by one in list
print(names)
name2=["sara","Anitha"]
names.extend(name2) # This is add extend of created one
print(names)
names.insert(0,"Murugesan") # insert the name where to be indexed
print(names)
print("--------------------------------")
print(list(range(5)))
print(list("KiruthikVarshan"))
a=[10,50,100,25,85]
print(a)
a.sort() # sort small to big
print(a)
a.sort(reverse=True) # Sort big to small
print(a)
a=["Orange","Apple","Zebra"] # sort ascending order
a.sort()
print(a)
a.sort(reverse=True) # sort decending order
print(a)
a=["Orange","Apple","Zebra"]
a.sort(key=len)
print(a)
"""

# Tuple in Python
# Immutable
# Surrounded by round brackets ()
"""
a = (1, 2.5, True, "Ram")
print(a)
print(type(a))
print(a[1])
print(a[-1])
print(a[0:2])
# tuple statement cannot change, but change tuple to list first, then change
# whatever could change, then rechange from list to tuple
b=list(a)
print(b)
print(type(b))
b.append("Raja") # Added the particular field
print(b)
a = tuple(b) # Change from list to tuple
print(a)
print(type(a))

for i in a: # This for loop given a data horizontal to vertical
    print(i)
if "Raja" in a:
    print("Raja is found") # Particular value have or not finding
else:
    print("Not Found")
print(len(a))

a = (1) # in tuple have only one value should show int, so should have given comma
print(type(a))
a = (1,)
print(type(a))
del a # This elements used to delete entire parameter
# print(a)

a = (1,2,3,4)
b = (5,6,7,8)
c = a+b # add two elements
print(c)
print(c.count(4)) # counted the particular value
c = (a,b) # nested tuple function
print(c)
print(c[0])
print(c[1])
print(c[0][3])
print(c[1][2])

x = ('Kumar',)*10
print(x)

a = (1,2,5,8,9,15,12,47,65,45,19)
print(max(a))
print(min(a))
"""

# Set in Python
"""
names={"Kumar","Venkatesh","Uma"}
print(names)
print(type(names))

# Access Value using For Loop
for name in names:
    print(name)

# Adding New Elements
names.add("Kavitha")
print(names)

# update another set of Data
a = {"Mageshwari", "Paviya", "sathya", "Nandhini"}
names.update(a)
print(names)

# Remove a particular variable
names.remove("Venkatesh")
print(names)

# Discard the particular variable
names.discard("Paviya")
print(names)

# Those above remove and discard are same, but similar difference
# remove function works the variable exactly match, removed or not match shown the error the console
# discard function works the variable exactly match, removed then shown the result, not match shown before the variable

names.clear()
print(names) # clear all elements, shown empty bracket

del names
print(names) # delete total elements, shown error elements
names={'Kumar','Kavi','Kiruthik','Kumar'}
print(names) # In set elemnts have same variable multiple time, its removed

a = {1, 2, 3, 4}
b = {'a', 'b','c', 'd'}
c = a.union(b) # union is joint a set and b set
print(c)
a.update(b) # update and add from b set to a set
print(a)

a={5,6,7,8,9}
b={5,6,7,8,9}

c=a.intersection(b) # common value from a set and b set
print(c)
a.intersection_update(b) # commom value from a nad b set and update to a set
print(a)
c = a.symmetric_difference(b)
print(c) # remove the commom value from a and b set then shown a and b whole numbers
a.symmetric_difference_update(b)
print(a) # remove common nos and update balance no from b set and add a set
c = a.isdisjoint(b)
print(c) # a and b not have a common nos, it is true = boolian type
c = a.issubset(b)
print(c) # a set all nos have on b set its true, or false
c = a.issuperset(b)
print(c) # b set all nos have on a set its true, or false
"""

# Dictionary in Python
"""
user={
    "name": "Kumar",
    "age": 25,
    "is Married": True
}

print(user)
print(type(user))
print(user["name"])
print(user.get('age'))
print(user.keys())
print(user.values())
print(user.items())

for x in user:
    print(x) # this operation to be used only shown keys
for x in user:
    print(x," ",user[x]) # This type of code shown keys and values
for x in user.keys():
    print(x) # This is directly shown only keys function from for loop
for x in user.values():
    print(x) # This is directly shown only values function from for loop
# below function using for have two elements, so use x and y elements
for x,y in user.items():
    print(x,y) # This is directly shown keys and values function from for loop
if "gender" in user:
    print("yes")
else:
    print("No")
    
# Changing Values

user.update({"gender":"male"})
print(user)
user["age"]=35
print(user)
user.pop("age")
print(user)
user.clear()
print(user)
"""

# Nested Dictionary
'''
users = {
    "user1": {
        "name": "Kumar",
        "age": 32,
        "isMarried": True
    },
    "user2": {
        "name": "Kavitha",
        "age": 24,
        "isMarried": True
    },
    "user3": {
        "name": "Kiruthik Varshan",
        "age": 3,
        "isMarried": False
    }
}
print(users)
'''

'''
# identify operators
# is
# is not

# a = [1,2]
# b = [1,2]
# c = a
# print(id(a))
# print(id(c))
# print(id(b))
# print(a is c)
# print(a is b)
# print(a==b)

# print(a is not c)
# print(a is not b)
# print(a!=b)
'''

# membership opertors
'''
a=[10,25,45,88]
print(22 in a)
print(22 not in a)
'''

### Function
'''
def welcome():
    print("welcome Kumar")

welcome()
welcome()
welcome()

# No Return Type Without Argument Function in Python
def add():
    a=int(input("Enter The Value of A : "))
    b=int(input("Enter The Value of B : "))
    c=a+b
    print("Total : ", c)
add()    

# No Return Type With Argument Function in Python
def sub(a, b):
    c = a - b
    print("Difference : ", c)
sub(25, 2)

# Return Type Without Argument Function in Python
def mul():
    a = int(input("Enter The Value of A : "))
    b = int(input("Enter The Value of B : "))
    c = a * b
    return c
x = mul()
print("Mul : ",x)

# Return Type With Argument Function in Python
def div(a, b):
    c = a / b
    return c
x = div(90, 10)
print("Div : ", x)

# Arbitary Arguments Fuctions in python (*)
def class_10(*students):
    print(students)
    for user in students:
        print(user)

class_10("Kumar", "Kavi", "Kiruthik", "KKK")

# Keyword Arguments Functions in python
def message(name,age):
    print(name, "Age is ", age)
message("Ram",25)
message(25,"Ram")
# so
message(age=25,name="Ram")

# Arbitary Keyword Arguments in Python (**)
def bioData(**data):
    print(data)

bioData(name="Kumar",age=32,gender="Male")

# Default Parameter Function in Python
def user(name,city="Erode"):
    print(name, " is from ", city)
user("Kumar", "Coimbatore")
user("Kumar")

# Passing a List as an Argument in Function Python
def total(marks):
    return sum(marks)
print("Total is ",total([55,75,80,95,47]))

# Recursive Function
# 1 * 2 * 3 * 4 * 5 = 120
def factorial(x):
    pass

factorial(5)

def factorial(x):
    if x==1:
        return 1
    else:
        return (x * factorial(x - 1))
print("factorial : " , factorial(5))

# how it is works
# it is call 5 automatically

c=lambda a:a+50
print(c(5))

c = lambda a,b:a * b
print(c(10,25))
'''

### Date Time in Python
'''
import datetime as dt

current_date = dt.date.today()
print("Current Date : ", current_date)

new=dt.date(2022,10,25)
print(new)
print("Year : ", new.year)
print("Month : ", new.month)
print("Day : ", new.day)
print("----------------------------------------")
a = dt.time(10,45,5,555505)
print(a)
print("Hour : ", a.hour)
print("Minute : ", a.minute)
print("Secoind : ", a.second)
print("Microsecound : ", a.microsecond)
print("----------------------------------------")
current_time = dt.datetime.now()
print("Current time : ", current_time)
print("----------------------------------------")
new = dt.datetime(2022,5,29,11,5,33,55468)
print(new)
print(new.date())
print(new.time())
print("----------------------------------------")
current = dt.datetime.now()
new_year = dt.datetime(2023,1,1)
difference = new_year - current
print(difference)
print("----------------------------------------")
current = dt.datetime.now()
print(current)
s=current.strftime("%A %B %D %Y")
print(s)
'''

## Math Function
import math
'''
print(math.sqrt(16))
print(math.ceil(35614.8))
print(math.floor(35614.8))

print(math.factorial(5))

print(math.fabs(5))
print(math.fabs(-5))

print(math.pow(2,3))
print(math.log2(2))
print(math.log10(2))

print(math.pi)
print(math.e)
'''

### try block in Python
'''
a = 10 / 0
print(a)
'''
# try:
#     a = 10/0
# except Exception as e:
#     print(e)