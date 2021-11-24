from dataclasses import dataclass
from turnos import Turno


@dataclass
class Professor(object):
    nome: str
    email: str
    turmas: list[str]
    turno: Turno

    def __csv__(self):
        return f'{self.nome},{self.email},{self.turmas},{self.turno}\n'

    def __str__(self):
        return f'Nome: {self.nome}, Email: {self.email}, Turmas: {self.turmas}, Turno: {self.turno}'
