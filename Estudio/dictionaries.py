product = {
    "name": "book",
    "quantity": 3,
    "price": 4.99 
}

person = {
    "firts_name": "ryan",
    "last_name": "ray"
}
print (type(product)) 
print (dir(person))

print (person.keys(),"\n")
print(person.items(),"\n")
print (person.values(),"\n")

#del person ELIMINAR

person.clear()
print (person)

products = [
    {"name": "book", "price": 10.99},
    {"name": "laptop", "price": 1000}

]
print (products)