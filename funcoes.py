# Função para ler ou criar arquivo txt
def carregar_contatos():
    lista_de_contatos_carregada = [] # lista vazia 

    try: # tenta esse bloco
        with open('contatos.txt', 'r', encoding='utf-8') as arquivo: # abrir o ariquivo contatos.txt para leitura
            
            for linha in arquivo:
                
                linha_limpa = linha.strip() # limpa as linha e remove espaçoes

                partes = linha_limpa.split(',') # define onde vai ser a quebra de linha 
                
                if len(partes) == 3: # verificação para ver se os contatos tem 3 partes
                    
                    contato = { # dicionario 
                        'nome': partes[0],
                        'telefone': partes[1],
                        'email': partes[2]
                    }
                    
                    # adicionar o dicionário recém-criado à nossa lista.
                    lista_de_contatos_carregada.append(contato)

    except FileNotFoundError: # se nao conseguir ler o arquivo ou ele não existir 
        print("\nArquivo de contatos não encontrado. Começando com uma agenda nova.")
    return lista_de_contatos_carregada # retorna a lista de contatos

# função para criar novo contato
def criar_contato(agenda_de_contatos):
    print("\n----Cadastro de novo contato----")

    nome_digitado = input("Qual o nome do contato --> ") # usuário digita o nome
    telefone_digitado = input("Qual o telefone --> ") # usuário digita o telefone
    email_digitado = input("Qual o email --> ") # usuário digita o email

    novo_contato = { # dicionario 
        'nome': nome_digitado,  
        'telefone': telefone_digitado,
        'email': email_digitado
    }

    agenda_de_contatos.append(novo_contato) # adicionar contato 
    print(f"\n----Novo contato {nome_digitado} salvo----")

# Função para listar os nomes 
def listar_contatos(agenda_de_contatos):
    print("\n----- Lista de contatos ----\n")
    
    for contato in agenda_de_contatos: # loop para listar os contatos 
        print("------------------------------")
        print(f"Nome:     {contato['nome']}")
        print(f"Telefone: {contato['telefone']}")
        print(f"E-mail:   {contato['email']}")
        
    print("------------------------------\n")
    print("-------- Fim da lista --------")

# Função para buscar contato
def buscar_contato(agenda_de_contatos):
    print("\n----- Buscador de Contatos ----\n")
    nome_buscado = input("Qual o nome do contato que você quer buscar --> ") # qual nome o usuário quer buscar
    
    contato_encontrado = False # verificador para saber se já foi encontrado

    for contato in agenda_de_contatos:
        if contato ['nome'] == nome_buscado:
            print("\n------------------------------")
            print("---- Contato Encontrado ----")
            print(f"Nome:     {contato['nome']}")
            print(f"Telefone: {contato['telefone']}")
            print(f"E-mail:   {contato['email']}")
            print("------------------------------\n")

            
            contato_encontrado = True
            break

    else:
        print("\n------------------------------")
        print(f"Contato {nome_buscado} não foi encontrado")

#Função para remover contato
def remover_contato(agenda_de_contatos):

    contato_encontrado = False

    print("\n------------------------------")
    print("---- Remover um contato ----")
    nome_buscado = input("Qual o nome do contato que você quer remover --> ")

    for contato in agenda_de_contatos:
        if contato ['nome'] == nome_buscado:
            agenda_de_contatos.remove(contato)
            print(f"\nContato {nome_buscado} foi removido com sucesso")
            print("\n------------------------------")

            contato_encontrado = True
            break
    else:
        print("\n------------------------------")
        print(f"Contato {nome_buscado} não foi encontrado")

# Função para salvar os contato em um arquivo
def salvar_agenda(agenda_de_contatos):
    print("\n----Salvando a sua agenda, até logo----")
    with open('contatos.txt', 'w', encoding='utf-8') as arquivo: # abre o arquivo 
        for contato in agenda_de_contatos:  # loop para escrever os contatos 
            arquivo.write(f"{contato['nome']},{contato['telefone']},{contato['email']}\n")


