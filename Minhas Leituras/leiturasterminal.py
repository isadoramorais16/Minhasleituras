print("\033[1;34;40m--------- Minhas Leituras ---------\033[m")
nome = input("Nome do Usuário: ")
print("\033[1;34;40mBem vindo(a)",str(nome),"ao programa Minhas Leituras,bom te ter aqui!\033[m")



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

try:
    idade = int(input("Quantos anos você tem? "))
    resposta = input("\033[1;34;40mGostaria que eu recomendasse livros para sua faixa etária?\033[m ").strip().lower()
    if resposta in ["sim","ss"]:
        rec_livros(idade)
    elif resposta in ["não",'nao','nn']:
        print("tudo bem, vamos prosseguir")
    else:
        print("Resposta não reconhecida. Por Favor, digite 'sim' ou 'não'")
except ValueError:
    print("Digite um número válido")

print("               ")

cidadeestado = input("Informe sua Cidade/Estado? ")
print("\033[1;34;40mAposto que deve ser um lugar muito bonito...\033[m")













    










