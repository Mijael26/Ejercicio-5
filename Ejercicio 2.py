# Una Empresa lee la información de las ventas de sus 25 vendedores, y por cada venta realizada lee
#         Número de vendedor     día     monto de venta
# El fin se detecta por monto = 0
# Se solicita:
# a)	Informar el numero de vendedor que  vendió más  (aquel de mayor monto total de venta).
# b)	Informar los números de vendedores cuyo monto total de venta superaron los $ 10000.


n_vendedor = [0]*(5)
sum_vendedor = [0] * (5)


for h in range (0,5,1) :
       n_vendedor[h] = h + 1


vendedor =  int(input("Ingrese numero de vendedor : "))
dia = int(input("Dia : "))
monto = int(input("Monto : "))

while monto != 0 :
    for h in range (0,5,1) :
        if vendedor == n_vendedor[h] :
            sum_vendedor[h] = sum_vendedor[h] + monto


    vendedor = int(input("Ingrese numero de vendedor : "))
    dia = int(input("Dia : "))
    monto = int(input("Monto : "))

print(f"El vendedor con mayor monto es : ")

for h in range(0,5,1) :
    if h == 0 :
        max = sum_vendedor[h]
        posmax = 1
    else :
        if sum_vendedor[h] > max :
            max = sum_vendedor[h]
            posmax =  h + 1


print(posmax)


print("los vendedores con un monto mayor a $10.000 son :  ")

for h in range(0,5,1) :
    if sum_vendedor[h] > 10000 :
        print(n_vendedor[h])