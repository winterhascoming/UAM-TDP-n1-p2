def Menu(Escolha,Cadastro):
    while Escolha != 7:
        print('''        [ 1 ] Cadastrar Usuário
        [ 2 ] Exibir Cadastros
        [ 3 ] Exibir Cadastros A -> Z
        [ 4 ] Buscar Usuário
        [ 5 ] Excluir Usuário
        [ 6 ] Editar Cadastro
        [ 7 ] Encerrar Sistema''')
        Escolha = int(input('>>>'))
        if Escolha == 1:
            CadastrarUsuarios(Cadastro)
        elif Escolha == 2:
            ExibirCadastros(Cadastro) 
        elif Escolha == 3:
            ExibirCadastrosAZ(Cadastro)
        elif Escolha == 4:
            BuscarUsuario(Cadastro)
        elif Escolha == 5:
            ExcluirUsuario(Cadastro)
        elif Escolha == 6:
            EditarUsuario(Cadastro)
        elif Escolha == 7:
            print('Encerrando Sistema...')
        else:
            print('Escolha inválida. Tente novamente!')
        print('-=' * 25)

def CadastrarUsuarios(Cadastro):
    Repetir = 0
    while Repetir != 1:
        Nome = input('Digite o Nome Completo a ser cadastrado: ')
        Email = input('Digite o email a ser cadastrado: ')
        if Cadastro.get(Nome):
            print('Nome já cadastrado no Sistema. ', Nome)
        elif Cadastro.get(Email):
            print('Email já cadastrado no Sistema', Email)
        else:
            Cadastro[Nome] = Email
        Repetir = int(input('''        [ 0 ] Cadastrar outro Usuário
        [ 1 ] Voltar ao Menu\n>>>''')) 

def ExibirCadastros(Cadastro):
        print(Cadastro)

def ExibirCadastrosAZ(Cadastro):
    for i in sorted(Cadastro, key = Cadastro.get, reverse=False):
        print(i, Cadastro[i])

def BuscarUsuario(Cadastro):
    Busca=input('Digite o nome do Usuário desejado: ')
    if Cadastro.get(Busca):
        print('Usuário: {} Cadastrado no Sistema.'.format(Busca))
    else:
        print('Usuário: {} Não Cadastrado no Sistema.'.format(Busca))

def ExcluirUsuario(Cadastro):
    Buscar = input('Digite o Email do usuário a ser excluído: ')
    Removido = []
    for i in Cadastro.items(): 
        if Cadastro[i] == Buscar:
            Removido.append(i)

    for item in Removido:
        Cadastro.pop(item)

    print(Cadastro)

def EditarUsuario(Cadastro):
    Buscar = input('Digite o email correspondente ao Usuário que deseja editar: ')
    Removido = []
    for key in Cadastro.items(): 
        if Cadastro[key] == Buscar:
            Removido.append(key)

    for item in Removido:
        Cadastro.pop(item)
        NovoNome = input('Digite o Nome Completo a ser cadastrado: ')
        Cadastro.update({NovoNome:Buscar})

    print(Cadastro)

def main():

    Escolha = 0
    Cadastro = {}
    Menu(Escolha, Cadastro)

if __name__ == "__main__":
    main()
