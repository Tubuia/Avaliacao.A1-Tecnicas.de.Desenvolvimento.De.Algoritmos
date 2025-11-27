#Criar um programa em Python que simule um sistema de verificação de idade para entrada em eventos.

idade = int(input("Digite a sua idade: ")) #variavel de idade do usuario

if idade >= 18: #condicional de idade minima para a participação do evento
    print("Você pode entrar no evento.") #saida para idade permitida
else:
    print("Você não é velho o bastante para participar do evento.") #saida para idade não permitida