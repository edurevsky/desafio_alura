from comandos_registro import registrarAluno, registrarProfessor, pedeEmail
from escola import Escola
from validadores import Email


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
    print('[9] - Ver Dados Simples de um Aluno')


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
                aluno = esc.listarAlunoComIndex(index)
            comando = int(input('Deseja editar o aluno? [1] - Sim | [0] - Não\nDigite o comando >> '))
            if comando == 1:
                print('Você quer editar:\n[1] - Nome | [3] - Turma | [4] - Status')
                comando = int(input('Digite o comando >> '))
                # Muda nome do aluno
                if comando == 1:
                    nome = input('Digite o nome a ser mudado: ')
                    esc.mudarNomeDoAluno(index, nome)
                    print(f'Aluno com ID {index} teve nome alterado para {nome}!')
                elif comando == 2:
                    email = pedeEmail()
                    esc.mudarEmailDoAluno(index, email)
                # Muda turma do aluno
                elif comando == 3:
                    turma = input('Digite a nova turma do aluno: ')
                    esc.mudarTurmaDoAluno(index, turma)
                # Muda turno do aluno
                elif comando == 4:
                    print('Mudar para:\n[1] - Ativo | [2] - Inativo')
                    comando = int(input('Digite o comando >> '))
                    if comando == 1:
                        esc.mudarStatusAlunoParaAtivo(index)
                        print(f'Mudando status do aluno com ID {index} para Ativo')
                    elif comando == 2:
                        esc.mudarStatusAlunoParaInativo(index)
                        print(f'Mudando status do aluno com ID {index} para Inativo')
                    else:
                        print('Comando não existe, voltando ao menu principal')
            else:
                pass

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
