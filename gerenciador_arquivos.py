import interface_usuario
import time
from rich.progress import Progress # barra de progresso
import csv # exportar para CSV
import json # exportar par JSON
import os


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
        interface_usuario.console.print("\nArquivo de contatos não encontrado. Começando com uma agenda nova.")
    return lista_de_contatos_carregada # retorna a lista de contatos

# Função para salvar os contato em um arquivo
def salvar_agenda(agenda_de_contatos):
    #Salva os contatos na contatos.txt
    with open('contatos.txt', 'w', encoding='utf-8') as arquivo: # abre o contatos.txt em modo escrita
        for contato in agenda_de_contatos:
            arquivo.write(f"{contato['nome']},{contato['telefone']},{contato['email']}\n") # escreve os contatos 

    #barra de progresso
    interface_usuario.console.print()
    with Progress() as progress:
        
        
        tarefa_de_salvamento = progress.add_task("[magenta3]Salvando...", total=100) # total da barra 

       
        while not progress.finished: # enquanto não finaliza a barra nao termina o loop
            
            # Avança a barra de progresso um pouquinho.
            progress.update(tarefa_de_salvamento, advance=1.5)

            # pequena pausa para ver a animação.
            time.sleep(0.02) 
    interface_usuario.console.print("\n[magenta3]Agenda salva com sucesso!")
    interface_usuario.console.print("O programa será encerrado.")
    time.sleep(1)
    print("\nO programa encerrou ")

#Função para exporta a agenda para JSON
def exportar_json(agenda_de_contatos):
    with open('contatos.json', 'w', encoding='utf-8') as arquivo_json:
            json.dump(agenda_de_contatos, arquivo_json, indent=4, ensure_ascii=False)
    interface_usuario.console.print()
    with Progress() as progress:
        
        
        tarefa_de_salvamento = progress.add_task("[magenta3]Salvando...", total=100) # total da barra 

       
        while not progress.finished: # enquanto não finaliza a barra nao termina o loop
            
            # Avança a barra de progresso um pouquinho.
            progress.update(tarefa_de_salvamento, advance=1.5)

            # pequena pausa para ver a animação.
            time.sleep(0.02) 
        
    caminho_completo = os.path.abspath("contatos.json")
    interface_usuario.console.print("\n[magenta3]Agenda Exportada para JSON com sucesso!")
    interface_usuario.console.print(f"Arquivo salvo em [cyan]{caminho_completo}")
            
#Função para exportar a agenda para CSV
def exportar_csv(agenda_de_contatos):
    cabecalhos = ['nome', 'telefone', 'email']
    with open('contatos.csv', 'w', encoding='utf-8', newline='') as arquivo_csv:
            escritor = csv.DictWriter(arquivo_csv, fieldnames=cabecalhos)
            escritor.writeheader()
            escritor.writerows(agenda_de_contatos)
    interface_usuario.console.print()
    with Progress() as progress:
        
        
        tarefa_de_salvamento = progress.add_task("[magenta3]Salvando...", total=100) # total da barra 

       
        while not progress.finished: # enquanto não finaliza a barra nao termina o loop
            
            # Avança a barra de progresso um pouquinho.
            progress.update(tarefa_de_salvamento, advance=1.5)

            # pequena pausa para ver a animação.
            time.sleep(0.02) 
    caminho_completo = os.path.abspath("contatos.csv")
    interface_usuario.console.print("\n[magenta3]Agenda Exportada para CSV com sucesso!")
    interface_usuario.console.print(f"Arquivo salvo em [cyan]{caminho_completo}")
