
import os
import pyfiglet
from rich.console import Console # deixa as linha coloridas
from rich.panel import Panel
from rich.table import Table
import time 
from rich.progress import Progress 
import json
import csv
# Crie um objeto console para usar o rich
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
    
    # Imprime o título em verde e dentro de um painel
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
    telefone_digitado = input("Qual o telefone --> ") # usuário digita o telefone
    email_digitado = input("Qual o email --> ") # usuário digita o email

    novo_contato = { # dicionario 
        'nome': nome_digitado,  
        'telefone': telefone_digitado,
        'email': email_digitado
    }

    agenda_de_contatos.append(novo_contato) # adicionar contato 
    console.print(f"\n----Novo contato {nome_digitado} salvo----")
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
    
    for contato in agenda_de_contatos:
        
        if contato ['nome'] == nome_buscado:
            # Cria a tabela
            tabela = Table(title="Contato Encontrado", show_header=True, header_style="magenta3")
        
            # Adiciona as colunas
            tabela.add_column("Nome", style="dark_slate_gray1", width=20)
            tabela.add_column("Telefone", style="dark_slate_gray1", width=20)
            tabela.add_column("E-mail", style="dark_slate_gray1")

            # A LINHA QUE FALTAVA: Adiciona os dados do contato encontrado
            tabela.add_row(contato['nome'], contato['telefone'], contato['email'])
            
            # Agora sim, imprime a tabela preenchida
            console.print(tabela)
            break

    else:
        console.print("\n------------------------------")
        console.print(f"Contato {nome_buscado} não foi encontrado")
        
    input("\nPressione Enter para voltar ao menu...")


#Função para remover contato
def remover_contato(agenda_de_contatos):
    desenhar_cabecalho("Remover um contato")

    console.print("Escreva e pressione 'ENTER'")    
    nome_buscado = input("Qual o nome do contato que você quer remover --> ")

    for contato in agenda_de_contatos: # loop para verificar se o contato existe
        if contato ['nome'] == nome_buscado:
            agenda_de_contatos.remove(contato) # remove o contato inteiro
            console.print(f"\nContato {nome_buscado} foi removido com sucesso")
            console.print("\n------------------------------")
            break
    else:
        console.print("\n------------------------------")
        console.print(f"Contato {nome_buscado} não foi encontrado")
    input("\nPressione Enter para voltar ao menu...")

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

def exportar_json(agenda_de_contatos):
    with open('contatos.json', 'w', encoding='utf-8') as arquivo_json:
            json.dump(agenda_de_contatos, arquivo_json, indent=4, ensure_ascii=False)
            console.print("\n[magenta3]Agenda Exportada para JSON com sucesso!")
            


def exportar_csv(agenda_de_contatos):
    cabecalhos = ['nome', 'telefone', 'email']
    with open('contatos.csv', 'w', encoding='utf-8', newline='') as arquivo_csv:
            escritor = csv.DictWriter(arquivo_csv, fieldnames=cabecalhos)
            escritor.writeheader()
            escritor.writerows(agenda_de_contatos)
            console.print("\n[magenta3]Agenda Exportada para CSV com sucesso!")




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

    input("\nPressione Enter para voltar ao menu...")


