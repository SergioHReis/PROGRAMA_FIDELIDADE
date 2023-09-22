# cliente.py

class Cliente:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
        self.pontos = 0
        self.historico_compras = []

    def fazer_compra(self, valor_da_compra):
        pontos_ganhos = valor_da_compra // 10  # Atribui 1 ponto a cada R$10 gastos
        self.pontos += pontos_ganhos
        self.historico_compras.append(valor_da_compra)

    def usar_pontos(self, pontos_utilizados):
        if pontos_utilizados <= self.pontos:
            self.pontos -= pontos_utilizados
            return True  # Pontos utilizados com sucesso
        else:
            return False  # Não há pontos suficientes para este resgate

    def __str__(self):
        return f"Cliente: {self.nome}, Pontos: {self.pontos}"
