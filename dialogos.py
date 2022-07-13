import os
from datetime import datetime

import date_utils
import input_utils
import list_utils
from atendimento_emergencial import AtendimentoEmergencial
from consulta import Consulta
from enfermeiro import Enfermeiro
from fisioterapeuta import Fisioterapeuta
from funcionario import Funcionario
from input_utils import get_int, get_int_min_max, get_float, get_string
from material import Material
from medico import Medico
from pessoa import Pessoa
from prescricao import Prescricao
from profissional_de_saude import ProfissionalDeSaude


def limpar_tela():
    """Executa o comando para limpar a tela"""
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')


def mostrar_menu():
    """Mostra a mensagem inicial e retorna o valor escolhido pelo usuário"""
    limpar_tela()
    print(
        '== SISTEMA HOSPITALAR =====================\nOlá, digite o número correspondente à ação que deseja realizar:\n[1] Cadastrar\n[2] Alterar\n[3] Visualizar\n[4] Excluir\n')
    return get_int_min_max('', 1, 4)


def mostrar_escolha_de_item(acao):
    """Mostra a mensagem de escolha de item e retorna o valor escolhido pelo usuário"""
    limpar_tela()
    print(
        f'O que deseja {acao}?\n[1] Pessoa\n[2] Consulta\n[3] Atendimento emergencial\n[4] Prescrição\n[5] Material\n[0] Cancelar')
    return get_int_min_max('', 0, 5)


def mostrar_escolha_de_pessoa():
    """Mostra a mensagem de escolha de tipo de pessoa e retorna o valor escolhido pelo usuário"""
    limpar_tela()
    print(
        'Em qual tipo a pessoa se encaixa?\n[1] Pessoa comum\n[2] Funcionário\n[3] Profissional de saúde\n[0] Cancelar')
    return get_int_min_max('', 0, 3)


def mostrar_escolha_de_profissional_de_saude():
    """Mostra a mensagem de escolha de tipo de profissional de saúde e retorna o valor escolhido pelo usuário"""
    limpar_tela()
    print('Qual o tipo de profissional de saúde?\n[1] Enfermeiro\n[2] Médico\n[3] Fisioterapeuta\n[0] Cancelar')
    return get_int_min_max('', 0, 3)


def cadastrar_pessoa(pessoas):
    """Realiza o procedimento e todas as checagens para cadastrar uma pessoa"""
    # Pedir os dados da pessoa
    cpf = abs(input_utils.get_int('Digite o CPF da pessoa (somente números, 11 dígitos): '))

    while True:
        if len(str(cpf)) == 11:
            # Conferir se já existe uma pessoa com esse CPF
            if list_utils.get_pessoa(pessoas, cpf) is None:
                break
            else:
                cpf = input_utils.get_int('Uma pessoa com este CPF já está cadastrada no sistema! Insira outro valor: ')
        else:
            cpf = input_utils.get_int(input_utils.MENSAGEM_ENTRADA_INCORRETA)

    nome = get_string(f'Digite o nome da pessoa: ')
    cep = get_string(f'Digite o CEP da pessoa: ')
    estado = get_string(f'Digite o estado da pessoa: ')
    cidade = get_string(f'Digite a cidade da pessoa: ')
    bairro = get_string(f'Digite o bairro da pessoa: ')
    numero = get_string(f'Digite o número da casa da pessoa: ')
    complemento = input(f'Digite o complemento da pessoa (ou deixe em branco): ')
    endereco = {'cep': cep, 'estado': estado, 'cidade': cidade, 'bairro': bairro, 'numero': numero,
                'complemento': complemento}
    ddd = get_int(f'Digite o DDD da pessoa: ')

    while len(str(ddd)) != 2:
        ddd = get_int(input_utils.MENSAGEM_ENTRADA_INCORRETA)
    numero_do_celular = get_int(f'Digite o celular da pessoa (sem traços): ')

    while len(str(numero_do_celular)) != 8 and len(str(numero_do_celular)) != 9:
        numero_do_celular = get_int(input_utils.MENSAGEM_ENTRADA_INCORRETA)

    celular = {'ddd': ddd, 'numero': numero_do_celular}
    tipo_de_pessoa = mostrar_escolha_de_pessoa()

    if tipo_de_pessoa == 1:
        pessoas.append(Pessoa(cpf, nome, celular, endereco))
    elif tipo_de_pessoa == 2:
        registro = input_utils.get_int('Digite o registro funcional do funcionário: ')

        while True:
            if list_utils.get_funcionario(pessoas, registro) is None:
                break
            else:
                registro = input(
                    'Um funcionário com este registro funcional já está cadastrado! Insira outro valor: ')

        pessoas.append(Funcionario(cpf, nome, celular, endereco, registro))
    elif tipo_de_pessoa == 3:
        salario_por_hora = input_utils.get_float('Digite o salário por hora do profissional de saúde: ')

        while True:
            if salario_por_hora >= 0:
                break
            else:
                salario_por_hora = input_utils.get_float(input_utils.MENSAGEM_ENTRADA_INCORRETA)

        tipo_de_profissional = mostrar_escolha_de_profissional_de_saude()

        if tipo_de_profissional == 1:
            registro = input_utils.get_int('Digite o registro COREN do enfemeiro: ')

            while True:
                if list_utils.get_enfermeiro(pessoas, registro) is None:
                    break
                else:
                    registro = input(
                        'Um enfermeiro com este registro já está cadastrado! Insira outro valor: ')

            pessoas.append(Enfermeiro(cpf, nome, celular, endereco, salario_por_hora, registro))
        elif tipo_de_profissional == 2:
            registro = input_utils.get_int('Digite o registro CRM do médico: ')

            while True:
                if list_utils.get_medico(pessoas, registro) is None:
                    break
                else:
                    registro = input(
                        'Um médico com este registro já está cadastrado! Insira outro valor: ')

            pessoas.append(Medico(cpf, nome, celular, endereco, salario_por_hora, registro))
        elif tipo_de_profissional == 3:
            registro = input_utils.get_int('Digite o registro CREFITO do fisioterapeuta: ')

            while True:
                if list_utils.get_fisioterapeuta(pessoas, registro) is None:
                    break
                else:
                    registro = input(
                        'Um fisioterapeuta com este registro já está cadastrado! Insira outro valor: ')

            pessoas.append(Fisioterapeuta(cpf, nome, celular, endereco, salario_por_hora, registro))

    print('Pessoa cadastrada!')
    input_utils.aguardar_enter()


def cadastrar_consulta(pessoas, consultas, atendimentos_emergenciais):
    limpar_tela()
    quantidade_de_profissionais = 0

    # Condições para o cadastro
    for pessoa in pessoas:
        if isinstance(pessoa, ProfissionalDeSaude):
            quantidade_de_profissionais += 1

    if quantidade_de_profissionais == 0:
        print('Não existem profissionais para realizar a consulta!')
        input_utils.aguardar_enter()
        return

    if len(pessoas) == 1 and quantidade_de_profissionais == 1:
        print('Cadastre pelo menos mais uma pessoa para ser o paciente!')
        input_utils.aguardar_enter()
        return

    # Pedir as informações
    cpf_paciente = input_utils.get_int('Digite o CPF do paciente: ')

    while True:
        paciente = list_utils.get_pessoa(pessoas, cpf_paciente)

        if paciente is None:
            cpf_paciente = input_utils.get_int('Não existe um paciente com este CPF! Digite novamente: ')
        else:
            # Se somente existir um profissional, e o paciente for este profissional, não há outro profissional para
            # atendê-lo
            if isinstance(paciente, ProfissionalDeSaude) and quantidade_de_profissionais == 1:
                cpf_paciente = input_utils.get_int(
                    'Não existe outro profissional de saúde para atender esta pessoa! Digite outro: ')
                continue

            # Confirmação
            confirmado = input_utils.get_sim_ou_nao(f'O paciente é {paciente.get_nome()}, confirmar? [S/N]: ')

            if confirmado:
                break
            else:
                cpf_paciente = input_utils.get_int('Digite o CPF do paciente: ')

    cpf_profissional = input_utils.get_int('Digite o CPF do profissional de saúde: ')

    while True:
        profissional = list_utils.get_pessoa(pessoas, cpf_profissional)

        if profissional is None or (
                type(profissional) is not Enfermeiro and type(profissional) is not Medico and type(
            profissional) is not Fisioterapeuta):
            cpf_profissional = input_utils.get_int(
                'O CPF digitado não pertence a nenhum profissional! Digite novamente: ')
        else:
            if cpf_paciente == cpf_profissional:
                cpf_profissional = input_utils.get_int(
                    'O profissional não pode ser seu paciente! Digite novamente: ')
            else:
                confirmado = input_utils.get_sim_ou_nao(
                    f'O profissional é {profissional.get_nome()}, confirmar? [S/N]: ')
                if confirmado:
                    break
                else:
                    continue

    entrada = input(
        'Digite a data de início e de fim da consulta (no formato 01/02/2020 13:00 - 01/02/2020 13:59): ').split(' - ')

    while True:
        if len(entrada) == 2:
            try:
                data_inicio = datetime.strptime(entrada[0], "%d/%m/%Y %H:%M")
                data_fim = datetime.strptime(entrada[1], "%d/%m/%Y %H:%M")

                if data_fim > data_inicio:
                    if date_utils.data_disponivel_profissional_e_paciente(data_inicio, data_fim, paciente, profissional,
                                                                          consultas,
                                                                          atendimentos_emergenciais):
                        break
                    else:
                        entrada = input(
                            'O profissional e/ou o paciente não está disponível neste horário! Digite outro: ').split(
                            ' - ')
                else:
                    entrada = input('A data de fim deve vir depois da data de início! Digite novamente: ').split(' - ')
            except ValueError:
                entrada = input(input_utils.MENSAGEM_ENTRADA_INCORRETA).split(' - ')
        else:
            entrada = input(input_utils.MENSAGEM_ENTRADA_INCORRETA).split(' - ')

    consultas.append(Consulta(len(consultas), data_inicio, data_fim, paciente, profissional))
    print('Consulta cadastrada com sucesso!')
    input_utils.aguardar_enter()


def cadastrar_atendimento_emergencial(pessoas, consultas, atendimentos_emergenciais, materiais):
    limpar_tela()

    # Condições para o cadastro
    if len(pessoas) == 0:
        print('Cadastre pelo menos uma pessoa antes de cadastrar o atendimento emergencial!')
        input_utils.aguardar_enter()
        return

    quantidade_de_profissionais = 0

    for pessoa in pessoas:
        if isinstance(pessoa, ProfissionalDeSaude):
            quantidade_de_profissionais += 1

    if quantidade_de_profissionais == 0:
        print('Cadastre pelo menos um profissional de saúde antes de cadastrar o atendimento emergencial!')
        input_utils.aguardar_enter()
        return

    if len(pessoas) == 1 and quantidade_de_profissionais == 1:
        print('Cadastre pelo menos mais uma pessoa para ser o paciente!')
        input_utils.aguardar_enter()
        return

    # Pedir informações
    cpf_paciente = input_utils.get_int('Digite o CPF do paciente: ')

    while True:
        paciente = list_utils.get_pessoa(pessoas, cpf_paciente)

        if paciente is not None:
            break
        else:
            cpf_paciente = input_utils.get_int('O CPF não pertence a uma pessoa! Digite novamente: ')

    motivo = input_utils.get_string('Digite o motivo do atendimento emergencial: ')

    entrada_datas = input(
        'Digite a data de início e de fim do atendimento (no formato 01/02/2020 13:00 - 01/02/2020 13:59): ').split(
        ' - ')

    while True:
        if len(entrada_datas) == 2:
            try:
                data_inicio = datetime.strptime(entrada_datas[0], "%d/%m/%Y %H:%M")
                data_fim = datetime.strptime(entrada_datas[1], "%d/%m/%Y %H:%M")

                if data_fim > data_inicio:
                    break
                else:
                    entrada_datas = input('A data de fim deve vir depois da data de início! Digite novamente: ').split(
                        ' - ')
            except ValueError:
                entrada_datas = input(input_utils.MENSAGEM_ENTRADA_INCORRETA).split(' - ')
        else:
            entrada_datas = input(input_utils.MENSAGEM_ENTRADA_INCORRETA).split(' - ')

    # Conferir se existe pelo menos um profissional de saúde disponível no horário
    quantidade_de_profissionais_disponiveis = 0

    for pessoa in pessoas:
        if isinstance(pessoa, ProfissionalDeSaude) and pessoa.get_cpf() != paciente.get_cpf():
            if date_utils.data_disponivel_profissional(data_inicio, data_fim, pessoa, consultas,
                                                       atendimentos_emergenciais):
                quantidade_de_profissionais_disponiveis += 1

    if quantidade_de_profissionais_disponiveis == 0:
        print('Não há nenhum profissional de saúde disponível neste horário!')
        input_utils.aguardar_enter()
        return

    profissionais = list()

    # Para pular a mensagem de inserir mais outro o paciente seja um profissional
    if isinstance(paciente, ProfissionalDeSaude):
        quantidade_de_profissionais -= 1

    while True:
        cpf_profissional = input_utils.get_int('Digite o CPF do profissional de saúde: ')

        while True:
            if cpf_profissional != cpf_paciente:
                profissional = list_utils.get_pessoa(pessoas, cpf_profissional)

                if isinstance(profissional, ProfissionalDeSaude):
                    if date_utils.data_disponivel_profissional(data_inicio, data_fim, profissional, consultas,
                                                               atendimentos_emergenciais):
                        if profissional not in profissionais:
                            profissionais.append(profissional)
                            break
                        else:
                            cpf_profissional = input_utils.get_int(
                                'O profissional já foi adicionado no atendimento! Digite novamente: ')
                    else:
                        cpf_profissional = input_utils.get_int(
                            'O profissional não está disponível neste horário! Digite outro: ')
                else:
                    cpf_profissional = input_utils.get_int(
                        'O CPF não pertence a um profissional de saúde! Digite novamente: ')
            else:
                cpf_profissional = input_utils.get_int('O paciente não pode atender a si mesmo! Digite outro: ')

        if quantidade_de_profissionais_disponiveis == len(profissionais):
            break
        else:
            continuar = input_utils.get_sim_ou_nao('Deseja inserir mais um profissional? [S/N]: ')

            if not continuar:
                break

    materiais_utilizados = list()

    if len(materiais) > 0 and input_utils.get_sim_ou_nao(
            'Foram utilizados materiais durante o atendimento emergencial? [S/N]: '):
        while True:
            nome_material = input_utils.get_string('Digite o nome do material: ')

            while True:
                material = list_utils.get_material(materiais, nome_material)

                if material is not None:
                    quantidade = input_utils.get_int('Digite a quantidade utilizada do material: ')

                    while True:
                        if quantidade >= 0:
                            break
                        else:
                            quantidade = input_utils.get_int(input_utils.MENSAGEM_ENTRADA_INCORRETA)

                    materiais_utilizados += quantidade * [material]
                    break
                else:
                    nome_material = input_utils.get_string('Material inexistente! Digite novamente: ')

            continuar = input_utils.get_sim_ou_nao('Deseja inserir mais um material? [S/N]: ')

            if not continuar:
                break

    atendimentos_emergenciais.append(
        AtendimentoEmergencial(len(atendimentos_emergenciais), motivo, data_inicio, data_fim, paciente, profissionais,
                               materiais_utilizados))
    print('Atendimento emergencial cadastrado!')
    input_utils.aguardar_enter()


def cadastrar_prescricao(pessoas, consultas, prescricoes):
    limpar_tela()

    # Condições para o cadastro
    if len(pessoas) == 0:
        print('Cadastre pelo menos uma pessoa antes de cadastrar a prescrição!')
        input_utils.aguardar_enter()
        return

    quantidade_de_medicos = 0

    for pessoa in pessoas:
        if type(pessoa) is Medico:
            quantidade_de_medicos += 1

    if quantidade_de_medicos == 0:
        print('Cadastre pelo menos um médico antes de cadastrar a prescrição!')
        input_utils.aguardar_enter()
        return

    if quantidade_de_medicos == 1 and len(pessoas) == 1:
        print('Cadastre pelo menos uma outra pessoa pare receber a prescrição!')
        input_utils.aguardar_enter()
        return

    if len(consultas) == 0:
        print('Pelo menos uma consulta deve ser realizada antes de cadastrar uma prescrição!')
        input_utils.aguardar_enter()
        return

    # Pedir informações
    cpf_paciente = input_utils.get_int('Digite o CPF do paciente: ')

    while True:
        paciente = list_utils.get_pessoa(pessoas, cpf_paciente)

        if paciente is not None:
            break
        else:
            cpf_paciente = input_utils.get_int('O CPF não pertence a uma pessoa! Digite novamente: ')

    consultas_com_medico = list()

    for consulta in consultas:
        if consulta.get_pessoa().get_cpf() == cpf_paciente and type(consulta.get_profissional_de_saude()) is Medico:
            consultas_com_medico.append(consulta)
            print(f'[{len(consultas_com_medico)}] ', end='')
            consulta.imprimir()

    if len(consultas_com_medico) == 0:
        print('Este paciente não possui consultas com médicos!')
        input_utils.aguardar_enter()
        return

    numero_consulta = input_utils.get_int_min_max('Digite o número da consulta: ', 1, len(consultas_com_medico)) - 1
    nome_do_medicamento = input_utils.get_string('Digite o nome do medicamento: ')
    intervalo = input_utils.get_string('Digite o intervalo para a ingestão do medicamento (ex. a cada 30 minutos): ')

    prescricoes.append(
        Prescricao(len(prescricoes), nome_do_medicamento, intervalo, consultas_com_medico[numero_consulta]))
    print('Prescrição cadastrada!')
    input_utils.aguardar_enter()


def cadastrar_material(materiais):
    limpar_tela()

    # Pedir as informações
    nome = get_string('Digite o nome do material: ')

    while True:
        for material in materiais:
            if material.get_nome() == nome:
                nome = get_string('Já existe um material com este nome! Insira novamente: ')
                continue

        break

    custo = get_float('Digite o custo de cada unidade do material: ')

    while custo < 0:
        custo = get_float(input_utils.MENSAGEM_ENTRADA_INCORRETA)

    materiais.append(Material(nome, custo))
    print('Material cadastrado!')
    input_utils.aguardar_enter()


def visualizar_pessoa(pessoas):
    """Realiza o procedimento e todas as checagens para visualizar uma pessoa"""
    limpar_tela()

    if len(pessoas) == 0:
        print('Não há pessoas cadastradas!')
        input_utils.aguardar_enter()
        return

    mensagem = 'CPFs cadastrados: '

    for pessoa in pessoas:
        mensagem += f'{pessoa.get_cpf()} '

    cpf = input_utils.get_int(f'{mensagem}\nDigite o CPF da pessoa: ')

    while True:
        pessoa = list_utils.get_pessoa(pessoas, cpf)

        if pessoa is not None:
            break
        else:
            cpf = input_utils.get_int('O CPF não pertence a uma pessoa! Digite novamente: ')

    pessoa.imprimir()
    input_utils.aguardar_enter()


def visualizar_consultas(consultas):
    limpar_tela()

    if len(consultas) == 0:
        print('Não há consultas cadastradas!')
        input_utils.aguardar_enter()
        return

    mensagem = 'CPFs com consultas cadastradas: '

    for consulta in consultas:
        if str(consulta.get_pessoa().get_cpf()) not in mensagem:
            mensagem += f'{consulta.get_pessoa().get_cpf()} '

    cpf = input_utils.get_int(f'{mensagem}\nDigite o CPF da pessoa: ')

    while True:
        consultas_da_pessoa = list_utils.get_consultas(consultas, cpf)

        if len(consultas_da_pessoa) > 0:
            break
        else:
            cpf = input_utils.get_int('O CPF não pertence a uma pessoa com consultas! Digite novamente: ')

    for consulta in consultas_da_pessoa:
        print('- ', end='')
        consulta.imprimir()

    input_utils.aguardar_enter()


def visualizar_atendimentos_emergenciais(atendimentos_emergenciais):
    limpar_tela()

    if len(atendimentos_emergenciais) == 0:
        print('Não há atendimentos emergenciais cadastrados!')
        input_utils.aguardar_enter()
        return

    mensagem = 'CPFs com atendimentos emergenciais cadastrados: '

    for atendimento_emergencial in atendimentos_emergenciais:
        if str(atendimento_emergencial.get_pessoa().get_cpf()) not in mensagem:
            mensagem += f'{atendimento_emergencial.get_pessoa().get_cpf()} '

    cpf = input_utils.get_int(f'{mensagem}\nDigite o CPF da pessoa: ')

    while True:
        atendimentos_da_pessoa = list_utils.get_atendimentos_emergenciais(atendimentos_emergenciais, cpf)

        if len(atendimentos_da_pessoa) > 0:
            break
        else:
            cpf = input_utils.get_int(
                'O CPF não pertence a uma pessoa com atendimentos emergenciais! Digite novamente: ')

    for atendimento_emergencial in atendimentos_da_pessoa:
        atendimento_emergencial.imprimir()

    input_utils.aguardar_enter()


def visualizar_prescricoes(prescricoes):
    limpar_tela()

    if len(prescricoes) == 0:
        print('Não há prescrições cadastradas!')
        input_utils.aguardar_enter()
        return

    mensagem = 'CPFs com prescrições cadastradas: '

    for prescricao in prescricoes:
        if str(prescricao.get_consulta().get_pessoa().get_cpf()) not in mensagem:
            mensagem += f'{prescricao.get_consulta().get_pessoa().get_cpf()} '

    cpf = input_utils.get_int(f'{mensagem}\nDigite o CPF da pessoa: ')

    while True:
        prescricoes_da_pessoa = list_utils.get_prescricoes(prescricoes, cpf)

        if len(prescricoes_da_pessoa) > 0:
            break
        else:
            cpf = input_utils.get_int('O CPF não pertence a uma pessoa com prescrições! Digite novamente: ')

    for prescricao in prescricoes:
        print('- ', end='')
        prescricao.imprimir()

    input_utils.aguardar_enter()


def visualizar_materiais(materiais):
    limpar_tela()

    if len(materiais) == 0:
        print('Não há materiais cadastrados!')
        input_utils.aguardar_enter()
        return

    mensagem = 'Materiais disponíveis: '

    for material in materiais:
        mensagem += f'{material.get_nome()}, '

    mensagem = mensagem[0:len(mensagem) - 2]
    nome = input_utils.get_string(f'{mensagem}\nDigite o nome do material: ')

    while True:
        material_existe = False

        for material in materiais:
            if material.get_nome() == nome:
                material.imprimir()
                material_existe = True

        if material_existe:
            break
        else:
            nome = input_utils.get_string('Material não existente! Digite novamente: ')

    input_utils.aguardar_enter()


def alterar_pessoa(pessoas):
    """Realiza o procedimento e todas as checagens para alterar uma pessoa"""
    limpar_tela()

    if len(pessoas) == 0:
        print('Não há pessoas cadastradas!')
        input_utils.aguardar_enter()
        return

    mensagem = 'CPFs cadastrados: '

    for pessoa in pessoas:
        mensagem += f'{pessoa.get_cpf()} '

    cpf = input_utils.get_int(f'{mensagem}\nDigite o CPF da pessoa: ')

    while True:
        pessoa = list_utils.get_pessoa(pessoas, cpf)

        if pessoa is not None:
            break
        else:
            cpf = input_utils.get_int('O CPF não pertence a uma pessoa! Digite novamente: ')

    while True:
        max = 10

        print(
            f'[1] CPF: {pessoa.get_cpf()}\n[2] Nome: {pessoa.get_nome()}\n[3] CEP: {pessoa.get_endereco()["cep"]}\n[4] Estado: {pessoa.get_endereco()["estado"]}\n[5] Cidade: {pessoa.get_endereco()["cidade"]}\n[6] Bairro: {pessoa.get_endereco()["bairro"]}\n[7] Número: {pessoa.get_endereco()["numero"]}\n[8] Complemento: {pessoa.get_endereco()["complemento"]}\n[9] DDD: {pessoa.get_celular()["ddd"]}\n[10] Número do celular: {pessoa.get_celular()["numero"]}',
            end='')

        if type(pessoa) is Funcionario:
            max = 11
            print(f'\n[11] Registro funcional: {pessoa.get_registro()}', end='')

        if isinstance(pessoa, ProfissionalDeSaude):
            max = 12

            if type(pessoa) is Enfermeiro:
                print(f'\n[11] Registro COREN: {pessoa.get_registro()}', end='')
            elif type(pessoa) is Medico:
                print(f'\n[11] Registro CRM: {pessoa.get_registro()}', end='')
            elif type(pessoa) is Fisioterapeuta:
                print(f'\n[11] Registro CREFITO: {pessoa.get_registro()}', end='')

            print(f'\n[12] Salário por hora: {pessoa.get_salario_por_hora()}', end='')

        campo = input_utils.get_int_min_max('\nDigite o número do campo para alterar: ', 1, max)

        if campo == 1:
            cpf_novo = input_utils.get_int('Digite o novo valor: ')

            while True:
                if len(str(cpf_novo)) == 11:
                    if list_utils.get_pessoa(pessoas, cpf_novo) is None:
                        pessoa.set_cpf(cpf_novo)
                        break
                    else:
                        cpf_novo = input_utils.get_int('Já existe uma pessoa com este CPF! Digite outro: ')
                else:
                    cpf_novo = input_utils.get_int('Entrada inválida! Digite um CPF com 11 dígitos: ')
        elif campo == 2:
            pessoa.set_nome(input_utils.get_string('Digite o novo valor: '))
        elif 3 <= campo <= 8:
            chaves = ['cep', 'estado', 'cidade', 'bairro', 'numero', 'complemento']
            endereco_novo = pessoa.get_endereco()
            endereco_novo[chaves[campo - 3]] = input_utils.get_string('Digite o novo valor: ')
            pessoa.set_endereco(endereco_novo)
        elif 9 <= campo <= 10:
            chaves = ['ddd', 'numero']
            celular_novo = pessoa.get_celular()
            celular_novo[chaves[campo - 9]] = input_utils.get_int('Digite o novo valor: ')

            while True:
                if (campo == 9 and len(str(celular_novo['ddd'])) == 2) or (campo == 10 and (
                        len(str(celular_novo['numero'])) == 8 or len(str(celular_novo['numero'])) == 9)):
                    break
                else:
                    celular_novo[chaves[campo - 9]] = input_utils.get_int('Entrada incorreta! Digite outro valor: ')

            pessoa.set_celular(celular_novo)
        elif campo == 11:
            registro_novo = input_utils.get_int('Digite o novo valor: ')

            while True:
                # Conferir se já existe outro funcionário ou profissional com o registro
                if type(pessoa) is Funcionario:
                    funcionario = list_utils.get_funcionario(pessoas, registro_novo)

                    if funcionario is None or funcionario.get_cpf() == pessoa.get_cpf():
                        break
                    else:
                        registro_novo = input_utils.get_int(
                            'Já existe um funcionário com este registro funcional! Digite outro: ')
                elif type(pessoa) is Enfermeiro:
                    enfermeiro = list_utils.get_enfermeiro(pessoas, registro_novo)

                    if enfermeiro is None or enfermeiro.get_cpf() == pessoa.get_cpf():
                        break
                    else:
                        registro_novo = input_utils.get_int(
                            'Já existe um enfermeiro com este registro COREN! Digite outro: ')
                elif type(pessoa) is Medico:
                    medico = list_utils.get_medico(pessoas, registro_novo)

                    if medico is None or medico.get_cpf() == pessoa.get_cpf():
                        break
                    else:
                        registro_novo = input_utils.get_int(
                            'Já existe um médico com este registro CRM! Digite outro: ')
                elif type(pessoa) is Fisioterapeuta:
                    fisioterapeuta = list_utils.get_fisioterapeuta(pessoas, registro_novo)

                    if fisioterapeuta is None or fisioterapeuta.get_cpf() == pessoa.get_cpf():
                        break
                    else:
                        registro_novo = input_utils.get_int(
                            'Já existe um fisioterapeuta com este registro CREFITO! Digite outro: ')

            pessoa.set_registro(registro_novo)
        elif campo == 12:
            pessoa.set_salario_por_hora(input_utils.get_float('Digite o novo valor: '))

        print('Campo alterado!')
        alterar_mais_um = input_utils.get_sim_ou_nao('Deseja alterar mais um campo? [S/N]: ')

        if not alterar_mais_um:
            break


def alterar_consulta(pessoas, consultas, atendimentos_emergenciais):
    limpar_tela()

    if len(consultas) == 0:
        print('Não há consultas cadastradas!')
        input_utils.aguardar_enter()
        return

    mensagem = 'CPFs com consultas cadastradas: '

    for consulta in consultas:
        if str(consulta.get_pessoa().get_cpf()) not in mensagem:
            mensagem += f'{consulta.get_pessoa().get_cpf()} '

    cpf = input_utils.get_int(f'{mensagem}\nDigite o CPF da pessoa: ')

    while True:
        consultas_da_pessoa = list_utils.get_consultas(consultas, cpf)

        if len(consultas_da_pessoa) > 0:
            break
        else:
            cpf = input_utils.get_int('O CPF não pertence a uma pessoa com consultas! Digite novamente: ')

    for i, consulta in enumerate(consultas_da_pessoa):
        print(f'[{i + 1}] ', end='')
        consulta.imprimir()

    numero_consulta = input_utils.get_int_min_max('Digite o número da consulta para alterar: ', 1,
                                                  len(consultas_da_pessoa)) - 1
    consulta_para_alterar = consultas_da_pessoa[numero_consulta]
    consultas_sem_a_alterada = consultas[:]
    consultas_sem_a_alterada.remove(consulta_para_alterar)

    while True:
        print(
            f'[1] Data: das {consulta_para_alterar.get_data_inicio()} às {consulta_para_alterar.get_data_fim()}\n[2] Paciente: {consulta_para_alterar.get_pessoa().get_nome()} (CPF {consulta_para_alterar.get_pessoa().get_cpf()})\n[3] Profissional de saúde: {consulta_para_alterar.get_profissional_de_saude().get_nome()} (CPF {consulta_para_alterar.get_profissional_de_saude().get_cpf()})')
        campo = input_utils.get_int_min_max('Digite o número do campo para alterar: ', 1, 3)

        if campo == 1:
            entrada = input('Digite o novo valor (no formato 01/02/2020 13:00 - 01/02/2020 13:59): ').split(' - ')

            while True:
                if len(entrada) == 2:
                    try:
                        data_inicio = datetime.strptime(entrada[0], "%d/%m/%Y %H:%M")
                        data_fim = datetime.strptime(entrada[1], "%d/%m/%Y %H:%M")

                        if data_fim > data_inicio:
                            if date_utils.data_disponivel_profissional_e_paciente(data_inicio, data_fim,
                                                                                  consulta_para_alterar.get_pessoa(),
                                                                                  consulta_para_alterar.get_profissional_de_saude(),
                                                                                  consultas_sem_a_alterada,
                                                                                  atendimentos_emergenciais):
                                break
                            else:
                                entrada = input(
                                    'O profissional e/ou o paciente não está disponível neste horário! Digite outro: ').split(
                                    ' - ')
                        else:
                            entrada = input(
                                'A data de fim deve vir depois da data de início! Digite novamente: ').split(' - ')
                    except ValueError:
                        entrada = input(input_utils.MENSAGEM_ENTRADA_INCORRETA).split(' - ')
                else:
                    entrada = input(input_utils.MENSAGEM_ENTRADA_INCORRETA).split(' - ')

            consulta_para_alterar.set_data_inicio(data_inicio)
            consulta_para_alterar.set_data_fim(data_fim)
        elif campo == 2:
            cpf_novo = input_utils.get_int(f'Digite o CPF da pessoa: ')

            while True:
                if cpf_novo != consulta_para_alterar.get_profissional_de_saude().get_cpf():
                    pessoa = list_utils.get_pessoa(pessoas, cpf_novo)

                    if pessoa is not None:
                        if date_utils.data_disponivel_profissional_e_paciente(consulta_para_alterar.get_data_inicio(),
                                                                              consulta_para_alterar.get_data_fim(),
                                                                              pessoa,
                                                                              consulta_para_alterar.get_profissional_de_saude(),
                                                                              consultas_sem_a_alterada,
                                                                              atendimentos_emergenciais):
                            break
                        else:
                            cpf_novo = input_utils.get_int(
                                'O paciente não está disponível neste horário! Digite outro: ')
                    else:
                        cpf_novo = input_utils.get_int(
                            'O CPF não pertence a uma pessoa com consultas! Digite outro: ')
                else:
                    cpf_novo = input_utils.get_int(
                        'O paciente não pode ser o profissional da consulta! Digite outro: ')

            consulta_para_alterar.set_pessoa(pessoa)
        elif campo == 3:
            cpf_novo = input_utils.get_int(f'Digite o CPF da pessoa: ')

            while True:
                if cpf_novo != consulta_para_alterar.get_pessoa().get_cpf():
                    profissional = list_utils.get_pessoa(pessoas, cpf_novo)

                    if profissional is not None and isinstance(profissional, ProfissionalDeSaude):
                        if date_utils.data_disponivel_profissional_e_paciente(consulta_para_alterar.get_data_inicio(),
                                                                              consulta_para_alterar.get_data_fim(),
                                                                              consulta_para_alterar.get_pessoa(),
                                                                              profissional,
                                                                              consultas_sem_a_alterada,
                                                                              atendimentos_emergenciais):
                            break
                        else:
                            cpf_novo = input_utils.get_int(
                                'O profissional não está disponível neste horário! Digite outro: ')
                    else:
                        cpf_novo = input_utils.get_int(
                            'O CPF não pertence a um profissional de saúde! Digite outro: ')
                else:
                    cpf_novo = input_utils.get_int(
                        'O profissional não pode ser o paciente da consulta! Digite outro: ')

            consulta_para_alterar.set_profissional_de_saude(profissional)

        print('Campo alterado!')
        alterar_mais_um = input_utils.get_sim_ou_nao('Deseja alterar mais um campo? [S/N]: ')

        if not alterar_mais_um:
            break


def alterar_atendimento_emergencial(pessoas, consultas, atendimentos_emergenciais, materiais):
    limpar_tela()

    # Condição para a alteração
    if len(atendimentos_emergenciais) == 0:
        print('Não há atendimentos emergenciais cadastrados!')
        input_utils.aguardar_enter()
        return

    # Printar pessoas com atendimentos
    mensagem = 'CPFs com atendimentos emergenciais cadastrados: '

    for atendimento_emergencial in atendimentos_emergenciais:
        if str(atendimento_emergencial.get_pessoa().get_cpf()) not in mensagem:
            mensagem += f'{atendimento_emergencial.get_pessoa().get_cpf()} '

    cpf = input_utils.get_int(f'{mensagem}\nDigite o CPF da pessoa: ')

    while True:
        atendimentos_emergenciais_da_pessoa = list_utils.get_atendimentos_emergenciais(atendimentos_emergenciais, cpf)

        if len(atendimentos_emergenciais_da_pessoa) > 0:
            break
        else:
            cpf = input_utils.get_int(
                'O CPF não pertence a uma pessoa com atendimentos emergenciais! Digite novamente: ')

    for i, atendimento_emergencial in enumerate(atendimentos_emergenciais_da_pessoa):
        print(f'[{i + 1}] ', end='')
        atendimento_emergencial.imprimir_compacto()

    numero_atendimento = input_utils.get_int_min_max('Digite o número do atendimento emergencial para alterar: ', 1,
                                                     len(atendimentos_emergenciais_da_pessoa)) - 1

    atendimento_para_alterar = atendimentos_emergenciais_da_pessoa[numero_atendimento]
    atendimentos_sem_o_alterado = atendimentos_emergenciais[:]
    atendimentos_sem_o_alterado.remove(atendimento_para_alterar)  # Utilizado para conferir os horários disponiveis

    while True:
        # Printar o atendimento escolhido
        mensagem_profissionais = ''

        for profissional in atendimento_para_alterar.get_profissionais_de_saude():
            mensagem_profissionais += f'{profissional.get_nome()} (CPF {profissional.get_cpf()}) '  # Lista de profissionais

        mensagem_materiais = ''

        if len(atendimento_para_alterar.get_materiais_utilizados()) != 0:
            for material in atendimento_para_alterar.get_materiais_utilizados():
                mensagem_material = f'{atendimento_para_alterar.get_materiais_utilizados().count(material)}x {material.get_nome()} (R$ {material.get_custo() * atendimento_para_alterar.get_materiais_utilizados().count(material)}) '

                if mensagem_material not in mensagem_materiais:
                    mensagem_materiais += mensagem_material
        else:
            mensagem_materiais = 'NENHUM'

        print(
            f'[1] Motivo: {atendimento_para_alterar.get_motivo()}\n[2] Data: das {atendimento_para_alterar.get_data_inicio()} às {atendimento_para_alterar.get_data_fim()}\n[3] Paciente: {atendimento_para_alterar.get_pessoa().get_nome()} (CPF {atendimento_para_alterar.get_pessoa().get_cpf()})\n[4] Profissionais de saúde: {mensagem_profissionais}\n[5] Materiais utilizados: {mensagem_materiais}')
        campo = input_utils.get_int_min_max('Digite o número do campo para alterar: ', 1, 5)

        # Alterações
        if campo == 1:
            atendimento_para_alterar.set_motivo(input_utils.get_string('Digite o novo valor: '))
            print('Campo alterado!')
        elif campo == 2:
            entrada = input('Digite o novo valor (no formato 01/02/2020 13:00 - 01/02/2020 13:59): ').split(' - ')

            while True:
                if len(entrada) == 2:
                    try:
                        data_inicio = datetime.strptime(entrada[0], "%d/%m/%Y %H:%M")
                        data_fim = datetime.strptime(entrada[1], "%d/%m/%Y %H:%M")

                        if data_fim > data_inicio:
                            # Conferir se todos os profisisonais do atendimento estão disponíveis no horário novo
                            todos_disponiveis = True

                            for profissional in atendimento_para_alterar.get_profissionais_de_saude():
                                if date_utils.data_disponivel_profissional(data_inicio, data_fim, profissional,
                                                                           consultas, atendimentos_sem_o_alterado):
                                    pass
                                else:
                                    todos_disponiveis = False

                            if todos_disponiveis:
                                break
                            else:
                                entrada = input(
                                    'Pelo menos um profissional não está disponível neste horário! Digite outro: ').split(
                                    ' - ')
                        else:
                            entrada = input(
                                'A data de fim deve vir depois da data de início! Digite novamente: ').split(' - ')
                    except ValueError:
                        entrada = input(input_utils.MENSAGEM_ENTRADA_INCORRETA).split(' - ')
                else:
                    entrada = input(input_utils.MENSAGEM_ENTRADA_INCORRETA).split(' - ')

            atendimento_para_alterar.set_data_inicio(data_inicio)
            atendimento_para_alterar.set_data_fim(data_fim)
            print('Campo alterado!')
        elif campo == 3:
            cpf_novo = input_utils.get_int(f'Digite o CPF da pessoa: ')

            # Armazenar o CPF dos profissionais para conferir com o do paciente
            cpf_dos_profissionais = list()

            for profissional in atendimento_para_alterar.get_profissionais_de_saude():
                cpf_dos_profissionais.append(profissional.get_cpf())

            while True:
                if cpf_novo not in cpf_dos_profissionais:
                    pessoa = list_utils.get_pessoa(pessoas, cpf_novo)

                    if pessoa is not None:
                        # Para o atendimento emergencial, não é necessário conferir o horário do paciente
                        break
                    else:
                        cpf_novo = input_utils.get_int('O CPF não pertence a uma pessoa com consultas! Digite outro: ')
                else:
                    cpf_novo = input_utils.get_int(
                        'O paciente não pode ser um profissional da consulta! Digite outro: ')

            atendimento_para_alterar.set_pessoa(pessoa)
            print('Campo alterado!')
        elif campo == 4:
            profissionais_novos = list()
            cpfs_disponiveis = list()

            for pessoa in pessoas:
                if isinstance(pessoa,
                              ProfissionalDeSaude) and pessoa.get_cpf() != atendimento_para_alterar.get_pessoa().get_cpf() and date_utils.data_disponivel_profissional(
                    atendimento_para_alterar.get_data_inicio(), atendimento_para_alterar.get_data_fim(), pessoa,
                    consultas, atendimentos_sem_o_alterado):
                    cpfs_disponiveis.append(pessoa.get_cpf())

            while True:
                cpf_profissional = input_utils.get_int('Digite o CPF do profissional de saúde: ')

                while True:
                    if cpf_profissional != atendimento_para_alterar.get_pessoa().get_cpf():
                        profissional = list_utils.get_pessoa(pessoas, cpf_profissional)

                        if isinstance(profissional, ProfissionalDeSaude):
                            if cpf_profissional in cpfs_disponiveis:
                                if profissional not in profissionais_novos:
                                    profissionais_novos.append(profissional)
                                    break
                                else:
                                    cpf_profissional = input_utils.get_int(
                                        'O profissional já foi adicionado no atendimento! Digite outro: ')
                            else:
                                cpf_profissional = input_utils.get_int(
                                    'O profissional não está disponível neste horário! Digite outro: ')
                        else:
                            cpf_profissional = input_utils.get_int(
                                'O CPF não pertence a um profissional de saúde! Digite outro: ')
                    else:
                        cpf_profissional = input_utils.get_int('O paciente não pode atender a si mesmo! Digite outro: ')

                if len(cpfs_disponiveis) == len(profissionais_novos):
                    break
                else:
                    continuar = input_utils.get_sim_ou_nao('Deseja inserir mais um profissional? [S/N]: ')

                    if not continuar:
                        break

            atendimento_para_alterar.set_profissionais_de_saude(profissionais_novos)
            print('Campo alterado!')
        elif campo == 5:
            if len(materiais) > 0:
                materiais_novos = list()

                while True:
                    nome_material = input_utils.get_string('Digite o nome do material: ')

                    while True:
                        material = list_utils.get_material(materiais, nome_material)

                        if material is not None:
                            quantidade = input_utils.get_int('Digite a quantidade utilizada do material: ')

                            while True:
                                if quantidade >= 0:
                                    break
                                else:
                                    quantidade = input_utils.get_int(input_utils.MENSAGEM_ENTRADA_INCORRETA)

                            materiais_novos += quantidade * [material]
                            break
                        else:
                            nome_material = input_utils.get_string('Material inexistente! Digite novamente: ')

                    continuar = input_utils.get_sim_ou_nao('Deseja inserir mais um material? [S/N]: ')

                    if not continuar:
                        atendimento_para_alterar.set_materiais_utilizados(materiais_novos)
                        print('Campo alterado!')
                        break

            else:
                print('Não há materiais cadastrados!')

        alterar_mais_um = input_utils.get_sim_ou_nao('Deseja alterar mais um campo? [S/N]: ')

        if not alterar_mais_um:
            break


def alterar_prescricao(consultas, prescricoes):
    limpar_tela()

    if len(prescricoes) == 0:
        print('Não há prescrições cadastradas!')
        input_utils.aguardar_enter()
        return

    mensagem = 'CPFs com prescrições cadastradas: '

    for prescricao in prescricoes:
        if str(prescricao.get_consulta().get_pessoa().get_cpf()) not in mensagem:
            mensagem += f'{prescricao.get_consulta().get_pessoa().get_cpf()} '

    cpf = input_utils.get_int(f'{mensagem}\nDigite o CPF da pessoa: ')

    while True:
        prescricoes_da_pessoa = list_utils.get_prescricoes(prescricoes, cpf)

        if len(prescricoes_da_pessoa) > 0:
            break
        else:
            cpf = input_utils.get_int('O CPF não pertence a uma pessoa com prescrições! Digite novamente: ')

    for i, prescricao in enumerate(prescricoes_da_pessoa):
        print(f'[{i + 1}] ', end='')
        prescricao.imprimir()

    numero_prescricao = input_utils.get_int_min_max('Digite o número da prescrição para alterar: ', 1,
                                                    len(prescricoes_da_pessoa)) - 1
    prescricao_para_alterar = prescricoes_da_pessoa[numero_prescricao]

    while True:
        print(
            f'[1] Nome do medicamento: {prescricao_para_alterar.get_nome_do_medicamento()}\n[2] Intervalo: {prescricao_para_alterar.get_intervalo()}\n[3] Consulta: ',
            end='')
        prescricao_para_alterar.get_consulta().imprimir()
        campo = input_utils.get_int_min_max('Digite o número do campo para alterar: ', 1, 3)

        if campo == 1:
            prescricao_para_alterar.set_nome_do_medicamento(input_utils.get_string('Digite o novo valor: '))
            print('Campo alterado!')
        elif campo == 2:
            prescricao_para_alterar.set_intervalo(input_utils.get_string('Digite o novo valor: '))
            print('Campo alterado!')
        elif campo == 3:
            consultas_da_pessoa_com_medico = list()

            for consulta in consultas:
                if type(consulta.get_profissional_de_saude()) is Medico:
                    consultas_da_pessoa_com_medico.append(consulta)
                    print(f'[{len(consultas_da_pessoa_com_medico)}] ', end='')
                    consulta.imprimir()

            if len(consultas_da_pessoa_com_medico) > 0:
                # Escolha da consulta
                numero_consulta = input_utils.get_int_min_max('Digite o número da consulta para colocar no lugar: ', 1,
                                                              len(consultas_da_pessoa_com_medico)) - 1
                prescricao_para_alterar.set_consulta(consultas_da_pessoa_com_medico[numero_consulta])
                print('Campo alterado!')
            else:
                print('Não há consultas para substituir!')
                input_utils.aguardar_enter()

        alterar_mais_um = input_utils.get_sim_ou_nao('Deseja alterar mais um campo? [S/N]: ')

        if not alterar_mais_um:
            break


def alterar_material(materiais):
    limpar_tela()

    if len(materiais) == 0:
        print('Não há materiais cadastrados!')
        input_utils.aguardar_enter()
        return

    mensagem = 'Materiais cadastrados: '

    for material in materiais:
        mensagem += f'{material.get_nome()}, '

    mensagem = mensagem[0:len(mensagem) - 2]

    nome = input_utils.get_string(f'{mensagem}\nDigite o nome do material: ')

    material_para_alterar = None

    while True:
        for material in materiais:
            if material.get_nome() == nome:
                material_para_alterar = material
                break

        if material_para_alterar is not None:
            break

        nome = input_utils.get_string('Material não existente! Digite novamente: ')

    while True:
        campo = input_utils.get_int_min_max(
            f'[1] Nome: {material_para_alterar.get_nome()}\n[2] Custo: {material_para_alterar.get_custo()}\nDigite o número do campo para alterar: ',
            1, 2)

        if campo == 1:
            material_para_alterar.set_nome(input_utils.get_string('Digite o novo valor: '))
        elif campo == 2:
            material_para_alterar.set_custo(input_utils.get_float('Digite o novo valor: '))

        print('Campo alterado!')

        alterar_mais_um = input_utils.get_sim_ou_nao('Deseja alterar mais um campo? [S/N]: ')

        if not alterar_mais_um:
            break


def excluir_pessoa(pessoas):
    """Realiza o procedimento e todas as checagens para excluir uma pessoa"""
    limpar_tela()

    if len(pessoas) == 0:
        print('Não há pessoas cadastradas!')
        input_utils.aguardar_enter()
        return

    mensagem = 'CPFs cadastrados: '

    for pessoa in pessoas:
        mensagem += f'{pessoa.get_cpf()} '

    cpf = input_utils.get_int(f'{mensagem}\nDigite o CPF da pessoa para excluir: ')

    while True:
        pessoa = list_utils.get_pessoa(pessoas, cpf)

        if pessoa is not None:
            break
        else:
            cpf = input_utils.get_int('O CPF não pertence a uma pessoa! Digite novamente: ')

    pessoas.remove(pessoa)
    print('Pessoa excluída!')
    input_utils.aguardar_enter()


def excluir_consulta(consultas):
    limpar_tela()

    if len(consultas) == 0:
        print('Não há consultas cadastradas!')
        input_utils.aguardar_enter()
        return

    mensagem = 'CPFs com consultas cadastradas: '

    for consulta in consultas:
        if str(consulta.get_pessoa().get_cpf()) not in mensagem:
            mensagem += f'{consulta.get_pessoa().get_cpf()} '

    cpf = input_utils.get_int(f'{mensagem}\nDigite o CPF da pessoa: ')

    while True:
        consultas_da_pessoa = list_utils.get_consultas(consultas, cpf)

        if len(consultas_da_pessoa) > 0:
            break
        else:
            cpf = input_utils.get_int('O CPF não pertence a uma pessoa com prescrições! Digite novamente: ')

    for i, consulta in enumerate(consultas_da_pessoa):
        print(f'[{i + 1}] ', end='')
        consulta.imprimir()

    numero_consulta = input_utils.get_int_min_max('Digite o número da consulta para excluir: ', 1,
                                                  len(consultas_da_pessoa)) - 1

    consultas.remove(consultas_da_pessoa[numero_consulta])
    print('Consulta excluída!')
    input_utils.aguardar_enter()


def excluir_atendimento_emergencial(atendimentos_emergenciais):
    limpar_tela()

    if len(atendimentos_emergenciais) == 0:
        print('Não há atendimentos emergenciais cadastrados!')
        input_utils.aguardar_enter()
        return

    mensagem = 'CPFs com atendimentos emergenciais cadastrados: '

    for atendimento_emergencial in atendimentos_emergenciais:
        if str(atendimento_emergencial.get_pessoa().get_cpf()) not in mensagem:
            mensagem += f'{atendimento_emergencial.get_pessoa().get_cpf()} '

    cpf = input_utils.get_int(f'{mensagem}\nDigite o CPF da pessoa: ')

    while True:
        atendimentos_da_pessoa = list_utils.get_atendimentos_emergenciais(atendimentos_emergenciais, cpf)

        if len(atendimentos_da_pessoa) > 0:
            break
        else:
            cpf = input_utils.get_int(
                'O CPF não pertence a uma pessoa com atendimentos emergenciais! Digite novamente: ')

    for i, atendimento in enumerate(atendimentos_da_pessoa):
        print(f'[{i + 1}] ', end='')
        atendimento.imprimir_compacto()

    numero_atendimento = input_utils.get_int_min_max('Digite o número do atendimento emergencial para excluir: ', 1,
                                                     len(atendimentos_da_pessoa)) - 1

    atendimentos_emergenciais.remove(atendimentos_da_pessoa[numero_atendimento])
    print('Atendimento emergencial excluído!')
    input_utils.aguardar_enter()


def excluir_prescricao(prescricoes):
    limpar_tela()

    if len(prescricoes) == 0:
        print('Não há prescrições cadastradas!')
        input_utils.aguardar_enter()
        return

    mensagem = 'CPFs com prescrições cadastradas: '

    for prescricao in prescricoes:
        if str(prescricao.get_consulta().get_pessoa().get_cpf()) not in mensagem:
            mensagem += f'{prescricao.get_consulta().get_pessoa().get_cpf()} '

    cpf = input_utils.get_int(f'{mensagem}\nDigite o CPF da pessoa: ')

    while True:
        prescricoes_da_pessoa = list_utils.get_prescricoes(prescricoes, cpf)

        if len(prescricoes_da_pessoa) > 0:
            break
        else:
            cpf = input_utils.get_int('O CPF não pertence a uma pessoa com prescrições! Digite novamente: ')

    for i, prescricao in enumerate(prescricoes_da_pessoa):
        print(f'[{i + 1}] ', end='')
        prescricao.imprimir()

    numero_prescricao = input_utils.get_int_min_max('Digite o número da prescrição para excluir: ', 1,
                                                    len(prescricoes_da_pessoa)) - 1

    prescricoes.remove(prescricoes_da_pessoa[numero_prescricao])
    print('Prescrição excluída!')
    input_utils.aguardar_enter()


def excluir_material(materiais):
    limpar_tela()

    if len(materiais) == 0:
        print('Não há materiais cadastrados!')
        input_utils.aguardar_enter()
        return

    mensagem = 'Materiais cadastrados: '

    for material in materiais:
        mensagem += f'{material.get_nome()}, '

    mensagem = mensagem[0:len(mensagem) - 2]

    nome = input_utils.get_string(f'{mensagem}\nDigite o nome do material: ')

    while True:
        material_excluido = False

        for material in materiais:
            if material.get_nome() == nome:
                materiais.remove(material)
                print('Material excluído!')
                input_utils.aguardar_enter()
                material_excluido = True

        if material_excluido:
            break

        nome = input_utils.get_string('Material não existente! Digite novamente: ')
