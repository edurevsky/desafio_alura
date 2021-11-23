from dataclasses import dataclass
from turnos import Turno, Matutino, Vespertino, Noturno


@dataclass
class Professor(object):
    """Classe tipo Professor que possui os atributos: nome, email, turma(lista), turno"""
    nome: str = None
    email: str = None
    turma = []
    turno: Turno = None

    def __str__(self):
        return f'{self.nome},{self.email},{self.turma},{self.turno}'


class ProfessorBuilder(object):
    """Classe responsável por 'montar' o professor"""
    def __init__(self):
        self.__professor = Professor()

    def comNome(self, nome):
        self.__professor.nome = nome
        return self

    def comEmail(self, email):
        self.__professor.email = email
        return self

    def comTurma(self, turma):
        self.__professor.turma.append(turma)
        return self

    def comTurnoMatutino(self):
        self.__professor.turno = Matutino()
        return self

    def comTurnoVespertino(self):
        self.__professor.turno = Vespertino()
        return self

    def comTurnoNoturno(self):
        self.__professor.turno = Noturno()
        return self

    def build(self):
        return self.__professor
    