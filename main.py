from comandos_registro import registrarAluno, registrarProfessor
from escola import Escola


def mostraOpcoes():
    """Interface do sistema"""
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
    """Comando para mostrar na tela caso valor recebido não seja tipo int"""
    print('Não foi inserido um número')


def pedeID():
    try:
        index = int(input('Digite o número do ID: '))
        return index
    except ValueError:
        mostraErroNumero()


if __name__ == '__main__':

    esc = Escola()

    while True:

        mostraOpcoes()
        comando = int(input('Digite o comando >> '))

        if comando == 1:
            try:
                aluno = registrarAluno()
                esc.adicionaAluno(aluno)
            except ValueError as e:
                print(e)

        elif comando == 2:
            try:
                professor = registrarProfessor()
                esc.adicionaProfessor(professor)
            except ValueError as e:
                print(e)

        elif comando == 3:
            esc.listarAlunos()

        elif comando == 4:
            esc.listarProfessores()

        elif comando == 5:
            index = pedeID()
            if index != None:
                esc.listarAlunoComIndex(index)

        elif comando == 6:
            index = pedeID()
            if index != None:
                esc.listarProfessorComIndex(index)

        elif comando == 7:
            codigo = input('Digite o código da turma: ')
            esc.listarAlunosPorTurma(codigo)

        elif comando == 8:
            index = pedeID()
            if index != None:
                esc.listarAlunosDoProfessor(index)
