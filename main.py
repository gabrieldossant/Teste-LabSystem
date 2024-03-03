"""
    TESTE LABSYSTEM, REALIZAR UM CRUD DE CADASTRO DE PRODUTOS 
    * Desenvolva uma tela de cadastro de produto, onde é possivel, listar os produtos, adicionar o produto, editar o produto e excluir o produto.
    * Na lista de produtos queremos que contenha, id do produto, data do cadastro, usuario que cadastrou, a descrição do produto, quantidade do produto e valor do produto.
    * Em editar o produto é possivel editar a descrição do produto e valor do produto.
"""
import mysql.connector # configure o banco de dados de sua preferência
import os # biblioteca que utilizo para limpar o Terminal
from prettytable import PrettyTable # biblioteca que serve para ajustar o tamanho da tabela de acordo com os dados contigos nela.
import re # biblioteca que utilizo para verificar se o usuário digitou um dado em um determinado padrão, por exemplo (Data).
import datetime # biblioteca que utilizo para ter o dia atual de hoje para manter o código sempre atualizado.

# Configuração de conexão com o banco de dados
conexao = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'bdCadastro',
)

hoje = datetime.date.today() # Armazeno em uma variável a data atual de hoje.

cursor = conexao.cursor() # cursor é o objeto que é utilizado para processar os resultados de uma consulta SQL.

def limpar_tela(): # Função para limpar a o terminal
    print("\n" * os.get_terminal_size().lines) 

def menu_principal(): # Menu principal 
    limpar_tela()
    print( 
        "+-------------------------------------------------------------+\n"
        "|                T E S T E   L A B  S Y S T E M               |\n"
        "+-------------------------------------------------------------+\n"
        "|                  M E N U   P R I N C I P A L                |\n"
        "|  - - - - - - - - - - - - - - - - - - - - - - - - - - - - -  |\n"
        "|                                                             |\n"
        "|                   [1] ADICIONAR PRODUTO                     |\n"
        "|                   [2] VISUALIZAR PRODUTOS                   |\n"
        "|                   [3] ATUALIZAR PRODUTOS                    |\n"
        "|                   [4] DELETAR PRODUTO                       |\n"
        "|                                                             |\n"
        "|                   [5] DETALHES DO TESTE                     |\n"
        "|                   [6] SAIR DO TESTE                         |\n"
        "|                                                             |\n"
        "+-------------------------------------------------------------+\n"
    )
    numero_escolhido_pelo_usuario = int(input('| escolha o que deseja aqui : ')) # Armazena o valor digitado pelo o usuário na variável.
    limpar_tela()
    identificar_escolha_usuario_menu(numero_escolhido_pelo_usuario) # Chamada da função que identifica a escolha do usuário.

def criar_produto(): # CREATE | Criação de um novo produto, onde é solicitado nome do usuario, nome do produto, descricao do produto, quantidade do produto e valor do produto.
    exibir_cabecalho_novo_produto()
    nome_usuario = input("| Digite seu nome (Usuário): ")
    limpar_tela()
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
    valor_produto = obter_numero_inteiro()
    comando = f'INSERT INTO bdCadastro.produtos (nome_produto, data_cadastro, nome_usuario, descricao_produto, quantidade, valor) VALUES ("{nome_produto}", "{hoje}", "{nome_usuario}", "{descricao_produto}", {quantidade_produto}, {valor_produto})'
    cursor.execute(comando)
    conexao.commit() # Modifica o banco de dados 
    limpar_tela()
    print(
        "+-------------------------------------------------------------+\n"
        "|        A D I C I O N A D O    C O M    S U C E S S O        |\n"
        "+-------------------------------------------------------------+\n"
        f"|   Nome do produto: {nome_produto}                                     \n"
        "| \n"
    )
    escolha_ver_produtos()

def visualizar_produtos(): # READ
    comando = f'SELECT * FROM produtos'
    cursor.execute(comando)
    resultados = cursor.fetchall()
    if not resultados:
        print("Nenhum produto cadastrado.")
        escolha_voltar_menu()
        return

    # Cria uma tabela formatada com prettytable
    tabela = PrettyTable()
    tabela.field_names = ["idProdutos", "Produtos", "Data cadastro", "NomeUsuário", "Descrição", "Qtd", "Valor"]

    for resultado in resultados:
        tabela.add_row(resultado)

    # Imprime a tabela formatada
    print(tabela)
    escolha_voltar_menu()

def editar_produto(): #UPDATE | Menu para editar os produtos
    limpar_tela()
    print(
        "+-------------------------------------------------------------+\n"
        "|      A T U A L I Z A R / E D I T A R     P R O D U T O      |\n"
        "+-------------------------------------------------------------+\n"
        "|                                                             |\n"
        "|            [1] EDITAR NOME DO PRODUTO                       |\n"
        "|            [2] EDITAR DESCRIÇÃO DO PRODUTO                  |\n"
        "|            [3] EDITAR QUANTIDADE DO PRODUTO                 |\n"
        "|            [4] EDITAR VALOR DO PRODUTO                      |\n"
        "|                                                             |\n"
        "|            [5] VOLTAR PARA O MENU                           |\n"
        "+-------------------------------------------------------------+\n"
        "|                                                             |\n"
    )                                   
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
    mostra_tabela()
    
    # Solicita o nome do produto a ser excluído
    nome_produto = input("| Digite o nome do produto que deseja DELETAR : ")

    # Corrige a sintaxe da consulta DELETE
    comando = f'DELETE FROM produtos WHERE nome_produto = "{nome_produto}"'
    
    try:
        cursor.execute(comando)
        conexao.commit()  # Confirma a exclusão no banco de dados
        print(
        "+-------------------------------------------------------------+\n"
        "|             P R O D U T O       E X C L U Í D O             |\n"
        "+-------------------------------------------------------------+\n"
        f"| - Produto : '{nome_produto}' Excluído com sucesso! \n"
        )
    except Exception as e:
        limpar_tela()
        print(
        "+-------------------------------------------------------------+\n"
        f"|  E R R O    A O     E X C L U I R    P R O D U T O   {e}   \n"
        "+-------------------------------------------------------------+\n"
        "|       Esse produto não existe na tabela de produtos         |\n"
        "|                       TENTE NOVAMENTE !                     |\n"
        )
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
    r = input("| Deseja contiuar editando? [S] / [N] : ")
    if r.upper()[0] == "S":
        limpar_tela()
        editar_produto()
    elif r.upper()[0] == "N":
        limpar_tela()
        menu_principal()
    else:
        erroCaracterEdt()

def escolha_ver_produtos(): # Assim que usuário modificar a tabela ele será redirecionado para essa função.
    r = input("| Deseja ver os produtos ? [S] / [N] :")
    if r.upper()[0] == "S":
        limpar_tela()
        visualizar_produtos()
    elif r.upper()[0] == "N":
        limpar_tela()
        menu_principal()
    else:
        erro_caracter_escolha_ver_tabela()

def escolha_voltar_menu(): # Assim que o usuário visualizar a tabela ele será redirecionado para essa função.
    r = input("| Deseja voltar para o menu ? [S]/[N] :")
    if r.upper()[0] == "S":
        limpar_tela()
        menu_principal()
    elif r.upper()[0] == "N":
        limpar_tela()
        saida()
    else:
        erro_caracter_voltar_menu()

def erro_caracter_voltar_menu():
    limpar_tela()
    print(
        "+-------------------------------------------------------------+\n"
        "|       V A L O R    I N S E R I D O     I N V Á L I D O  !   |\n"
        "+-------------------------------------------------------------+\n"
        "|                                                             |\n"
        "|   Digite [S] de SIM para visualizar a tabela de produtos    |\n"
        "|   Digite [N] de NÃO para voltar para o menu principal       |\n"
        "|                      Tente novamente !                      |\n"
        "+-------------------------------------------------------------+\n"
    )
    escolha_voltar_menu()

def erro_caracter_escolha_ver_tabela(): 
    limpar_tela()
    print(
        "+-------------------------------------------------------------+\n"
        "|       V A L O R    I N S E R I D O     I N V Á L I D O  !   |\n"
        "+-------------------------------------------------------------+\n"
        "|                                                             |\n"
        "|   Digite [S] de SIM para visualizar a tabela de produtos    |\n"
        "|   Digite [N] de NÃO para voltar para o menu principal       |\n"
        "|                      Tente novamente !                      |\n"
        "+-------------------------------------------------------------+\n"
    )
    escolha_ver_produtos()

def erroCaracterEdt(): 
    limpar_tela()
    print(
        "+-------------------------------------------------------------+\n"
        "|       V A L O R    I N S E R I D O     I N V Á L I D O  !   |\n"
        "+-------------------------------------------------------------+\n"
        "|                                                             |\n"
        "|   Digite [S] de SIM para visualizar a tabela de produtos    |\n"
        "|   Digite [N] de NÃO para voltar para o menu principal       |\n"
        "|                      Tente novamente !                      |\n"
        "+-------------------------------------------------------------+\n"
    )
    continuar_editando()

def exibir_cabecalho_novo_produto():
    print(
        "+-------------------------------------------------------------+\n"
        "|           A D I C I O N A N D O    P R O D U T O            |\n"
        "+-------------------------------------------------------------+\n"
        "|                                                             |\n"
    )

def obter_numero_inteiro():
    while True:
        try:
            qtd = int(input("| Digite a quantidade desse produto: "))
            return qtd
        except ValueError:
            print("Erro: Por favor, digite apenas números inteiros.")

def erro_menu_editar(): # Função que exibe uma mensagem de se o usuário escolher um número fora do padrão. 
    limpar_tela()
    print(
        "+-------------------------------------------------------------+\n"
        "|              N Ú M E R O        I N V Á L I D O   !         |\n"
        "+-------------------------------------------------------------+\n"
        "|            Digite os numeros somente de [1] à [5]           |\n"
        "|                       TENTE NOVAMENTE !                     |\n"
        "+-------------------------------------------------------------+\n"
    )
    editar_produto()

def produto_atualizado(mensagem, produto_atualizado):
    limpar_tela()
    print(
        "+-------------------------------------------------------------+\n"
        "|             P R O D U T O         A T U A L I Z A D O       |\n"
        "+-------------------------------------------------------------+\n"
        f"|   ({mensagem}) ({produto_atualizado})              \n"
        "| \n"
    )
    escolha_ver_produtos()

def editar_nome_produto(): # 1 edita o nome do produto na tabela de cadastro de produtos
    limpar_tela()
    mostra_tabela()
    exibir_nome_atualizado = "Nome do produto atualizado: "
    id_produto = input("| Escolha o ID na coluna idProdutos que deseja editar \n | :")
    novo_nome_produto = input("| Editar nome do produto : ")
    comando = f'UPDATE produtos SET nome_produto = "{novo_nome_produto}" WHERE idProdutos = "{id_produto}"'  
    cursor.execute(comando)
    conexao.commit() # Modifica o banco de dados
    limpar_tela()
    produto_atualizado(exibir_nome_atualizado, novo_nome_produto)
    escolha_ver_produtos

def editar_descricao_produto(): # 2 edita a descrição do produto na tabela de cadastro de produtos
    limpar_tela()
    mostra_tabela()
    exibir_descricao_atualizada = "Descrição do produto atualizado : "
    id_produto = input("| Escolha o ID do produto que deseja editar a descrição: ")
    nova_descricao_produto = input("| Editar descrição: ")
    comando = (f'UPDATE produtos SET descricao_produto = "{nova_descricao_produto}" WHERE idProdutos = "{id_produto}"')
    cursor.execute(comando)
    conexao.commit() # Modifica o banco de dados
    produto_atualizado(exibir_descricao_atualizada, nova_descricao_produto)
    escolha_ver_produtos

def editar_quantidade_produto(): # 3 edita a quantidade do produto da tabela cadastro de produtos
    limpar_tela()
    mostra_tabela()
    exibir_quantidade_atualizada = "Quantidade do produto atualizado : "
    id_produto = input("| Escolha o ID do produto que deseja editar a descrição \n | :")
    nova_quantidade_produto = int(input("| Editar descrição : "))
    comando = f'UPDATE produtos SET quantidade = "{nova_quantidade_produto} WHERE idProdutos = "{id_produto}"'
    cursor.execute(comando)
    conexao.commit() # edita o banco de dados
    produto_atualizado(exibir_quantidade_atualizada, nova_quantidade_produto)
    escolha_ver_produtos()

def editar_valor_produto(): # 4 edita o valor da tabela cadastro de produtos
    limpar_tela()
    mostra_tabela()
    exiibir_valor_atualizado = "Valor do produto atualizado : "
    id_produto = input("| Escolha o ID do produto que deseja editar o valor \n | :")
    novo_valor_produto = int(input("| Editar valor : "))
    comando = f'UPDATE produtos SET valor = {novo_valor_produto} WHERE idProdutos = "{id_produto}"'
    cursor.execute(comando)
    conexao.commit() # edita o banco de dados
    produto_atualizado(exiibir_valor_atualizado, novo_valor_produto)
    escolha_ver_produtos()

def detalhes_teste():
    limpar_tela()
    print(
        "+-------------------------------------------------------------+\n"
        "|            D E T A L H E S    D O    T E S T E              |\n"
        "+-------------------------------------------------------------+\n"
        "|                                                             |\n"
        "|    MySQL Workbench 8.0                                      |\n"
        "|    Python 3.12                                              |\n"
        "|    - - - - - - - - - -                                      |\n"
        "|    Configure a conexão com o BD de sua preferência          |\n"
        "|    a partir da linha 6 do projeto e no import.              |\n"
        "|                                                             |\n"
        "+-------------------------------------------------------------+\n"
        )
    escolha_voltar_menu()

def erro_menu():
    limpar_tela()
    print(
        "+-------------------------------------------------------------+\n"
        "|      N Ú M E R O    D I G I T A D O   I N V Á L I D O       |\n"
        "+-------------------------------------------------------------+\n"
        "|                                                             |\n"
        "|         DIGITE APENAS OS NUMEROS ENTRE [1] À [6]            |\n"
        "|                                                             |\n"
        "|            T E N T E       N O V A M E N T E   !            |\n"
        "|                                                             |"
        "+-------------------------------------------------------------+\n"
        )
    menu_principal()

def saida():
    limpar_tela()
    print(
        "+-------------------------------------------------------------+\n"
        "|                T E S T E   L A B  S Y S T E M               |\n"
        "+-------------------------------------------------------------+\n"
        "|                                                             |\n"
        "| * Obrigado pela oportunidade e pelo desafio proporcionado!  |\n"
        "|                                                             |\n"
        "|   Dados de contato:                                         |\n"
        "|     - Telefone: 11-96579-1902                               |\n"
        "|     - E-mail: gabrieldosantossilva17@gmail.com              |\n"
        "|     - Github: https://github.com/gabrieldossant             |\n"
        "|                                                             |\n"
        "+-------------------------------------------------------------+\n"
        "|                                                             |\n"
        "| Gostaria de expressar minha gratidão e entusiasmo pela      |\n"
        "| possibilidade de fazer parte da LabSystem.                  |\n"
        "|                                                             |\n"
        "| Estou ansioso para contribuir com meu conhecimento,         |\n"
        "| habilidades, e dedicação para impulsionar o sucesso da      |\n"
        "| equipe.                                                     |\n"
        "|                                                             |\n"
        "+-------------------------------------------------------------+\n"
    )
    quit()

def mostra_tabela():
    comando = 'SELECT * FROM produtos'
    cursor.execute(comando)
    resultados = cursor.fetchall()
    if not resultados:
        print("Nenhum produto cadastrado.")
        escolha_voltar_menu()
        return

    # Cria uma tabela formatada com prettytable
    tabela = PrettyTable()
    tabela.field_names = ["idProdutos", "Produtos", "Data cadastro", "NomeUsuário", "Descrição", "Qtd", "Valor"]

    for resultado in resultados:
        tabela.add_row(resultado)

    # Imprime a tabela formatada
    print(tabela)


menu_principal()
cursor.close()
conexao.close()