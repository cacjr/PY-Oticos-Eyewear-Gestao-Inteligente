class Produto:

    def __init__(self, nome, codigo, categoria, quantidade, preco, fornecedor, descricao):
        self.nome = nome
        self.codigo = codigo
        self.categoria = categoria
        self.quantidade = quantidade
        self.preco = preco
        self.fornecedor = fornecedor
        self.descricao = descricao

    def exibir_dados(self):
        print(f"\nNome: {self.nome}")
        print(f"Codigo: {self.codigo}")
        print(f"Categoria: {self.categoria}")
        print(f"Quantidade em estoque: {self.quantidade}")
        print(f"Preco: R$ {self.preco:.2f}")
        print(f"Fornecedor: {self.fornecedor}")
        print(f"Descricao: {self.descricao}")
        print("-" * 35)

    def adicionar_estoque(self, quantidade):
        self.quantidade += quantidade

    def remover_estoque(self, quantidade):
        if quantidade <= self.quantidade:
            self.quantidade -= quantidade
            return True
        return False

    def valor_em_estoque(self):
        return self.preco * self.quantidade

    def to_string_arquivo(self):
        return f"{self.nome};{self.codigo};{self.categoria};{self.quantidade};{self.preco};{self.fornecedor};{self.descricao}\n"
