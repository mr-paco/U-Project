
print("Calculadora")
a=int(input("Primer numero que desea usar ="))
b=int(input("Segundo numero que desea usar="))
while True:
    print("""
    Elija el numero de la operacion que desea realizar
    1]Sumar
    2]Restar
    3]Multiplicar
    4]Dividir
    5]Salir
    """)
    operacion=int(input())
    if operacion==1:
        print(" ")
        print("Total:",a,"+",b,"=",a+b)
    
    if operacion==2:
        print(" ")
        print("Total:",a,"-",b,"=",a-b)
        
    if operacion==3:
        print(" ")
        print("Total:",a,"*",b,"=",a*b)
        
    if operacion==4:
        print(" ")
        print("Total:",a,"/",b,"=",a/b)
        
    if operacion==5:
        print(" Muchas gracias ")
        print("\U0001F480")
        