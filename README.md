# Óticos Eyewear - Sistema de Gestão de Estoque

Sistema desenvolvido em **Python** para gerenciamento de estoque, vendas e controle financeiro de uma ótica. O projeto permite cadastrar produtos, registrar vendas, controlar movimentações do estoque e gerar relatórios completos.

---

## Funcionalidades

O sistema oferece as seguintes funcionalidades:

- Cadastro de produtos
- Listagem de produtos cadastrados
- Atualização de estoque
- Remoção de produtos
- Busca de produtos por código
- Verificação automática de estoque baixo
- Registro de vendas
- Relatório de vendas
- Histórico de movimentações
- Relatório completo de estoque
- Relatório financeiro
- Salvamento automático dos dados em arquivos `.txt`

---

## Estrutura do Projeto

```
sistema_estoque_vendas/
│
├── __pycache__/
├── funcoes_estoque.py
├── funcoes_vendas.py
├── historico.py
├── produto.py
├── venda.py
├── main.py
│
├── produtos.txt
├── vendas.txt
└── historico.txt
```

### Arquivos

| Arquivo | Descrição |
|----------|-----------|
| `main.py` | Arquivo principal do sistema |
| `funcoes_estoque.py` | Funções relacionadas ao gerenciamento do estoque |
| `funcoes_vendas.py` | Funções responsáveis pelo registro e controle das vendas |
| `historico.py` | Controle das movimentações realizadas no sistema |
| `produto.py` | Classe Produto |
| `venda.py` | Classe Venda |
| `produtos.txt` | Banco de dados dos produtos |
| `vendas.txt` | Banco de dados das vendas |
| `historico.txt` | Histórico das movimentações |

---

# Menu do Sistema

Ao executar o programa, o seguinte menu será apresentado:

```
========================================
         OPTICOS EYEWEAR
   SISTEMA DE GESTAO DE ESTOQUE
========================================

1  - Cadastrar produto
2  - Listar produtos
3  - Atualizar estoque
4  - Remover produto
5  - Verificar estoque baixo
6  - Buscar produto
7  - Relatorio de estoque
8  - Registrar venda
9  - Relatorio de vendas
10 - Historico de movimentacoes
11 - Relatorio financeiro completo
12 - Salvar dados
13 - Sair
========================================
```

---

# Persistência de Dados

O sistema utiliza arquivos de texto para armazenar as informações:

- **produtos.txt**
  - Produtos cadastrados

- **vendas.txt**
  - Histórico de vendas

- **historico.txt**
  - Todas as movimentações realizadas no estoque

Os dados são carregados automaticamente ao iniciar o sistema e salvos sempre que solicitado ou ao encerrar a aplicação.

---

# Relatórios Disponíveis

O sistema disponibiliza diversos relatórios para facilitar a gestão da ótica.

### Relatório de Estoque

Exibe:

- Produtos cadastrados
- Quantidade disponível
- Valor unitário
- Produtos com estoque baixo

---

### Relatório Financeiro

Apresenta informações como:

- Total de vendas
- Receita obtida
- Produtos vendidos
- Movimentações registradas
- Situação atual do estoque

---

### Histórico de Movimentações

Registra automaticamente:

- Cadastro de produtos
- Atualizações de estoque
- Remoções
- Vendas realizadas

---

# Como Executar

## 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/sistema-estoque-vendas.git
```

## 2. Acesse a pasta

```bash
cd sistema-estoque-vendas
```

## 3. Execute o programa

```bash
python main.py
```

---

# Requisitos

- Python 3.10 ou superior

Não é necessária a instalação de bibliotecas externas.

---

# Tecnologias Utilizadas

- Python
- Programação Orientada a Objetos (POO)
- Manipulação de Arquivos
- Modularização
- Tratamento de Exceções

---

# Conceitos Aplicados

Durante o desenvolvimento foram utilizados diversos conceitos da linguagem Python, como:

- Organização modular do código
- Classes e Objetos
- Encapsulamento
- Manipulação de listas
- Persistência em arquivos
- Tratamento de erros
- Estruturas condicionais
- Estruturas de repetição
- Funções
- Boas práticas de programação

---

# Objetivo

Desenvolver uma aplicação simples, organizada e funcional para auxiliar no controle de estoque e vendas de uma ótica, permitindo uma gestão eficiente dos produtos e do fluxo financeiro.
