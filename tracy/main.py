# betty.tracy.main.py
# betty.naomi.main.py
from _spy.vitollino.main import Cena, Elemento, STYLE, Texto
bananeira = "https://bykamy.com.br/media/magpleasure/mpblog/upload/a/e/ae69211a1a37d81e6472903dca1ff6c7.jpg"
banana = "https://i.imgur.com/VbszxUx.png"
banana1 = "https://i.imgur.com/VbszxUx.png"
banana2 = "https://i.imgur.com/VbszxUx.png"
banana3 = "https://i.imgur.com/VbszxUx.png"
banana4 = "https://i.imgur.com/VbszxUx.png"
caminhao = ""
geleia = "https://static.extratoverde.com.br/public/extratoverde/imagens/produtos/geleia-organica-zero-acucar-sabor-banana-shambala-240g-2457.png"
podre = "https://i.imgur.com/sGUZfwF.png"
lixeira = "https://cdn.pixabay.com/photo/2012/04/24/16/34/garbage-40357_960_720.png"
STYLE["width"]=1100
STYLE["height"]="600px"
def Incrivel_banana_python():
	cena = Cena (img = bananeira)
	elemento = Elemento(img = banana ,
                         tit="banana",
                         style=dict(left=320 , top=250, width="100px", height="120px"))
	elemento1 = Elemento(img = banana1 ,
                         tit="banana1",
                         style=dict(left=400, top=250, width="90px", height="110px"))                      
	elemento.entra(cena)
	elemento2 = Elemento(img = banana ,
                         tit="banana2",
                         style=dict(left=40 , top=250, width="80px", height="90px"))
	elemento3 = Elemento(img = banana ,
                         tit="banana3",
                         style=dict(left=150, top=300, width="60px", height="80px"))
	elemento4 = Elemento(img = banana ,
                         tit="banana4",
                         style=dict(left=640,top=400, width="100px", heigth="2000px"))
	Caminhao = Elemento(img = caminhao ,
                         tit="caminhao",
                         style=dict(left=750,top=400,width="350px",heigth="100px"))
	Geleia = Elemento(img = geleia , 
                        tit= "geleia",
                        style=dict(left=50,top=400,width="80px",heigth="50px"))
	Podre = Elemento(img = podre ,
                       tit= "podre",
                       style=dict(left=500,top=450,width="100px",heigth="80px"))
        
	Lixeira = Elemento(img = lixeira ,
                        tit= "lixeira", 
                        style=dict(left=200,top=420,width="200px",heigth="250px"))
	elemento1.entra(cena)
	elemento2.entra(cena)
	elemento3.entra(cena)
	elemento4.entra(cena)
	Lixeira.entra(cena)
	Caminhao.entra(cena)
	Geleia.entra(cena)
	Podre.entra(cena)
	cena.vai()
Incrivel_banana_python()
