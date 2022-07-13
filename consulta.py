import math


class Consulta:
    def __init__(self, id, data_inicio, data_fim, pessoa, profissional_de_saude):
        self.id = id
        self.data_inicio = data_inicio
        self.data_fim = data_fim
        self.pessoa = pessoa
        self.profissional_de_saude = profissional_de_saude
        self.custo = self.get_custo()

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_custo(self):
        # Calcular o custo
        diferenca = self.data_fim - self.data_inicio
        horas = diferenca.days * 24 + diferenca.seconds / 3600
        return self.profissional_de_saude.get_salario_por_hora() * math.ceil(horas)

    def set_custo(self, custo):
        self.custo = custo

    def get_data_inicio(self):
        return self.data_inicio

    def set_data_inicio(self, data_inicio):
        self.data_inicio = data_inicio

    def get_data_fim(self):
        return self.data_fim

    def set_data_fim(self, data_fim):
        self.data_fim = data_fim

    def get_pessoa(self):
        return self.pessoa

    def set_pessoa(self, pessoa):
        self.pessoa = pessoa

    def get_profissional_de_saude(self):
        return self.profissional_de_saude

    def set_profissional_de_saude(self, profissional_de_saude):
        self.profissional_de_saude = profissional_de_saude

    def imprimir(self):
        print(
            f'Consulta de {self.get_pessoa().get_nome()} com o/a {type(self.get_profissional_de_saude()).__name__} {self.get_profissional_de_saude().get_nome()} das {self.get_data_inicio()} às {self.get_data_fim()} - R$ {self.get_custo()}')
