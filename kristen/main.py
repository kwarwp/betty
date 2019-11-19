# betty.kristen.main.py
from _spy.vitollino.main import Cena, Texto, Elemento, STYLE
Campo='https://turismo.buenosaires.gob.ar/sites/turismo/files/campo_de_golf_1200_c.jpg'

def Quadra():
	Cena_Campo= Cena(img=Campo)
	Cena_Campo.vai()
Quadra()