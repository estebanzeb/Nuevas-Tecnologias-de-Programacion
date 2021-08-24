x = 40
if x > 30:
    print ("x is less tha 30","\n")
else:
    print ("x is greater tha 30","\n")

x = 30
if x == 30:
    print ("x is 30","\n")
else:
    print ("x is not 30","\n")

color = "violet"

if color == "blue":
    print ("Es el mismo","\n")
elif color == "violet":
    print ("Es el mismo","\n")
else:
    print ("No es el mismo","\n")

name = "John"
last_name = "Carter"

if name == "John":
    if last_name == "Carter":
        print ("You are John Carter\n")
    else:
        print ("You are not John Carter\n")
else:
    print ("You are not John\n")


x = 5
y = 6
if x > 2:
    if x < 10:
        print (x)

if x > 2 and x <= 10:
    print (x , "is greater that two and less that or ten")
if x > 2 or x <= 20:
    print (x , "is greater than two or less or equal to twenty")
if (not(x == y)):
    print(x , "is not equal " , y)