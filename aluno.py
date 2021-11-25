from dataclasses import dataclass
from turnos import Turno
from status import Status


@dataclass
class Aluno(object):
    nome: str
    email: str
    turma: str
    cgm: str
    turno: Turno
    status: Status

    def __dados__(self):
        return f'O(a) aluno(a) {self.nome} {self.status.desc} e {self.turno.desc}'

    def __str__(self):
        return f'Nome: {self.nome}, Email: {self.email}, Turma: {self.turma}, CGM: {self.cgm}, Turno: {self.turno}, Status: {self.status}'
