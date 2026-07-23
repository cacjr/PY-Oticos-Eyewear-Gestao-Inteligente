from datetime import datetime
import random

from venda import Venda
from funcoes_estoque import buscar_produto


def registrar_venda(lista_produtos, lista_vendas):
    print("\n===== REGISTRAR VENDA =====")

    codigo_produto = input("Digite o codigo do produto: ")
    produto = buscar_produto(lista_produtos, codigo_produto)

    if produto is None:
        print("Produto nao encontrado.")
        return

    print(f"\nProduto encontrado: {produto.nome}")
    print(f"Preco: R$ {produto.preco:.2f}")
    print(f"Estoque disponivel: {produto.quantidade}")

    try:
        quantidade = int(input("Digite a quantidade vendida: "))

        if quantidade <= 0:
            print("Quantidade invalida.")
            return

        if quantidade > produto.quantidade:
            print(f"Erro: estoque insuficiente. Disponivel: {produto.quantidade}")
            return

        print("\nDeseja aplicar desconto?")
        print("1 - Sim")
        print("2 - Nao")
        opcao_desconto = int(input("Opcao: "))

        desconto = 0
        if opcao_desconto == 1:
            desconto = float(input("Digite o percentual de desconto (ex: 10 para 10%): "))
            if desconto < 0 or desconto > 100:
                print("Desconto invalido. Nenhum desconto sera aplicado.")
                desconto = 0

        subtotal = produto.preco * quantidade
        valor_desconto = subtotal * (desconto / 100)
        total = subtotal - valor_desconto

        print(f"\nSubtotal: R$ {subtotal:.2f}")
        if desconto > 0:
            print(f"Desconto ({desconto}%): R$ {valor_desconto:.2f}")
        print(f"Total a pagar: R$ {total:.2f}")

        confirmar = input("\nConfirmar venda? (S/N): ").upper()

        if confirmar != "S":
            print("Venda cancelada.")
            return

        produto.remover_estoque(quantidade)

        codigo_venda = f"VENDA_{datetime.now().strftime('%Y%m%d%H%M%S')}_{random.randint(100, 999)}"

        nova_venda = Venda(
            codigo_venda,
            produto.codigo,
            produto.nome,
            quantidade,
            produto.preco,
            desconto,
            total,
            datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        )

        lista_vendas.append(nova_venda)
        nova_venda.exibir_recibo()
        print("Venda registrada com sucesso!")

    except ValueError:
        print("Erro: digite valores numericos validos.")


def relatorio_vendas(lista_vendas):
    print("\n===== RELATORIO DE VENDAS =====")

    if len(lista_vendas) == 0:
        print("Nenhuma venda registrada ainda.")
        return

    total_faturado = 0
    total_itens_vendidos = 0

    for venda in lista_vendas:
        print(f"\nVenda: {venda.codigo_venda}")
        print(f"Data: {venda.data_hora}")
        print(f"Produto: {venda.nome_produto}")
        print(f"Quantidade: {venda.quantidade}")
        print(f"Preco unitario: R$ {venda.preco_unitario:.2f}")
        if venda.desconto_percentual > 0:
            print(f"Desconto: {venda.desconto_percentual}%")
        print(f"Total: R$ {venda.total:.2f}")
        print("-" * 30)

        total_faturado += venda.total
        total_itens_vendidos += venda.quantidade

    print("\n===== RESUMO DAS VENDAS =====")
    print(f"Total de vendas realizadas: {len(lista_vendas)}")
    print(f"Total de itens vendidos: {total_itens_vendidos}")
    print(f"Faturamento total: R$ {total_faturado:.2f}")


def salvar_vendas(lista_vendas, nome_arquivo):
    try:
        with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
            for venda in lista_vendas:
                arquivo.write(venda.to_string_arquivo())
        print("Vendas salvas com sucesso!")
    except Exception as erro:
        print(f"Erro ao salvar vendas: {erro}")


def carregar_vendas(nome_arquivo):
    lista_vendas = []

    try:
        with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                dados = linha.strip().split(";")
                if len(dados) == 8:
                    venda = Venda(
                        dados[0], dados[1], dados[2], int(dados[3]),
                        float(dados[4]), float(dados[5]), float(dados[6]), dados[7]
                    )
                    lista_vendas.append(venda)

    except FileNotFoundError:
        print("Arquivo de vendas nao encontrado.")

    return lista_vendas
