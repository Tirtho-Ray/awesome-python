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
