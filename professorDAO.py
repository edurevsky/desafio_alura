import csv
from professor import Professor
from turnos import Tarde


class ProfessorDAO():

    def salvar(self, professor):
        with open('professores.csv', 'w') as f:
            f.write(professor.__csv__())

    
    def carregar(self):
        pass


    def remover(self):
        pass



# a = Professor('fulano', 'fulano@escola.pr.gov.br', ['0001', '0002'], Tarde())
# ProfessorDAO().salvar(a)