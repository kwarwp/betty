# betty.lisa.main.py
from _spy.vitollino.main import Cena, Elemento, STYLE, Texto
FUTURO = "https://www.ideiasdecor.com/wp-content/uploads/2018/09/plantas-de-casas-57.jpg"
FULANINHO= "https://pngimage.net/wp-content/uploads/2018/06/pessoa-em-p%C3%A9-png.png"
STYLE["width"]=1100

def meu_futuro():
	Cfuturistica = Cena (img = FUTURO)
	Cfuturistica.vai()
	fulaninho = Elemento (img = FULANINHO, tit= "men",
                            style=dict(left=370 , top=370, width="400px", height="200px"))
	fulaninho.entra(Cfuturistica)  
	txtmen = Texto (Cfuturistica,
                     "Olá, vem dar uma olhada na casa, estava te esperando.Clique na porta.")
	fulaninho.vai = txtmen.vai                     
meu_futuro()