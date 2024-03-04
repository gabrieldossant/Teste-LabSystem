import mysql.connector # configure o banco de dados de sua preferência
import datetime # biblioteca que utilizo para ter o dia atual de hoje para manter o código sempre atualizado.


def criar_conexao():
    # Configuração de conexão com o banco de dados
    conexao = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = '',
        database = 'bdCadastro',
    )
    return conexao

def inserir(nome_produto, nome_usuario, descricao_produto, quantidade_produto, valor_produto):
    conexao = criar_conexao()
    cursor = conexao.cursor() # cursor é o objeto que é utilizado para processar os resultados de uma consulta SQL.
    comando = f'INSERT INTO bdCadastro.produto (nome, data_cadastro, nome_usuario, descricao, quantidade, valor) VALUES ("{nome_produto}", "{datetime.datetime.now()}", "{nome_usuario}", "{descricao_produto}", {quantidade_produto}, {valor_produto})'
    cursor.execute(comando)
    conexao.commit() # Modifica o banco de dados
    conexao.close()

def listar():
    conexao = criar_conexao()
    cursor = conexao.cursor() # cursor é o objeto que é utilizado para processar os resultados de uma consulta SQL.
    comando = f'SELECT * FROM produto'
    cursor.execute(comando)
    resultados = cursor.fetchall()
    conexao.close()
    return resultados

def atualizar_nome_produto(novo_nome_produto, id): # Função para atualizar nome de um produto
    conexao = criar_conexao()
    cursor = conexao.cursor() # cursor é o objeto que é utilizado para processar os resultados de uma consulta SQL.
    comando = f'UPDATE produto SET nome = "{novo_nome_produto}" WHERE id = "{id}"'  
    cursor.execute(comando)
    conexao.commit() # Modifica o banco de dados

def atualizar_descricao(nova_descricao_produto, id): # Função para atualizar a descrição de um produto
    conexao = criar_conexao()
    cursor = conexao.cursor() # cursor é o objeto que é utilizado para processar os resultados de uma consulta SQL.
    comando = (f'UPDATE produto SET descricao = "{nova_descricao_produto}" WHERE id = "{id}"')
    cursor.execute(comando)
    conexao.commit() # Modifica o banco de dados
    conexao.close()

def atualizar_quantidade_produto(nova_quantidade_produto, id):# Função para atualizar a quantidade de um produto
    conexao = criar_conexao()
    cursor = conexao.cursor() # cursor é o objeto que é utilizado para processar os resultados de uma consulta SQL.
    comando = f'UPDATE produto SET quantidade = "{nova_quantidade_produto} WHERE id = "{id}"'
    cursor.execute(comando)
    conexao.commit() # edita o banco de dados
    conexao.close()

def atualizar_valor(novo_valor_produto, id): # Função para atualizar o valor de um produto
    conexao = criar_conexao()
    cursor = conexao.cursor() # cursor é o objeto que é utilizado para processar os resultados de uma consulta SQL.
    comando = f'UPDATE produto SET valor = {novo_valor_produto} WHERE id= "{id}"'
    cursor.execute(comando)
    conexao.commit() # Modifica o banco de dados
    conexao.close()

def deletar(id):
    conexao = criar_conexao()
    cursor = conexao.cursor() # cursor é o objeto que é utilizado para processar os resultados de uma consulta SQL.
    comando = f'DELETE FROM produto WHERE id = "{id}"'
    cursor.execute(comando)
    conexao.commit()  # Confirma a exclusão no banco de dados
    conexao.close()