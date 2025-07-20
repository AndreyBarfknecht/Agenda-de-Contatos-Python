import interface_usuario
import re # colocar padão nas info

#padao nome
# Padrão que aceita letras de a-z, A-Z, caracteres acentuados e espaços.
PADRAO_NOME = r"^[a-zA-Záàâãéèêíïóôõöúçñ ]+$" # padrão do nome 
PADRAO_TELEFONE = r"^[\d\s()-]+$" # padrão nome /d = digitos 0 - 9 /s = espaço
PADRAO_EMAIL = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$" # Garante que as partes do e-mail contenham caracteres válidos.

def nome_padrao():
    while True: # loop do nome
            nome_digitado = input("Qual o nome do contato --> ") # usuário digita o nome 
            if not nome_digitado.strip(): # verifica se o nome não está vazio
                interface_usuario.console.print("[magenta]O nome não pode estar vazio!!!")
                continue

            if not re.match(PADRAO_NOME, nome_digitado): # verifica se o nome não tem caracteres especiais
                interface_usuario.console.print("[magenta]O nome contém caracteres especiais. Use apenas letras e espaços")
                continue
            break
    return nome_digitado
    
def telefone_padrao():
    while True: # loop do telefone
        telefone_digitado = input("Qual o telefone --> ") # usuário digita o telefone
        if not telefone_digitado.strip(): # verifica se não está em branco
            interface_usuario.console.print("[magenta]O telefone não pode estar vazio!!!")
            continue
        #telefone_digitado = input("Qual o telefone --> ") # usuário digita o telefone
        if not re.match(PADRAO_TELEFONE, telefone_digitado): # verifica se está no pradão
            interface_usuario.console.print("[magenta]O telefone contém letras ou caracteres especiais. Use apenas números e espaços")
            continue
        break
    return telefone_digitado

def email_padrao():
    while True: # loop do email 
        email_digitado = input("Qual o email --> ") # usuário digita o email
        if not email_digitado.strip():
            interface_usuario.console.print("[magenta]O email não pode estar vazio!!!")
            continue
            #email_digitado = input("Qual o email --> ") # usuário digita o email
        if not re.match(PADRAO_EMAIL, email_digitado):
            interface_usuario.console.print("[magenta]Formato de e-mail inválido. Por favor, tente novamente.")
            continue
        break
    return email_digitado