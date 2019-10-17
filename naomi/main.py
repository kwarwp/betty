# betty.naomi.main.py
from _spy.vitollino.main import Cena, Elemento, STYLE, Texto
bananeira = "https://bykamy.com.br/media/magpleasure/mpblog/upload/a/e/ae69211a1a37d81e6472903dca1ff6c7.jpg"
banana = "https://i.imgur.com/VbszxUx.png"
banana1 = "https://i.imgur.com/VbszxUx.png"
banana2 = "https://i.imgur.com/VbszxUx.png"
banana3 = "https://i.imgur.com/VbszxUx.png"
banana4 = "https://i.imgur.com/VbszxUx.png"
caminhao = "https://i.imgur.com/M62FANW.png"
geleia = "https://static.extratoverde.com.br/public/extratoverde/imagens/produtos/geleia-organica-zero-acucar-sabor-banana-shambala-240g-2457.png"
banana_madura = "https://i.imgur.com/sGUZfwF.png"
lixeira = "https://cdn.pixabay.com/photo/2012/04/24/16/34/garbage-40357_960_720.png"
podre1 = "https://i.imgur.com/sGUZfwF.png"
STYLE["width"]=1100
STYLE["height"]="600px"
DICIONARIO_CAMINHAO = {}
BOAS = "banana banana1 banana2 banana3 banana4".split()
cenario=None

def Incrivel_banana_python():
	global cenario
	cenario = Cena (img = bananeira)
	elemento = Elemento(img = banana ,
                         tit="banana",drag=True,
                         style=dict(left=320 , top=250, width="100px", height="120px"))
	elemento1 = Elemento(img = banana1 ,
                         tit="banana1",drag=True,
                         style=dict(left=400, top=250, width="90px", height="110px"))                      
	elemento.entra(cenario)
	elemento2 = Elemento(img = banana ,
                         tit="banana2",drag=True,
                         style=dict(left=40 , top=250, width="80px", height="90px"))
	elemento3 = Elemento(img = banana ,
                         tit="banana3",drag=True,
                         style=dict(left=150, top=300, width="60px", height="80px"))
	elemento4 = Elemento(img = banana ,
                         tit="banana4",drag=True,
                         style=dict(left=640,top=400, width="100px", heigth="2000px"))
	Caminhao = Elemento(img = caminhao ,drop=DICIONARIO_CAMINHAO,
                         tit="caminhao",
                         style=dict(left=750,top=400,width="350px",heigth="100px"))
	Geleia = Elemento(img = geleia , 
                        tit= "geleia",
                        style=dict(left=50,top=400,width="80px",heigth="50px"))
	Banana_madura= Elemento(img = banana_madura ,
                       tit= "banana_madura",
                       style=dict(left=500,top=450,width="100px",heigth="80px"))
        
	Lixeira = Elemento(img = lixeira ,
                        tit= "lixeira", 
                        style=dict(left=200,top=420,width="200px",heigth="250px"))
	"""banana_madura1 = Elemento(img = banana_madura1 ,
                        tit= "banana_madura1",
                        style=dict(left=150,top=400,width="100px",heigth="250px"))"""
	elemento1.entra(cenario)
	elemento2.entra(cenario)
	elemento3.entra(cenario)
	elemento4.entra(cenario)
	Lixeira.entra(cenario)
	Caminhao.entra(cenario)
	Geleia.entra(cenario)
	Banana_madura.entra(cenario)
	"""banana_madura1.entra(cenario)"""
	cenario.vai()
    
def aceita_banana_boa(evento, nome):
    global cenario
    Texto(cenario, f"Muito bem, esta coisa {nome} boa  pode ser vendida!").vai() 
def aceita_banana_madura(evento, nome):
    global cenario
    Texto(cenario, f"voce não deveria vender esta coisa {nome}!").vai()
    
DICIONARIO_CAMINHAO={coisa:aceita_banana_boa for coisa in BOAS}
DICIONARIO_CAMINHAO.update(banana_madura=aceita_banana_madura)
Incrivel_banana_python()
