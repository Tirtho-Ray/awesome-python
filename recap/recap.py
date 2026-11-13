# print("hello world")

# a = 10
# b = 30
# c = a+b
# print (c)


# variable 
name = " rax"
age = 10
isAdmin = True
hight = 5.6

t,y,u = 10,20,30
d=f=g =10

print (name , age , isAdmin, hight)

# user input 

userName  = input("Enter your name ")
print(userName)

# Data type check 

x =100

print(type(x))


# String 
# Syntax: string[start:stop:step]
text = "Python Programming"

print(text[0:6])   # Python
print(text[7:])    # Programming
print(text[:6])    # Python
print(text[::2])   # Every second character
print(text[::-1])  # Reverse string

#  ==>
# Method	    Purpose
# upper()	    Convert to uppercase
# lower()	    Convert to lowercase
# title()	    Title case
# capitalize()	Capitalize first character
# strip()	    Remove surrounding whitespace
# replace()	    Replace text
# split()	    Convert string into list
# join()	    Join iterable elements
# find()	    Find substring position
# count()	    Count occurrences
# startswith()	Check starting text
# endswith()	Check ending text




# ==> Useful numeric functions:
# print(abs(-10))       # 10
# print(round(10.567, 2)) # 10.57
# print(pow(2, 3))      # 8
# print(max(10, 20, 30)) # 30
# print(min(10, 20, 30)) # 10
# print(sum([10, 20, 30])) # 60


# ==> Constants // fix value , its dont change 
# PI = 3.14159
# MAX_USERS = 100
# DATABASE_NAME = "my_database"



# ======================

# operator

# 1: Arithmetic 
# +,-,*,/. //,%,**

#2:Comparison (Relational) Operators
# == 
# !=
# >=
# <=
# >
# <

##3: Logical Operators
# and	Both conditions must be True	True and False → False
# or	At least one condition True	True or False → True
# not	Reverses Boolean result	not True → False



# 4. Assignment Operators
# Operator	Example	Equivalent
# =	x = 10	Assign
# +=	x += 5	x = x + 5
# -=	x -= 5	x = x - 5
# *=	x *= 5	x = x * 5
# /=	x /= 5	x = x / 5
# //=	x //= 5	x = x // 5
# %=	x %= 5	x = x % 5
# **=	x **= 2	x = x ** 2
# &=	x &= 5	x = x & 5
# \|=	x \|= 5	x = x \| 5
# ^=	x ^= 5	x = x ^ 5
# >>=	x >>= 1	x = x >> 1
# <<=	x <<= 1	x = x << 1
# @=	x @= y	Matrix multiplication assignment



# 5. Bitwise Operators
# Operator	Name	Example
# &	    AND     	5 & 3 → 1
# \|	OR      	5 \| 3 → 7
# ^	    XOR     	5 ^ 3 → 6
# ~	    NOT     	~5 → -6
# <<	Left Shift	5 << 1 → 10
# >>	Right Shift	5 >> 1 → 2

# 6. Membership Operators

# Operator	Meaning
# in	        Value exists
# not in	    Value does not exist


#  ==> Membership Operators
# in
# not in

numbers = [10, 20, 30, 40]

print(20 in numbers)  # True
print(50 in numbers)  # False

numbers = [10, 20, 30]

print(50 not in numbers)  # True
print(20 not in numbers)  # False








# <============================>            <=============================>
#  ==> Conditional Statements (if, elif, else, nested if, match-case).
age = 18

if age < 18:
    print("vote")
else:
    print("can not vote")



mark = 75

if mark  >=80:
    print("A+")
elif mark >=70:
    print("A-")
else:
    print("fail")



age = 22
has_id = True

if age >= 18:
    if has_id:
        print("Entry allowed")
    else:
        print("ID required")
else:
    print("Underage")



#  ==> Nested 

username = "admin"
password = "12345"

if username == "admin":

    if password == "12345":
        print("Login Successful")

    else:
        print("Wrong Password")

else:
    print("Invalid Username")


#  ==> Match-Case Statement
day = 3

match day:
    case 1:
        print("Monday")

    case 2:
        print("Tuesday")

    case 3:
        print("Wednesday")

    case 4:
        print("Thursday")

    case _:
        print("Invalid Day")


# short hand ternary 

roll  = 50

result  = "topper" if roll >= 60 else "Not Topper"

print(result)

# multiple  condition using short ternary
marks = 75
grade = "A" if marks >= 80 else "B" if marks >= 60 else "C"
print(grade)



#<=====================>     <==================>
# Loops in python

# range(start, stop, step)

# for i in range (1,10):
#     print(i)


# for i in range(10, 0, -1):  // reverse loop
#     print(i)

# num =[ 10,20,30 ,40]

# for number in num :
#     print(number)




##  ===> while loop

# i = 0
# while i <10 :
#     print(i)
#     i +=1


## ===>  nested loop

# for i in range(1,4) :
#     for j in range(1,4):
#         print(i,j)


# for i in range(1, 6):
#     for j in range(i):
#         print("*", end=" ")
#     print()


# for i in range(1,40):
#     if i >= 5:
#         break
#     print(i)

# for i in range(1,40):
#     if i == 5:
#         continue
#     print(i)





# ---------------------------------------------------------------------

# ===---> list  ( array )

# num =[10,20,30,40,50]
# name =["ray","sam","jisan"]
# mix =[10,"ray"]

# num.remove(10)  #remove() — Remove by value
# num.pop(1)      #remove() — Remove by value

# del num[1]
# # numbers.clear()

# num.sort()
# num.sort(reverse=True)



# # Nested List
# matrix = [[1, 2], [3, 4]]

# fruits = ["Apple", "Banana", "Mango", "Orange"]

# print(fruits[0])   # Apple
# print(fruits[1])   # Banana
# print(fruits[-1])  # Orange
# print(fruits[-2])  # Mango


# Method	কাজ
# append()	End element add one 
# insert()	Specific index-এ add
# extend()	Multiple elements add

# fruits.append("Tamato")
# fruits.insert(1,"Trax")
# fruits.extend(["Mango", "Orange"])

# # print(num[0])


# fruits = ["Apple", "Banana", "Mango"]

# for fruit in fruits:
#     print(fruit)





# ----------------------------------------------------------

# 2. Tuple 

# Empty Tuple
data = ()

# Tuple with values
numbers = (10, 20, 30, 40)

# Different data types
data = (10, "Python", 3.14, True)

# Duplicate values
numbers = (10, 20, 10, 30)


fruits = ("Apple", "Banana", "Mango", "Orange")

print(fruits[0])   # Apple
print(fruits[2])   # Mango
print(fruits[-1])  # Orange



# tuple can not change direct  

numbers = (10, 20, 30)
temp = list(numbers)
temp[0] = 100
numbers = tuple(temp)
print(numbers)
# (100, 20, 30)

#Tuple slicing 
numbers = (10, 20, 30, 40, 50)
print(numbers[1:4])
# (20, 30, 40)

languages = ("Python", "Java", "C++")

for language in languages:
    print(language)


student = ("Ray", 21, "CSE", "Bangladesh")

name, age, department, country = student

print(f"Name: {name}")
print(f"Age: {age}")
print(f"Department: {department}")
print(f"Country: {country}")


#---------------------------------------------------------- 

# 3. Set ( {} )

# Empty Set
numbers = set()
# Set with values
numbers = {10, 20, 30, 40}
# Duplicate values
numbers = {10, 20, 10, 30, 20} # set does not accept duplicated value 
print(numbers)
# {10, 20, 30}

# serise  = {2,3,4,4,5,5,6}
# serise.update([4,6,7,8,])


A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
result = A & B
print(result)
# {3, 4}

print(A - B)
# {1, 2}

print(A ^ B)
# {1, 2, 5, 6}


languages = {"Python", "Java", "C++"}

for language in languages:
    print(language)







