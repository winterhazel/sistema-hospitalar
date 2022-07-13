from enfermeiro import Enfermeiro
from fisioterapeuta import Fisioterapeuta
from funcionario import Funcionario
from medico import Medico


def get_pessoa(pessoas, cpf):
    """Retorna a pessoa com o CPF inserido ou None se não existir"""
    for pessoa in pessoas:
        if pessoa.get_cpf() == cpf:
            return pessoa

    return None


def get_funcionario(pessoas, registro):
    """Retorna o funcionário com o registro inserido ou None se não existir"""
    for pessoa in pessoas:
        if type(pessoa) is Funcionario and pessoa.get_registro() == registro:
            return pessoa

    return None


def get_enfermeiro(pessoas, registro):
    """Retorna o enfermeiro com o registro inserido ou None se não existir"""
    for pessoa in pessoas:
        if type(pessoa) is Enfermeiro and pessoa.get_registro() == registro:
            return pessoa

    return None


def get_medico(pessoas, registro):
    """Retorna o médico com o registro inserido ou None se não existir"""
    for pessoa in pessoas:
        if type(pessoa) is Medico and pessoa.get_registro() == registro:
            return pessoa

    return None


def get_fisioterapeuta(pessoas, registro):
    """Retorna o fisioterapeuta com o registro inserido ou None se não existir"""
    for pessoa in pessoas:
        if type(pessoa) is Fisioterapeuta and pessoa.get_registro() == registro:
            return pessoa

    return None


def get_consultas(consultas, cpf):
    """Retorna uma lista com todas as consultas da pessoa com o CPF inserido"""
    consultas_do_cpf = list()

    for consulta in consultas:
        if consulta.get_pessoa().get_cpf() == cpf:
            consultas_do_cpf.append(consulta)

    return consultas_do_cpf


def get_atendimentos_emergenciais(atendimentos_emergenciais, cpf):
    """Retorna uma lista com todos os atendimentos emergenciais da pessoa com o CPF inserido"""
    atendimentos_do_cpf = list()

    for atendimento in atendimentos_emergenciais:
        if atendimento.get_pessoa().get_cpf() == cpf:
            atendimentos_do_cpf.append(atendimento)

    return atendimentos_do_cpf


def get_prescricoes(prescricoes, cpf):
    """Retorna uma lista com todas as prescrições da pessoa com o CPF inserido"""
    prescricoes_do_cpf = list()

    for prescricao in prescricoes:
        if prescricao.get_consulta().get_pessoa().get_cpf() == cpf:
            prescricoes_do_cpf.append(prescricao)

    return prescricoes_do_cpf


def get_material(materiais, nome):
    """Retorna o material com o nome inserido ou None se não existir"""
    for material in materiais:
        if material.get_nome() == nome:
            return material

    return None
