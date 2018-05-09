# betty.roxanne.main.py
from _spy.vitollino.main import Elemento, Cena, Texto
from _spy.vitollino.main import STYLE
STYLE["width"] = 600
STYLE["height"] = 600


PISTA = "https://i.imgur.com/VyNCZo7.jpg"

def Robotica ():
    pista = Cena(img=PISTA)
    pista.vai()
    

Robotica()