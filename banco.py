
import sqlite3

# conectando...
conn = sqlite3.connect('projetos.db')
# definindo um cursor

def criarTabela():
        cursor = conn.cursor()
        # criando a tabela
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS projetos (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                nome_projeto TEXT NOT NULL,
                data_de_inicio DATE NOT NULL,
                data_de_fim DATE NOT NULL
        );
        """)
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS atividades (
                id INTEGER NOT NULL,
                nome_atividade TEXT NOT NULL,
                data_de_inicio DATE NOT NULL,
                data_de_fim DATE NOT NULL,
                finalizada BOOL 
        );
        """)

        print('Tabela criada com sucesso.')
        # desconectando...
        conn.close()