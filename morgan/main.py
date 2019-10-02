# betty.morgan.main.py
from _spy.vitollino.main import Cena, Elemento, STYLE, Texto
cidade = "http://www.trabalhosescolares.net/wp-content/uploads/2019/08/cidade_trabalhos_escolares-696x464.jpg"
carro = "https://www.pinclipart.com/picdir/middle/106-1066670_audi-clipart-fast-car-lamborghini-de-lado-png.png]"
STYLE["width"]=1400
STYLE["height"]="600px"
def cidade_legal():
	cenario = Cena (img = cidade)
	elemento_carro = Elemento(img = carro,
	tit="carro",style=dict(left=320 , top=250, width="100px", height="120px"))
	elemento_carro.entra(cenario)
	cenario.vai()
cidade_legal()    