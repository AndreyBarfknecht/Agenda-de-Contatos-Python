import os # descobrir o sistema OP
import pyfiglet # gerar o titulo em ASCII
from rich.table import Table # para listar os contatos dentro de uma tabela
from rich.panel import Panel # imprime o logo ASCII dentro de um painel
from rich.console import Console # deixa as linha coloridas
import gerenciador_arquivos
import validadores

console = Console() 




# Função para dar clear na tela
def limpar_tela():
    # Verifica se o sistema operacional é Windows ('nt') ou outro (Linux/macOS)
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

# Função para desenhar o nome em ASCII
def desenhar_cabecalho(texto_do_titulo):
    """Limpa a tela e desenha um cabeçalho estilizado."""
    limpar_tela() 
    
    # Gera o texto em ASCII Art
    titulo_ascii = pyfiglet.figlet_format(texto_do_titulo, font="slant")
    
    # Imprime o título  dentro de um painel
    console.print(Panel.fit(f"[bright_blue]{titulo_ascii}[/]", subtitle="[Andrey]"))
    console.print() # Imprime uma linha em branco para dar espaço



# função para criar novo contato
def criar_contato(agenda_de_contatos):
    desenhar_cabecalho("Criar Contato")
    console.print("Escreva e pressione 'ENTER'")
    
    #Perguntas no padrão
    nome_recebido = validadores.nome_padrao()
    telefone_recebido = validadores.telefone_padrao()
    email_recebido = validadores.email_padrao()

    novo_contato = { # dicionario 
        'nome': nome_recebido,
        'telefone': telefone_recebido,
        'email': email_recebido
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
        console.print(f"[magenta3]\n----Novo contato {nome_recebido} salvo----")
        
    input("\nPressione Enter para voltar ao menu...")

# Função para listar os nomes 
def listar_contatos(agenda_de_contatos):
    desenhar_cabecalho("Lista de Contatos")
    # Limpa a tela e desenha o cabeçalho para esta "página"
    
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
        #valores recebidos do validadores.py
    
    desenhar_cabecalho("Buscar Contato")

    while True: # loop principal
        console.print("Escreva e pressione 'ENTER'")
        
        nome_recebido = validadores.nome_padrao()


        resultados_encontrados = [] # lista de resultados encontrados

        for contato in agenda_de_contatos:
            
            if nome_recebido.lower() == contato['nome'].lower(): # busca pelo nome tanto com letra maiúsculas/minúsculas
                resultados_encontrados.append(contato) # adiciona a lista de resultados_encontrados
            
        if resultados_encontrados: # se achar contato
        # Cria a tabela
            tabela = Table(title=f"\n[bright_blue]Contato(s) Encontrados com o nome [magenta3]{nome_recebido}", show_header=True, header_style="magenta3")
        
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
            console.print(f"Contato {nome_recebido} não foi encontrado")
            

        console.print()
        continuar = console.input("[yellow]Deseja fazer uma nova busca? (s/n) --> ").lower()
        if continuar != "s":
            break
        #input("\nPressione Enter para voltar ao menu...")
        limpar_tela()
        desenhar_cabecalho("Buscar Contato")

#Função para remover contato
def remover_contato(agenda_de_contatos):
        #valores recebidos do validadores.py

    desenhar_cabecalho("Remover um contato") # desenha o nome gigante
    while True:
        console.print("Escreva e pressione 'ENTER'")    
        nome_recebido = validadores.nome_padrao()


        resultados_encontrados = [] # lista de resultados encontrados

        for contato in agenda_de_contatos: #loop para buscar os contatos encontrados
            
            if nome_recebido.lower() == contato['nome'].lower(): # busca pelo nome tanto com letra maiúsculas/minúsculas
                resultados_encontrados.append(contato) # adiciona a lista de resultados_encontrados

        if len (resultados_encontrados) == 0: # se não tiver nenhum contato com o nome buscado 
                console.print(f"\n[yellow]Nenhum contato encontrado com o termo '{nome_recebido}'.[/yellow]")

        elif len (resultados_encontrados) == 1: # se tem 1 contato com esse
        
            # cria tabela
            tabela = Table(title=f"\n[bright_blue]Contato Encontrados com o nome {nome_recebido}", show_header=True, header_style="magenta3")
            # Adiciona as colunas
            tabela.add_column("Nome", style="dark_slate_gray1", width=20)
            tabela.add_column("Telefone", style="dark_slate_gray1", width=20)
            tabela.add_column("E-mail", style="dark_slate_gray1")
            for contato in resultados_encontrados: # passa pela lista de resultados e adiciona a tabela
                tabela.add_row(contato['nome'], contato['telefone'], contato['email'])
            console.print(tabela) # imprime a tabela
            console.print("[magenta3]Tem certeza que deseja remover este contato? (s/n)")
            confirmacao = console.input(f"\nDigite 's' pra remover o contato ou 'n' para não remover o contato na lista\n --> ")
            if confirmacao.lower() == "s": # se o usuario quiser remover
                contato_para_remover = resultados_encontrados[0] # define o contato para remover
                agenda_de_contatos.remove(contato_para_remover) # remove o contato
                console.print(f"\n[magenta3]Contato foi removido com sucesso")
            else:
                console.print("\n[magenta3]Contato não foi removido") # se nao for removido

        
        # se foir encontrado mais de 1 contato com o mesmo nome
        else:
            console.print("[yellow]Vários contatos foram encontrados. Por favor, escolha qual deles remover:[/yellow]")
            # cria tabela
            tabela = Table(title=f"\n[bright_blue]Contatos Encontrados com o nome [magenta3]{nome_recebido}", show_header=True, header_style="magenta3")
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

                        console.print(f"[bold yellow]Você escolheu remover o contato:[/bold yellow] [white]{contato_para_remover['nome']}[/white]")
                        confirmacao = input("Tem certeza absoluta? (s/n) --> ").lower()
                   
                        if confirmacao == 's':
                        # Se SIM, agora sim execute a remoção
                            agenda_de_contatos.remove(contato_para_remover)
                            console.print(f"\n[bold green]Contato '{contato_para_remover['nome']}' removido com sucesso![/bold green]")
                        else:
                        # Se NÃO, apenas avise que a operação foi cancelada
                            console.print("[cyan]Remoção cancelada pelo usuário.[/cyan]")
                        
                        break

                    else:
                    # O usuário digitou um número, mas está fora do intervalo válido
                        console.print(f"[bold red]Escolha inválida. Por favor, digite um número entre 1 e {len(resultados_encontrados)}.[/bold red]")

                except ValueError:
                # Se o int() falhar, significa que o usuário não digitou um número
                    console.print("[bold red]Entrada inválida. Por favor, digite apenas o número correspondente.[/bold red]")

        console.print() 
        continuar = console.input("[yellow]Deseja fazer uma nova busca? (s/n) --> ").lower() # se quiser repetir a def
        if continuar != "s":
            break
        #input("\nPressione Enter para voltar ao menu...")
        limpar_tela()
        desenhar_cabecalho("Remover Contato")

def editar_contato(agenda_de_ceontato):
        #valores recebidos do validadores.py
    desenhar_cabecalho("Editar contato")
    
    while True:
        console.print("Escreva e pressione 'ENTER'")    

        nome_recebido = validadores.nome_padrao()

        resultados_encontrados = []

        for contato in agenda_de_ceontato:
            if nome_recebido.lower() == contato['nome'].lower():
                resultados_encontrados.append(contato)

        if len (resultados_encontrados) == 0:
            console.print(f"\n[yellow]Nenhum contato encontrado com o termo '{nome_recebido}'.[/yellow]")
            #input("\n Pressione enter para voltar ao menu...")


        elif len (resultados_encontrados) == 1:
            # cria tabela
            tabela = Table(title=f"\n[bright_blue]Contato Encontrados com o nome {nome_recebido}", show_header=True, header_style="magenta3")
            # Adiciona as colunas
            tabela.add_column("Nome", style="dark_slate_gray1", width=20)
            tabela.add_column("Telefone", style="dark_slate_gray1", width=20)
            tabela.add_column("E-mail", style="dark_slate_gray1")
            for contato in resultados_encontrados: # passa pela lista de resultados e adiciona a tabela
                tabela.add_row(contato['nome'], contato['telefone'], contato['email'])
                console.print(tabela)
            #console.print("[magenta3]Tem certeza que deseja editar este contato (s/n)")
            confirmacao = console.input(f"\nDigite 's' pra editar o contato ou 'n' para não editar.\n --> ")
            if confirmacao.lower() == "s":
                desenhar_cabecalho(f"Contato {nome_recebido}")
                contato_para_editar = resultados_encontrados[0]
                while True:
                    console.print(f"nome: {contato['nome']}\ntelefone: {contato['telefone']}\nemail: {contato['email']}")
                    console.print(f"\nO que você deseja editar?")
                    console.print("[1] - Nome")
                    console.print("[2] - Telefone")
                    console.print("[3] - Email")
                    console.print("[4] Salvar e voltar ao menu principal")
                    escolha = console.input("Digite uma das opçoes 1-4, e pressione 'ENTER'\n-->")
                    if escolha == "1":
                        desenhar_cabecalho("Novo\nNome")
                        console.print("Escreva e pressione 'ENTER'\n")
                        nome_recebido = validadores.nome_padrao()
                        contato_para_editar['nome'] = nome_recebido
                        console.print("\n[yellow]Sucesso, nome atualizado")
                        input("\nPressione enter para voltar...")
                        limpar_tela()
                        desenhar_cabecalho(f"Contato {nome_recebido}")

                    elif escolha == "2":
                        desenhar_cabecalho("Novo\nTelefone")
                        console.print("Escreva e pressione 'ENTER'\n")
                        telefone_recebido = validadores.telefone_padrao()
                        contato_para_editar['telefone'] = telefone_recebido
                        console.print("\n[yellow]Sucesso, telefone atualizado")
                        input("\nPressione enter para voltar ao menu...")
                        limpar_tela()
                        desenhar_cabecalho(f"Contato {nome_recebido}")

                    elif escolha == "3":
                        desenhar_cabecalho("Novo\nEmail")
                        console.print("Escreva e pressione 'ENTER'\n")
                        email_recebido = validadores.email_padrao()
                        contato_para_editar['email'] = email_recebido
                        console.print("\n[yellow]Sucesso, email atualizado")
                        input("\nPressione enter para voltar ao menu...")
                        limpar_tela()
                        desenhar_cabecalho(f"Contato {nome_recebido}")

                    elif escolha == "4":
                        console.print("\n[yellow]Contato Salvo")
                        #input("\nPressione enter para voltar ao menu...")
                        break

                    else:
                        console.print("Operação invalida")

            """console.print() 
            continuar = console.input("[yellow]Deseja fazer uma nova busca? (s/n) --> ").lower() # se quiser repetir a def
            if continuar != "s":
            break
            #input("\nPressione Enter para voltar ao menu...")
            limpar_tela()
            desenhar_cabecalho("Remover Contato")"""

        else:

            console.print("[yellow]Vários contatos foram encontrados. Por favor, escolha qual deles quer editar:[/yellow]")
            # cria tabela
            tabela = Table(title=f"\n[bright_blue]Contatos Encontrados com o nome [magenta3]{nome_recebido}", show_header=True, header_style="magenta3")
            # Adiciona as colunas
            tabela.add_column("Número",style="dark_slate_gray1", width=20)
            tabela.add_column("Nome", style="dark_slate_gray1", width=20)
            tabela.add_column("Telefone", style="dark_slate_gray1", width=20)
            tabela.add_column("E-mail", style="dark_slate_gray1")
            for indice, contato in enumerate(resultados_encontrados): #lopp para adicionar os contatos na tabela
                tabela.add_row(str(indice + 1), contato['nome'], contato['telefone'], contato['email'])
            
        

            while True:
                limpar_tela()
                desenhar_cabecalho("Editar Contato")
                console.print(tabela)
                escolha_str = console.input ("Digite o 'Número' do contato que você quer editar ou digite '0' para cancelar\n--> ")


                try:
                #  converte a escolha para um número inteiro
                    escolha_num = int(escolha_str)

                # Verifica se o usuário quer cancelar
                    if escolha_num == 0:
                        console.print("[cyan]Operação cancelada.[/cyan]")
                        break
                
                # Verifica se o número está no intervalo correto
                    elif 1 <= escolha_num <= len(resultados_encontrados):
                        contato_para_editar = resultados_encontrados[escolha_num - 1]
                    
                    # Pega o índice correto (usuário digita 1, que é o índice 0)
                        #indice_para_editar = escolha_num - 1
                        #contato_alvo = resultados_encontrados[indice_para_editar]

                    while True:
                        limpar_tela()
                        desenhar_cabecalho("Editar contato")

                        console.print(f"\nnome: {contato_para_editar['nome']}\ntelefone: {contato_para_editar['telefone']}\nemail: {contato_para_editar['email']}")
                        console.print(f"\nO que você deseja editar?")
                        console.print("[1] - Nome")
                        console.print("[2] - Telefone")
                        console.print("[3] - Email")
                        console.print("[4] Salvar e voltar ao menu principal")
                        escolha = console.input("Digite uma das opçoes 1-4, e pressione 'ENTER'\n-->")
                        if escolha == "1":
                            desenhar_cabecalho("Novo\nNome")
                            console.print("Escreva e pressione 'ENTER'\n")
                            nome_recebido = validadores.nome_padrao()
                            contato_para_editar['nome'] = nome_recebido
                            console.print("\n[yellow]Sucesso, nome atualizado")
                            input("\nPressione enter para voltar...")
                            limpar_tela()
                            desenhar_cabecalho(f"Contato {nome_recebido}")

                        elif escolha == "2":
                            desenhar_cabecalho("Novo\nTelefone")
                            console.print("Escreva e pressione 'ENTER'\n")
                            telefone_recebido = validadores.telefone_padrao()
                            contato_para_editar['telefone'] = telefone_recebido
                            console.print("\n[yellow]Sucesso, telefone atualizado")
                            input("\nPressione enter para voltar ao menu...")
                            limpar_tela()
                            desenhar_cabecalho(f"Contato {nome_recebido}")

                        elif escolha == "3":
                            desenhar_cabecalho("Novo\nEmail")
                            console.print("Escreva e pressione 'ENTER'\n")
                            email_recebido = validadores.email_padrao()
                            contato_para_editar['email'] = email_recebido
                            console.print("\n[yellow]Sucesso, email atualizado")
                            input("\nPressione enter para voltar ao menu...")
                            limpar_tela()
                            desenhar_cabecalho(f"Contato {nome_recebido}")

                        elif escolha == "4":
                            console.print("\n[yellow]Contato Salvo")
                            input("\nPressione enter para voltar ao menu...")
                            break

                        else:
                            console.print("Operação invalida")
                    
                        
                    

                        
                    #else:
                        # O usuário digitou um número, mas está fora do intervalo válido
                        #console.print(f"[bold red]Escolha inválida. Por favor, digite um número entre 1 e {len(resultados_encontrados)}.[/bold red]")

                except ValueError:
                # Se o int() falhar, significa que o usuário não digitou um número
                    console.print("[bold red]Entrada inválida. Por favor, digite apenas o número correspondente.[/bold red]")

        console.print()
        continuar = console.input("[yellow]Deseja fazer uma nova busca? (s/n) --> ").lower()
        if continuar != "s":
                break
            #input("\nPressione Enter para voltar ao menu...")
        limpar_tela()
        desenhar_cabecalho("Editar Contato")

#Função que chamas as outras para exportar
def exporta_lista(agenda_de_contatos):
    desenhar_cabecalho("Exportar Agenda")
    console.print("[dark_slate_gray1][1] Exportar para JSON.")
    console.print("[dark_slate_gray1][2] Exportar para CSV.")
    console.print()
    console.print("[magenta3]Digite uma das opções 1 ou 2, e pressione 'ENTER'. ")

    escolha_usuario = input("--> ")

    if escolha_usuario == "1":
        gerenciador_arquivos.exportar_json(agenda_de_contatos)

    elif escolha_usuario == "2":
        gerenciador_arquivos.exportar_csv(agenda_de_contatos)

    else:
        console.print("Você não digitou 1 ou 2 !!!")
    input("\nPressione Enter para voltar ao menu...")
