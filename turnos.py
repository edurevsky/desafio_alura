from abc import ABCMeta, abstractmethod


class Turno(metaclass=ABCMeta):
    @abstractmethod
    def __str__(self):
        pass


class Manha(Turno):

    def __str__(self):
        return 'Manha'


class Tarde(Turno):

    def __str__(self):
        return 'Tarde'


class Noite(Turno):

    def __str__(self):
        return 'Noite'
