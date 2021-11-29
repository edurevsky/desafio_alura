from comandos_registro import registrarAluno, registrarProfessor, pedeEmail
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
    print('[9] - Ver Dados de um Aluno com ID')


def mostraErroNumero():
    """Comando para mostrar na tela caso valor recebido não seja tipo int"""
    print('Não foi inserido um número')


def pedeID():
    try:
        index = int(input('Digite o número do ID: '))
        return index
    except ValueError:
        mostraErroNumero()
        return None


def editarNomeAluno(index):
    nome = input('Digite o nome a ser mudado: ')
    esc.mudarNomeDoAluno(index, nome)
    print(f'Aluno (ID: {index}) teve nome alterado para {nome}.')


def editarEmailAluno(index):
    email = pedeEmail()
    esc.mudarEmailDoAluno(index, email)
    print(f'Email do aluno (ID: {index}) mudado para {email}.')


def editarTurmaAluno(index):
    turma = input('Digite a nova turma do aluno: ')
    esc.mudarTurmaDoAluno(index, turma)
    print(f'Turma do aluno (ID: {index}) mudado para {turma}')


def editarTurnoAluno(index):
    print('Para qual turno?\n[1] - Manha | [2] - Tarde | [3] - Noite')
    comando = int(input('Digite o comando >> '))
    if comando == 1:
        esc.mudarTurnoDoAlunoParaManha(index)
        print(f'Turno do aluno (ID: {index}) mudado para Manha')
    elif comando == 2:
        esc.mudarTurnoDoAlunoParaTarde(index)
        print(f'Turno do aluno (ID: {index}) mudado para Tarde')
    elif comando == 3:
        esc.mudarTurnoDoAlunoParaNoite(index)
        print(f'Turno do aluno (ID: {index}) mudado para Noite')


def editarStatusAluno(index):
    print('Mudar para:\n[1] - Ativo | [2] - Inativo')
    comando = int(input('Digite o comando >> '))
    if comando == 1:
        esc.mudarStatusAlunoParaAtivo(index)
        print(f'Status do aluno (ID: {index}) mudado para Ativo')
    elif comando == 2:
        esc.mudarStatusAlunoParaInativo(index)
        print(f'Status do aluno (ID: {index}) mudado para Inativo')


def mostraDadosAlunoComOpcoes(index):
    if index != None:
        esc.listarAlunoComIndex(index)
    comando = int(input('Deseja editar o aluno? [1] - Sim | [0] - Não\nDigite o comando >> '))
    if comando == 1:
        print('Você quer editar:\n[1] - Nome | [2] - Email | [3] - Turma | [4] - Turno | [5] - Status')
        comando = int(input('Digite o comando >> '))
        # Muda nome do aluno
        if comando == 1:
            editarNomeAluno(index)
        # Muda email do aluno
        elif comando == 2:
            editarEmailAluno(index)
        # Muda turma do aluno
        elif comando == 3:
            editarTurmaAluno(index)
        # Muda Turno do aluno
        elif comando == 4:
            editarTurnoAluno(index)
        # Muda Status do aluno
        elif comando == 5:
            editarStatusAluno(index)
        else:
            print('Opção não existe, voltando ao menu principal')
    else:
        pass # Não fazer nada


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
            mostraDadosAlunoComOpcoes(index)

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

        elif comando == 9:
            index = pedeID()
            if index != None:
                esc.listarDadosAlunoComIndex(index)
