# betty.kristen.main.py
from _spy.vitollino.main import Cena, Texto, Elemento, STYLE
Campo='https://turismo.buenosaires.gob.ar/sites/turismo/files/campo_de_golf_1200_c.jpg'
Dogin='http://3.bp.blogspot.com/-4A5-CTXo8Jk/VUqmCKVdwfI/AAAAAAAAzzI/aiYW51qUD-s/s1600/dog_PNG147.png'
Carinha='https://myrealdomain.com/images/pessoa-correndo-4.png'
Pombo='http://www.pombocorreiodf.com.br/wp-content/uploads/2018/03/pombo-voando.png'
Lixeira_Vidro='https://metadistribuidorars.com.br/wp-content/uploads/2019/01/984.png'
Lixeira_Papel='https://assets.xtechcommerce.com/uploads/images/medium/5d66494a592658739ffd0904b0a12e00.png'
Lixeira_Metal='http://www.belosch.com.br/arquivos/produtos/_fotoMarcaVisu012R1JDBVZL_5a2e75a7515d2ebe63d498a1eaef6624.png'
Lixeira_Plastico='https://dotstore.s3-sa-east-1.amazonaws.com/582/produtos/detalhe/02%20basculantes%20-%20copia.png'
STYLE['width']=1350
STYLE['height']='600px'

def Quadra():
	Cena_Campo= Cena(img=Campo)
	Cena_Campo.vai()
	Elemento_Dogin=Elemento(img=Dogin, tit="DOGIN1",style=dict(left=100, top=500, width="120px",height="20"))   
	Elemento_Dogin.entra(Cena_Campo)
	Elemento_Carinha=Elemento(img=Carinha, tit="CARINHA1",style=dict(left=500, top=300, width="190px",height="300px"))
	Elemento_Carinha.entra(Cena_Campo)
	Elemento_Pombo=Elemento(img=Carinha, tit="POMBO1",style=dict(left=200, top=100, width="190px",height="300px"))
	Elemento_Pombo.entra(Cena_Campo)
	Elemento_Lixeira_Vidro=Elemento(img=Lixeira_Vidro, tit="LIXEIRA_VIDRO1",style=dict(left=700, top=450, width="190px",height="150px"))
	Elemento_Lixeira_Vidro.entra(Cena_Campo)
	Elemento_Lixeira_Papel=Elemento(img=Lixeira_Papel, tit="LIXEIRA_PAPEL1",style=dict(left=800, top=450, width="150px",height="150px"))
	Elemento_Lixeira_Papel.entra(Cena_Campo)
	Elemento_Lixeira_Metal=Elemento(img=Lixeira_Metal, tit="LIXEIRA_METAL1",style=dict(left=900, top=450, width="120px",height="150px"))
	Elemento_Lixeira_Metal.entra(Cena_Campo)
	Elemento_Lixeira_Plastico=Elemento(img=Lixeira_Plastico, tit="LIXEIRA_PLASTICO1",style=dict(left=1100, top=450, width="100px",height="150px"))
	Elemento_Lixeira_Plastico.entra(Cena_Campo)    
    
Quadra()