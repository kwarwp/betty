# betty.naomi.main.py
from _spy.vitollino.main import Cena, Elemento, STYLE, Texto
bananeira = "https://bykamy.com.br/media/magpleasure/mpblog/upload/a/e/ae69211a1a37d81e6472903dca1ff6c7.jpg"
banana = "https://i.imgur.com/VbszxUx.png"
banana1 = "https://i.imgur.com/VbszxUx.png"
banana2 = "https://i.imgur.com/VbszxUx.png"
banana3 ="https://i.imgur.com/VbszxUx.png"

STYLE["width"]=1100
STYLE["height"]="600px"
def minions():
	cena = Cena (img = bananeira)
	elemento = Elemento(img = banana ,
                         tit="banana",
                         style=dict(left=320 , top=250, width="100px", height="120px"))
	elemento1 = Elemento(img = banana1 ,
                         tit="banana1",
                         style=dict(left=400, top=250, width="100px", height="120px"))                      
	elemento.entra(cena)
	elemento2 = Elemento(img = banana ,
                         tit="banana2",
                         style=dict(left=100 , top=250, width="80px", height="100px"))
	elemento3 = Elemento(img = banana ,
                         tit="banana3",
                         style=dict(left=200, top=250, width="80px", height="100px"))
	elemento1.entra(cena)
	elemento2.entra(cena)
	elemento3.entra(cena)
	cena.vai()
minions()
