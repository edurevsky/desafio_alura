from comandos_registro import registrarAluno, registrarProfessor, pedeEmail
from escola import Escola


"""
------------- Comandos da interface -------------
"""

def mostraOpcoes():
    """Interface do sistema"""
    print() # Quebra de linha 
    print('[1] - Cadastrar Aluno')
    print('[2] - Cadastrar Professor')
    print('[3] - Listar Alunos')
    print('[4] - Listar Professores')
    print('[5] - Consultar e Editar Aluno com ID')
    print('[6] - Consultar e Professor com ID')
    print('[7] - Listar Alunos por Turma')
    print('[8] - Listar Alunos de um Professor')
    print('[9] - Ver Dados de um Aluno com ID')
    print('[10] - Remover Aluno com ID')
    print('[11] - Remover Professor com ID')
    print('[0] - SAIR')


def mostraErroNumero():
    """Comando para mostrar na tela caso valor recebido não seja tipo int"""
    print('Não foi inserido um número')


def pedeID():
    """Faz verificação se o input será do tipo int, caso contrário trata o ValueError e retorna None"""
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
    else:
        print('Opção não existe.')


def editarStatusAluno(index):
    print('Mudar para:\n[1] - Ativo | [2] - Inativo')
    comando = int(input('Digite o comando >> '))
    if comando == 1:
        esc.mudarStatusAlunoParaAtivo(index)
        print(f'Status do aluno (ID: {index}) mudado para Ativo')
    elif comando == 2:
        esc.mudarStatusAlunoParaInativo(index)
        print(f'Status do aluno (ID: {index}) mudado para Inativo')
    else:
        print('Opção não existe.')


def editarNomeProfessor(index):
    nome = input('Digite o nome a ser mudado: ')
    esc.mudarNomeProfessor(index, nome)
    print(f'Professor (ID: {index}) teve seu nome alterado para {nome}.')


def editarEmailProfessor(index):
    email = pedeEmail()
    esc.mudarEmailProfessor(index, email)
    print(f'Professor (ID: {index}) teve seu email alterado para {email}.')


def mostraAlunoComOpcoes(index):
    if index != None:
        if esc.listarAlunoIndex(index):
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


def mostraProfessorComOpcoes(index):
    if index != None:
        if esc.listarProfessorIndex(index):
            comando = int(input('Deseja editar o professor? [1] - Sim | [0] - Não\nDigite o comando >> '))
            if comando == 1:
                print('Você quer editar:\n[1] - Nome | [2] - Email')
                comando = int(input('Digite o comando >> '))
                # Muda nome do professor
                if comando == 1:
                    editarNomeProfessor(index)
                # Muda email do professor
                elif comando == 2:
                    editarEmailProfessor(index)
                else:
                    print('Opção não existe, voltando ao menu principal')
            else:
                pass 


"""
------------- Executável -------------
"""

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
                mostraAlunoComOpcoes(index)

        elif comando == 6:
            index = pedeID()
            if index != None:
                esc.listarProfessorIndex(index)

        elif comando == 7:
            codigo = input('Digite o código da turma: ')
            esc.listarAlunosTurma(codigo)

        elif comando == 8:
            index = pedeID()
            if index != None:
                esc.listarAlunosProfessor(index)

        elif comando == 9:
            index = pedeID()
            if index != None:
                esc.listarDadosAlunoIndex(index)

        elif comando == 10:
            index = pedeID()
            if index != None:
                esc.removeAluno(index)

        elif comando == 11:
            index = pedeID()
            if index != None:
                esc.removeProfessor(index)

        elif comando == 0:
            exit()

        else:
            print('\nComando digitado não existe.')
