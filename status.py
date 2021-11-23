from abc import ABCMeta, abstractmethod


class Status(metaclass=ABCMeta):
    @abstractmethod
    def __str__(self):
        pass


class Ativo(Status):

    def __str__(self):
        return 'Ativo'


class Inativo(Status):

    def __str__(self):
        return 'Inativo'