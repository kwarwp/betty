# betty.sarah.main.py
from _spy.vitollino.main import Cena,Elemento,Texto,STYLE
praia="https://www.fotoswiki.org/Uploads/fotoswiki.org/ImagensGrandes/praias-7.jpg"
barco="https://cdn.pixabay.com/photo/2014/04/02/16/23/boat-307125_960_720.png"
bolsonaro="https://pbs.twimg.com/media/CnqKuEnW8AAXMbU.png"
morinho="https://midianinja.org/files/2018/11/moronu.png"
STYLE["width"]=1280
STYLE["height"]="670px"
def foto1():
	cenapraia=Cena(img=praia)
	cenapraia.vai()
	elementobarco=Elemento(img=barco,style=dict (top=400,left=300,width="600px",heigth="400px"))
	elementobarco.entra(cenapraia)
	elementobolsonaro=Elemento(img=bolsonaro,style=dict (top=350,left=500,width="200px",heigth="100px"))
	elementobolsonaro.entra(cenapraia)
	elementomorinho=Elemento(img=morinho,style=dict (top=350,left=500,width="200px",heigth="100px"))
	elementomorinho.entra(cenapraia)
foto1()
