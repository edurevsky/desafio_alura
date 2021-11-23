from dataclasses import dataclass
from turnos import Turno, Matutino, Vespertino, Noturno
from status import Status, Ativo, Inativo
from validadores import Cgm, Email


@dataclass
class Aluno(object):
    """Classe tipo Aluno que possui os atributos: nome, email, turma, cgm, turno, status"""
    nome: str = None
    email: str = None
    turma: str = None
    cgm: str = None
    turno: Turno = None
    status: Status = None

    def _paraAtivo(self):
        self.status = Ativo()

    def _paraInativo(self):
        self.status = Inativo()

    def __str__(self) -> str:
        return f'{self.nome},{self.email},{self.turma},{self.cgm},{self.turno},{self.status}'


class AlunoBuilder(object):
    """Classe responsável por 'montar' o aluno"""
    def __init__(self):
        self.__aluno = Aluno()

    def comNome(self, nome):
        self.__aluno.nome = nome
        return self

    def comEmail(self, email):
        self.__aluno.email = email
        return self

    def comTurma(self, turma):
        self.__aluno.turma = turma
        return self

    def comCgm(self, cgm):
        self.__aluno.cgm = cgm
        return self

    def comTurnoMatutino(self):
        self.__aluno.turno = Matutino()
        return self

    def comTurnoVespertino(self):
        self.__aluno.turno = Vespertino()
        return self

    def comTurnoNoturno(self):
        self.__aluno.turno = Noturno()
        return self

    def comStatusAtivo(self):
        self.__aluno.status = Ativo()
        return self

    def comStatusInativo(self):
        self.__aluno.status = Inativo()
        return self

    def build(self):
        return self.__aluno


x = AlunoBuilder()

print(x)