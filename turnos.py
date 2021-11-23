from abc import ABCMeta, abstractmethod


class Turno(metaclass=ABCMeta):
    @abstractmethod
    def __str__(self):
        pass


class Matutino(Turno):

    def __str__(self):
        return 'Matutino'


class Vespertino(Turno):

    def __str__(self):
        return 'Vespertino'

    
class Noturno(Turno):

    def __str__(self):
        return 'Noturno'
