from lib.interface import *
from lib.arquivo import *
from time import sleep

# Variável para armazenar o arquivo txt
arq = 'cadastros.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

# Estrutura de repetição para rodar o programa até o usuário dar a opção: "Sair do programa"
while True:
    resp = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa','Editar um Usuário', 'Apagar um Usuário', 'Sair do Sistema'])
    
    #Condição se a opção for 1
    if resp == 1:
        # Opção de listar o conteúdo de um arquivo 
        lerArquivo(arq)
        
    #Condição se a opção for 2
    elif resp == 2:
        # Opção de cadastrar um novo usuário
       cabecalho('NOVO CADASTRO')
       nome_usuario = str(input('Nome: '))
       idade = leiaInt('Idade: ')
       cadastrar(arq, nome_usuario, idade)
    
    #Condição se a opção for 3
    elif resp == 3:
        # Opção de editar usuário existente
        cabecalho('EDITAR USUÁRIO')
        nome_usuario = str(input('Qual usuário gostaria de editar: '))
        nova_idade = leiaInt('Nova idade:')
        editarNome(arq, nome_usuario, nova_idade)

         #Condição se a opção for 4
    elif resp == 4:
        # Opção de apagar usuário existente
        cabecalho('APAGAR USUARIO')
        apagar = str(input('Qual o nome do usuário que deseja apagar? '))
        apagarUsuario(arq, apagar)


    #Condição se a opção for 4
    elif resp == 5:
        cabecalho('Saindo do sistema... Até logo!')
        sleep(1)
        break

    #Condição se a opção for inválida(diferente de 1, 2 ou 3)
    else: 
        cabecalho('ERRO! Digite uma opção válida!')
        sleep(2)
