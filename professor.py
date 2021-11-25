from dataclasses import dataclass
from turnos import Turno


@dataclass
class Professor(object):
    nome: str
    email: str
    turmas: list[str]
    turno: Turno

    def __dados__(self):
        return f'O(a) Professor(a) {self.nome} {self.turno.desc}'

    def __str__(self):
        return f'Nome: {self.nome}, Email: {self.email}, Turmas: {self.turmas}, Turno: {self.turno}'
