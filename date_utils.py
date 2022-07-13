def intervalos_colidem(inicio_1, fim_1, inicio_2, fim_2):
    """Confere se dois intervalos possuem algum momento em comum"""
    delta = 0

    if (inicio_1 <= fim_2) and (inicio_2 <= fim_1):
        inicio_mais_tarde = max(inicio_1, inicio_2)
        fim_mais_cedo = min(fim_1, fim_2)
        delta = (fim_mais_cedo - inicio_mais_tarde).seconds + 1
        delta = max(0, delta)

    return delta != 0


def data_disponivel_profissional(data_inicio, data_fim, profissional, consultas, atendimentos_emergenciais):
    """
    Confere se o profissional inserido está disponível naquele horário
    O profissional pode ser tanto um paciente como uma pessoa atendendo. Portanto, esta função confere as duas coisas
    """
    # Conferir com as consultas
    for consulta in consultas:
        cpfs = [consulta.get_pessoa().get_cpf(), consulta.get_profissional_de_saude().get_cpf()]

        if profissional.get_cpf() in cpfs:
            if intervalos_colidem(data_inicio, data_fim, consulta.get_data_inicio(), consulta.get_data_fim()):
                return False

    # Conferir com os atendimentos emergenciais
    for atendimento_emergencial in atendimentos_emergenciais:
        cpfs = [atendimento_emergencial.get_pessoa().get_cpf()]

        for profissional_do_atendimento in atendimento_emergencial.get_profissionais_de_saude():
            cpfs.append(profissional_do_atendimento.get_cpf())

        if profissional.get_cpf() in cpfs:
            if intervalos_colidem(data_inicio, data_fim, atendimento_emergencial.get_data_inicio(),
                                  atendimento_emergencial.get_data_fim()):
                return False

    return True


def data_disponivel_profissional_e_paciente(data_inicio, data_fim, paciente, profissional, consultas,
                                            atendimentos_emergenciais):
    """
    Confere se o profissional e o paciente inseridos estão disponíveis naquele horário
    Eu basicamente fiz uma função para conferir os dois juntos para que o programa não precisasse rodar este código duas
    vezes estas checagens
    """
    # Conferir com as consultas
    for consulta in consultas:
        cpfs = [consulta.get_pessoa().get_cpf(), consulta.get_profissional_de_saude().get_cpf()]

        if profissional.get_cpf() in cpfs or paciente.get_cpf() in cpfs:
            if intervalos_colidem(data_inicio, data_fim, consulta.get_data_inicio(), consulta.get_data_fim()):
                return False

    # Conferir com os atendimentos emergenciais
    for atendimento_emergencial in atendimentos_emergenciais:
        cpfs = [atendimento_emergencial.get_pessoa().get_cpf()]

        for profissional_do_atendimento in atendimento_emergencial.get_profissionais_de_saude():
            cpfs.append(profissional_do_atendimento.get_cpf())

        if profissional.get_cpf() in cpfs or paciente.get_cpf() in cpfs:
            if intervalos_colidem(data_inicio, data_fim, atendimento_emergencial.get_data_inicio(),
                                  atendimento_emergencial.get_data_fim()):
                return False

    return True
