from aluno import Aluno
from professor import Professor
from validadores import Cgm, Email
from turnos import Manha, Tarde, Noite, Turno
from status import Ativo, Inativo, Status


turnos = '[1] Manha - [2] Tarde - [3] Noite\n'


def pedeNome():
    nome = input(f'Digite o nome: ')
    return nome


def pedeEmail():
    email = input('Digite o email: ')
    while not Email(email).valida():
        email = input('Digite um email válido (@escola.pr.gov.br): ')
    return email


def pedeCgm():
    cgm = input('Digite o CGM: ')
    while not Cgm(cgm).valida():
        cgm = input('Digite um CGM válido (8 dígitos): ')
    return cgm


def registrarAluno():
    """Pede os atributos com inputs e retorna um objeto tipo `Aluno`"""
    nome = pedeNome()

    email = pedeEmail()

    turma = input('Digite o código da turma: ')

    cgm = pedeCgm()

    turno = int(input(turnos + 'Digite o número correspondente ao turno: '))
    if turno == 1:
        aluno = Aluno(nome, email, turma, cgm, Manha(), Ativo())
    elif turno == 2:
        aluno = Aluno(nome, email, turma, cgm, Tarde(), Ativo())
    elif turno == 3:
        aluno = Aluno(nome, email, turma, cgm, Noite(), Ativo())
    else:
        raise ValueError('Não foi inserido um turno válido.\nRegistro cancelado.')
    
    stringAluno = (f"Aluno '{aluno.nome} - {aluno.cgm}' foi registrado no sistema.")
    input(f'Por padrão, o aluno terá status como Ativo.\n{stringAluno}\nAperte Enter para continuar...')
    return aluno


def registrarProfessor():
    """Pede os atributos com inputs e retorna um objeto tipo `Professor`"""
    nome = pedeNome()

    email = pedeEmail()
    
    qntTurmas = int(input('Digite quantas turmas o professor tem: '))
    while qntTurmas <= 0:
        qntTurmas = int(input('Digite uma quantidade válida: '))
    i = 0
    while i < qntTurmas and qntTurmas < 25:
        listaTurmas = []
        t = input('Digite o código da turma: ')
        listaTurmas.append(t)
        i += 1
    
    turno = int(input(turnos + 'Digite o número correspondente ao turno: '))
    if turno == 1:
        professor = Professor(nome, email, listaTurmas, Manha())
    elif turno == 2:
        professor = Professor(nome, email, listaTurmas, Tarde())
    elif turno == 3:
        professor = Professor(nome, email, listaTurmas, Noite())
    else:
        raise ValueError('Não foi inserido um turno válido.\nRegistro cancelado.')
    input(f"Professor '{professor.nome} - {professor.email}' foi registrado no sistema.\nAperte Enter para continuar...")
    return professor
