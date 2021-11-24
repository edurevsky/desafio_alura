from abc import ABCMeta, abstractmethod


class Status(metaclass=ABCMeta):
    @abstractmethod
    def __str__(self):
        pass


class Ativo(Status):

    def __init__(self):
        self.__descricao = 'O aluno está ativo em seus estudos'

    @property
    def desc(self):
        return self.__descricao

    def __str__(self):
        return 'Ativo'


class Inativo(Status):

    def __init__(self):
        self.__descricao = 'O aluno não está ativo em seus estudos'

    @property
    def desc(self):
        return self.__descricao

    def __str__(self):
        return 'Inativo'
