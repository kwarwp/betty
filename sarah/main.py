# betty.sarah.main.py
from _spy.vitollino.main import Cena,Elemento,Texto,STYLE
naruto="https://uploads.jovemnerd.com.br/wp-content/uploads/2017/03/v-naruto-1210x540.jpg"
logonaruto="https://logodownload.org/wp-content/uploads/2014/10/naruto-shippuden-logo-1.png"
STYLE["width"]=1000
STYLE["height"]="670px"
def foto1():
	cenanaruto=Cena(img=naruto)
	elementologonaruto=Elemento(img=logonaruto,style=dict (top=400,left=300,width="450px",heigth="400px"))
	elementologonaruto.entra(cenanaruto)
	cenanaruto.vai()
foto1()
