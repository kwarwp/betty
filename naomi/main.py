# betty.naomi.main.py
from _spy.vitollino.main import Cena, Elemento, STYLE, Texto
bananeira = "https://bykamy.com.br/media/magpleasure/mpblog/upload/a/e/ae69211a1a37d81e6472903dca1ff6c7.jpg"
banana0 = "https://i.imgur.com/VbszxUx.png"
banana1 = "https://i.imgur.com/VbszxUx.png"
banana2 = "https://i.imgur.com/VbszxUx.png"
banana3 = "https://i.imgur.com/VbszxUx.png"
banana4 = "https://i.imgur.com/VbszxUx.png"
caminhao = "https://i.imgur.com/Izt2rSG.png"               
gelequa = "https://static.extratoverde.com.br/public/extratoverde/imagens/produtos/geleia-organica-zero-acucar-sabor-banana-shambala-240g-2457.png"
banana_madura0 = "https://i.imgur.com/sGUZfwF.png"
banana_madura1 = "https://i.imgur.com/sGUZfwF.png"
banana_madura2 = "https://i.imgur.com/sGUZfwF.png"                           
banana_madura3 = "https://i.imgur.com/sGUZfwF.png"
banana_madura4 = "https://i.imgur.com/sGUZfwF.png"
lixeira = "https://cdn.pixabay.com/photo/2012/04/24/16/34/garbage-40357_960_720.png"                  
STYLE["width"]=1100
STYLE["height"]="600px"
DICIONARIO_CAMINHAO = {}
DICIONARIO_LIXEIRA = {}
DICIONARIO_GELEQUA = {}
BOAS = "banana0 banana1 banana2 banana3 banana4".split()
MADURAS = "banana_madura0 banana_madura1 banana_madura2 banana_madura3 banana_madura4".split()
cenario=None
tela_inicial="https://i.imgur.com/sIvENaT.jpg"

def Incrivel_banana_python():                        
	global cenario
	cenario = Cena (img = bananeira)
	cenario2 = Cena (img = tela_inicial)
	elemento = Elemento(img = banana0 ,                        
                         tit="banana0",drag=True,
                         style=dict(left=320 , top=250, width="100px", height="120px"))
	elemento1 = Elemento(img = banana1 ,
                         tit="banana1",drag=True,
                         style=dict(left=400, top=250, width="90px", height="110px"))                                
	elemento2 = Elemento(img = banana2 ,                       
                         tit="banana2",drag=True,
                         style=dict(left=40 , top=250, width="80px", height="90px"))            
	elemento3 = Elemento(img = banana3 ,
                         tit="banana3",drag=True,
                         style=dict(left=150, top=300, width="60px", height="80px")) 
	elemento4 = Elemento(img = banana4 ,
                         tit="banana4",drag=True,
                         style=dict(left=400,top=400, width="100px", heigth="2000px"))
	Caminhao = Elemento(img = caminhao ,drop=DICIONARIO_CAMINHAO, 
                         tit="caminhao", 
                         style=dict(left=750,top=460,width="330px",heigth="100px"))
	Geleia = Elemento(img = gelequa ,drop=DICIONARIO_GELEQUA,
                        tit= "gelequa",
                        style=dict(left=50,top=400,width="80px",heigth="50px"))
	Banana_madura0= Elemento(img = banana_madura0 ,
                       tit= "banana_madura0",drag=True,                                         
                       style=dict(left=490,top=500,width="100px",heigth="80px"))
	Banana_madura1= Elemento(img = banana_madura1 ,
                       tit= "banana_madura1",drag=True,
                       style=dict(left=650,top=350,width="100px",heigth="80px"))
	Banana_madura2= Elemento(img = banana_madura2 ,
                       tit= "banana_madura2",drag=True,
                       style=dict(left=600,top=420,width="100px",heigth="80px"))
	Banana_madura3= Elemento(img = banana_madura3 ,
                       tit= "banana_madura3",drag=True,
                       style=dict(left=60,top=500,width="100px",heigth="80px"))
	Banana_madura4= Elemento(img = banana_madura4 ,
                       tit= "banana_madura4",drag=True,
                       style=dict(left=89,top=251,width="100px",heigth="80px"))                    
                       
        
	Lixeira = Elemento(img = lixeira , drop = DICIONARIO_LIXEIRA,
                        tit= "lixeira", 
                        style=dict(left=200,top=420,width="200px",heigth="250px"))
	
	elemento.entra(cenario)
	elemento1.entra(cenario)
	elemento2.entra(cenario)
	elemento3.entra(cenario)
	elemento4.entra(cenario)
	Lixeira.entra(cenario)
	Caminhao.entra(cenario)
	Geleia.entra(cenario)
	Banana_madura0.entra(cenario)
	Banana_madura1.entra(cenario)
	Banana_madura2.entra(cenario)
	Banana_madura3.entra(cenario) 
	Banana_madura4.entra(cenario)   
    
	cenario2.vai()
	cenario2.meio = cenario.vai()
	"""cenario.vai()"""
    
def aceita_banana_boa(evento, nome):
	global cenario
    
	nome=nome[:-1]
	Texto(cenario, f"Muito bem, esta {nome} boa  pode ser vendida!").vai() 
def rejeita_banana_madura_caminhao(evento, nome):
	global cenario	
	nome=nome[:-1]
	Texto(cenario, f"Você não deveria vender esta {nome}, ela não vai resistir até chegar no mercado!").vai()
def rejeita_banana_madura_lixeira(evento, nome):
	global cenario
	nome=nome[:-1]
	Texto(cenario, f"Você não deveria desperdiçar esta {nome}, ela pode ser usada pra fazer geléia!").vai()   
def rejeita_banana_boa_lixeira(evento, nome):
	global cenario
	nome=nome[:-1]
	Texto(cenario, f"Você não deveria desperdiçar esta boa {nome}, ela pode ser vendida!").vai()  
def aceita_gelequa(evento, nome):
	global cenario
	nome=nome[:-1]
	Texto(cenario,f"Muito bem!!! Essa {nome} pode virar uma geléia!").vai()
def rejeita_gelequa_boa(evento, nome):
	global cenario
	nome=nome[:-1]
	Texto(cenario,f"Essa {nome} está boa e pode ser vendida!").vai()
    

DICIONARIO_CAMINHAO={coisa:aceita_banana_boa for coisa in BOAS}
DICIONARIO_CAMINHAO.update(banana_madura0= rejeita_banana_madura_caminhao)
DICIONARIO_CAMINHAO.update(banana_madura1= rejeita_banana_madura_caminhao)
DICIONARIO_CAMINHAO.update(banana_madura2= rejeita_banana_madura_caminhao)
DICIONARIO_CAMINHAO.update(banana_madura3= rejeita_banana_madura_caminhao)
DICIONARIO_CAMINHAO.update(banana_madura4= rejeita_banana_madura_caminhao)

DICIONARIO_LIXEIRA={coisamadura: rejeita_banana_madura_lixeira for coisamadura in MADURAS}
DICIONARIO_LIXEIRA.update(banana0=rejeita_banana_boa_lixeira)
DICIONARIO_LIXEIRA.update(banana1=rejeita_banana_boa_lixeira)
DICIONARIO_LIXEIRA.update(banana2=rejeita_banana_boa_lixeira)
DICIONARIO_LIXEIRA.update(banana3=rejeita_banana_boa_lixeira)
DICIONARIO_LIXEIRA.update(banana4=rejeita_banana_boa_lixeira)

DICIONARIO_GELEQUA={gelequa: aceita_gelequa for gelequa in MADURAS}
DICIONARIO_GELEQUA.update(banana0= rejeita_gelequa_boa)
DICIONARIO_GELEQUA.update(banana1= rejeita_gelequa_boa)
DICIONARIO_GELEQUA.update(banana2= rejeita_gelequa_boa)
DICIONARIO_GELEQUA.update(banana3= rejeita_gelequa_boa)
DICIONARIO_GELEQUA.update(banana4= rejeita_gelequa_boa)

Incrivel_banana_python()

