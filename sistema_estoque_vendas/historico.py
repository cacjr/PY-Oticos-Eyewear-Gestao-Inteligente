from datetime import datetime


class HistoricoMovimentacao:

    def __init__(self, codigo_produto, nome_produto, tipo_movimentacao, quantidade, data_hora, observacao=""):
        self.codigo_produto = codigo_produto
        self.nome_produto = nome_produto
        self.tipo_movimentacao = tipo_movimentacao
        self.quantidade = quantidade
        self.data_hora = data_hora
        self.observacao = observacao

    def exibir(self):
        print(f"[{self.data_hora}] {self.tipo_movimentacao.upper()}: {self.nome_produto} - Qtd: {self.quantidade} - {self.observacao}")

    def to_string_arquivo(self):
        return f"{self.codigo_produto};{self.nome_produto};{self.tipo_movimentacao};{self.quantidade};{self.data_hora};{self.observacao}\n"


class GerenciadorHistorico:

    def __init__(self, nome_arquivo="historico.txt"):
        self.nome_arquivo = nome_arquivo
        self.historico = []
        self.carregar_historico()

    def adicionar_movimentacao(self, codigo_produto, nome_produto, tipo_movimentacao, quantidade, observacao=""):
        nova_movimentacao = HistoricoMovimentacao(
            codigo_produto,
            nome_produto,
            tipo_movimentacao,
            quantidade,
            datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
            observacao
        )
        self.historico.append(nova_movimentacao)
        self.salvar_historico()

    def relatorio_historico(self):
        print("\n===== HISTORICO DE MOVIMENTACOES =====")
        if len(self.historico) == 0:
            print("Nenhuma movimentacao registrada.")
            return

        for movimentacao in self.historico:
            movimentacao.exibir()

        print(f"\nTotal de movimentacoes: {len(self.historico)}")

    def salvar_historico(self):
        try:
            with open(self.nome_arquivo, "w", encoding="utf-8") as arquivo:
                for movimentacao in self.historico:
                    arquivo.write(movimentacao.to_string_arquivo())
        except Exception as erro:
            print(f"Erro ao salvar historico: {erro}")

    def carregar_historico(self):
        try:
            with open(self.nome_arquivo, "r", encoding="utf-8") as arquivo:
                for linha in arquivo:
                    dados = linha.strip().split(";")
                    if len(dados) == 6:
                        movimentacao = HistoricoMovimentacao(
                            dados[0], dados[1], dados[2], int(dados[3]), dados[4], dados[5]
                        )
                        self.historico.append(movimentacao)
        except FileNotFoundError:
            pass
