"""Tarefa 003 - Extrai com Expressões Regulares os dados de cada palestrante
a partir do arquivo TXT gerado na tarefa 002.

Estrutura observada no código-fonte:

  <div class="col-12 col-lg-3 gy-3 palestrante-item" id="Palestrante1" ...>
      ... <img src="/media/static/palestrantes/Alan_..._Sp19MPv.png" ...>   -> imagem
  </div>
  <div class="modal fade" id="modal1">
      ... <h4>Nome completo</h4> <br> <h6>Local de trabalho</h6> ...        -> nome / trabalho
      <div class="modal-body"> <p>email@dominio</p> ...                     -> contato
  </div>
"""
import html as htmllib
import re

ARQUIVO_ENTRADA = "pagina.txt"

# "Tempered dots": avançam sem atravessar o início do próximo bloco,
# evitando misturar dados de palestrantes diferentes.
_ATE_PROX_ITEM = r'(?:(?!id="Palestrante\d+").)*?'
_ATE_PROX_MODAL = r'(?:(?!id="modal\d+").)*?'

# Grupo 1: número do palestrante | Grupo 2: caminho da imagem
REGEX_IMAGEM = re.compile(
    r'<div[^>]*palestrante-item[^>]*id="Palestrante(\d+)"'
    + _ATE_PROX_ITEM +
    r'<img[^>]*?src="([^"]+)"',
    re.DOTALL,
)

# Grupo 1: número do modal | 2: nome | 3: local de trabalho | 4: contato (e-mail)
REGEX_MODAL = re.compile(
    r'<div[^>]*class="modal fade"[^>]*id="modal(\d+)"'
    + _ATE_PROX_MODAL +
    r'<h4[^>]*>(.*?)</h4>'
    + _ATE_PROX_MODAL +
    r'<h6[^>]*>(.*?)</h6>'
    + _ATE_PROX_MODAL +
    r'<div[^>]*class="modal-body"[^>]*>\s*<p[^>]*>(.*?)</p>',
    re.DOTALL,
)

REGEX_TAGS = re.compile(r"<[^>]+>")
REGEX_ESPACOS = re.compile(r"\s+")


def _limpar(texto: str) -> str:
    texto = REGEX_TAGS.sub("", texto)
    texto = htmllib.unescape(texto)
    return REGEX_ESPACOS.sub(" ", texto).strip()


def extrair_palestrantes(caminho: str = ARQUIVO_ENTRADA) -> list[dict]:
    with open(caminho, encoding="utf-8") as f:
        conteudo = f.read()

    imagens = {n: src for n, src in REGEX_IMAGEM.findall(conteudo)}
    palestrantes = []
    for n, nome, trabalho, contato in REGEX_MODAL.findall(conteudo):
        palestrantes.append({
            "numero": int(n),
            "name": _limpar(nome),
            "work": _limpar(trabalho),
            "email": _limpar(contato),
            "image_src": imagens.get(n, "").strip(),
        })
    print(f"[003] {len(palestrantes)} palestrantes extraídos")
    return palestrantes


if __name__ == "__main__":
    for p in extrair_palestrantes():
        print(p)
