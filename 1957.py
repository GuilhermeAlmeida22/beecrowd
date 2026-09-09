n = int(input())

hexa = "0123456789ABCDEF"

resultado = ""

while n != 0:
    posicao = n % 16
    resultado += hexa[posicao]
    n //= 16
    
print(resultado[::-1])