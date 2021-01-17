resultado = None
try:
    a = int(input("Primer número: "))
    b = int(input("Segundo número: "))
    resultado = a / b
except ZeroDivisionError as e:
    print("Ocurrió un error con ZeroDivisionError", e)  
    print(type(e))  
except TypeError as e:
    print("Ocurrió un error con TypeError", e)  
    print(type(e)) 
#except ValueError as e:
#    print("Ocurrió un error con ValueError", e)  
#    print(type(e))    
except Exception as e:
    print("Ocurrió un error con exception", e)  
    print(type(e)) 
else:
    print("No hubo ninguna excepción")
finally:
    print("Fin del manejo de excepciones")    
    
print("resultado: ", resultado)    
print("continuamos...")    