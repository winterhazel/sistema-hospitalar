from datetime import datetime

MENSAGEM_ENTRADA_INCORRETA = 'Entrada incorreta! Insira novamente: '


def get_int(mensagem):
    """Pede um valor necessariamente inteiro"""
    valor = input(mensagem)

    while True:
        if valor.isnumeric():
            return int(valor)
        else:
            valor = input(MENSAGEM_ENTRADA_INCORRETA)


def get_int_min_max(mensagem, minimo, maximo):
    """Pede um valor necessariamente inteiro e dentro de um intervalo"""
    valor = input(mensagem)

    while True:
        if valor.isnumeric():
            valor = int(valor)

            if minimo <= valor <= maximo:
                return valor

        valor = input(MENSAGEM_ENTRADA_INCORRETA)


def get_float(mensagem):
    """Pede um número que pode ser decimal"""
    valor = input(mensagem)

    while True:
        if valor.replace('.', '', 1).isdigit():
            return float(valor)
        else:
            valor = input(MENSAGEM_ENTRADA_INCORRETA)


def get_string(mensagem):
    """Pede uma string com pelo menos uma caractere"""
    valor = input(mensagem)

    while True:
        if len(valor) > 0:
            return valor
        else:
            valor = input(MENSAGEM_ENTRADA_INCORRETA)


def get_sim_ou_nao(mensagem):
    """Pede sim ou não e retorna um boolean"""
    valor = input(mensagem).upper()

    while True:
        if valor == 'S' or valor == 'N':
            return valor == 'S'
        else:
            valor = input(MENSAGEM_ENTRADA_INCORRETA).upper()


def get_data(mensagem):
    """Pede uma data no formato DIA/MES/ANO HORA:MINUTO (ex. 01/01/2022 12:00) e retorna um Date"""
    mensagem_atual = mensagem

    while True:
        try:
            return datetime.strptime(input(mensagem_atual), "%d/%m/%Y %H:%M")
        except ValueError:
            mensagem_atual = MENSAGEM_ENTRADA_INCORRETA


def aguardar_enter():
    """Solicita que o usuário aperte ENTER para o programa continuar"""
    input('Pressione ENTER para continuar')
