from funcoes_estoque import (
    cadastrar_produto,
    listar_produtos,
    atualizar_estoque,
    remover_produto,
    verificar_estoque_baixo,
    salvar_produtos,
    carregar_produtos,
    buscar_produto_codigo,
    gerar_relatorio,
    relatorio_financeiro_completo
)
from funcoes_vendas import registrar_venda, relatorio_vendas, salvar_vendas, carregar_vendas
from historico import GerenciadorHistorico

NOME_ARQUIVO_PRODUTOS = "produtos.txt"
NOME_ARQUIVO_VENDAS = "vendas.txt"
NOME_ARQUIVO_HISTORICO = "historico.txt"


def exibir_menu():
    print("\n" + "=" * 40)
    print("         OPTICOS EYEWEAR")
    print("   SISTEMA DE GESTAO DE ESTOQUE")
    print("=" * 40)
    print("1  - Cadastrar produto")
    print("2  - Listar produtos")
    print("3  - Atualizar estoque")
    print("4  - Remover produto")
    print("5  - Verificar estoque baixo")
    print("6  - Buscar produto")
    print("7  - Relatorio de estoque")
    print("8  - Registrar venda")
    print("9  - Relatorio de vendas")
    print("10 - Historico de movimentacoes")
    print("11 - Relatorio financeiro completo")
    print("12 - Salvar dados")
    print("13 - Sair")
    print("=" * 40)


def main():
    lista_produtos = carregar_produtos(NOME_ARQUIVO_PRODUTOS)
    lista_vendas = carregar_vendas(NOME_ARQUIVO_VENDAS)
    gerenciador_historico = GerenciadorHistorico(NOME_ARQUIVO_HISTORICO)

    print("\nSistema iniciado com sucesso!")
    print(f"Produtos carregados: {len(lista_produtos)}")
    print(f"Vendas registradas: {len(lista_vendas)}")
    print(f"Movimentacoes no historico: {len(gerenciador_historico.historico)}")

    while True:
        exibir_menu()

        try:
            opcao = int(input("Escolha uma opcao: "))

            if opcao == 1:
                cadastrar_produto(lista_produtos, gerenciador_historico)

            elif opcao == 2:
                listar_produtos(lista_produtos)

            elif opcao == 3:
                atualizar_estoque(lista_produtos, gerenciador_historico)

            elif opcao == 4:
                remover_produto(lista_produtos, gerenciador_historico)

            elif opcao == 5:
                verificar_estoque_baixo(lista_produtos)

            elif opcao == 6:
                buscar_produto_codigo(lista_produtos)

            elif opcao == 7:
                gerar_relatorio(lista_produtos)

            elif opcao == 8:
                registrar_venda(lista_produtos, lista_vendas)

                # Registra a ultima venda no historico
                if len(lista_vendas) > 0:
                    ultima_venda = lista_vendas[-1]
                    gerenciador_historico.adicionar_movimentacao(
                        ultima_venda.codigo_produto,
                        ultima_venda.nome_produto,
                        "venda",
                        ultima_venda.quantidade,
                        f"Venda {ultima_venda.codigo_venda}"
                    )
                    salvar_vendas(lista_vendas, NOME_ARQUIVO_VENDAS)

            elif opcao == 9:
                relatorio_vendas(lista_vendas)

            elif opcao == 10:
                gerenciador_historico.relatorio_historico()

            elif opcao == 11:
                relatorio_financeiro_completo(lista_produtos, lista_vendas, gerenciador_historico)

            elif opcao == 12:
                salvar_produtos(lista_produtos, NOME_ARQUIVO_PRODUTOS)
                salvar_vendas(lista_vendas, NOME_ARQUIVO_VENDAS)
                gerenciador_historico.salvar_historico()

            elif opcao == 13:
                salvar_produtos(lista_produtos, NOME_ARQUIVO_PRODUTOS)
                salvar_vendas(lista_vendas, NOME_ARQUIVO_VENDAS)
                gerenciador_historico.salvar_historico()
                print("\nDados salvos com sucesso!")
                print("Sistema encerrado. Ate logo!")
                break

            else:
                print("Opcao invalida. Tente novamente.")

        except ValueError:
            print("Erro: digite um numero valido.")


if __name__ == "__main__":
    main()
