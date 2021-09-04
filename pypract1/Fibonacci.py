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