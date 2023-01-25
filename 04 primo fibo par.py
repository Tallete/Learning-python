
def es_fibonacci (numero):
    last_1 = 0
    last_2 = 1  
    while numero >= last_1:  
        if last_1 == numero:
            return True
        next = last_1 + last_2
        last_1 = last_2
        last_2 = next
    return False

def es_par(numero):
    return numero%2==0

def es_primo (numero):
    divisor = 2
    while divisor < numero:
        if numero % divisor == 0:
            return False
        divisor += 1
    return True

def check_num(numero):
    primo = es_primo(numero)
    par = es_par(numero)
    fibo = es_fibonacci(numero)
    print (f"el número {numero}", "es primo," if primo else "no es primo,", "es par," if par else "es impar,", "y " "es fibonacci" if fibo else "no es fibonacci" )

for i in range(10, 20):
    check_num(i)
