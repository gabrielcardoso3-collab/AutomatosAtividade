"""Executa todas as tarefas em sequência (002 a 006)."""
from tarefa002_baixar_html import baixar_html
from tarefa003_extrair_dados import extrair_palestrantes
from tarefa004_baixar_imagens import baixar_imagens
from tarefa006_registrar_dados import registrar

if __name__ == "__main__":
    baixar_html()                       # 002
    palestrantes = extrair_palestrantes()  # 003
    baixar_imagens(palestrantes)        # 004
    registrar(palestrantes)             # 005 + 006
