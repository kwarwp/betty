# betty.julia.main.py
from  _spy.vitollino.main import Cena, Elemento, STYLE, Texto
Espaco="https://hypescience.com/wp-content/uploads/2016/05/espaco-tres-dimensoes-3d.jpg"
nave=""
STYLE["width"]=1100
STYLE["height"]="600px"
def sistemasolar():
	espaco=Cena(img=Espaco)
	espaco.vai()
	elementonave=Elemento(img = nave, tit="nave", style=dict( left=320 , top=250, width="100px", height="120px"))
	elementonave.entra(espaco)
    
    
    
sistemasolar()    

