from pessoa import Pessoa


class Funcionario(Pessoa):
    def __init__(self, cpf, nome, celular, endereco, registro_funcional):
        super().__init__(cpf, nome, celular, endereco)
        self.registro_funcional = registro_funcional

    def get_registro(self):
        return self.registro_funcional

    def set_registro(self, registro):
        self.registro_funcional = registro

    def imprimir(self):
        super().imprimir()
        print(f'Registro funcional: {self.registro_funcional}')
