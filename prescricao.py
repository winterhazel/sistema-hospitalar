class Prescricao:
    def __init__(self, id, nome_do_medicamento, intervalo, consulta):
        self.id = id
        self.nome_do_medicamento = nome_do_medicamento
        self.intervalo = intervalo
        self.consulta = consulta

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_nome_do_medicamento(self):
        return self.nome_do_medicamento

    def set_nome_do_medicamento(self, nome_do_medicamento):
        self.nome_do_medicamento = nome_do_medicamento

    def get_intervalo(self):
        return self.intervalo

    def set_intervalo(self, intervalo):
        self.intervalo = intervalo

    def get_consulta(self):
        return self.consulta

    def set_consulta(self, consulta):
        self.consulta = consulta

    def imprimir(self):
        print(
            f'Medicamento: {self.nome_do_medicamento}; intervalo: {self.intervalo}; prescrito por: {self.consulta.get_profissional_de_saude().get_nome()}')
