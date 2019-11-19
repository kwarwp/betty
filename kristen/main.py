# betty.kristen.main.py
from _spy.vitollino.main import Cena, Texto, Elemento, STYLE
Campo='https://turismo.buenosaires.gob.ar/sites/turismo/files/campo_de_golf_1200_c.jpg'
Dogin='http://3.bp.blogspot.com/-4A5-CTXo8Jk/VUqmCKVdwfI/AAAAAAAAzzI/aiYW51qUD-s/s1600/dog_PNG147.png'
Carinha='https://myrealdomain.com/images/pessoa-correndo-4.png'
STYLE['width']=1350
STYLE['height']='600px'

def Quadra():
	Cena_Campo= Cena(img=Campo)
	Cena_Campo.vai()
	Elemento_Dogin=Elemento(img=Dogin, tit="DOGIN1",style=dict(left=300, top=500, width="120px",height="20") )   
	Elemento_Dogin.entra(Cena_Campo)
	Elemento_Carinha=Elemento(img=Carinha, tit="CARINHA1",style=dict(left=500, top=300, width="190px",height="300"))
	Elemento_Carinha.entra(Cena_Campo)
    
Quadra()