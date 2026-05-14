# 📊 Sistema de Gestão de Clientes (CRUD)

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![SQLite](https://img.shields.io/badge/SQLite-Database-lightgrey?style=for-the-badge&logo=sqlite)

Este é um sistema de gerenciamento de clientes via linha de comando (CLI) desenvolvido em Python. O projeto demonstra a integração entre a lógica de programação, menus interativos e a persistência de dados utilizando um banco de dados relacional (**SQLite3**).

O projeto foi construído com uma arquitetura modularizada, separando as responsabilidades de banco de dados, regras de negócio e interface com o usuário, preparando o terreno para frameworks web mais avançados como o Django.

---

## ✨ Funcionalidades (CRUD)

O sistema possui um menu interativo em *loop* infinito que oferece as seguintes operações:

- **[C]reate (Cadastrar):** Adiciona novos clientes (Nome e E-mail) ao banco de dados com prevenção contra *SQL Injection*.
- **[R]ead (Listar):** Busca e exibe todos os clientes cadastrados formatados na tela.
- **[U]pdate (Atualizar):** Permite buscar um cliente pelo seu ID e atualizar o seu endereço de e-mail.
- **[D]elete (Excluir):** Remove permanentemente um registro do banco de dados através do seu ID.

---

## 📂 Estrutura do Projeto

O código fonte foi refatorado em múltiplos arquivos para garantir uma melhor organização e manutenção (separação de responsabilidades):

```text
📁 projeto_gestao/
│
├── 📄 main.py          # Arquivo principal: controla o menu, limpa a tela e gerencia o fluxo do usuário.
├── 📄 clientes.py      # Regras de negócio: contém as 4 funções principais do CRUD.
├── 📄 banco.py         # Configuração de dados: gerencia a conexão com o SQLite e cria a tabela.
├── 📄 empresa.db       # Arquivo do banco de dados (gerado automaticamente na primeira execução).
└── 📄 README.md        # Documentação do projeto.
```

---

## 🚀 Como Executar o Projeto

### Pré-requisitos
- Ter o **Python 3.x** instalado em sua máquina.
- Nenhuma biblioteca externa é necessária, pois o `sqlite3` e o `os` são nativos do Python.

### Passo a Passo

1. Faça o clone deste repositório ou baixe os arquivos fonte.
2. Abra o terminal (ou prompt de comando) e navegue até a pasta do projeto:
   ```bash
   cd caminho/para/a/pasta/projeto_gestao
   ```
3. Execute o arquivo principal:
   ```bash
   python main.py
   ```
4. O sistema criará o arquivo `empresa.db` automaticamente e o menu será exibido na tela.

---

## 🎯 Desafios para Aprimoramento

Este projeto base pode ser expandido! Aqui estão algumas ideias de implementações futuras (níveis de dificuldade progressiva):

- **Nível 1:** Adicionar confirmação (S/N) antes de excluir um cliente e criar um filtro de busca por nome.
- **Nível 2:** Validar a duplicidade de e-mails na hora do cadastro e permitir atualizações parciais (ex: atualizar só o nome, mantendo o e-mail intacto).
- **Nível 3:** Adicionar novos campos (como "Telefone") e implementar o conceito de *Soft Delete* (mudar o status para inativo em vez de apagar do banco).

---

Feito com 💻 e ☕ durante a Formação Python & Django!