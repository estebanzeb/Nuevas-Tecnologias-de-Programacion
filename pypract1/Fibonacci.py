lista = [0,1]
n=10
k=2
for i in range(n):
    print(lista[k - 1] )
    print(lista[k - 2] )

    lista.append(lista[k - 1] + lista[k - 2])
    #print(lista)
    k = k + 1
print(lista)
#print(dir(lista))

def fib(n):
    a, b = 0,1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()
m = int(input("Ingresa límite máximo de la sucesión: "))     
fib(m)