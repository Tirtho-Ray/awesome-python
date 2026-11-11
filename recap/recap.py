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


