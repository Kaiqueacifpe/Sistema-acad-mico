alunos = []


def adicionar_aluno(nome):
    aluno_novo = {
        "nome": nome,
        "notas": [],
        "frequencia": 0
    }
    alunos.append(aluno_novo)
    print(f'Aluno {nome} adicionado com sucesso.')


def adicionar_nota(nome, nota):
    for aluno in alunos:
        if aluno['nome'] == nome and len(aluno['notas']) < 4:
            aluno['notas'].append(nota)
            print(f'Nota {nota} adicionada para o aluno {nome}.')
            return
    print(f'Não foi possível adicionar a nota para o aluno {nome}.')


def adicionar_frequencia(nome, frequencia):
    for aluno in alunos:
        if aluno['nome'] == nome:
            aluno['frequencia'] = frequencia
            print(f'Frequência de {frequencia} adicionada para o aluno {nome}.')
            return
    print(f'Aluno {nome} não encontrado.')


def remover_aluno(nome):
    for i in range(len(alunos)):
        if alunos[i]['nome'] == nome:
            alunos.pop(i)
            print(f'Aluno {nome} removido com sucesso.')
            return
    print(f'Aluno {nome} não encontrado.')


def editar_nome_aluno(nome_antigo, nome_novo):
    for aluno in alunos:
        if aluno['nome'] == nome_antigo:
            aluno['nome'] = nome_novo
            print(f'Nome do aluno alterado para {nome_novo} com sucesso.')
            return
    print(f'Aluno {nome_antigo} não encontrado.')


def listar_alunos():
    if not alunos:
        print("Nenhum aluno cadastrado.")
        return
    for aluno in alunos:
        status = 'Aprovado'
        media_nota = sum(aluno['notas']) / len(aluno['notas']) if aluno['notas'] else 0
        carga_horaria = 100
        if media_nota < 7.0:
            status = 'Reprovado por nota'
        elif aluno['frequencia'] < (carga_horaria * 75 / 100):
            status = 'Reprovado por falta'
        print(f"{aluno['nome']} - Média: {media_nota:.2f} / Frequência: {aluno['frequencia']} aulas - ({status})")


def menu():
    print("\nBem Vindo ao Sistema Acadêmico")
    print("Menu:")
    print("1 - Adicionar novo aluno")
    print("2 - Adicionar nota")
    print("3 - Adicionar frequência")
    print("4 - Remover aluno")
    print("5 - Editar nome do aluno")
    print("6 - Listar alunos")
    print("7 - Sair do programa")

    return input("Digite sua opção: ")


def main():
    while True:
        opcao = menu()
        if opcao == "1":
            nome = input('Digite o nome do aluno: ')
            adicionar_aluno(nome)
        elif opcao == "2":
            nome = input('Digite o nome do aluno: ')
            nota = float(input('Digite a nota do aluno: '))
            adicionar_nota(nome, nota)
        elif opcao == "3":
            nome = input('Digite o nome do aluno: ')
            frequencia = int(input('Digite a frequência do aluno: '))
            adicionar_frequencia(nome, frequencia)
        elif opcao == "4":
            nome = input('Digite o nome do aluno a remover: ')
            remover_aluno(nome)
        elif opcao == "5":
            nome_antigo = input('Digite o nome atual do aluno: ')
            nome_novo = input('Digite o novo nome do aluno: ')
            editar_nome_aluno(nome_antigo, nome_novo)
        elif opcao == "6":
            listar_alunos()
        elif opcao == "7":
            print("Bye bye...")
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()
