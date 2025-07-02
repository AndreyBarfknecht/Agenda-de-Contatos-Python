# Agenda de Contatos Simples em Python

Este é um projeto de uma agenda de contatos simples, desenvolvida em Python como parte de um estudo acadêmico. O programa permite ao usuário gerenciar contatos (nome, telefone e e-mail) através de um menu interativo no terminal.

A principal característica do projeto é a persistência de dados: os contatos são salvos em um arquivo de texto (`contatos.txt`), garantindo que as informações não sejam perdidas ao fechar o programa.

> Projeto concluído ✔️

---

##  funcionalidades

-   [x] **Adicionar Novos Contatos:** Permite ao usuário inserir nome, telefone e e-mail de um novo contato.
-   [x] **Listar Todos os Contatos:** Exibe de forma organizada todos os contatos salvos na agenda.
-   [x] **Buscar um Contato Específico:** Permite a busca de um contato pelo nome.
-   [x] **Remover um Contato:** Apaga um contato da agenda a partir do nome fornecido.
-   [x] **Salvar em Arquivo:** Salva automaticamente a lista de contatos no arquivo `contatos.txt` ao sair do programa.
-   [x] **Carregar do Arquivo:** Carrega automaticamente os contatos salvos no arquivo `contatos.txt` ao iniciar o programa.

---

## 🛠️ Tecnologias e Conceitos Utilizados

-   **Python 3**
-   **Manipulação de Estruturas de Dados:**
    -   Listas (`list`) para armazenar o conjunto de contatos.
    -   Dicionários (`dict`) para armazenar as informações de cada contato individual.
-   **Manipulação de Arquivos:**
    -   Leitura e escrita em arquivos de texto (`.txt`).
    -   Uso do gerenciador de contexto (`with open(...)`) para garantir o manuseio seguro dos arquivos.
-   **Programação Estruturada:**
    -   Modularização do código em funções para cada tarefa específica.
    -   Uso de laços de repetição (`while`) e condicionais (`if/elif/else`).
-   **Tratamento de Exceções:**
    -   Uso do bloco `try...except` para lidar com a ausência do arquivo de contatos na primeira execução.

---

## 🚀 Como Rodar o Projeto

Para executar este projeto em sua máquina local, siga os passos abaixo.

### Pré-requisitos

-   Ter o **Python 3** instalado em seu sistema.

### Passo a Passo

1.  **Clone o repositório** (ou baixe os arquivos):
    ```bash
    git clone [link-do-seu-repositorio-no-github]
    ```

2.  **Navegue até o diretório** do projeto:
    ```bash
    cd nome-da-pasta-do-projeto
    ```

3.  **Execute o programa principal**:
    ```bash
    python main.py
    ```

Após a execução, o menu interativo da agenda será exibido no seu terminal.

---

## 📂 Estrutura de Arquivos

O projeto está organizado da seguinte forma:

agenda-de-contatos/
├── main.py           # Arquivo principal que executa o programa e o menu
├── funcoes.py        # Módulo com todas as funções da agenda (criar, listar, etc.)
└── contatos.txt      # Arquivo de texto onde os contatos são salvos (criado na primeira execução)


---

## 👨‍💻 Autor

Andrey Barfknecht Rodrigues

[![LinkedIn](https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/seu-usuario-aqui/)
[![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/seu-usuario-aqui)
