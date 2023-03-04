def reverse (frase):                            #  Usamos recursividad para  darle la vuelta a la frase.
    if len(frase) > 1:
        frase_reverse = reverse(frase[1:]) + frase[0]
        return(frase_reverse)
    else:
        return frase[0]

def reversion (frase):                          #  Usamos un bucle para  construir una nueva frase  desde el final.
    contador = -1
    frase_invertida = ""
    for num in range(len(frase)):               
        frase_invertida += frase[contador]      
        contador-=1
    return frase_invertida

print(reverse("hola mundo cruel")) 
print(reversion("hola mundo cruel")) 
