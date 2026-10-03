"""Tarefa 005 - Cria o banco event.db com a tabela speaker."""
import sqlite3

BANCO = "event.db"

SQL = """
CREATE TABLE IF NOT EXISTS speaker (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(255) NOT NULL,
    work VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    image VARCHAR(255) NOT NULL
);
"""


def criar_banco() -> None:
    with sqlite3.connect(BANCO) as con:
        con.execute(SQL)
    print(f"[005] Banco '{BANCO}' e tabela 'speaker' prontos")


if __name__ == "__main__":
    criar_banco()
