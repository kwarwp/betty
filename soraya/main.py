# betty.soraya.main.py
from _spy.vitollino.main import Cena, STYLE, Texto, Elemento
praia = "http://baboonnomundao.com.br/bannersist/conteudo/BC_Floripa_-_SC.jpg"
pessoa = "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Dilma_Rousseff_2010_Transparent.png/480px-Dilma_Rousseff_2010_Transparent.png
STYLE["width"]=1500
STYLE["height"]="600px"

def lol():
	Cenario = Cena(img = praia)
	Cenario.vai()
	elementopessoa = Elemento(img = pessoa tit="banana", drag=True,
                         style=dict(left=320 , top=250, width="100px", height="120px"))  
    
lol()