import os
#import funciones as fn
from funciones import *
os.system("cls")

#####################################################
menu()
opc= validar_opciones([1,2,3,4])

if opc==1:
    sumar_2_numeros()
  
elif opc==2:
    num1= validar_numero()
    num2= validar_numero()
    restar_2_numeros(num1,num2)
elif opc==3:
    total= multiplicar_2_numeros()
    print("EL total es:",total)
else:
    num1= int(input("Ingrese primer número: "))
    num2= int(input("Ingrese segundo número: "))
    lista=[]
    lista.append(dividir_2_numeros(num1,num2))
    print(lista)