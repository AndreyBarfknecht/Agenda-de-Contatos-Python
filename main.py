"""Agenda de Contatos Simples
Permite cadastrar contatos com nome, telefone e e-mail. O usuário pode listar, buscar e remover
contatos. Trabalha com listas, dicionários e pode incluir armazenamento em arquivo."""

import funcoes
from funcoes import *
#Lista de contatos 
agenda_de_contatos = funcoes.carregar_contatos() # Função para carregar os contatos do arquivo.txt

# começo do programa
while True:
    desenhar_cabecalho("Agenda de Contatos")

    # Imprime o menu usando o console do rich
    console.print("[dark_slate_gray1][1] Adicionar Contato.")
    console.print("[dark_slate_gray1][2] Listar Contatos.")
    console.print("[dark_slate_gray1][3] Buscar Contato.")
    console.print("[dark_slate_gray1][4] Remover Contato.")
    console.print("[dark_slate_gray1][5] Sair e Salvar.")
    console.print("[dark_slate_gray1][6] Exportar agenda para outros formatos.")
    console.print() # Linha em branco
    console.print("[magenta3]Digite uma das opções 1-6, e pressione 'ENTER'. ")
    escolha_usuario = input("--> ")
   
    #escolha do usuario
    if escolha_usuario == "1":
        funcoes.criar_contato(agenda_de_contatos)
    elif escolha_usuario =="2":
        funcoes.listar_contatos(agenda_de_contatos)
    elif escolha_usuario == "3":
        funcoes.buscar_contato(agenda_de_contatos)
    elif escolha_usuario == "4":
        funcoes.remover_contato(agenda_de_contatos)
    elif escolha_usuario == "5":
        funcoes.salvar_agenda(agenda_de_contatos)
        break # Fim do programa
    elif escolha_usuario == "6":
        funcoes.exporta_lista(agenda_de_contatos)
    else:
        console.print("\n----------------------------------------------")
        console.print("Por favor digite uma das opções acima (1 - 6) ")
        console.print("----------------------------------------------")
        input("\nPressione Enter para voltar ao menu...")

