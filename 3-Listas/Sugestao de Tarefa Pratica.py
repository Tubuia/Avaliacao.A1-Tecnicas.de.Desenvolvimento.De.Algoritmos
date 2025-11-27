#Criar um programa que receba nomes de alunos e armazene em uma lista, permitindo exibir todos os nomes ao final.
alunos = [] #lista que vai armazenar os nomes
while True:
    nome = input("Digite o nome do aluno (ou pressione ENTER para encerrar): ") #variavel dos nomes que serão cadastrados
    if nome == "": #verificação do nome vazio para quebrar a estrutura de repetição e terminar o codigo
        break #quebra do while
    alunos.append(nome) #adição do nome a lista

print(f"Alunos cadastrados: {alunos}") #saida do codigo