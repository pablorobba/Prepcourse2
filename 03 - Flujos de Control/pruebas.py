n = 3
primo = True
while True:
     
    if (n % 2 == 0):
        primo = False 
 
    else:
        print(n, "es primo")
        print("¿desea continuar?")
        if (input() != "sí"):
            break    
         
    n += 1