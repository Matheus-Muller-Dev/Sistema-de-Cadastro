from lib.interface import  *

#Função utilizada para verificar o arquivo 
def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else: 
        return True


# Função utilizada para criar o arquivo   
def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um erro na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')
    
    
# Função utilizada para ler o arquivo
def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Houve um erro ao abrir o arquivo!')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.strip().split(';')
            if len(dado) == 2:
                nome, idade = dado
                print(f'{nome:<30}{idade:>2} Idade')
            else: 
                print('Linha inválida encontrada no arquivo.')
    finally:
        a.close


# Função utilizada para fazer o cadastro    
def cadastrar(arq, nome = 'desconhecido', idade = 0):
    try:
        a = open(arq, 'at')
    
    except:
        print('Houve um erro ao abrir o arquivo!')

    else: 
        try:
            a.write(f'{nome};{idade}\n')

        except:
            print('Houve um erro na hora de escrever os dados!')
        
        else: 
            print(f'Novo registro de {nome} adicionado.')
            a.close()

# Função para apagar usuário
def apagarUsuario(arquivo, nome_usuario):
    try:
        with open(arquivo, 'r') as file:
            linhas = file.readlines()

        with open(arquivo, 'w') as file:
            usuario_removido = False
            for linha in linhas:
                if nome_usuario not in linha:
                    file.write(linha)
                else:
                    usuario_removido = True

            if usuario_removido:
                print(f'Usuário {nome_usuario} foi removido com sucesso!')
            else:
                print(f'Usuário {nome_usuario} não encontrado.')
    except FileNotFoundError:
        print('Arquivo não encontrado.')

# Função para editar arquivo
def editarNome(arquivo, nome_usuario, nova_idade):
    try:
        with open(arquivo, 'r') as file:
            linhas = file.readlines() 

        usuario_editado = False  

        with open(arquivo, 'w') as file:
            for linha in linhas:
                if ';' in linha:
                    nome, idade = linha.strip().split(';')
                    if nome == nome_usuario:
                        nova_linha = f'{nome};{nova_idade}\n'
                        file.write(nova_linha)
                        usuario_editado = True
                        print(f'O usuário {nome} teve a sua idade atualizada para: {nova_idade}')
                    else:
                        file.write(linha)  
                else:
                    file.write(linha)  

        if not usuario_editado:
            print(f'Nome {nome_usuario} não encontrado.')

    except FileNotFoundError:
        print('Arquivo não foi encontrado.')

                    
                    
