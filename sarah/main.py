# betty.sarah.main.py
from _spy.vitollino.main import Cena,Elemento,Texto,STYLE
praia="https://www.fotoswiki.org/Uploads/fotoswiki.org/ImagensGrandes/praias-7.jpg"
STYLE["width"]=1280
STYLE["height"]="670px"
def foto1():
	cenapraia=Cena(img=praia)
	cenapraia.vai()
foto1()