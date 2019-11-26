# betty.anastasia.main.py 
from _spy.vitollino.main import Cena, Texto, Elemento, STYLE 
espaco="https://www.jornaljoca.com.br/wp-content/uploads/2019/04/espaco-2.jpg"
nave=""

STYLE["width"]=1100
STYLE["height"]="800px"
ESPACO= Cena ( img=espaco)

def funciona():
	ESPACO.vai()
	NAVE=Elemento(img=nave, tit="NAVE1",style=dict(left=300, top=40, width="200px", height="260px"))
	NAVE.entra(ESPACO)
funciona()