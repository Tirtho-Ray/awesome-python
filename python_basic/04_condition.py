#  Control Flow (if, elif, else)


#         Start
#           │
#           ▼
#    Is Age >=18?
#       /       \
#     Yes       No
#     │          │
# Access     Denied           -------------> control follow 


age = 20

if age >= 18:
    print("adult")



if age >=18 :
    print("adult")
else:
    print("not adult")


mark = 75

if mark >= 80:
    print("A+")
elif mark >= 70:
    print("a-")
else:
    print("NOTHING")


# NESTED

year = 30
citizen = True

if year >= 18:
    if citizen :
        print("Your ar now entry here")
    else:
        print("citizen required")
else:
    print("Too young")


money = 200
if money >= 100 and money <=600:
    print("worker here")


# real world example 

role = "admin"
if role =="admin" and role =="teacher":
    print("Your are authentic")
else:
    print("unauthorize access")


# find the largest number 

a =  int(input("Enter number a :"))
b =  int(input("Enter then number b:"))

if a == b :
    print("Tow are same ")
elif a > b:
    print("A ia big")
else:
    print("A is small")



# Real time login 

email = str(input("Enter the email: "))
password  = str(input(" Enter the password: "))


if email == "tirthoray10@gmail.com" and password == "T10":
    print("login successfully")
else:
    print("Invalid credential ")


