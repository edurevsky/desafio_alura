from abc import ABCMeta, abstractmethod, abstractproperty


class Turno(metaclass=ABCMeta):
    @abstractproperty
    def desc(self):
        pass

    @abstractmethod
    def __str__(self):
        pass


class Manha(Turno):

    def __init__(self):
        self.__desc = 'Está registrado no turno da manhã'

    @property
    def desc(self):
        return self.__desc

    def __str__(self):
        return 'Manha'


class Tarde(Turno):

    def __init__(self):
        self.__desc = 'Está registrado no turno da tarde'

    @property
    def desc(self):
        return self.__desc

    def __str__(self):
        return 'Tarde'


class Noite(Turno):

    def __init__(self):
        self.__desc - 'Está registrado no turno da noite'

    @property
    def desc(self):
        return self.__desc

    def __str__(self):
        return 'Noite'
