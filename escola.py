from status import Ativo, Inativo
from turnos import Manha, Noite, Tarde


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

    def erroIndex(self, index):
        return f"Não há entidade com ID(index): '{index}' na lista."


    def adicionaProfessor(self, professor):
        self.professores.append(professor)


    def removeProfessor(self, index):
        try:
            del self.professores[index]
        except IndexError:
            print(self.erroIndex(index))


    def adicionaAluno(self, aluno):
        self.alunos.append(aluno)


    def removeAluno(self, index):
        try:
            del self.alunos[index]
        except IndexError:
            print(self.erroIndex(index))


    def listarProfessores(self):
        if len(self.professores) > 0:
            i = 0
            for professor in self.professores:
                print(f'ID(index): {i} - {professor}')
                i += 1
        else:
            print('Ainda não há professores registrados no sistema.')


    def listarAlunos(self):
        if len(self.alunos) > 0:
            i = 0
            for aluno in self.alunos:
                print(f'ID(index): {i} - {aluno}')
                i += 1
        else:
            print('Ainda não há alunos registrados no sistema.')
        

    def listarProfessorComIndex(self, index):
        try:
            print(self.professores[index])
        except IndexError:
            print(self.erroIndex(index))


    def listarAlunoComIndex(self, index):
        try:
            print(self.alunos[index])
        except IndexError:
            print(self.erroIndex(index))

    def listarDadosAlunoComIndex(self, index):
        try:
            print(self.alunos[index].__dados__())
        except IndexError:
            print(self.erroIndex(index))


    def listarDadosProfessorComIndex(self, index):
        try:
            print(self.professores[index].__dados__())
        except IndexError:
            print(self.erroIndex(index))


    def listarAlunosPorTurma(self, codigo):
        for aluno in self.alunos:
            if aluno.turma == codigo:
                print(aluno)
            else:
                print(f'Não há aluno na turma {codigo}')
    

    def listarAlunosDoProfessor(self, index):
        try:
            for codigo in self.professores[index].turmas:
                self.listarAlunosPorTurma(codigo)
        except IndexError:
            print(self.erroIndex(index))


    def mudarStatusAlunoParaAtivo(self, index):
        try:
            self.alunos[index].status = Ativo()
        except IndexError:
            print(self.erroIndex(index))
    

    def mudarStatusAlunoParaInativo(self, index):
        try:
            self.alunos[index].status = Inativo()
        except IndexError:
            print(self.erroIndex(index))


    def mudarTurmaDoAluno(self, index, turma):
        try:
            self.alunos[index].turma = turma
        except IndexError:
            print(self.erroIndex(index))


    def mudarTurnoDoAlunoParaManha(self, index):
        try:
            self.alunos[index].turno = Manha()
        except IndexError:
            print(self.erroIndex(index))


    def mudarTurnoDoAlunoParaTarde(self, index):
        try:
            self.alunos[index].turno = Tarde()
        except IndexError:
            print(self.erroIndex(index))
            

    def mudarTurnoDoAlunoParaNoite(self, index):
        try:
            self.alunos[index].turno = Noite()
        except IndexError:
            print(self.erroIndex(index))


    def mudarNomeDoAluno(self, index, nome):
        try:
            self.alunos[index].nome = nome
        except IndexError:
            print(self.erroIndex(index))


    def mudarEmailDoAluno(self, index, email):
        try:
            self.alunos[index].email = email
        except IndexError:
            print(self.erroIndex(index))

