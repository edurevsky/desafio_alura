from abc import ABCMeta, abstractmethod, abstractproperty


class Status(metaclass=ABCMeta):
    @abstractproperty
    def desc(self):
        pass

    @abstractmethod
    def __str__(self):
        pass


class Ativo(Status):

    def __init__(self):
        self.__desc = 'Está ativo(a) em seus estudos'

    @property
    def desc(self):
        return self.__desc

    def __str__(self):
        return 'Ativo'


class Inativo(Status):

    def __init__(self):
        self.__desc = 'Está inativo(a) em seus estudos'

    @property
    def desc(self):
        return self.__desc

    def __str__(self):
        return 'Inativo'
