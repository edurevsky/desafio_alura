import csv
from aluno import Aluno


class AlunoDAO():

    def salvar(self, aluno):
        with open('alunos.csv', 'a') as f:
            f.write(aluno.__csv__())

    
    def carregar(self):
        alunos = []
        with open('alunos.csv', 'r') as f:
            leitor = csv.reader(f)
            for linha in leitor:
                nome, email, turma, cgm, turno, status = linha
                aluno = Aluno(nome, email, turma, cgm, turno, status)
                alunos.append(aluno)
        return alunos
    

    def remover(self, cgmDoAluno: str):
        """Remove aluno pelo seu CGM"""
        alunos = []
        with open('alunos.csv', 'r') as f:
            leitor = csv.reader(f)
            for linha in leitor:
                alunos.append(linha)
                for campo in linha:
                    if campo == cgmDoAluno:
                        alunos.remove(linha)
        with open('alunos.csv', 'w') as nf:
            escreve = csv.writer(nf)
            escreve.writerows(alunos)


    def alterarParaAtivo(self):
        pass


    def alterarParaInativo(self):
        pass

        
# a = Aluno('eu', 'eu@escola.pr.gov.br', '0003', '11112222', Manha(), Ativo())
# AlunoDAO().remover('11112222')
# del x[0]
# print(x)