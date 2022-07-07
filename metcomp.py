
ax = int(input('Põe o ax aê cupinxa: '))
N = int(input('Quantos termos a série vai ter? '))



def fatorial(num): # Cálcula fatoração
    aux1 = 1
    while (num > 0):
        aux1 *= num
        num -= 1
    return aux1

def potencia(num, n): # Cálcula potenciação
    count = n - 1
    while (count > 0):
        num *= ax
        count -= 1
    return num

aux2 = N
exp = 1
while (aux2 > 0):
    exp += (potencia(ax, aux2))/(fatorial(aux2))
    print(fatorial(aux2))    
    print(potencia(ax, aux2)) 
    aux2 -= 1


#print(fatorial(N))    
#print(potencia(ax, N))  
print(exp)  
