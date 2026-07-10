# Loops Deep Dive (Industry Level)


# Start
#   │
#   ▼
# Do Work
#   │
#   ▼
# More Work?
#  │     │
# Yes    No
#  │      │
#  ▼      ▼
# Repeat  End  ------> syntax 

# 1. while Loop
# 2. for Loop


# while loop
# while condition 
    # code

# count = 1

# while count <=5:
#     print(count)
#     count +=1

# number = int(input("Start: "))

# while number > 0:
#     print(number)
#     number -= 1

# print("Finished!")




#For loop 

# for variable in iterable:
#     code


# for i in range (100):
#     print("TRax")


# range(start, stop)
# for i in range( 1,6):
#     print(i)

# range(start, stop, step)
for i in range(1,5,2):
    print(i)



# Loop Through String

name = "python"
for ch in name:
    print(ch)

# Loop Through List
fruits =["Apple","Mango","Banana"]

for fruits in fruits:
    print(fruits)


# break
for i in range(10):
    if i ==5:
        break
    print(i)


# continue  -< skip then iterator 
for i in range(6):
    if i ==3:
        continue
    print(i)   # here skip 3 