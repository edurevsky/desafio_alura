from comandos_registro import registrarAluno, registrarProfessor
from escola import Escola


def mostraOpcoes():
    print() # Quebra de linha 
    print('[1] - Cadastrar Aluno')
    print('[2] - Cadastrar Professor')
    print('[3] - Listar Alunos')
    print('[4] - Listar Professores')
    print('[5] - Consultar Aluno com ID')
    print('[6] - Consultar Professor com ID')
    print('[7] - Listar Alunos por Turma')
    print('[8] - Listar Alunos de um Professor')


def mostraErroNumero():
    print('Não foi inserido um número')


def tenteFazer(algo):
    try:
        algo
    except ValueError:
        mostraErroNumero()


if __name__ == '__main__':

    while True:

        esc = Escola()
        mostraOpcoes()
        comando = int(input('Digite o comando >> '))

        if comando == 1:
            aluno = registrarAluno()
            esc.adicionaAluno(aluno)

        elif comando == 2:
            professor = registrarProfessor()
            esc.adicionaProfessor(professor)

        elif comando == 3:
            esc.listarAlunos()

        elif comando == 4:
            esc.listarProfessores()

        elif comando == 5:
            index = int(input('Digite o número do ID: '))
            tenteFazer(esc.listarAlunoComIndex(index))

        elif comando == 6:
            index = int(input('Digite o número do ID: '))
            tenteFazer(esc.listarProfessorComIndex(index))

        elif comando == 7:
            codigo = input('Digite o código da turma: ')
            tenteFazer(esc.listarAlunosPorTurma(codigo))

        elif comando == 8:
            index = int(input('Digite o número do ID: '))
            tenteFazer(esc.listarAlunosDoProfessor(index))
