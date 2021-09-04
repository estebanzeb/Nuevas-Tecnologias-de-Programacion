foods = ['apple', 'bread', 'cheese', 'milk', 'bananas', 'graves']

print (foods[0])
print (foods[1])
print (foods[2])
print (foods[3])

print ("\n")

for food in foods:
    if food == 'apple' or food == 'bread': 
            print("You have to buy this " + food + "  primero\n") 
    if food == 'bananas':
           break#Salir del for 
    if food == 'cheese':
           continue#Ignorar
    print (food,"\n")

for number in range(1, 9):
    print(number)

for letter in 'Hello':
    print(letter)

count = 4

while count <= 10:
    print(count)
    count += 1