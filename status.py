from abc import ABCMeta, abstractmethod, abstractproperty


class Status(metaclass=ABCMeta):
    """Classe 'mãe' que serve de base para os Status: `Ativo` e `Inativo`"""
    @abstractproperty
    def desc(self):
        pass

    @abstractmethod
    def __str__(self):
        pass


class Ativo(Status):
    """Classe que herda de `Status`
    
    Possui uma property que retorna o conteúdo privado desc
    """
    def __init__(self):
        self.__desc = 'está ativo(a) em seus estudos'

    @property
    def desc(self):
        return self.__desc

    def __str__(self):
        return 'Ativo'


class Inativo(Status):
    """Classe que herda de `Status`
    
    Possui uma property que retorna o conteúdo privado desc
    """
    def __init__(self):
        self.__desc = 'está inativo(a) em seus estudos'

    @property
    def desc(self):
        return self.__desc

    def __str__(self):
        return 'Inativo'
