import os
import platform

restaurantes = [{'nome':'SushiMan', 'categoria': 'Japonesa', 'ativo':True},
                {'nome':'Familia Gasperin', 'categoria': 'Pizza', 'ativo':False}]

def exibir_nome_do_programa():

    '''Exibe o nome da aplicação'''

    print("""
    ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
    ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
    ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
    ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
    ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
    """)

def voltar_ao_menu_principal():
    input('\nAperte uma tecla para voltar ao menu principal.')
    main()

def exibir_subtitulo(texto):

    '''Exibe o subtítulo na tela
    
    Inputs: texto a ser exibido na tela
    
    Output: faz o print do texto'''

    print(texto)

def finalizar_app():

    '''Limpa o console e finaliza a aplicação.'''

    limpar_console()
    exibir_subtitulo('Saindo da aplicação.\n')

def exibir_opcoes():

    '''Exibe quais opções o usuário pode escolher'''

    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurante')
    print('3. Ativar Restaurante')
    print('4. Sair\n')

def opcao_invalida():

    '''Exibe no console a mensagem informando que a opção escolhida é inválida'''

    print('Opção inválida.')
    voltar_ao_menu_principal()

def cadastrar_restaurante():

    '''Cadastra um restaurante e o adiciona na lista de restaurantes
    
    Inputs: 
    - Nome do restaurante
    - Categoria do restaurante
    
    Outputs:
    - Mensagem de confirmação'''

    limpar_console()
    exibir_nome_do_programa()
    exibir_subtitulo('CADASTRO DE NOVOS RESTAURANTES\n')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite a categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome': nome_do_restaurante,'categoria': categoria, 'ativo': False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    voltar_ao_menu_principal()

def listar_restaurantes():

    '''Lista os restaurantes que ja foram cadastrados'''

    limpar_console()
    exibir_nome_do_programa()
    exibir_subtitulo('LISTANDO RESTAURANTES\n')

    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        status = 'Ativado' if restaurante['ativo'] else 'Desativado'
        print(f'- {nome_restaurante} | {categoria} | {status}')

    voltar_ao_menu_principal()

def alternar_status():

    '''Ativa ou desativa o status do restaurante
    
    Inputs:
    - Nome do restaurante
    
    Outputs:
    -Mensagem de confirmação ou negação'''

    limpar_console()
    exibir_nome_do_programa()
    exibir_subtitulo('ALTERNANDO STATUS DO RESTAURANTE\n')
    nome_restaurante = input('Digite o nome do restaurante que deseja alternar o satus: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado.'
            print(mensagem)

    if not restaurante_encontrado:
        print('O restaurante não foi encontrado.')

    voltar_ao_menu_principal()

def escolher_opcao():

    '''Pergunta ao usuário qual a ação desejada e executa a função correspondente
    
    Inputs:
    - Escolha da opção por dígitos de 1 a 4
    
    Outputs:
    - Executa as funções correspondentes para cada opção'''

    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        print(f'Você escolheu a opção {opcao_escolhida}.\n')

        if opcao_escolhida == 1:
            cadastrar_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_status()
        elif opcao_escolhida == 4:
            limpar_console()
            exibir_nome_do_programa()
            print('Saindo da aplicação.')
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def limpar_console():
    sistema = platform.system()
    if sistema == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def main():
    '''Exibe o menu principal do programa'''
    limpar_console()
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()