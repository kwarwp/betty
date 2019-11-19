# betty.anastasia.main.py 
from _spy.vitollino.main import Cena, Texto, Elemento, STYLE 
espaco="https://conhecimentocientifico.r7.com/wp-content/uploads/2017/02/destaque.jpg"
nave="http://www.theartofcats.com/gallery2/d/10062-2/nave-espacial-em-png-queroimagem-cei__a-crispim.png"

STYLE["width"]=1100
STYLE["height"]="800px"
ESPACO= Cena ( img=espaco)

def funciona():
	ESPACO.vai()
	NAVE=Elemento(img=nave, tit="NAVE1",style=dict(left=200, top=300, width="90px", height="100px"))
	NAVE.entra(ESPACO)
funciona()