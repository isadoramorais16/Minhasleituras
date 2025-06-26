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
            if len(dados) == 7:
                minha_leitura = {
                    "nome": dados[0],
                    "senha": dados[1],
                    "Cidade/Estado": dados[2],
                    "preferência de gênero": dados[3],
                    "idade": dados[4],
                    "faixa etária": dados[5],
                    "preferência de leitura": dados[6]
                }
                leituras.append(minha_leitura)

def salvar_dados():
    with open(arquivo, "w", encoding="utf-8") as f:
        for let in leituras:
            linha = f"{let['nome']}|{let['idade']}|{let['Cidade/Estado']}|{let['preferência de gênero']}|{let['faixa etária']}|{let['senha']}|{let['preferência de leitura']}\n"
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
    carregar_dados()
    login()
    if login() == True:
        print("\033[1;36;40m--------- Minha Biblioteca ---------\033[m")
        print("\033[1;36;40m|1.\033[m Adicionar livro ")
        print("\033[1;36;40m|2.\033[m Lista de  livros ")
        print("\033[1;36;40m|3.\033[m Remover livro ")
        print("\033[1;36;40m|4.\033[m Voltar ao menu principal ")
        print("\033[1;36;40m|5.\033[m Marcar livro como lido")
        print("\033[1;36;40m|6.\033[m Ver progresso de leitura ")
        opção = input("\033[1;36;40m Digite uma opção: \033[m")
        if opção == "1":
            adicionar_livro()
        elif opção == "2":
            listar_livros()
        elif opção == "3":
            remover_livro()
        elif opção == "4":
            menu()
        elif opção == "5":
            marcar_livro_lido()
        elif opção == "6":
            progresso_livro()
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
    while True:
        pref_book = input("Você prefere livros digitais ou físicos? ").strip().lower()
        if not pref_book:
            print("\033[31mCampo obrigatório!\033[0;0m")
        elif pref_book in ["digital", "físico", "fisicos","físicos","digitais"]:
            print(f"\033[1;34;40mVocê prefere livros {pref_book}. Legal!\033[m")
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



def login():
    carregar_dados()
    nome = input("Digite seu nome: ").strip()
    senha = input("Digite sua senha: ").strip()
    for let in leituras:
        if let["nome"].lower() == nome.lower() and let["senha"] == senha:
            print(f"\033[1;32mBem-vindo(a), {let['nome']}!\033[m")
            return menu_2()
        else:
            print("\033[31mUsuário ou senha incorretos. Tente novamente.\033[0;0m")
            return False


def ritmo_leitura():
    print("\033[1;34;40m--------- Ritmo de Leitura e Estudo ---------\033[m")
    digital_livros = int(input("Quantos livros DIGITAIS você tem lido no último ano? "))
    resposta = input("Você gostaria de saber quantos livros digitais você lerá nos próximos 5 anos? ").strip().lower()
    if resposta in ["sim", "ss", "Sim"]:
        digital_result = digital_livros * 5
        print("\033[1;34;40mSe continuar nesse ritmo você lerá", digital_result, "livros digitais nos próximos 5 anos\033[m")
        if digital_result >= 50:
            print("\033[1;32mVocê é um leitor digital ávido!\033[0;0m")
        elif digital_result >= 20:
            print("\033[1;33mVocê é um leitor digital moderado!\033[0;0m")
        elif digital_result >= 10:
            print("\033[1;34mVocê é um leitor digital ocasional!\033[0;0m")
        else:
            print("\033[1;31mVocê é um leitor digital iniciante! Que tal explorar mais o hábito de leitura? \033[0;0m")
    elif resposta in ["não", "nao", "nn", "Não"]:
        print("\033[1;34;40mTudo bem, vamos continuar.\033[m")
    fisico_livros = int(input("Quantos livros FÍSICOS você tem lido no último ano? "))
    resposta_2 = input("Você gostaria de saber quantos livros físicos você lerá nos próximos 5 anos? ").strip().lower()
    if resposta_2 in ["sim", "ss", "Sim"]:
        fisico_result = fisico_livros * 5
        print("\033[1;34;40mSe continuar nesse ritmo você lerá", fisico_result, "livros físicos nos próximos 5 anos\033[m")
        if fisico_result >= 50:
            print("\033[1;32mVocê é um leitor ávido!\033[0;0m")
        elif fisico_result >= 20:
            print("\033[1;33mVocê é um leitor moderado!\033[0;0m")
        elif fisico_result >= 10:
            print("\033[1;34mVocê é um leitor ocasional!\033[0;0m")
        else:
            print("\033[1;31mVocê é um leitor iniciante! Que tal explorar mais o hábito de leitura? \033[0;0m")
    elif resposta_2 in ["não", "nao", "nn", "Não"]:
        print("\033[1;34;40mTudo bem, vamos continuar.\033[m")
    horas_estudo = int(input("Quantas horas você se dedica aos livros de estudos por semana? "))
    horas_result = horas_estudo * 52
    print("\033[1;34;40mSe continuar nesse ritmo você estudará", horas_result, "horas em um ano!\033[m")
    if horas_result <= 550:
        print("\033[1;31mVocê é um estudante iniciante! Que tal dedicar mais tempo aos estudos?\033[0;0m")
    elif horas_result >= 550:
        print("\033[1;32mVocê é um estudante dedicado! Continue assim!\033[0;0m")


def progresso_livro(paginas_lidas, total_paginas, largura=30):
    total_paginas = int(input("Digite o total de páginas do livro: "))
    paginas_lidas = int(input("Quantas páginas você já leu? "))
    paginas_hora = float(input("Quantas páginas você tem lido por hora? "))
    if total_paginas <= 0:
        return "Livro sem páginas?"
    elif paginas_lidas > total_paginas:
        paginas_lidas = total_paginas
    elif paginas_lidas < 0:
        return "Número de páginas lidas não pode ser negativo."
    elif not paginas_lidas:
        return "Você ainda não leu nenhuma página."
    elif not total_paginas:
        return "O total de páginas não pode ser zero."
    elif paginas_hora <= 0:
        return "Média de páginas por hora inválida."
    elif paginas_hora > total_paginas:
        return "Média de páginas por hora não pode ser maior que o total de páginas."

    porcentagem = paginas_lidas / total_paginas
    preenchido = int(largura * porcentagem)
    vazio = largura - preenchido
    barra = f"[{'█' * preenchido}{' ' * vazio}]"
    porcento = round(porcentagem * 100)

    return f"{barra} {porcento}% ({paginas_lidas}/{total_paginas} páginas)"


def prever_tempo_restante(paginas_lidas, total_paginas, media_paginas_por_hora):
    if paginas_hora <= 0:
        return "Média inválida."

    paginas_restantes = total_paginas - paginas_lidas
    horas_totais = paginas_restantes / paginas_hora
    horas = int(horas_totais)
    minutos = round((horas_totais - horas) * 60)

    return f"⏳ Estimativa de tempo para terminar: {horas}h {minutos}min"





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

faixas ={"Criança":{"min":0, "max":11,"livros":["O Pequeno Príncipe, Chapeuzinho Vermelho,Diário de um Banana"]},
    "Adolescente":{"min":12,"max":17,"livros":["Harry Potter,Crepúsculo,Jogos Vorazes",]},
    "Jovem":{"min":18,"max":25,"livros":["1984,O sol é para todos,Quarto de Despejo"]},
    "Adulto":{"min":26,"max":1000,"livros":["Café com Deus Pai, A Abolição do Homem"]}}



menu()









    










