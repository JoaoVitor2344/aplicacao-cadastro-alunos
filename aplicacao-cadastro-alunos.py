alunos = []

def encontraAluno(matricula):
    for aluno in alunos:
        if matricula == aluno['matricula']:
            return 1
    
    return 0

# Salvar
def cadastrar():
    print("\n ### Operação Cadastrar ###")

    matricula = input("Matricula: ")
    if encontraAluno(matricula):
        if int(input("Matricula já cadastrada. Tentar Novamente? [1-Sim/2-Não] R: ")) == 1:
            cadastrar()
        else: 
            menu()

    curso = input("curso: ")
    nome = input("nome: ")
    idade = input("idade: ")

    alunos.append(
        {'matricula':matricula, 'curso':curso, 'nome':nome, 'idade':idade}
    )
    
    if encontraAluno(matricula):
        print("Aluno cadastrado com sucesso!")

    if int(input("Gostaria de cadastrar uma nova pessoa? [1-Sim/2-Não] R: ")) == 1:
        cadastrar()
    else: 
        menu()

# Atualizar
def atualizar():
    print("\n ### Operação Atualizar ###")

    matricula = input("Matricula: ")
    if encontraAluno(matricula):
        curso = input("curso: ")
        nome = input("nome: ")
        idade = input("idade: ")
        
        for i in range(0, len(alunos)):
            if alunos[i]['matricula'] == matricula:
                alunos[i]['curso'] = curso
                alunos[i]['nome'] = nome
                alunos[i]['idade'] = idade

                print("Aluno atualizado com sucesso!")

                if int(input("Gostaria de atualizar outra pessoa? [1-Sim/2-Não] R: ")) == 1:
                    atualizar()
                else: 
                    menu()
    else:
        if int(input("Matrícula não encontrada. Tentar Novamente? [1-Sim/2-Não] R: ")) == 1:
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
    if encontraAluno(matricula):
        for aluno in alunos:
            for i in range(len(alunos)):
                if matricula == aluno['matricula']:
                    del alunos[i]

                    if encontraAluno(matricula):
                        if int(input("Não foi possivel remover o aluno. Tentar Novamente? [1-Sim/2-Não] R: ")) == 1:
                            remover()
                        else: 
                            menu()
                    else:
                        print("Aluno removido com sucesso!")     

                    if int(input("Gostaria de remover outra pessoa? [1-Sim/2-Não] R: ")) == 1:
                        remover()
                    else: 
                        menu()
                    
                    break
    else:
        if int(input("Matrícula não encontrada. Tentar Novamente? [1-Sim/2-Não] R: ")) == 1:
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

if __name__ == "__main__":
    menu()