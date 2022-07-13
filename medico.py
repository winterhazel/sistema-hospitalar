from profissional_de_saude import ProfissionalDeSaude


class Medico(ProfissionalDeSaude):
    def __init__(self, cpf, nome, celular, endereco, salario_por_hora, registro_crm):
        super().__init__(cpf, nome, celular, endereco, salario_por_hora)
        self.registro_crm = registro_crm

    def get_registro(self):
        return self.registro_crm

    def set_registro(self, registro):
        self.registro_crm = registro

    def imprimir(self):
        super().imprimir()
        print(f'Registro CRM: {self.registro_crm}')
