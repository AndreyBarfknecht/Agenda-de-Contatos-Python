"""Agenda de Contatos Simples
Permite cadastrar contatos com nome, telefone e e-mail. O usuário pode listar, buscar e remover
contatos. Trabalha com listas, dicionários e pode incluir armazenamento em arquivo."""

import interface_usuario
import gerenciador_arquivos


#Lista de contatos 
agenda_de_contatos = gerenciador_arquivos.carregar_contatos() # Função para carregar os contatos do arquivo.txt

# começo do programa
while True:
    interface_usuario.desenhar_cabecalho("Agenda de Contatos")

    # Imprime o menu usando o interface_usuario.console do rich
    interface_usuario.console.print("[dark_slate_gray1][1] Adicionar Contato.")
    interface_usuario.console.print("[dark_slate_gray1][2] Listar Contatos.")
    interface_usuario.console.print("[dark_slate_gray1][3] Buscar Contato.")
    interface_usuario.console.print("[dark_slate_gray1][4] Remover Contato.")
    interface_usuario.console.print("[dark_slate_gray1][5] Editar Contato.")
    interface_usuario.console.print("[dark_slate_gray1][6] Exportar agenda para outros formatos.")
    interface_usuario.console.print("[dark_slate_gray1][7] Salvar e Sair.")
    interface_usuario.console.print() # Linha em branco
    interface_usuario.console.print("[magenta3]Digite uma das opções 1-6, e pressione 'ENTER'. ")
    escolha_usuario = input("--> ")
   
    #escolha do usuario
    if escolha_usuario == "1":
        interface_usuario.criar_contato(agenda_de_contatos)
    elif escolha_usuario =="2":
        interface_usuario.listar_contatos(agenda_de_contatos)
    elif escolha_usuario == "3":
        interface_usuario.buscar_contato(agenda_de_contatos)
    elif escolha_usuario == "4":
        interface_usuario.remover_contato(agenda_de_contatos)
    elif escolha_usuario == "5":
        interface_usuario.editar_contato(agenda_de_contatos)
    elif escolha_usuario == "6":
        interface_usuario.exporta_lista(agenda_de_contatos)
    elif escolha_usuario == "7":
        gerenciador_arquivos.salvar_agenda(agenda_de_contatos)
        break # Fim do programa
    else:
        interface_usuario.console.print("\n----------------------------------------------")
        interface_usuario.console.print("Por favor digite uma das opções acima (1 - 6) ")
        interface_usuario.console.print("----------------------------------------------")
        input("\nPressione Enter para voltar ao menu...")

