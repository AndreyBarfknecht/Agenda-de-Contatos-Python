# 📞 Agenda de Contatos Python

Uma aplicação simples e eficiente para gerenciar contatos pessoais, desenvolvida em Python como projeto acadêmico. O programa oferece uma interface de linha de comando intuitiva para adicionar, listar, buscar e remover contatos, com persistência de dados garantida.

## ✨ Funcionalidades

- ➕ **Adicionar Contatos**: Insira nome, telefone e e-mail de novos contatos
- 📋 **Listar Contatos**: Visualize todos os contatos salvos de forma organizada
- 🔍 **Buscar Contatos**: Encontre contatos específicos pelo nome
- 🗑️ **Remover Contatos**: Exclua contatos da agenda
- 💾 **Persistência Automática**: Dados salvos automaticamente em arquivo de texto
- 🔄 **Carregamento Automático**: Contatos carregados na inicialização do programa

## 🛠️ Tecnologias e Conceitos

### Linguagem
- **Python 3.x**

### Estruturas de Dados
- **Listas** (`list`) - Armazenamento do conjunto de contatos
- **Dicionários** (`dict`) - Informações individuais de cada contato

### Manipulação de Arquivos
- Leitura e escrita em arquivos `.txt`
- Gerenciador de contexto (`with open()`) para manuseio seguro

### Programação Estruturada
- Modularização em funções específicas
- Controle de fluxo com `while` e `if/elif/else`

### Tratamento de Exceções
- Blocos `try...except` para robustez da aplicação

## 📁 Estrutura do Projeto

```
agenda-de-contatos/
├── main.py          # 🚀 Arquivo principal - menu interativo
├── funcoes.py       # 🔧 Módulo com funções da agenda
└── contatos.txt     # 📄 Arquivo de persistência dos dados
```

## 🚀 Como Executar

### Pré-requisitos
- Python 3.x instalado no sistema

### Instalação e Execução

1. **Clone o repositório**
   ```bash
   git clone https://github.com/AndreyBarfknecht/Agenda-de-Contatos-Python.git
   ```

2. **Navegue até o diretório**
   ```bash
   cd Agenda-de-Contatos-Python
   ```

3. **Execute o programa**
   ```bash
   python main.py
   ```

## 🎯 Como Usar

Após executar o programa, você verá um menu interativo com as seguintes opções:

1. **Adicionar Contato** - Insira nome, telefone e e-mail
2. **Listar Contatos** - Visualize todos os contatos salvos
3. **Buscar Contato** - Encontre um contato pelo nome
4. **Remover Contato** - Exclua um contato da agenda
5. **Sair** - Encerra o programa (dados são salvos automaticamente)

## 📝 Exemplo de Uso

```
=== AGENDA DE CONTATOS ===
1. Adicionar Contato
2. Listar Contatos
3. Buscar Contato
4. Remover Contato
5. Sair

Escolha uma opção: 1

--- Adicionar Novo Contato ---
Nome: João Silva
Telefone: (11) 99999-9999
E-mail: joao@email.com

Contato adicionado com sucesso!
```

## 🎓 Objetivos Educacionais

Este projeto foi desenvolvido para demonstrar e praticar:

- Fundamentos da programação em Python
- Manipulação de estruturas de dados
- Operações de entrada/saída de arquivos
- Organização e modularização de código
- Tratamento de erros e exceções
- Interface de linha de comando
- Persistência de dados

## 📊 Status do Projeto

✅ **Concluído** - Todas as funcionalidades implementadas e testadas

## 🤝 Contribuições

Sugestões e melhorias são bem-vindas! Sinta-se à vontade para:

- Reportar bugs
- Sugerir novas funcionalidades
- Enviar pull requests
- Compartilhar feedback

## 📄 Licença

Este projeto é de uso educacional e está disponível sob licença MIT.

## 👨‍💻 Autor

**Andrey Barfknecht Rodrigues**

---

*Desenvolvido com 💙 como projeto de estudo em Python*