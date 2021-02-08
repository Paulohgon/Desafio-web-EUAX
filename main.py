import sqlite3
from datetime import date
from banco import criarTabela
#criando a tabela no banco de dados caso nao haja
criarTabela()
#conectnando
conn = sqlite3.connect('projetos.db')
cursor = conn.cursor()
while(True):
    opcao = int(input('Voce deseja adcionar novos projetos(1), verificar o estado deles(2), deletar algum projeto(3),ou sair(4)'))
    if(opcao == 1):#adicionar novo projeto

        # solicitando os dados ao usuário
        nome_projeto = input('Nome do projeto: ')
        dataIni = input('Data a qual o projeto foi iniciado(yyyy-mm-dd): ')
        dataFim = input('Data a qual o projeto deve ser finalizado(yyyy-mm-dd): ')

        # inserindo dados na tabela
        cursor.execute("""
        INSERT INTO projetos (nome_projeto, data_de_inicio, data_de_fim)
        VALUES (?,?,?)
        """, (nome_projeto, dataIni, dataFim))

        print('Dados inseridos com sucesso.\nAgora insira o numero de atividades do projeto {}'.format(nome_projeto))

        numero_ativ = int(input())
        for atividade in range (1,numero_ativ + 1):
            #atrelando as atividades com o id do projeto
            cursor.execute("SELECT * FROM projetos WHERE id = (select max(id) from projetos)")
            id_do_projeto = cursor.fetchone()
            # solicitando os dados ao usuário
            nome_atividade = input('Qual o nome da atividade:')
            data_de_inicio = input('Data a qual a atividade foi iniciada(yyyy-mm-dd): ')
            data_de_termino = input('Data a qual a atividade deve ser finalizada(yyyy-mm-dd): ')          
            finalizada = input('O projeto foi finalizado? (Y/N)')
            fim = 0
            if (finalizada == "Y"):
                fim = 1
            # inserindo dados na tabela atividades
            cursor.execute("""INSERT INTO atividades (id, nome_atividade, data_de_inicio, data_de_fim,finalizada) 
            VALUES (?,?,?,?,?)""", (id_do_projeto[0], nome_atividade, data_de_inicio,data_de_termino,fim))
        print('Dados inseridos com sucesso')

        conn.commit()  
    elif(opcao == 2):#ver os estados dos projetos
        #exibindo todos os projetos do banco para poder escolher um
        cursor.execute("SELECT * FROM projetos;")
        for linha in cursor.fetchall():
            print(linha)
        #selecionando o projeto
        id_desejada = int(input("Qual a id do pojeto que voce deseja acessar?"))
        cursor.execute("SELECT * FROM projetos WHERE id = {}".format(id_desejada))
        projeto_desejado = cursor.fetchone()
        #pegando todas as atividades pertencentes a esse projeto
        cursor.execute("SELECT * FROM atividades WHERE id = {}".format(id_desejada))
        atividades_do_projeto = cursor.fetchall()
        numero_de_atividades = len(atividades_do_projeto)
        #pegando as atividades finalizadas para ver a porcentagem do termino do projeto
        cursor.execute("SELECT * FROM atividades WHERE finalizada = 1".format(id_desejada))
        atividades_terminadas = cursor.fetchall()
        numero_de_terminadas = len(atividades_terminadas)
        porcentagem = (numero_de_terminadas/numero_de_atividades) * 100

        print("\n\nO projeto selecionado foi {}, ele tem as seguintes atividades\n{} e está {}% completo!\n".format(projeto_desejado,atividades_do_projeto, porcentagem))

        
    if(opcao==3):#deletar projetos
        #exibindo todos os projetos do banco para poder escolher um
        cursor.execute("SELECT * FROM projetos;")
        for linha in cursor.fetchall():
            print(linha)
        #escolhendo o projeto pela id e eliminando ele e suas atividades
        id_eliminada = int(input("\nQual a id do projeto que deseja eliminar"))
        cursor.execute("DELETE FROM projetos WHERE id = {}".format(id_eliminada))
        conn.commit()
        cursor.execute("DELETE FROM atividades WHERE id = {}".format(id_eliminada))    
        conn.commit()
        print("Projeto eliminado com sucesso!")
    if(opcao == 4):#sair
        break

conn.close()