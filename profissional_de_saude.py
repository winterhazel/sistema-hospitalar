from pessoa import Pessoa


class ProfissionalDeSaude(Pessoa):
    def __init__(self, cpf, nome, celular, endereco, salario_por_hora):
        super().__init__(cpf, nome, celular, endereco)
        self.salario_por_hora = salario_por_hora

    def get_salario_por_hora(self):
        return self.salario_por_hora

    def set_salario_por_hora(self, salario_por_hora):
        self.salario_por_hora = salario_por_hora

    def get_registro(self):
        return -1

    def set_registro(self, registro):
        pass

    def imprimir(self):
        super().imprimir()
        print(f'Salário por hora: R$ {self.salario_por_hora}')
