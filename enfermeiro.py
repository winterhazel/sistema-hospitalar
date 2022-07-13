from profissional_de_saude import ProfissionalDeSaude


class Enfermeiro(ProfissionalDeSaude):
    def __init__(self, cpf, nome, celular, endereco, salario_por_hora, registro_coren):
        super().__init__(cpf, nome, celular, endereco, salario_por_hora)
        self.registro_coren = registro_coren

    def get_registro(self):
        return self.registro_coren

    def set_registro(self, registro):
        self.registro_coren = registro

    def imprimir(self):
        super().imprimir()
        print(f'Registro COREN: {self.registro_coren}')
