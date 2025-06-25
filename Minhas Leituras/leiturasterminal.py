import os 
import re
import random

arquivo = "minhas_leituras.txt "
leituras = []
def carregar_dados():
    if not os.path.exists(arquivo):
        return
    with open(arquivo, "r", encoding="utf-8") as f:
        for linha in f:
            dados = linha.strip().split("|")
            if len(dados) == 5:
                minha_leitura = {
                    "nome": dados[0],
                    "idade": dados[1],
                    "Cidade/Estado": dados[2],
                    "preferência de gênero": dados[3],
                    "faixa etária": dados[4]
                }
                leituras.append(minha_leitura)

def salvar_dados():
    with open(arquivo, "w", encoding="utf-8") as f:
        for let in leituras:
            linha = f"{let['nome']}|{let['idade']}|{let['Cidade/Estado']}|{let['preferência de gênero']}|{let['faixa etária']}\n"
            f.write(linha)


def menu():
    while True:
        print("\033[1;34;40m--------- Minhas Leituras ---------\033[m")
        print("\033[1;34;40m|1.\033[m Cadastrar usuário ")
        print("\033[1;34;40m|2.\033[m Login do usuário ")
        print("\033[1;34;40m|3.\033[m Visitar Minha Lista de livros ")
        print("\033[1;34;40m|4.\033[m Ritmo de Leitura e Estudo ")
        print("\033[1;34;40m|5.\033[m Sair")
        opção = input("\033[1;34;40m Digite uma opção: \033[m")
        if opção == "1":
            cadastrar_usuario()
        elif opção == "2":
            login_usuario()
        elif opção == "3":
            minha_lista()
        elif opção == "4":
            ritmo_leitura()
        elif opção == "5":
            print("\033[1;34;40mObrigado por usar o programa Minhas Leituras! Até logo!\033[m")
            break
        else:
            print("\033[0;31mOpção inválida. Por favor, escolha uma opção válida.\033[m")


def cadastrar_usuario():
    while True:
        nome = input("Qual é o seu nome? ").strip()
        if not nome:
            print("\033[31mCampo obrigatório!\033[0;0m")
        elif " " in (nome):
            print("\033[31mO nome não pode conter espaços!\033[0;00m")
        elif any(i.isdigit() for i in nome):
            print("\033[31mNão é válido utilização de números.\033[0;0m") 
        else:
            print("\033[1;34;40mBem vindo(a) ao programa Minhas Leituras,", nome, "\033[m")
            break

    while True:
        senha = input("Digite uma senha numérica de 6 dígitos: ")
        if not senha:
            print("\033[31mCampo obrigatório!\033[0;0m")
        elif " " in str(senha):
            print("\033[31mA senha não pode conter espaços!\033[0;00m")
        elif len(str(senha)) < 6:
            print("\033[31mA senha deve ter no mínimo 6 dígitos!\033[0;0m")
        elif len(str(senha)) > 6:
            print("\033[31mA senha não pode conter mais de 6 dígitos!\033[0;0m")
        elif any(not i.isdigit() for i in senha):
            print("\033[31mA senha deve conter apenas números!\033[0;00m")
        else:
            print("\033[32mSenha cadastrada com sucesso.\033[0;0m")
            break
    print("\033[1;34;40mVamos começar com algumas perguntas para personalizar sua experiência.\033[m")
    while True:
        idade = int(input("Quantos anos você tem? "))
        if not idade:
            print("\033[31mCampo obrigatório!\033[0;0m")
        elif idade < 0:
            print("\033[31mIdade inválida. Por favor, insira uma idade positiva.\033[0;0m")
        elif idade > 100:
            print("\033[31mIdade inválida. Por favor, insira uma idade abaixo de 100.\033[0;0m")
        elif any(not i.isdigit() for i in str(idade)):
            print("\033[31mA idade deve conter apenas números!\033[0;00m")
        else:
            print(f"\033[1;34;40mVocê tem {idade} anos certo?!\033[m")
            break
    while True:
        recom = input("\033[1;34;40mGostaria que eu recomendasse livros para sua faixa etária?\033[m  ").strip().lower()
        if not recom:
            print("\033[31mCampo obrigatório!\033[0;0m")
        elif recom in ["sim", "ss", "Sim"]:
            rec_livros(idade)
        elif recom in ["não","nao","nn","Não"]:
            print("Tudo bem, vamos prosseguir.")
        else:
            print("Resposta não reconhecida. Por favor, digite 'sim' ou 'não'.")
        break
    while True:
        cidade_estado = input("informe sua Cidade/Estado: ")
        if not cidade_estado:
            print("\033[31mCampo obrigatório!\033[0;0m")
        elif not re.match(r"^[A-Za-z\s]+,[A-Z]{2}$", cidade_estado):
            print("\033[31mFormato inválido. Use 'Cidade, Estado' (ex: São Paulo,SP).\033[0;0m")
        elif re.search(r"^(Pernambuco|Paraíba|Rio Grande do Norte|Ceará|Alagoas|Bahia|Sergipe|Minas Gerais|Espírito Santo|Rio de Janeiro|São Paulo|Paraná|Santa Catarina|Rio Grande do Sul)$", cidade_estado):
            print("\033[32mCidade/Estado não reconhecido.\033[0;0m")
        else:
            print("\033[1;32mCidade/Estado cadastrado com sucesso.\033[0;0m")
            break
    print("Temos algumas recomendações para autores específicos dessa região!")
    while True:
        cid_recom = input("Gostaria de ver as recomendações?").strip().lower()
        if cid_recom in ["sim", "ss", "Sim"]:
            rec_aut(cidade_estado)
        elif cid_recom in ["não","nao","nn","Não"]:
            print("Tudo bem, vamos prosseguir.")
        else:
            print("Resposta não reconhecida. Por favor, digite 'sim' ou 'não'.")
            break
    while True:
        gen = input("Qual gênero literário que você mais se identifica? ").strip().lower()
        if gen in ["romance", "ficção", "aventura", "fantasia", "terror", "suspense", "biografia", "autoajuda"]:
            print(f"Ótima escolha! Seu gênero favorito é {gen}.")
        else:
            print("Gênero não reconhecido. Por favor, escolha entre: romance, ficção, aventura, fantasia, terror, suspense, biografia ou autoajuda.")
            break
            
    leituras.append({
            "nome": nome,
            "idade": idade,
            "Cidade/Estado": cidade_estado,
            "preferência de gênero": gen,
            "faixa etária": rec_livros(idade),
            })
    salvar_dados()
    print(f"\033[1;34;40mUsuário '{nome}' cadastrado com sucesso!\033[m")

    

def login_usuario():
        nome = input("Digite seu nome: ")
        for let in leituras:
            if let["nome"].lower() == nome.lower():
                print(f"Bem-vindo(a) de volta, {let['nome']}!")
                print(f"Idade: {let['idade']}")
                print(f"Cidade/Estado: {let['Cidade/Estado']}")
                print(f"Preferência de gênero: {let['preferência de gênero']}")
                print(f"Faixa etária: {let['faixa etária']}")
                return
        print("Usuário não encontrado. Por favor, cadastre-se primeiro.")
        
    
        




autores = {"Nordeste": {"livros": ["Ariano Suassuna", "João Cabral de Melo Neto", "Graciliano Ramos", "Jorge Amado", "Clarice Lispector"]},
           "Sudeste": {"livros": ["Machado de Assis", "Carlos Drummond de Andrade", "Clarice Lispector", "Adélia Prado", "Rubem Fonseca"]},
           "Sul": {"livros": ["Erico Verissimo", "Lya Luft", "Manoel de Barros", "Mário Quintana", "Cecília Meireles"]},
           "Centro-Oeste": {"livros": ["Guimarães Rosa", "Cora Coralina", "Ariano Suassuna"]},
           "Norte": {"livros": ["Joaquim Nabuco", "Dalcídio Jurandir", "Milton Hatoum"]}}

def rec_aut(cidade_estado):
    estado = cidade_estado.split(",")[1].strip().upper()
    for regiao, info in autores.items():
        if estado in info["livros"]:
            print(f"\n\033[1;34;40mRecomendações de autores da região {regiao}:\033[m")
            for autor in info["livros"]:
                print(f"📚 {autor}")
            return
    print("Nenhuma recomendação encontrada para a sua região.")



faixas ={"Criança":{"min":0, "max":11,"livros":["O Pequeno Príncipe, Chapeuzinho Vermelho,Diário de um Banana"]},
    "Adolescente":{"min":12,"max":17,"livros":["Harry Potter,Crepúsculo,Jogos Vorazes",]},
    "Jovem":{"min":18,"max":25,"livros":["1984,O sol é para todos,Quarto de Despejo"]},
    "Adulto":{"min":26,"max":1000,"livros":["Café com Deus Pai, A Abolição do Homem"]}}


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



print("               ")

menu()









    










