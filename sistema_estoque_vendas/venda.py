class Venda:

    def __init__(self, codigo_venda, codigo_produto, nome_produto, quantidade, preco_unitario, desconto_percentual, total, data_hora):
        self.codigo_venda = codigo_venda
        self.codigo_produto = codigo_produto
        self.nome_produto = nome_produto
        self.quantidade = quantidade
        self.preco_unitario = preco_unitario
        self.desconto_percentual = desconto_percentual
        self.total = total
        self.data_hora = data_hora

    def exibir_recibo(self):
        print("\n" + "=" * 40)
        print("         OPTICOS EYEWEAR")
        print("         RECIBO DE VENDA")
        print("=" * 40)
        print(f"Venda n.: {self.codigo_venda}")
        print(f"Data/Hora: {self.data_hora}")
        print("-" * 40)
        print(f"Produto: {self.nome_produto}")
        print(f"Codigo: {self.codigo_produto}")
        print(f"Quantidade: {self.quantidade}")
        print(f"Preco unitario: R$ {self.preco_unitario:.2f}")
        if self.desconto_percentual > 0:
            print(f"Desconto aplicado: {self.desconto_percentual}%")
        print(f"TOTAL A PAGAR: R$ {self.total:.2f}")
        print("=" * 40)
        print("       Obrigado pela compra!")
        print("=" * 40 + "\n")

    def to_string_arquivo(self):
        return f"{self.codigo_venda};{self.codigo_produto};{self.nome_produto};{self.quantidade};{self.preco_unitario};{self.desconto_percentual};{self.total};{self.data_hora}\n"
