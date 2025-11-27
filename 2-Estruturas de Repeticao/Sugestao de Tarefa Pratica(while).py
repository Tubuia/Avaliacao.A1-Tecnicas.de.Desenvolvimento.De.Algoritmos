#Desenvolver um contador de 1 a 100 com while, exibindo apenas números pares.
i = 1 #variavel que armazena o numero do contador
while i <= 100: #estrutura de repetição while que opera até a variavel i chegar ao numero 100
    if i % 2 == 0: #estrutura condicional que verifica se o resto de i dividido por 2 é igual a 0
        print(i)
        i += 1 #incremento de 1 a i
    else:
        i += 1 #incremento de 1 a i