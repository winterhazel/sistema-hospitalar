import dialogos
import tests

# Objetos
pessoas = list()
consultas = list()
atendimentos_emergenciais = list()
materiais = list()
prescricoes = list()

# tests.init(pessoas, consultas, atendimentos_emergenciais, materiais)  # Cadastrar automaticamente algumas coisas
acoes = ['cadastrar', 'alterar', 'visualizar', 'excluir']

while True:
    acao = dialogos.mostrar_menu() # Pedir ação
    item = dialogos.mostrar_escolha_de_item(acoes[acao - 1]) # Pedir item

    if acao == 1:
        # Cadastrar
        if item == 1:
            dialogos.cadastrar_pessoa(pessoas)
        elif item == 2:
            dialogos.cadastrar_consulta(pessoas, consultas, atendimentos_emergenciais)
        elif item == 3:
            dialogos.cadastrar_atendimento_emergencial(pessoas, consultas, atendimentos_emergenciais, materiais)
        elif item == 4:
            dialogos.cadastrar_prescricao(pessoas, consultas, prescricoes)
        elif item == 5:
            dialogos.cadastrar_material(materiais)
    elif acao == 2:
        # Alterar
        if item == 1:
            dialogos.alterar_pessoa(pessoas)
        elif item == 2:
            dialogos.alterar_consulta(pessoas, consultas, atendimentos_emergenciais)
        elif item == 3:
            dialogos.alterar_atendimento_emergencial(pessoas, consultas, atendimentos_emergenciais, materiais)
        elif item == 4:
            dialogos.alterar_prescricao(consultas, prescricoes)
        elif item == 5:
            dialogos.alterar_material(materiais)
    elif acao == 3:
        # Visualizar
        if item == 1:
            dialogos.visualizar_pessoa(pessoas)
        elif item == 2:
            dialogos.visualizar_consultas(consultas)
        elif item == 3:
            dialogos.visualizar_atendimentos_emergenciais(atendimentos_emergenciais)
        elif item == 4:
            dialogos.visualizar_prescricoes(prescricoes)
        elif item == 5:
            dialogos.visualizar_materiais(materiais)
    elif acao == 4:
        # Excluir
        if item == 1:
            dialogos.excluir_pessoa(pessoas)
        elif item == 2:
            dialogos.excluir_consulta(consultas)
        elif item == 3:
            dialogos.excluir_atendimento_emergencial(atendimentos_emergenciais)
        elif item == 4:
            dialogos.excluir_prescricao(prescricoes)
        elif item == 5:
            dialogos.excluir_material(materiais)
