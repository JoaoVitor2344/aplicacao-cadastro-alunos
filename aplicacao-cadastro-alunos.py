alunos = []

# Salvar
def cadastrar():
    print("\n ### Operação Cadastrar ###")

    matricula = input("Matricula: ")
    curso = input("curso: ")
    nome = input("nome: ")
    idade = input("idade: ")

    alunos.append(
        {'matricula':matricula, 'curso':curso, 'nome':nome, 'idade':idade}
    )

    print("Aluno cadastrado com sucesso!")

    if int(input("Gostaria de cadastrar uma nova pessoa? [1-Sim/2-Não] \n")) == 1:
        cadastrar()
    else: 
        menu()

# Atualizar
def atualizar():
    print("\n ### Operação Atualizar ###")

    matricula = input("Matricula: ")
    curso = input("curso: ")
    nome = input("nome: ")
    idade = input("idade: ")
    
    for i in range(0, len(alunos)):
        if alunos[i]['matricula'] == matricula:
            alunos[i]['curso'] = curso
            alunos[i]['nome'] = nome
            alunos[i]['idade'] = idade

            print("Aluno atualizado com sucesso!")

            if int(input("Gostaria de atualizar outra pessoa? [1-Sim/2-Não] \n")) == 1:
                atualizar()
            else: 
                menu()
                
    if input("Matricula inexistente! Tentar novamente? [1-Sim/2-Não]") == 1:
        atualizar()
    else:
        menu()

# Listar 
def listar():
    print("\n ### Operação Listar ###")

    if len(alunos) > 0:
        for i in range(0, len(alunos)):
            print("Matrícula: " + str(alunos[i]['matricula']) + ', Curso: ' + str(alunos[i]['curso']) + ', Nome: ' + str(alunos[i]['nome']) + ', Idade: ' + str(alunos[i]['idade']))
    else:
        print("Nenhum aluno cadastrado!")

    menu()

# Remover
def remover():
    print("\n ### Operação Remover ###")

    matricula = input("Digite a matricula do aluno para remover: ")
    i = 0
    for key in alunos:
        if matricula == key['matricula']:
            del alunos[i]
            print("Aluno removido com sucesso!")

            if int(input("Gostaria de remover outra pessoa? [1-Sim/2-Não] \n")) == 1:
                remover()
            else: 
                menu()
            break
        i += 1
    if int(input("Matrícula não encontrada. Tentar Novamente? [1-Sim/2-Não] \n")) == 1:
        remover()
    else: 
        menu()

def menu():
    print("\n ### Menu ### \n# 1 - cadastrar # \n# 2 - remover # \n# 3 - listar # \n# 4 - atualizar # \n# 5 - fechar #")
    resposta = int(input("Digite a operação: "))

    if resposta == 1:
        cadastrar()
    elif resposta == 2:
        remover()
    elif resposta == 3:
        listar()    
    elif resposta == 4:
        atualizar()
    elif resposta == 5:
        exit()

menu()