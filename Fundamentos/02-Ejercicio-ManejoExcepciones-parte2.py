resultado = None
a = "10"
b = 0
try:
    resultado = a / b
except ZeroDivisionError as e:
    print("Ocurrió un error con ZeroDivisionError", e)  
    print(type(e))  
except TypeError as e:
    print("Ocurrió un error con TypeError", e)  
    print(type(e)) 
except Exception as e:
    print("Ocurrió un error con exception", e)  
    print(type(e)) 
    
print("resultado: ", resultado)    
print("continuamos...")    