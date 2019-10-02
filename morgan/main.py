# betty.morgan.main.py
from _spy.vitollino.main import Cena, Elemento, STYLE, Texto
cidade = "http://www.trabalhosescolares.net/wp-content/uploads/2019/08/cidade_trabalhos_escolares-696x464.jpg"
carro = "https://www.nicepng.com/png/full/377-3779595_lamborghini-aventador-s-matte-black.png"
pessoa = "https://pngimage.net/wp-content/uploads/2018/06/pessoa-em-p%C3%A9-png.png"
STYLE["width"]=1400
STYLE["height"]="600px"
def cidade_legal():
	cenario = Cena (img = cidade)
	elemento_carro = Elemento (img = carro,
	tit="carro",style=dict(left=300 , top=340, width="550px", height="300px"))
	elemento_pessoa = Elemento (img = pessoa,
	tit="homem",style=dict(left=700 , top=300, width="200px", height="300px"))    
	elemento_carro.entra(cenario)
	elemento_pessoa.entra(cenario)    
	cenario.vai()
cidade_legal()    