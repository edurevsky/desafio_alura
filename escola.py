from aluno import AlunoBuilder
from professor import ProfessorBuilder


class Escola(object):

    def __init__(self):
        self.__alunos = []
        self.__professores = []

    def addAluno(self, aluno):
        self.__alunos.append(aluno)

    def removeAluno(self, index):
        del self.__alunos[index]

    def addProfessor(self, professor):
        self.__professores.append(professor)

    def removeProfessor(self, index):
        del self.__professores[index]

    def listarTodosAlunos(self):
        for i in self.__alunos:
            print(i)

    def listarTodosProfessores(self):
        for i in self.__professores:
            print(i)

    def mudarStatusAlunoParaAtivo(self, indexAluno):
        self.__alunos[indexAluno]._paraAtivo()

    def mudarStatusAlunoParaInativo(self, indexAluno):
        self.__alunos[indexAluno]._paraInativo()

    def listarAlunosComTurma(self, codTurma):
        for i in self.__alunos:
            if i.turma == codTurma:
                print(i)

    def listarAlunosDeUmProfessor(self, indexProfessor):
        """Recebe o index do professor que está na lista professores e printa seus alunos com base em seus códigos de turma."""
        for codigo in self.__professores[indexProfessor].turma:
                print('Alunos da turma ' + codigo)
            # for aluno in self.__alunos:
                self.listarAlunosComTurma(codigo)


esc = Escola()

p1 = ProfessorBuilder().comNome('Silvio').comEmail('silvio@escola.pr.gov.br').comTurma('0001').comTurma('0002').comTurnoVespertino().build()
a1 = AlunoBuilder().comNome('Eduardo').comEmail('eduardo@escola.pr.gov.br').comTurma('0001').comCgm('11111111').comTurnoVespertino().comStatusAtivo().build()
a2 = AlunoBuilder().comNome('João').comEmail('joao@escola.pr.gov.br').comTurma('0002').comCgm('22222222').comTurnoVespertino().comStatusAtivo().build()

esc.addProfessor(p1)
esc.addAluno(a1)
esc.addAluno(a2)

esc.listarAlunosDeUmProfessor(0)

# esc.listarAlunosComTurma('0001')
# esc.listarTodosAlunos()