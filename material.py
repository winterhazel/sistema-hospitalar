class Material:
    def __init__(self, nome, custo):
        self.nome = nome
        self.custo = custo

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome

    def get_custo(self):
        return self.custo

    def set_custo(self, custo):
        self.custo = custo

    def imprimir(self):
        print(f'{self.nome} - R$ {self.custo} cada unidade')