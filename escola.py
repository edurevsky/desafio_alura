from aluno import Aluno
from professor import Professor
from status import Ativo
from turnos import Manha, Tarde
from alunoDAO import AlunoDAO


class Escola(object):

    def __init__(self):
        self.__professores = []
        self.__alunos = AlunoDAO().carregar()

    @property
    def alunos(self):
        return self.__alunos

    @property
    def professores(self):
        return self.__professores


    def adicionaProfessor(self, professor):
        self.professores.append(professor)


    def removeProfessor(self, indexDoProfessor):
        del self.professores[indexDoProfessor]


    def adicionaAluno(self, aluno):
        AlunoDAO().salvar(aluno)


    def removeAluno(self, cgmDoAuluno):
        AlunoDAO().remover(cgmDoAuluno)


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


    def listarAlunosPorTurma(self, codigo):
        for aluno in self.alunos:
            if aluno.turma == codigo:
                print(aluno)

    
    def listarAlunosDoProfessor(self, indexDoProfessor):
        for codigo in self.professores[indexDoProfessor].turmas:
            self.listarAlunosPorTurma(codigo)


esc = Escola()


p1 = Professor('Fulano', 'fulano@escola.pr.gov.br', ['0001'], Manha())
p2 = Professor('John Doe', 'john.doe@escola.pr.gov.br', ['0002'], Tarde())

a1 = Aluno('Ciclano', 'ciclano@escola.pr.gov.br', '0001', '11111111', Manha(), Ativo())
a2 = Aluno('Beltrano', 'beltrano@escola.pr.gov.br', '0001', '22222222', Manha(), Ativo())
a3 = Aluno('Sem Nome', 'sem.nome@escola.pr.gov.br', '0002', '33333333', Tarde(), Ativo())

# esc.adicionaAluno(a1)
# esc.adicionaAluno(a2)
# esc.adicionaAluno(a3)
# esc.adicionaProfessor(p1)
# esc.adicionaProfessor(p2)
esc.listarAlunos()
# print(esc.alunos)
# esc.listarAlunosPorTurma('0001')