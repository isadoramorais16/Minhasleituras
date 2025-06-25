import re


def cadastrar_usuario():
    while True:
        nome = input("Qual seu nome? ")
        if not nome:
            print("Campo Obrigatório")
        elif any(i.isdigit() for i in nome):
            print("não é possível utilizar números")
        else:
            print("\033[1;35;47mBem vindo(a)",nome,"ao programa Minhas Leituras\033[m")
        print("Vou fazer algumas perguntas para personalizar sua experiência")
        while True:
            idade = int(input("Quantos anos você tem? "))
            if not idade:
                print("Campo Obrigatório")
            elif idade < 0:
                print("Não é permitido o uso de números negativos! ")
            elif re.search(r'[a-z+A-Z]'):
                print("Somente permitido o uso de números")
            else:
                resp = input("Gostaria de receber recomendações de livros para sua faixa etária?")
                if resp == ["ss","sim","Sim"]:
                    rec_livros
                elif not resp:
                    print("Campo Obrigatório!")
                elif resp ==["nn","não","Não"]:
                    print("Tudo bem. Vamos prosseguir")
                cidade_estado = input("Digite sua Cidade/Estado: ")

                
        
        


def menu():
    print("----------Minhas Leituras-----------")
    print("|1. Cadastrar Usuário")
    print("|2. Lista de Leituras")
    print("|3. Sair")
    while True:
        opcao=input("Selecione uma opção: ")
        if not opcao:
            print("Campo obrigatório")
        elif opcao == "1":
            print("----Cadastro do Usuário----")
            cadastrar_usuario()
        elif opcao == "2":
            menu_2()
        elif opcao == "3":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Digite uma opção dentre as possíveis.")

def menu_2():
    print("----------Lista de Leituras--------")
    print("1.Adicionar novo livro")
    print("2.Visualizar minha Biblioteca")
    print("3.Excluir Livro")
    print("4.Marcar Livro como Lido")
    print("5.Voltar")
    while True:
        opcao_2 = input("Selecione uma opção: ")
        if not opcao_2:
            print("Campo Obrigatório!")
        elif opcao_2 == "1":
            adicionar_livro()
        elif opcao_2 == "2":
            meuslivros()
        else:
            print("Opção inválida. Digite uma opção dentre as possíveis.")

def adicionar_livro():
    while True:
        book = input("Digite o nome do Livro")
        if not book:
            print("Campo obrigatório!")

         









faixas ={"Criança":{"min":0, "max":11,"livros":["O Pequeno Príncipe, Chapeuzinho Vermelho,Diário de um Banana"]},
    "Adolescente":{"min":12,"max":17,"livros":["Harry Potter,Crepúsculo,Jogos Vorazes",]},
    "Jovem":{"min":18,"max":25,"livros":["1984,O sol é para todos,Quarto de Despejo"]},
    "Adulto":{"min":26,"max":1000,"livros":["Café com Deus Pai"]}}


def rec_livros(idade):
    faixa_encontrada = None
    for faixa, info in faixas.items():
        if info["min"]<= idade <= info["max"]:
            faixa_encontrada = faixa
            livros = info["livros"]
            break
    if faixa_encontrada:
        print(f"\n\033[1;34;40mFaixa etária\033[m:{faixa_encontrada.capitalize()}")
        print("📚Livros recomendados:")
        for livro in livros:
             print(f"\033[1;34;40m{livro}\033[m")
        return
    print("Idade fora do intervalo permitido.")

menu()













    










