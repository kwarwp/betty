# betty.lisa.main.py
from _spy.vitollino.main import Cena, Elemento, STYLE, Texto
FUTURO = "https://www.ideiasdecor.com/wp-content/uploads/2018/09/plantas-de-casas-57.jpg"
FULANINHO= "https://pngimage.net/wp-content/uploads/2018/06/pessoa-em-p%C3%A9-png.png"
STYLE["width"]=1100

def meu_futuro():
	Cfuturistica = Cena (img = FUTURO)
	Cfuturistica.vai()
	fulaninho = Elemento (img = FULANINHO, tit= "mulher",
                            style=dict(left=320 , top=250, width="1OOpx", height="120px"))
	fulaninho.entra(Cfuturistica)    
meu_futuro()

