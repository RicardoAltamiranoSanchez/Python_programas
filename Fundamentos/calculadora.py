n=0
#funcion de suma
def sumar():
  numero=int(input("Digite el primer numero"))
  numero2=int(input("Digite el segundo numero")) 
  return numero+numero2
#funcion de resta  
def resta():
  numero=int(input("Digite el primer numero"))
  numero2=int(input("Digite el segundo numero")) 
  return numero-numero2
#funcion de multiplicacion
def multiplicacion():
    numero=int(input("Digite el primer numero"))
    numero2=int(input("Digite el segundo numero")) 
    return numero*numero2
#funcion de division
def division():
    numero=int(input("Digite el primer numero"))
    numero2=int(input("Digite el segundo numero")) 
    return numero/numero2   
while n<3:
    print("Calculadora\n 1.suma\n 2.resta\n3.multiplicacion\n4.division")
    opcion=int(input("\nDigite la opcion\n"))
    if(opcion==1):
        print(sumar())
    elif(opcion==2):
        print(resta())
    elif(opcion==3):
        print(multiplicacion())
    elif(opcion==4):
        print(division())
    else:print("no existe esa opcion")                
    n+=1     
 
     
     
