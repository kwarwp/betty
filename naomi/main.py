# betty.naomi.main.py
from _spy.vitollino.main import Cena, Elemento, STYLE, Texto
bananeira = "https://bykamy.com.br/media/magpleasure/mpblog/upload/a/e/ae69211a1a37d81e6472903dca1ff6c7.jpg"
banana = "https://i.imgur.com/VbszxUx.png"
STYLE["width"]=1100
STYLE["height"]="600px"

def minions():
	cena = Cena (img = bananeira)
	elemento = Elemento(img = banana)
	elemento.entra(cena)
	cena.vai()
minions()