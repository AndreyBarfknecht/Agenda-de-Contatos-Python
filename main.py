"""9. Agenda de Contatos Simples
Permite cadastrar contatos com nome, telefone e e-mail. O usuário pode listar, buscar e remover
contatos. Trabalha com listas, dicionários e pode incluir armazenamento em arquivo."""

import funcoes

#Lista de contatos 
agenda_de_contatos = funcoes.carregar_contatos()

# começo do programa
print("\n----Bem vindo a agenda de Contatos Digital----")
while True:
    
        escolha_usuario = input(f"\n1 - Cadastrar\n2 - Listar Contatos\n3 - Buscar Contato\n4 - Remover Contato\n5 - Sair\n--> ")
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
            print("\nO programa encerrou ")
            break
    
    


