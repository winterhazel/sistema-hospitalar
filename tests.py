"""Arquivo com algumas funções para ajudar a testar"""

from datetime import datetime

import list_utils
from consulta import Consulta
from fisioterapeuta import Fisioterapeuta
from medico import Medico
from pessoa import Pessoa


def cadastrar_pessoa(pessoas, cpf, nome, cep, estado, cidade, bairro, numero, complemento, ddd, numero_do_celular):
    endereco = {'cep': cep, 'estado': estado, 'cidade': cidade, 'bairro': bairro, 'numero': numero,
                'complemento': complemento}
    celular = {'ddd': ddd, 'numero': numero_do_celular}
    pessoas.append(Pessoa(cpf, nome, celular, endereco))


def cadastrar_medico(pessoas, cpf, nome, cep, estado, cidade, bairro, numero, complemento, ddd, numero_do_celular,
                     registro, salario):
    endereco = {'cep': cep, 'estado': estado, 'cidade': cidade, 'bairro': bairro, 'numero': numero,
                'complemento': complemento}
    celular = {'ddd': ddd, 'numero': numero_do_celular}
    pessoas.append(Medico(cpf, nome, celular, endereco, salario, registro))


def cadastrar_fisioterapeuta(pessoas, cpf, nome, cep, estado, cidade, bairro, numero, complemento, ddd,
                             numero_do_celular, registro, salario):
    endereco = {'cep': cep, 'estado': estado, 'cidade': cidade, 'bairro': bairro, 'numero': numero,
                'complemento': complemento}
    celular = {'ddd': ddd, 'numero': numero_do_celular}
    pessoas.append(Fisioterapeuta(cpf, nome, celular, endereco, salario, registro))


def cadastrar_consulta(pessoas, consultas, cpf_do_paciente, cpf_do_profissional, data_inicio, data_fim):
    consultas.append(Consulta(len(consultas), datetime.strptime(data_inicio, "%d/%m/%Y %H:%M"),
                              datetime.strptime(data_fim, "%d/%m/%Y %H:%M"),
                              list_utils.get_pessoa(pessoas, cpf_do_paciente),
                              list_utils.get_pessoa(pessoas, cpf_do_profissional)))


def init(pessoas, consultas, atendimentos_emergenciais, materiais):
    """Cadastra alguns itens automaticamente"""
    cadastrar_pessoa(pessoas, 32508428779, 'Douglas Pereira Rodrigues', '14031529', 'SP', 'Ribeirão Preto', 'Centro',
                     '107', '', 16, 35697831)
    cadastrar_pessoa(pessoas, 32508428778, 'Douglas Pereira Rodrigues 2', '14031529', 'SP', 'Ribeirão Preto', 'Centro',
                     '107', '', 16, 35697831)
    cadastrar_medico(pessoas, 56772977637, 'Kauã Azevedo Melo', '14031529', 'SP', 'Ribeirão Preto', 'Centro', '108', '',
                     16, 35697832, 29, 200)
    cadastrar_fisioterapeuta(pessoas, 88006580081, 'Gabriela Cardoso Ribeiro', '14031529', 'SP', 'Ribeirão Preto',
                             'Centro', '109', '', 16, 35697833, 30, 400)
    cadastrar_consulta(pessoas, consultas, 32508428779, 56772977637, '01/02/2020 13:00', '01/02/2020 13:59')
    cadastrar_consulta(pessoas, consultas, 32508428778, 88006580081, '01/02/2020 19:00', '01/02/2020 19:59')
    cadastrar_consulta(pessoas, consultas, 88006580081, 56772977637, '01/02/2020 16:00', '01/02/2020 16:59')
