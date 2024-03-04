def exibir_menu_principal():
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

def exibir_adicionado_com_sucesso(nome_produto):
    print(
        "+-------------------------------------------------------------+\n"
        "|        A D I C I O N A D O    C O M    S U C E S S O        |\n"
        "+-------------------------------------------------------------+\n"
        f"|   Nome do produto: {nome_produto}                                     \n"
        "| \n"
    )

def exibir_tela_editar_produto():
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

def exibir_produto_excluido(id):
    print(
        "+-------------------------------------------------------------+\n"
        "|             P R O D U T O       E X C L U Í D O             |\n"
        "+-------------------------------------------------------------+\n"
        f"| - Produto : '{id}' Excluído com sucesso! \n"
        )
    
def exibir_erro_excluir_produto(e):
    print(
        "+-------------------------------------------------------------+\n"
        f"|  E R R O    A O     E X C L U I R    P R O D U T O   {e}   \n"
        "+-------------------------------------------------------------+\n"
        "|       Esse produto não existe na tabela de produtos         |\n"
        "|                       TENTE NOVAMENTE !                     |\n"
        )
    
def exibir_erro_caracter_voltar_menu():
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

def exibir_erro_caracter_escolha_ver_tabela():
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

def exibir_erro_caracter_editar():
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

def exibir_adiciando_produto():
    print(
        "+-------------------------------------------------------------+\n"
        "|           A D I C I O N A N D O    P R O D U T O            |\n"
        "+-------------------------------------------------------------+\n"
        "|                                                             |\n"
    )

def exibir_erro_menu_editar():
    print(
        "+-------------------------------------------------------------+\n"
        "|              N Ú M E R O        I N V Á L I D O   !         |\n"
        "+-------------------------------------------------------------+\n"
        "|            Digite os numeros somente de [1] à [5]           |\n"
        "|                       TENTE NOVAMENTE !                     |\n"
        "+-------------------------------------------------------------+\n"
    )

def exibir_produto_atualizado(mensagem, produto_atualizado):
    print(
        "+-------------------------------------------------------------+\n"
        "|             P R O D U T O         A T U A L I Z A D O       |\n"
        "+-------------------------------------------------------------+\n"
        f"|   ({mensagem}) ({produto_atualizado})              \n"
        "| \n"
    )

def exibir_detalhes_teste():
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
    
def exibir_erro_menu_principal():
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
    
def exibir_tela_de_saida():
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