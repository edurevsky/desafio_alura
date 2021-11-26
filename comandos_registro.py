from aluno import Aluno
from professor import Professor
from validadores import Cgm, Email
from turnos import Manha, Tarde, Noite, Turno
from status import Ativo, Inativo, Status


turnos = '[1] Manha - [2] Tarde - [3] Noite\n'


def registrarAluno():
    nome = input('Digite o nome do aluno: ')

    email = input('Digite o email do aluno: ')
    while not Email(email).valida():
        email = input('Digite um email válido (@escola.pr.gov.br): ')

    turma = input('Digite o código da turma: ')

    cgm = input('Digite o CGM do aluno: ')
    while not Cgm(cgm).valida():
        cgm = input('Digite um CGM válido (8 números): ')

    turno = int(input(turnos + 'Digite o número correspondente ao turno: '))
    while not turno == 1 or turno == 2 or turno == 3:
        turno = int(input(turnos + 'Digite um turno válido: '))
    if turno == 1:
        aluno = Aluno(nome, email, turma, cgm, Manha(), Ativo())
    elif turno == 2:
        aluno = Aluno(nome, email, turma, cgm, Tarde(), Ativo())
    elif turno == 3:
        aluno = Aluno(nome, email, turma, cgm, Noite(), Ativo())
    
    stringAluno = (f"Aluno '{aluno.nome} - {aluno.cgm}' foi registrado no sistema.")
    input(f'Por padrão, o aluno terá status como Ativo.\n{stringAluno}\nAperte Enter para continuar...')

    return aluno


def registrarProfessor():
    nome = input('Digite o nome do professor: ')

    email = input('Digite o email do professor: ')
    while not Email(email).valida():
        email = input('Digite um email válido (@escola.pr.gov.br): ')
    
    qntTurmas = int(input('Digite quantas turmas o professor tem: '))
    while qntTurmas <= 0:
        qntTurmas = int(input('Digite uma quantidade válida: '))
    i = 0
    while i < qntTurmas:
        listaTurmas = []
        t = input('Digite o código da turma: ')
        listaTurmas.append(t)
        i += 1
    
    turno = int(input(turnos + 'Digite o número correspondente ao turno: '))
    while not turno == 1 or turno == 2 or turno == 3:
       turno = int(input(turnos + 'Digite um turno válido: '))
    if turno == 1:
        professor = Professor(nome, email, listaTurmas, Manha())
    elif turno == 2:
        professor = Professor(nome, email, listaTurmas, Tarde())
    elif turno == 3:
        professor = Professor(nome, email, listaTurmas, Noite())

    input(f"Professor '{professor.nome} - {professor.email}' foi registrado no sistema.\nAperte Enter para continuar...")
    return professor


registrarAluno()