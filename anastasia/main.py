# betty.anastasia.main.py 
from _spy.vitollino.main import Cena, Texto, Elemento, STYLE 
espaco="https://conhecimentocientifico.r7.com/wp-content/uploads/2017/02/destaque.jpg"

STYLE["width"]=1100
STYLE["height"]="800px"
ESPACO= Cena ( img=espaco)

def funciona():
	ESPACO.vai()
	NAVE=Elemento(img=nave, tit="NAVE1",style=dict(left=100, top=250, width="80px", height="90px"))
	NAVE.entra(ESPACO)
funciona()