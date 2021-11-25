from aluno import Aluno
from professor import Professor
from status import Ativo, Inativo
from turnos import Manha, Tarde


class Escola(object):

    def __init__(self):
        self.__professores = []
        self.__alunos = []

    @property
    def alunos(self):
        return self.__alunos

    @property
    def professores(self):
        return self.__professores


    def adicionaProfessor(self, professor):
        self.professores.append(professor)


    def removeProfessor(self, index):
        del self.professores[index]


    def adicionaAluno(self, aluno):
        self.alunos.append(aluno)


    def removeAluno(self, index):
        del self.alunos[index]


    def listarProfessores(self):
        i = 0
        for professor in self.professores:
            print(f'ID: {i} - {professor}')
            i += 1


    def listarAlunos(self):
        i = 0
        for aluno in self.alunos:
            print(f'ID: {i} - {aluno}')
            i += 1

        
    def listarProfessorComIndex(self, index):
        print(self.professores[index])


    def listarAlunoComIndex(self, index):
        print(self.alunos[index])


    def listarDadosAlunoComIndex(self, index):
        print(self.alunos[index].__dados__())


    def listarDadosProfessorComIndex(self, index):
        print(self.professores[index].__dados__())


    def listarAlunosPorTurma(self, codigo):
        for aluno in self.alunos:
            if aluno.turma == codigo:
                print(aluno)

    
    def listarAlunosDoProfessor(self, index):
        for codigo in self.professores[index].turmas:
            self.listarAlunosPorTurma(codigo)


    def mudarStatusAlunoParaAtivo(self, index):
        self.alunos[index].status = Ativo()

    
    def mudarStatusAlunoParaInativo(self, index):
        self.alunos[index].status = Inativo()


esc = Escola()

esc.listarProfessores()

p1 = Professor('Fulano', 'fulano@escola.pr.gov.br', ['0001'], Manha())
# p2 = Professor('John Doe', 'john.doe@escola.pr.gov.br', ['0002'], Tarde())

a1 = Aluno('Ciclano', 'ciclano@escola.pr.gov.br', '0001', '11111111', Manha(), Ativo())
# a2 = Aluno('Beltrano', 'beltrano@escola.pr.gov.br', '0001', '22222222', Manha(), Ativo())
# a3 = Aluno('Sem Nome', 'sem.nome@escola.pr.gov.br', '0002', '33333333', Tarde(), Ativo())

esc.adicionaAluno(a1)
esc.adicionaProfessor(p1)
# esc.adicionaAluno(a2)
# esc.adicionaAluno(a3)
# esc.adicionaProfessor(p1)
# esc.adicionaProfessor(p2)
esc.mudarStatusAlunoParaInativo(0)
esc.listarDadosAlunoComIndex(0)
# print(esc.alunos)
# esc.listarAlunosPorTurma('0001')