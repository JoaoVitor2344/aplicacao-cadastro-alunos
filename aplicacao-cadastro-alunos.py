alunos = [
    {'matricula':'1', 'curso':'ads', 'nome':'joão', 'idade':'18'}
]

def cadastrar():
    print("### Operação Cadastrar ###")

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

def remover():
    print("### Operação Remover ###")

    matricula = input("Digite a matricula do aluno para remover: ")
    for key in alunos:
        if matricula == key:
            del matricula[key]
            print("Aluno removido com sucesso!")
            break

    if int(input("Gostaria de remover outra pessoa? [1-Sim/2-Não] \n")) == 1:
        remover()
    else: 
        menu()

def listar():
    print("### Operação Listar ###")

    for i in range(0, len(alunos)):
        print(str(alunos[i]['matricula']) + ', ' + str(alunos[i]['curso']) + ', ' + str(alunos[i]['nome']) + ', ' + str(alunos[i]['idade']))

    menu()

def atualizar():
    print("### Operação Atualizar ###")

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

def menu():
    print("### Menu ### \n# 1 - cadastrar # \n# 2 - remover # \n# 3 - listar # \n# 4 - atualizar # \n# 5 - fechar #")
    resposta = int(input("Digite a operação: "))

    if resposta == 1:
        cadastrar()
    elif resposta == 2:
        remover()
    elif resposta == 3:
        listar()    
    elif resposta == 4:
        atualizar()

menu()