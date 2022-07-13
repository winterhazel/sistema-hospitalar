class Pessoa:
    def __init__(self, cpf, nome, celular, endereco):
        self.cpf = cpf
        self.nome = nome
        self.celular = celular
        self.endereco = endereco

    def get_cpf(self):
        return self.cpf

    def set_cpf(self, cpf):
        self.cpf = cpf

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome

    def get_celular(self):
        return self.celular

    def set_celular(self, celular):
        self.celular = celular

    def get_endereco(self):
        return self.endereco

    def set_endereco(self, endereco):
        self.endereco = endereco

    def imprimir(self):
        print(f'Nome: {self.nome}\nCPF: {self.cpf}\nCelular ({self.celular["ddd"]}) {self.celular["numero"]}\nCEP: {self.endereco["cep"]} - Estado: {self.endereco["estado"]}\nCidade: {self.endereco["cidade"]} - Bairro: {self.endereco["bairro"]}\nNúmero: {self.endereco["numero"]} - Complemento: {self.endereco["complemento"]}')