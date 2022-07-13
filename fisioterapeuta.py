from profissional_de_saude import ProfissionalDeSaude


class Fisioterapeuta(ProfissionalDeSaude):
    def __init__(self, cpf, nome, celular, endereco, salario_por_hora, registro_crefito):
        super().__init__(cpf, nome, celular, endereco, salario_por_hora)
        self.registro_crefito = registro_crefito

    def get_registro(self):
        return self.registro_crefito

    def set_registro(self, registro):
        self.registro_crefito = registro

    def imprimir(self):
        super().imprimir()
        print(f'Registro CREFITO: {self.registro_crefito}')
