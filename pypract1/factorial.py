nums = 10

#Por ejemplo, 5! = 5.4.3.2.1 = 120

for i in range(nums):
    #op = nums
    if (i >= 1):
        nums = nums * (i)
        print(nums)

def factorial(n):
   if n==0 or n==1:
            resultado=1
   elif n>1:
            resultado=n*factorial(n-1)
   return resultado
factnumero=factorial(int(input("Por favor ingresa el número para averiguar el factorial: ")))
print(f"El factorial es: {factnumero}")
