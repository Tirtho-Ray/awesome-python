# 10 -> operand
# + -> operator
# 10 -> operand

# operators  -> 
# 1. Arithmetic
# 2. Assignment
# 3. Comparison
# 4. Logical
# 5. Identity
# 6. Membership
# 7. Bitwise (Introduction)



# 1. Arithmetic


# | Operator | Meaning        |
# | -------- | -------------- |
# | +        | Addition       |
# | -        | Subtraction    |
# | *        | Multiplication |
# | /        | Division       |
# | //       | Floor Division |
# | %        | Modulus        |
# | **       | Power          |


a=10
b=20
print(a+b)
print(a-b)
print(a/b)
print(a*b)
print(a//b) #-> print(10 // 3) here not come decimal 

# Power (**)
print( 2 ** 3)



# 2: Assignment Operators
x = 10
x +=10
x -=3
x /=2
x *=3
print(x)




# 3. Comparison Operators
# | Operator | Meaning       |
# | -------- | ------------- |
# | ==       | Equal         |
# | !=       | Not Equal     |
# | >        | Greater       |
# | <        | Less          |
# | >=       | Greater Equal |
# | <=       | Less Equal    |

print(10==10)
print(4!=5)
print(3>5)
print(4<10)
print(5>=6)
print(10<=100)





# 4. Logical Operators
# and

# or
# not

###### not use this 
# &&
# ||
# !

print( True and True)
print( True and False)

age  = 20
print(age>18 and age<=20)


a= None 
print( a is None)


# 5. Identity Operators

a = None

print(a is None)

# 6. Membership Operators  -> is check is is available  in item or not 
# not in 

name  = "Tirtho"
print("T" in name)

numbers = [ 10, 50, 30]
print(10 in numbers)


# 7. Bitwise Operators (Introduction)

# &
# |
# ^
# ~
# <<
# >>

print(2 + 3 * 4)  # use math securance 
print((2 + 3) * 4)

#  min project 1
num = int(input("Enter the number :"))
if num % 2 == 0:
    print("Even")
else:
    print("odd")

# Mini Project 2
# Power Calculator

num1 = int(input("Enter the first  number:"))
num2 = int(input("Enter second number:"))
print(num1**num2)