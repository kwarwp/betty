# betty.julia.main.py
from _spy.vitollino.main import Cena

link_para_primeira_imagem = "https://i.imgur.com/IPa06hM.jpg"
link_para_segunda_imagem = "https://i.imgur.com/rHzbmtM.jpg"
link_para_terceira_imagem = "https://i.imgur.com/NnVA765.jpg"
link_para_quarta_imagem = "https://i.imgur.com/XJXjA9r.jpg"
primeira_cena=Cena(link_para_primeira_imagem)
segunda_cena=Cena(link_para_segunda_imagem)
terceira_cena=Cena(link_para_terceira_imagem)
quarta_cena=Cena(link_para_quarta_imagem)
primeira_cena.direita = segunda_cena
segunda_cena.esquerda = primeira_cena
segunda_cena.direita = terceira_cena
terceira_cena.esquerda = segunda_cena
terceira_cena.direita = quarta_cena
quarta_cena.esquerda = terceira_cena
quarta_cena.direita = primeira_cena
primeira_cena.esquerda = quarta_cena
primeira_cena.vai()