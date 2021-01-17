
print("programa para areas\n")
print("1 Cuadrado\n2 Rectangulo")
opcion=int(input("Escoja una opcion"))
if (opcion==1):
  base=int(input("Digite un lado\n"))
  print("El Resultado del  area es:",base*4,
  "\nEl resultado del perimetro es:",base+base)
if (opcion==2):
    
    base=int(input("Digite la base\n"))
    altura=int(input("Digite la altura\n"))
    print("El Resultado del  area es:",base*altura,
        " \nEl resultado del perimetro es:",(base+altura)*2)
            
else:
    print("Esa opcion no existe")