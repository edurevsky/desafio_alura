from aluno import Aluno, AlunoBuilder
from validadores import Cgm, Email
from professor import Professor, ProfessorBuilder


"""
Tudo bagunçado
"""

def registrarAluno():
    builder = AlunoBuilder()

    nome = input('Digite o nome: ')

    email = input('Digite o email: ')

    while Email(email).valida() != True:
        email = input('Digite um email válido: ')

    turma = input('Digite o código da turma: ')

    cgm = input('Digite o CGM: ')

    while Cgm(cgm).valida() != True:
        cgm = input('Digite um CGM válido: ')

    turno = int(input('Turnos:\n[1] Matutino\n[2] Vespertino\n[3] Noturno\nDigite o número correspondente ao turno: '))
    if turno == 1:
        aluno = builder.comTurnoMatutino()
    elif turno == 2:
        aluno = builder.comTurnoVespertino()
    elif turno == 3:
        aluno = builder.comTurnoNoturno()
    else:
        raise ValueError('Número inserido não corresponde a um turno.')

    status = int(input('Status:\n[1] Ativo\n[2] Inativo\nDigite o número correspondente ao status do aluno: '))
    if status == 1:
        builder.comStatusAtivo()
    elif status == 2:
        builder.comStatusInativo()
    else:
        raise ValueError('Número inserido não corresponde a um status.')

    aluno = builder.comNome(nome).comEmail(email).comTurma(turma).comCgm(cgm).build()
    print(aluno)

def registrarProfessor():
    builder = ProfessorBuilder()

    nome = input('Digite o nome: ')

    email = input('Digite o email: ')
    while Email(email).valida() != True:
        email = input('Digite um email válido: ')

    qnt = int(input('Digite a quantidade de turmas o professor tem: '))
    i = 0
    while qnt < 1:
        qnt = int(input('Digite uma quantidade válida: '))
    while i < qnt:
        turma = input('Digite o código da turma: ')
        builder.comTurma(turma)
        i += 1
    
    turno = int(input('Turnos:\n[1] Matutino\n[2] Vespertino\n[3] Noturno\nDigite o número correspondente ao turno: '))
    if turno == 1:
        professor = builder.comTurnoMatutino()
    elif turno == 2:
        professor = builder.comTurnoVespertino()
    elif turno == 3:
        professor = builder.comTurnoNoturno()
    else:
        raise ValueError('Número inserido não corresponde a um turno.')

    professor = builder.comNome(nome).comEmail(email).build()
    print(professor)


registrarAluno()