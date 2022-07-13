import math


class AtendimentoEmergencial:
    def __init__(self, id, motivo, data_inicio, data_fim, pessoa, profissionais_de_saude, materiais_utilizados):
        self.id = id
        self.motivo = motivo
        self.data_inicio = data_inicio
        self.data_fim = data_fim
        self.pessoa = pessoa
        self.profissionais_de_saude = profissionais_de_saude
        self.materiais_utilizados = materiais_utilizados
        self.custo = self.get_custo()

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_motivo(self):
        return self.motivo

    def set_motivo(self, motivo):
        self.motivo = motivo

    def get_custo(self):
        # Calcular o custo
        diferenca = self.data_fim - self.data_inicio
        horas = diferenca.days * 24 + diferenca.seconds / 3600
        custo_por_hora = 0

        for profissional in self.profissionais_de_saude:
            custo_por_hora += profissional.get_salario_por_hora()

        self.custo = custo_por_hora * math.ceil(horas)

        for material_utilizado in self.materiais_utilizados:
            self.custo += material_utilizado.get_custo()

        return self.custo

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

    def get_profissionais_de_saude(self):
        return self.profissionais_de_saude

    def set_profissionais_de_saude(self, profissionais_de_saude):
        self.profissionais_de_saude = profissionais_de_saude

    def get_materiais_utilizados(self):
        return self.materiais_utilizados

    def set_materiais_utilizados(self, materiais_utilizados):
        self.materiais_utilizados = materiais_utilizados

    def imprimir(self):
        mensagem_profissionais = ''

        for profissional in self.profissionais_de_saude:
            mensagem_profissionais += f'{type(profissional).__name__} {profissional.get_nome()} (CPF {profissional.get_cpf()}) '

        mensagem_materiais = ''

        if len(self.materiais_utilizados) > 0:
            mensagem_materiais += '\nMateriais utilizados: '

            for material in self.materiais_utilizados:
                mensagem_material = f'{self.materiais_utilizados.count(material)}x {material.get_nome()} (R$ {material.get_custo() * self.materiais_utilizados.count(material)}) '

                if mensagem_material not in mensagem_materiais:
                    mensagem_materiais += mensagem_material

        print(
            f'=================\nATENDIMENTO EMERGENCIAL\nData: das {self.data_inicio} às {self.data_fim}\nMotivo: {self.motivo}\nProfissionais de saúde: {mensagem_profissionais}{mensagem_materiais}\nTOTAL: R$ {self.get_custo()}\n=================')

    def imprimir_compacto(self):
        print(
            f'Atendimento emergencial das {self.data_inicio} às {self.data_fim} em razão de {self.motivo} (R$ {self.get_custo()})')
