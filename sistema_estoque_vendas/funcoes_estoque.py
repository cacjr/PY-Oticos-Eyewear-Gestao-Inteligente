from produto import Produto


def buscar_produto(lista_produtos, codigo):
    for produto in lista_produtos:
        if produto.codigo == codigo:
            return produto
    return None


def cadastrar_produto(lista_produtos, gerenciador_historico=None):
    try:
        nome = input("Digite o nome do produto: ")
        codigo = input("Digite o codigo do produto: ")
        categoria = input("Digite a categoria: ")
        quantidade = int(input("Digite a quantidade em estoque: "))
        preco = float(input("Digite o preco do produto: "))
        fornecedor = input("Digite o fornecedor: ")
        descricao = input("Digite a descricao do produto: ")

        if quantidade < 0 or preco < 0:
            print("Erro: quantidade e preco nao podem ser negativos.")
            return

        if buscar_produto(lista_produtos, codigo) is not None:
            print("Erro: ja existe um produto com esse codigo.")
            return

        novo_produto = Produto(nome, codigo, categoria, quantidade, preco, fornecedor, descricao)
        lista_produtos.append(novo_produto)

        if gerenciador_historico is not None:
            gerenciador_historico.adicionar_movimentacao(
                codigo, nome, "cadastro", quantidade, "Cadastro inicial"
            )

        print("Produto cadastrado com sucesso!")

    except ValueError:
        print("Erro: quantidade ou preco invalido. Tente novamente.")


def listar_produtos(lista_produtos):
    if len(lista_produtos) == 0:
        print("Nenhum produto cadastrado.")
    else:
        print("\n===== LISTA DE PRODUTOS =====")
        for produto in lista_produtos:
            produto.exibir_dados()


def buscar_produto_codigo(lista_produtos):
    codigo = input("Digite o codigo do produto: ")
    produto = buscar_produto(lista_produtos, codigo)

    if produto is not None:
        print("\n===== PRODUTO ENCONTRADO =====")
        produto.exibir_dados()
    else:
        print("Produto nao encontrado.")


def atualizar_estoque(lista_produtos, gerenciador_historico=None):
    codigo = input("Digite o codigo do produto: ")
    produto = buscar_produto(lista_produtos, codigo)

    if produto is None:
        print("Produto nao encontrado.")
        return

    print(f"Estoque atual: {produto.quantidade} unidades")
    print("1 - Adicionar ao estoque")
    print("2 - Remover do estoque")

    try:
        opcao = int(input("Escolha uma opcao: "))
        quantidade = int(input("Digite a quantidade: "))

        if quantidade < 0:
            print("Erro: a quantidade nao pode ser negativa.")
            return

        if opcao == 1:
            produto.adicionar_estoque(quantidade)
            if gerenciador_historico is not None:
                gerenciador_historico.adicionar_movimentacao(
                    produto.codigo, produto.nome, "adicao", quantidade, "Adicao manual ao estoque"
                )
            print("Estoque atualizado com sucesso!")

        elif opcao == 2:
            if produto.remover_estoque(quantidade):
                if gerenciador_historico is not None:
                    gerenciador_historico.adicionar_movimentacao(
                        produto.codigo, produto.nome, "remocao", quantidade, "Remocao manual do estoque"
                    )
                print("Estoque atualizado com sucesso!")
            else:
                print("Erro: quantidade insuficiente em estoque.")

        else:
            print("Opcao invalida.")

    except ValueError:
        print("Erro: digite valores numericos validos.")


def remover_produto(lista_produtos, gerenciador_historico=None):
    codigo = input("Digite o codigo do produto que deseja remover: ")
    produto = buscar_produto(lista_produtos, codigo)

    if produto is None:
        print("Produto nao encontrado.")
        return

    if gerenciador_historico is not None:
        gerenciador_historico.adicionar_movimentacao(
            produto.codigo, produto.nome, "exclusao", produto.quantidade, "Produto removido do sistema"
        )

    lista_produtos.remove(produto)
    print("Produto removido com sucesso!")


def verificar_estoque_baixo(lista_produtos):
    encontrou = False

    for produto in lista_produtos:
        if produto.quantidade <= 5:
            if not encontrou:
                print("\n===== ALERTA: ESTOQUE BAIXO =====")
            produto.exibir_dados()
            encontrou = True

    if not encontrou:
        print("Nenhum produto com estoque baixo.")


def gerar_relatorio(lista_produtos):
    print("\n===== RELATORIO DE ESTOQUE =====")

    if len(lista_produtos) == 0:
        print("Nenhum produto cadastrado.")
        return

    total_produtos = len(lista_produtos)
    valor_total = 0
    produto_mais_caro = lista_produtos[0]
    quantidade_estoque_baixo = 0

    for produto in lista_produtos:
        valor_produto = produto.preco * produto.quantidade
        valor_total += valor_produto

        if produto.preco > produto_mais_caro.preco:
            produto_mais_caro = produto

        if produto.quantidade <= 5:
            quantidade_estoque_baixo += 1

        print(f"\nProduto: {produto.nome}")
        print(f"Quantidade: {produto.quantidade}")
        print(f"Valor em estoque: R$ {valor_produto:.2f}")

    print("\n===== RESUMO DO ESTOQUE =====")
    print(f"Total de produtos cadastrados: {total_produtos}")
    print(f"Valor total do estoque: R$ {valor_total:.2f}")
    print(f"Produto mais caro: {produto_mais_caro.nome} (R$ {produto_mais_caro.preco:.2f})")
    print(f"Produtos com estoque baixo: {quantidade_estoque_baixo}")


def relatorio_financeiro_completo(lista_produtos, lista_vendas, gerenciador_historico):
    print("\n" + "=" * 45)
    print("      RELATORIO FINANCEIRO COMPLETO")
    print("=" * 45)

    valor_estoque = 0
    for produto in lista_produtos:
        valor_estoque += produto.preco * produto.quantidade

    total_vendido = 0
    for venda in lista_vendas:
        total_vendido += venda.total

    print(f"\nValor total em estoque: R$ {valor_estoque:.2f}")
    print(f"Faturamento total com vendas: R$ {total_vendido:.2f}")
    print(f"Total de movimentacoes registradas: {len(gerenciador_historico.historico)}")
    print(f"Total de vendas realizadas: {len(lista_vendas)}")


def salvar_produtos(lista_produtos, nome_arquivo):
    try:
        with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
            for produto in lista_produtos:
                arquivo.write(produto.to_string_arquivo())
        print("Produtos salvos com sucesso!")
    except Exception as erro:
        print(f"Erro ao salvar produtos: {erro}")

def carregar_produtos(nome_arquivo):
    lista_produtos = []

    try:
        with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                dados = linha.strip().split(";")

                if len(dados) == 7:
                    nome = dados[0]
                    codigo = dados[1]
                    categoria = dados[2]
                    quantidade = int(dados[3])
                    preco = float(dados[4])
                    fornecedor = dados[5]
                    descricao = dados[6]

                    produto = Produto(nome, codigo, categoria, quantidade, preco, fornecedor, descricao)
                    lista_produtos.append(produto)

    except FileNotFoundError:
        print("Arquivo de produtos nao encontrado. O sistema comecara com estoque vazio.")

    return lista_produtos
