import os 
import re


arquivo = "minhas_leituras.txt "
leituras = []
def carregar_dados():
    if not os.path.exists(arquivo):
        return
    with open(arquivo, "r", encoding="utf-8") as f:
        for linha in f:
            dados = linha.strip().split("|")
            if len(dados) == 6:
                minha_leitura = {
                    "nome": dados[0],
                    "idade": dados[1],
                    "Cidade/Estado": dados[2],
                    "preferência de gênero": dados[3],
                    "senha": dados[4],
                    "faixa etária": dados[5]
                }
                leituras.append(minha_leitura)

def salvar_dados():
    with open(arquivo, "w", encoding="utf-8") as f:
        for let in leituras:
            linha = f"{let['nome']}|{let['idade']}|{let['Cidade/Estado']}|{let['preferência de gênero']}|{let['faixa etária']}|{let['senha']}\n"
            f.write(linha)




def menu():
    while True:
        print("\033[1;34;40m--------- Minhas Leituras ---------\033[m")
        print("\033[1;34;40m|1.\033[m Cadastrar usuário ")
        print("\033[1;34;40m|2.\033[m Visitar Minha Biblioteca ")
        print("\033[1;34;40m|3.\033[m Ritmo de Leitura e Estudo ")
        print("\033[1;34;40m|4.\033[m Sair")
        opção = input("\033[1;34;40m Digite uma opção: \033[m")
        if opção == "1":
            cadastrar_usuario()
        elif opção == "2":
            menu_2()
        elif opção == "3":
            ritmo_leitura()
        elif opção == "4":
            print("\033[1;34;40mObrigado por usar o programa Minhas Leituras! Até logo!\033[m")
            break
        else:
            print("\033[0;31mOpção inválida. Por favor, escolha uma opção válida.\033[m")


def menu_2():
    while True:
        validar_login = input("Você já possui um usuário cadastrado? (sim/não): ").strip().lower()
        if validar_login not in ["sim", "não", "nao", "ss", "nn", "não"]:
            print("\033[31mResposta inválida. Por favor, responda com 'sim' ou 'não'.\033[0;0m")
        else:
            if validar_login == "sim":
                nome_usuario = input("Digite seu nome de usuário: ").strip()
                senha_usuario = input("Digite sua senha: ").strip()
                if validar_login(nome_usuario, senha_usuario):
                    print("Login bem-sucedido! ✅")
                else:
                    print("Usuário ou senha incorretos. ❌")
            else:
                print("\033[1;36;40m--------- Minha Biblioteca ---------\033[m")
                print("\033[1;36;40m|1.\033[m Adicionar livro ")
                print("\033[1;36;40m|2.\033[m Lista de  livros ")
                print("\033[1;36;40m|3.\033[m Remover livro ")
                print("\033[1;36;40m|4.\033[m Voltar ao menu principal ")
                print("\033[1;36;40m|5.\033[m Marcar livro como lido")
                opção = input("\033[1;34;40m Digite uma opção: \033[m")
                if opção == "1":
                    adicionar_livro()
                elif opção == "2":
                    listar_livros()
                elif opção == "3":
                    remover_livro()
                elif opção == "4":
                    menu()
                else:
                    print("\033[0;31mOpção inválida. Por favor, escolha uma opção válida.\033[m")
            continue




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
            print("\033[1;34;40mBem vindo(a) ao programa Minhas Leituras,", nome, "!\033[m")
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
        elif not re.match(r"^[a-zA-Z\s]+,\s*[A-Z]{2}$", cidade_estado):
            print("\033[31mFormato inválido. Use o formato 'Cidade, Estado' (ex: São Paulo, SP).\033[0;0m")
        else:
            print("\033[1;32mCidade/Estado cadastrado com sucesso.\033[0;0m")
            break
    print("\033[1;34;40mAgora, vamos falar sobre seus gêneros literários favoritos.\033[m")
    while True:
        gen = input("Qual gênero literário que você mais se identifica? ").strip().lower()
        if gen in ("romance", "ficção", "aventura", "fantasia", "terror", "suspense", "biografia", "autoajuda"):
            print(f"Ótima escolha! Seu gênero favorito é {gen}.")
            print("\033[1;34;40mPerfeito! Vamos salvar suas informações.\033[m")
            
        else:
            print("\033[31mGênero não reconhecido. Por favor, escolha entre: romance, ficção, aventura, fantasia, terror, suspense, biografia ou autoajuda.\033[0;0m")
        break
    leituras.append({
                "nome": nome,
                "idade": idade,
                "Cidade/Estado": cidade_estado,
                "preferência de gênero": gen,
                "faixa etária": "Criança" if idade <= 11 else "Adolescente" if idade <= 17 else "Jovem" if idade <= 25 else "Adulto",
                "senha": senha
            }) 
    salvar_dados()
    print(f"\033[1;32mUsuário cadastrado com sucesso!\033[m")
    return menu()



        
    
        







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




menu()










    










