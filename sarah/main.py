# betty.sarah.main.py
from _spy.vitollino.main import Cena,Elemento,Texto,STYLE
praia="https://www.fotoswiki.org/Uploads/fotoswiki.org/ImagensGrandes/praias-7.jpg"
barco="https://cdn.pixabay.com/photo/2014/04/02/16/23/boat-307125_960_720.png"
bolsonaro="https://pbs.twimg.com/media/CnqKuEnW8AAXMbU.png"
STYLE["width"]=1280
STYLE["height"]="670px"
def foto1():
	cenapraia=Cena(img=praia)
	elementobarco=Elemento(img=barco,style=dict (top=400,left=300,width="600px",heigth="400px"))
	elementobarco.entra(cenapraia)
	elementobolsonaro=Elemento(img=bolsonaro,style=dict (top=330,left=500,width="1px",heigth="8000px"))
	elementobolsonaro.entra(cenapraia)
	textobolsonaro=Texto(cenapraia,"Comunismo é coisa do lula")
	elementobolsonaro.vai=textobolsonaro.vai
	cenapraia.vai()
foto1()
