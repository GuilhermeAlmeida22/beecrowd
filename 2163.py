n, m = map(int, input().split())

matriz = []

for i in range(n):
    linha = list(map(int, input().split()))
    matriz.append(linha)
    
achou = False

for i in range(1, n - 1):
    for j in range(1, m - 1):
        if matriz[i][j] == 42:
            if (matriz[i - 1][j] == 7 and
                matriz[i][j - 1] == 7 and
                matriz[i + 1][j] == 7 and
                matriz[i][j + 1] == 7 and
                matriz[i - 1][j - 1] == 7 and
                matriz[i + 1][j - 1] == 7 and
                matriz[i + 1][j + 1] == 7 and
                matriz[i - 1][j + 1] == 7):
                    achou = True
                    print(i + 1, j + 1)
                    
if achou == False:
    print(0, 0)