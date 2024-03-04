"""
    TESTE LABSYSTEM, REALIZAR UM CRUD DE CADASTRO DE PRODUTOS 
    * Desenvolva uma tela de cadastro de produto, onde é possivel, listar os produtos, adicionar o produto, editar o produto e excluir o produto.
    * Na lista de produtos queremos que contenha, id do produto, data do cadastro, usuario que cadastrou, a descrição do produto, quantidade do produto e valor do produto.
    * Em editar o produto é possivel editar a descrição do produto e valor do produto.
"""

import telas
import banco
import formato
import os # biblioteca que utilizo para limpar o Terminal

def limpar_tela(): # Função para limpar a o terminal
    print("\n" * os.get_terminal_size().lines) 

def menu_principal(): # Menu principal 
    limpar_tela()
    telas.exibir_menu_principal()
    numero_escolhido_pelo_usuario = int(input('| escolha o que deseja aqui : ')) # Armazena o valor digitado pelo o usuário na variável.
    limpar_tela()
    identificar_escolha_usuario_menu(numero_escolhido_pelo_usuario) # Chamada da função que identifica a escolha do usuário.

def criar_produto(): # CREATE | Criação de um novo produto, onde é solicitado nome do usuario, nome do produto, descricao do produto, quantidade do produto e valor do produto.
    exibir_cabecalho_novo_produto()
    nome_produto = input("| Digite o nome do produto : ") 
    limpar_tela()
    exibir_cabecalho_novo_produto()
    print("| Ex: Marca, Modelo, Material, Utilidade, Config, etc.. ")
    descricao_produto = input("| Descrição do produto : ")
    limpar_tela()
    exibir_cabecalho_novo_produto()
    quantidade_produto = obter_numero_inteiro()
    limpar_tela()
    exibir_cabecalho_novo_produto()
    valor_produto = obter_numero_real() 
    banco.inserir(nome_produto, nome_usuario, descricao_produto, quantidade_produto, valor_produto)
    limpar_tela()
    telas.exibir_adicionado_com_sucesso(nome_produto)
    escolha_ver_produtos()

def visualizar_produtos(): # READ
    resultados = banco.listar()
    tabela = formato.tabela_formata(resultados)
    print(tabela)
    escolha_voltar_menu()

def editar_produto(): #UPDATE | Menu para editar os produtos
    limpar_tela()
    telas.exibir_tela_editar_produto()                                  
    escolha_usuario_menu_editar = int(input("| :")) # Condicional para verificar a escolha do usuário no menu editar
    if (escolha_usuario_menu_editar == 1): 
        editar_nome_produto()
    elif (escolha_usuario_menu_editar == 2): 
        editar_descricao_produto()
    elif (escolha_usuario_menu_editar == 3): 
        editar_quantidade_produto()
    elif (escolha_usuario_menu_editar == 4): 
        editar_valor_produto()
    elif (escolha_usuario_menu_editar == 5): 
        menu_principal()
    else: 
        erro_menu_editar()

def deletar_produto(): # DELETE
    # Mostra os produtos cadastrados antes de deletar
    resultados = banco.listar()
    tabela = formato.tabela_formata(resultados)
    print(tabela)
    id = input("| Digite o id do produto que deseja DELETAR : ")
    banco.deletar(id)
    try:
        telas.exibir_produto_excluido(id)
    except Exception as e:
        limpar_tela()
        telas.exibir_erro_excluir_produto(e)
        deletar_produto()
    escolha_ver_produtos()
    limpar_tela()

def identificar_escolha_usuario_menu(escolha_usuario_menu_principal): # Verifica a escolha do usuário no MENU PRINCIPAL
    if (escolha_usuario_menu_principal == 1): 
        criar_produto()
    elif (escolha_usuario_menu_principal == 2): 
        visualizar_produtos() 
    elif (escolha_usuario_menu_principal == 3): 
        editar_produto() 
    elif (escolha_usuario_menu_principal == 4): 
        deletar_produto()
    elif (escolha_usuario_menu_principal == 5): 
        detalhes_teste() 
    elif (escolha_usuario_menu_principal == 6):
        saida()
    else: 
        erro_menu()

def continuar_editando(): # Função que pergunta ao usuário se ele deseja continuar editando.
    resposta_usuario = input("| Deseja contiuar editando? [S] / [N] : ")
    if resposta_usuario.upper()[0] == "S":
        limpar_tela()
        editar_produto()
    elif resposta_usuario.upper()[0] == "N":
        limpar_tela()
        menu_principal()
    else:
        telas.exibir_erro_inserido_invalido
        continuar_editando()

def escolha_ver_produtos(): # Assim que usuário modificar a tabela ele será redirecionado para essa função.
    resposta_usuario = input("| Deseja ver os produtos ? [S] / [N] :")
    if resposta_usuario.upper()[0] == "S":
        limpar_tela()
        visualizar_produtos()
    elif resposta_usuario.upper()[0] == "N":
        limpar_tela()
        menu_principal()
    else:
        telas.exibir_erro_inserido_invalido()
        escolha_ver_produtos()

def escolha_voltar_menu(): # Assim que o usuário visualizar a tabela ele será redirecionado para essa função.
    resposta_usuario = input("| Deseja voltar para o menu ? [S]/[N] :")
    if resposta_usuario.upper()[0] == "S":
        limpar_tela()
        menu_principal()
    elif resposta_usuario.upper()[0] == "N":
        limpar_tela()
        saida()
    else:
        telas.exibir_erro_inserido_invalido()
        escolha_voltar_menu()

def exibir_cabecalho_novo_produto():
    telas.exibir_adiciando_produto()

def obter_numero_inteiro(): # Função que verifica se o usuário digitou um número e inteiro
    while True:
        try:
            qtd = int(input("| Digite a quantidade desse produto: "))
            if(qtd < 0):
                raise ValueError
            return qtd
        except ValueError:
            print("DIGITE UM NÚMERO INTEIRO!")

def obter_numero_real(): # Função que verifica se o usuário digitou um número e inteiro
    while True:
        try:
            qtd = float(input("| Digite o valor desse produto: "))
            if(qtd < 0):
                raise ValueError
            return qtd
        except ValueError:
            print("DIGITE UM NÚMERO Inteiro OU Real !")

def erro_menu_editar(): # Função que exibe uma mensagem de se o usuário escolher um número fora do padrão. 
    limpar_tela()
    telas.exibir_erro_menu_editar()
    editar_produto()

def produto_atualizado(mensagem, produto_atualizado):
    limpar_tela()
    telas.exibir_produto_atualizado(mensagem, produto_atualizado)
    escolha_ver_produtos()

def editar_nome_produto(): # 1 edita o nome do produto na tabela de cadastro de produtos
    limpar_tela()
    resultados = banco.listar()
    tabela = formato.tabela_formata(resultados)
    print(tabela)
    exibir_nome_atualizado = "Nome do produto atualizado: "
    id = input("| Escolha o ID na coluna idProdutos que deseja editar \n | :")
    novo_nome_produto = input("| Editar nome do produto : ")
    banco.atualizar_nome_produto(novo_nome_produto, id)
    limpar_tela()
    produto_atualizado(exibir_nome_atualizado, novo_nome_produto)
    escolha_ver_produtos

def editar_descricao_produto(): # 2 edita a descrição do produto na tabela de cadastro de produtos
    limpar_tela()
    resultados = banco.listar()
    tabela = formato.tabela_formata(resultados)
    print(tabela)
    exibir_descricao_atualizada = "Descrição do produto atualizado : "
    id = input("| Escolha o ID do produto que deseja editar a descrição: ")
    nova_descricao_produto = input("| Editar descrição: ")
    banco.atualizar_descricao(nova_descricao_produto, id)
    produto_atualizado(exibir_descricao_atualizada, nova_descricao_produto)
    escolha_ver_produtos

def editar_quantidade_produto(): # 3 edita a quantidade do produto da tabela cadastro de produtos
    limpar_tela()
    resultados = banco.listar()
    tabela = formato.tabela_formata(resultados)
    print(tabela)
    exibir_quantidade_atualizada = "Quantidade do produto atualizado : "
    id = input("| Escolha o ID do produto que deseja editar a descrição \n | :")
    nova_quantidade_produto = int(input("| Editar descrição : "))
    banco.atualizar_quantidade_produto(nova_quantidade_produto, id)
    produto_atualizado(exibir_quantidade_atualizada, nova_quantidade_produto)
    escolha_ver_produtos()

def editar_valor_produto(): # 4 edita o valor da tabela cadastro de produtos
    limpar_tela()
    resultados = banco.listar()
    tabela = formato.tabela_formata(resultados)
    print(tabela)
    exiibir_valor_atualizado = "Valor do produto atualizado : "
    id_produto = input("| Escolha o ID do produto que deseja editar o valor \n | :")
    novo_valor_produto = int(input("| Editar valor : "))
    banco.atualizar_valor(novo_valor_produto, id_produto)
    produto_atualizado(exiibir_valor_atualizado, novo_valor_produto)
    escolha_ver_produtos()

def detalhes_teste():
    limpar_tela()
    telas.exibir_detalhes_teste()
    escolha_voltar_menu()

def erro_menu():
    limpar_tela()
    telas.exibir_erro_menu_principal()
    menu_principal()

def saida():
    limpar_tela()
    telas.exibir_tela_de_saida()
    quit()

nome_usuario = input("DIGITE SEU NOME PARA INICIAR O TESTE: ")
menu_principal()
