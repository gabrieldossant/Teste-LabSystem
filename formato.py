from prettytable import PrettyTable # biblioteca que serve para ajustar o tamanho da tabela de acordo com os dados contigos nela.

def tabela_formata(resultados):
    if not resultados:
        print("Nenhum produto cadastrado.")
        return

    # Cria uma tabela formatada com prettytable
    tabela = PrettyTable()
    tabela.field_names = ["ID", "NOME", "DATA DE CADASTRO", "DESCRIÇÃO", "NOME DE USUÁRIO", "QUANTIDADE", "VALOR"]

    for resultado in resultados:
        tabela.add_row(resultado)

    # Imprime a tabela formatada
    return tabela