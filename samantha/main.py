# betty.samantha.main.py
from _spy.vitollino.main import Cena, Texto, Elemento, STYLE
Namek='https://images3.alphacoders.com/677/thumb-1920-677271.png'
Battle='https://www.pngfind.com/pngs/m/340-3407741_goku-vs-vegeta-png-dragon-ball-goku-vs.png'
STYLE['width']=1380
STYLE['height']='605px'

def dragonballz():
	Cena_Namek= Cena(img=Namek)
	Cena_Namek.vai()
	Elemento_Battle=Elemento(img=Battle, tit="BATTLE1",style=dict(left=300, top=500, width="126" height="26"))
	elemento_Battle.entra(Cena_Namek)
    
    
dragonballz()