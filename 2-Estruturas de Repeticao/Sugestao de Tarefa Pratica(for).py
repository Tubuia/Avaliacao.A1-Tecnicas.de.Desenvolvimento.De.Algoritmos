#Desenvolver um contador de 1 a 100 com for, exibindo apenas números pares.
for i in range(1, 101): #estrutura de repetição for aonde i esta pode possuir valores de 1 a 101
    if i % 2 == 0: #estrutura condicional que verifica se o resto de i dividido por 2 é igual a 0
        print(i)
        i += 1 #incremento de 1 a i
    else:
        i += 1 #incremento de 1 a i