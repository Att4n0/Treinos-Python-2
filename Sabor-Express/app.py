import os
#Pra detectar o sistema operacional lá em baixo

import subprocess
#Pra dar instruções para programas externos. O clear, do bash, é um executável externo.
#O subprocess, em teoria, é mais seguro e moderno do que o import os. Vale dar uma conferida.
#Onde puder usar o subprocess no lugar do os, talvez seja melhor. Mas pesquisa, antes.

restaurantes = [
    {'nome':'Praça', 'categoria':'Japonesa', 'ativo':False}, 
    {'nome':'Pizza Suprema', 'categoria':'Pizza', 'ativo':True}, 
    {'nome':'Cantina', 'categoria':'Italiano', 'ativo':False}
]
#Lista de dicionários com nomes dos restaurantes e seus atributos.

def exibir_nome_do_programa():

    '''Exibe o nome do programa no topo do menu'''

    print('\n𝑺𝒂𝒃𝒐𝒓 𝑬𝒙𝒑𝒓𝒆𝒔𝒔\n')

def exibir_opcoes():

    '''Esta função exibe as opções na tela quando o menu principal é acionado.
    Essas são as opções que o usuário pode escolher, usando os números à esquerda.'''

    print ('1. Cadastrar restaurante')
    print ('2. Listar restaurantes')
    print ('3. Alternar estado do restaurante')
    print ('4. Sair\n')

def limpa_tela():

    '''Esta função é chamada toda vez queé necessário limpar a tela para clareza visual.
    Ela automaticamente detecta o sistema operacional do usuário entre Windows, Linux e Mac, usando o comando apropriado.'''

    if os.name == 'nt':
        #nt, aqui, delimita o windows.
        subprocess.run('cls', shell=True)
    else:
        subprocess.run(['clear'])
        #Pra linux e Mac
    
        #Podia ter usado o "os.system('clear')", mas, se puder, evita o os.

def exibir_subtitulos(texto):

    ''' Exibe um subtítulo estilizado na tela 
    
    Inputs:
    - texto: str - O texto do subtítulo
    '''

    limpa_tela()
    #Chama a função limpa_tela, que faz... o que ela faz.

    linha = '*' * len(texto)
    #Variável que cria asteriscos conforme o tamanho do texto. É estético, vai aparecer antes e depois dos subtítulos pra dar um charme.

    print(linha)
    print(texto)
    print(linha)
    print ()

def finalizar_app():

    '''Função chamada quando a opção "Sair" é escolhida no menu.
        Limpa a tela e exibe mensagem de finalização.
    '''

    if os.name == 'nt':
        #nt, aqui, delimita o windows.
        subprocess.run('cls', shell=True)
    else:
        subprocess.run(['clear'])
        #Pra linux e Mac

        #Podia ter usado o "os.system('clear')", mas, se puder, evita o os.
    
    exibir_subtitulos('Finalizando...\n')

def opcao_invalida():
    
    '''Quando o usuário imprime uma entrada diferente das opções do menu, a funçõ explica a situação e retorna ao menu.'''

    print('Opção Inválida!\n')
    input('Digite uma tecla para voltar ao Menu Principal.\n')
    main()

def voltar_ao_menu():
    
    '''Esta opção retorna ao menu sempre que solicitado pelas funções principais do programa (listagem, cadastro, etc.).
    
    Inputs:
    - Qualquer tecla do usuário no prompt

    Outputs:
    - Retorna ao menu principal

    '''

    input('\nDigite uma tecla para retornar ao menu principal.\n')
    main()

def cadastrar_novo_restaurante():
    
    '''Esta função é chamada pelo menu. Permite cadastrar um novo restaurante no banco de dados.
    
    Inputs:
    - Nome do restaurante
    - Categoria do restaurante

    Outputs
    - Adiciona um novo restaurante à lista de restaurantes

    '''

    exibir_subtitulos('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'\nDigite o nome da categoria do restaurante {nome_do_restaurante}: ')

    dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria, 'ativo':False}
    #Cria um dicionário usando os dados inseridos para o restaurante. Por padrão, ele não está "ativado"
    #(só significa que o 'ativo' é False e ele será mudado em outra função)
    #Note que se essa categoria será mudada depois, ela tem que existir, e por isso, deve ser declarada aqui).

    restaurantes.append(dados_do_restaurante)
    #Vai incluir o dicionário na lista de restaurantes, que é uma variável global indicada lá em cima.

    print(f'\nO restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n')
    voltar_ao_menu()

def listar_restaurantes():

    '''Esta função é chamada pelo menu. Ela lista os restaurantes atualmente cadastrados, bem como categoria e status de ativação.
    
    Output:
    - Exibe lista de restaurantes, categorias e status de ativação
    '''
    
    exibir_subtitulos('Lista dos restaurantes')

    print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status ')

    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        #Vai registrar na variável apenas o atributo 'nome' na lista. Esse atributo, é claro, é o nome do restaurante.
        categoria = restaurante['categoria']
        ativo = 'Ativado' if restaurante['ativo'] else 'Desativado'

        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')
        #O ljust faz com que, independente do tamanho do texto, existam X(aqui, 20) caracteres. Ajusta no espaçamento e estética.

    voltar_ao_menu()

def alternar_estado_restaurante():

    '''Esta função é chamada pelo menu. Ela permite mudar o status de ativação de um dos restaurantes cadastrados.
    
    Inputs:
    - Nome do restaurante que se quer mudar o status de ativação

    Outputs:
    - Muda o status de ativação do restaurante, se for encontrado.
    - Exibe mensagem informando o sucesso ou não da mudança.
    '''
    
    exibir_subtitulos('Alternando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alternar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            #Isso inverte a condição atual na categoria 'ativo'. True vira False, False vira true.

            mensagem = f'\nO restaurante {nome_restaurante} foi ativado com sucesso!' if restaurante['ativo'] else f'\nO restaurante {nome_restaurante} foi desativado com sucesso!'
            #Ternário: a variável toma um valor em um caso, outro valor em outro.

            print(mensagem)

    if not restaurante_encontrado:
        #Caso o restaurante não seja encontrado, restaurante_encontrado continua False, portanto o not transforma em True e este laço if acontece.
        print(f'\nO restaurante {nome_restaurante} não foi encontrado.')

    voltar_ao_menu()

def escolher_opcao():

    ''' Solicita e executa a opção escolhida pelo usuário 

    Inputs
    - Número relativo à escolha do usuário

    Outputs:
    - Executa a opção escolhida pelo usuário
    '''
    
    #opcao_escolhida = input ('Escolha uma opção: ') Não funciona aqui, porque a entrada, por padrão, é uma string. 
    # Duas opções:

    #Após o input que dá em string, faz uma nova variável que transforma o string em int:
    #opcao_escolhida = int(opcao_escolhida)
    #É, pode usar o mesmo nome de variável, mesmo.

    #OU:
    try:
        opcao_escolhida = int(input ('Escolha uma opção: '))
        
        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()

        elif opcao_escolhida == 2:
            listar_restaurantes()

        elif opcao_escolhida == 3:
            alternar_estado_restaurante()

        elif opcao_escolhida == 4:
            finalizar_app()

        else:
            opcao_invalida()

    except ValueError:
        opcao_invalida()

def main():

    '''Função vital, que é chamada ao abrir o programa e ao retornar ao menu. É ela que inicia a chamada de todas as outras
    funções.'''
    
    limpa_tela()
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    #Basicamente, se o programa foi aberto por si, e não chamado por outro programa, ele executa o que está em baixo.
    main()