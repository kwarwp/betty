# betty.lisa.main.py
from _spy.vitollino.main import Cena, Elemento, STYLE, Texto
FUTURO = "https://www.ideiasdecor.com/wp-content/uploads/2018/09/plantas-de-casas-57.jpg"
FULANINHO= "https://www.pinpng.com/pngs/m/109-1091652_woman-gray-people-cutout-cut-out-people-people.png"
STYLE["width"]=1100

def meu_futuro():
	Cfuturistica = Cena (img = FUTURO)
	Cfuturistica.vai()
	fulaninho = Elemento (img = FULANINHO ,
                            tit= "mulher"
                            style=dict(left=320 , top=250, width="100px", height="120px"))
	fulaninho.entra(Cfuturistica)    
meu_futuro()
