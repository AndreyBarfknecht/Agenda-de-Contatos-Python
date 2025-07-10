
import os # descobrir o sistema OP
import pyfiglet # gerar o titulo em ASCII
from rich.console import Console # deixa as linha coloridas
from rich.panel import Panel # imprime o logo ASCII dentro de um painel
from rich.table import Table # para listar os contatos dentro de uma tabela
import time # ajuda nas animaçoes da barra de progresso 
from rich.progress import Progress # barra de progresso
import json # exportar par JSON
import csv # exportar para CSV

#objeto console para usar o rich
console = Console()



def limpar_tela():
    # Verifica se o sistema operacional é Windows ('nt') ou outro (Linux/macOS)
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def desenhar_cabecalho(texto_do_titulo):
    """Limpa a tela e desenha um cabeçalho estilizado."""
    limpar_tela() 
    
    # Gera o texto em ASCII Art
    titulo_ascii = pyfiglet.figlet_format(texto_do_titulo, font="slant")
    
    # Imprime o título  dentro de um painel
    console.print(Panel.fit(f"[bright_blue]{titulo_ascii}[/]", subtitle="[Andrey]"))
    console.print() # Imprime uma linha em branco para dar espaço


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
        console.print("\nArquivo de contatos não encontrado. Começando com uma agenda nova.")
    return lista_de_contatos_carregada # retorna a lista de contatos

# função para criar novo contato
def criar_contato(agenda_de_contatos):
    desenhar_cabecalho("Criar Contato")
    console.print("Escreva e pressione 'ENTER'")
    
    nome_digitado = input("Qual o nome do contato --> ") # usuário digita o nome 
    while not nome_digitado.strip(): # verifica se o nome não está vazio
        console.print("[yellow]O nome não pode estar vazio!!!")
        nome_digitado = input("Qual o nome do contato --> ") # usuário digita novamente

    telefone_digitado = input("Qual o telefone --> ") # usuário digita o telefone
    while not telefone_digitado.strip():
        console.print("[yellow]O telefone não pode estar vazio!!!")
        telefone_digitado = input("Qual o telefone --> ") # usuário digita o telefone

    email_digitado = input("Qual o email --> ") # usuário digita o email
    while not email_digitado.strip():
        console.print("[yellow]O email não pode estar vazio!!!")
        email_digitado = input("Qual o email --> ") # usuário digita o email


    novo_contato = { # dicionario 
        'nome': nome_digitado,  
        'telefone': telefone_digitado,
        'email': email_digitado
    }

    # verificar se o contato existe
    contato_existente = False
    for contato in agenda_de_contatos:
        if  novo_contato == contato:
            contato_existente = True
            break
            
    if contato_existente: # se o contato já existe
        console.print()
        console.print("[magenta3]Este contato já existe na agenda")
        
    else:
        agenda_de_contatos.append(novo_contato) # adiciona o contato, se ele não existe
        console.print(f"[magenta3]\n----Novo contato {nome_digitado} salvo----")
        
    input("\nPressione Enter para voltar ao menu...")

# Função para listar os nomes 
def listar_contatos(agenda_de_contatos):
    # Limpa a tela e desenha o cabeçalho para esta "página"
    desenhar_cabecalho("Lista de Contatos")
    
    if not agenda_de_contatos:
        console.print("[yellow]Sua agenda está vazia.[/yellow]")
    else:
        # Cria uma tabela com bordas e título
        tabela = Table(title="Seus Contatos", show_header=True, header_style="magenta3")
        
        # Adiciona as colunas
        tabela.add_column("Nome", style="dark_slate_gray1", width=20)
        tabela.add_column("Telefone", style="dark_slate_gray1", width=20)
        tabela.add_column("E-mail", style="dark_slate_gray1")

        # Adiciona as linhas com os dados dos contatos
        for contato in agenda_de_contatos:
            tabela.add_row(contato['nome'], contato['telefone'], contato['email'])
        
        # Imprime a tabela inteira no console
        console.print(tabela)

    # Pausa para o usuário ler antes de voltar ao menu
    input("\nPressione Enter para voltar ao menu...")

# Função para buscar contato
def buscar_contato(agenda_de_contatos):
    desenhar_cabecalho("Buscar Contato")
    
    console.print("Escreva e pressione 'ENTER'")
    
    nome_buscado = input("Qual o nome do contato que você quer buscar --> ") # qual nome o usuário quer buscar
    while not nome_buscado.strip(): # verifica se não está em branco
        console.print("[magenta3]Você digitou um nome em branco!!!")
        nome_buscado = input("Qual o nome do contato que você quer buscar --> ") # qual nome o usuário quer buscar

    resultados_encontrados = [] # lista de resultados encontrados

    for contato in agenda_de_contatos:
        
        if nome_buscado.lower() in contato['nome'].lower(): # busca pelo nome tanto com letra maiúsculas/minúsculas
            resultados_encontrados.append(contato) # adiciona a lista de resultados_encontrados
        
    if resultados_encontrados: # se achar contato
    # Cria a tabela
        tabela = Table(title=f"\n[bright_blue]Contato Encontrados com o nome [magenta3]{nome_buscado}", show_header=True, header_style="magenta3")
    
        # Adiciona as colunas
        tabela.add_column("Nome", style="dark_slate_gray1", width=20)
        tabela.add_column("Telefone", style="dark_slate_gray1", width=20)
        tabela.add_column("E-mail", style="dark_slate_gray1")

        for contato in resultados_encontrados: # passa pela lista de resultados e adiciona a tabela
        #Adiciona os dados do contato encontrado
            tabela.add_row(contato['nome'], contato['telefone'], contato['email'])
    
        # imprime a tabela preenchida
        console.print(tabela)
        

    else: # se não mostra que não existe nenhum contato com o nome buscado
        console.print("\n------------------------------")
        console.print(f"Contato {nome_buscado} não foi encontrado")
        
    input("\nPressione Enter para voltar ao menu...")


#Função para remover contato
def remover_contato(agenda_de_contatos):
    desenhar_cabecalho("Remover um contato") # desenha o nome gigante

    console.print("Escreva e pressione 'ENTER'")    
    nome_buscado = input("Qual o nome do contato que você quer remover --> ")
    while not nome_buscado.strip(): # verifica se o nome não está em branco
        console.print("[magenta3]Você digitou um nome em branco!!!")
        nome_buscado = input("Qual o nome do contato que você quer remover --> ") # pede para digitar novamente
    
    resultados_encontrados = [] # lista de resultados encontrados

    for contato in agenda_de_contatos: #loop para buscar os contatos encontrados
        
        if nome_buscado.lower() in contato['nome'].lower(): # busca pelo nome tanto com letra maiúsculas/minúsculas
            resultados_encontrados.append(contato) # adiciona a lista de resultados_encontrados

    if len (resultados_encontrados) == 0: # se não tiver nenhum contato com o nome buscado 
            console.print(f"\n[yellow]Nenhum contato encontrado com o termo '{nome_buscado}'.[/yellow]")

    elif len (resultados_encontrados) == 1: # se tem 1 contato com esse
       
            # cria tabela
            tabela = Table(title=f"\n[bright_blue]Contato Encontrados com o nome {nome_buscado}", show_header=True, header_style="magenta3")
            # Adiciona as colunas
            tabela.add_column("Nome", style="dark_slate_gray1", width=20)
            tabela.add_column("Telefone", style="dark_slate_gray1", width=20)
            tabela.add_column("E-mail", style="dark_slate_gray1")
            for contato in resultados_encontrados: # passa pela lista de resultados e adiciona a tabela
                tabela.add_row(contato['nome'], contato['telefone'], contato['email'])
                console.print(tabela) # imprime a tabela
            console.print("[magenta3]Tem certeza que deseja remover este contato? (s/n)")
            confirmacao = console.input(f"\nDigite 's' pra remover o contato\n'n' para deixar o contato na lista\n -->")
            if confirmacao == "s".lower(): # se o usuario quiser remover
                contato_para_remover = resultados_encontrados[0] # define o contato para remover
                agenda_de_contatos.remove(contato_para_remover) # remove o contato
                console.print(f"\n[magenta3]Contato foi removido com sucesso")
            else:
                console.print("\n[magenta3]Contato não foi removido") # se nao for removido
    
    
    # se foir encontrado mais de 1 contato com o mesmo nome
    else:
        console.print("[yellow]Vários contatos foram encontrados. Por favor, escolha qual deles remover:[/yellow]")
        # cria tabela
        tabela = Table(title=f"\n[bright_blue]Contatos Encontrados com o nome [magenta3]{nome_buscado}", show_header=True, header_style="magenta3")
        # Adiciona as colunas
        tabela.add_column("Número",style="dark_slate_gray1", width=20)
        tabela.add_column("Nome", style="dark_slate_gray1", width=20)
        tabela.add_column("Telefone", style="dark_slate_gray1", width=20)
        tabela.add_column("E-mail", style="dark_slate_gray1")
        for indice, contato in enumerate(resultados_encontrados): #lopp para adicionar os contatos na tabela
            tabela.add_row(str(indice + 1), contato['nome'], contato['telefone'], contato['email'])
        
        console.print(tabela)

        while True:
            escolha_str = console.input ("Digite o 'Número' do contato que você quer remover ou digite '0' para cancelar\n--> ")

            try:
            #  converte a escolha para um número inteiro
                escolha_num = int(escolha_str)

            # Verifica se o usuário quer cancelar
                if escolha_num == 0:
                    console.print("[cyan]Operação cancelada.[/cyan]")
                    break
            
            # Verifica se o número está no intervalo correto
                elif 1 <= escolha_num <= len(resultados_encontrados):
                
                # Pega o índice correto (usuário digita 1, que é o índice 0)
                    indice_para_remover = escolha_num - 1
                
                # define o contato para remover
                    contato_para_remover = resultados_encontrados[indice_para_remover]

                # Remove o contato da LISTA PRINCIPAL
                    agenda_de_contatos.remove(contato_para_remover)

                    console.print(f"\n[bold green]Contato '{contato_para_remover['nome']}' removido com sucesso![/bold green]")
                    break
                else:
                # O usuário digitou um número, mas está fora do intervalo válido
                    console.print(f"[bold red]Escolha inválida. Por favor, digite um número entre 1 e {len(resultados_encontrados)}.[/bold red]")

            except ValueError:
            # Se o int() falhar, significa que o usuário não digitou um número
                console.print("[bold red]Entrada inválida. Por favor, digite apenas o número correspondente.[/bold red]")


    input("\nPressione Enter para voltar ao menu...")
    

    """for contato in agenda_de_contatos: # loop para verificar se o contato existe
        if contato ['nome'] == nome_buscado:
            agenda_de_contatos.remove(contato) # remove o contato inteiro
            console.print(f"\nContato {nome_buscado} foi removido com sucesso")
            console.print("\n------------------------------")
            break
    else:
        console.print("\n------------------------------")
        console.print(f"Contato {nome_buscado} não foi encontrado")
    input("\nPressione Enter para voltar ao menu...")"""

# Função para salvar os contato em um arquivo
def salvar_agenda(agenda_de_contatos):
    #Salva os contatos na contatos.txt
    with open('contatos.txt', 'w', encoding='utf-8') as arquivo: # abre o contatos.txt em modo escrita
        for contato in agenda_de_contatos:
            arquivo.write(f"{contato['nome']},{contato['telefone']},{contato['email']}\n") # escreve os contatos 

    #barra de progresso
    console.print()
    with Progress() as progress:
        
        
        tarefa_de_salvamento = progress.add_task("[magenta3]Salvando...", total=100) # total da barra 

       
        while not progress.finished: # enquanto não finaliza a barra nao termina o loop
            
            # Avança a barra de progresso um pouquinho.
            progress.update(tarefa_de_salvamento, advance=1.5)

            # pequena pausa para ver a animação.
            time.sleep(0.02) 
    console.print("\n[magenta3]Agenda salva com sucesso!")
    console.print("O programa será encerrado.")
    time.sleep(1)

#Função para exporta a agenda para JSON
def exportar_json(agenda_de_contatos):
    with open('contatos.json', 'w', encoding='utf-8') as arquivo_json:
            json.dump(agenda_de_contatos, arquivo_json, indent=4, ensure_ascii=False)
    console.print()
    with Progress() as progress:
        
        
        tarefa_de_salvamento = progress.add_task("[magenta3]Salvando...", total=100) # total da barra 

       
        while not progress.finished: # enquanto não finaliza a barra nao termina o loop
            
            # Avança a barra de progresso um pouquinho.
            progress.update(tarefa_de_salvamento, advance=1.5)

            # pequena pausa para ver a animação.
            time.sleep(0.02) 
    console.print("\n[magenta3]Agenda Exportada para JSON com sucesso!")
            

#Função para exportar a agenda para CSV
def exportar_csv(agenda_de_contatos):
    cabecalhos = ['nome', 'telefone', 'email']
    with open('contatos.csv', 'w', encoding='utf-8', newline='') as arquivo_csv:
            escritor = csv.DictWriter(arquivo_csv, fieldnames=cabecalhos)
            escritor.writeheader()
            escritor.writerows(agenda_de_contatos)
    console.print()
    with Progress() as progress:
        
        
        tarefa_de_salvamento = progress.add_task("[magenta3]Salvando...", total=100) # total da barra 

       
        while not progress.finished: # enquanto não finaliza a barra nao termina o loop
            
            # Avança a barra de progresso um pouquinho.
            progress.update(tarefa_de_salvamento, advance=1.5)

            # pequena pausa para ver a animação.
            time.sleep(0.02) 
            
    console.print("\n[magenta3]Agenda Exportada para CSV com sucesso!")

#Função que chamas as outras para exportar
def exporta_lista(agenda_de_contatos):
    desenhar_cabecalho("Exportar Agenda")
    console.print("[dark_slate_gray1][1] Exportar para JSON.")
    console.print("[dark_slate_gray1][2] Exportar para CSV.")
    console.print()
    console.print("[magenta3]Digite uma das opções 1 ou 2, e pressione 'ENTER'. ")

    escolha_usuario = input("--> ")

    if escolha_usuario == "1":
        exportar_json(agenda_de_contatos)

    elif escolha_usuario == "2":
        exportar_csv(agenda_de_contatos)

    else:
        console.print("Você não digitou 1 ou 2 !!!")
    input("\nPressione Enter para voltar ao menu...")