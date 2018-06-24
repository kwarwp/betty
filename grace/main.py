# betty.grace.main.py
from _spy.vitollino.main import Cena, Texto, Elemento, STYLE, INVENTARIO
#colocar codog soraya.main e import bloco
from browser import document, alert, html
STYLE["width"]=900

CARINHAF ="https://i.imgur.com/n6b2S6t.png"
ALIMENTO1 = "https://i.imgur.com/kUlL42h.jpg"
ALIMENTO2 = "https://i.imgur.com/wPCVCa4.jpg"
DESCANSO1 =  "https://i.imgur.com/kALoNiv.jpg"
DESCANSO2 = "https://i.imgur.com/uLJYxzK.jpg"
DIVERSAO1 = "https://i.imgur.com/qXk60ff.jpg"
DIVERSAO2 ="https://i.imgur.com/PkJbh6T.jpg"
EXCRMENTO1 = "https://i.imgur.com/6bhgxtG.jpg"
EXCREMENTO2 = "https://i.imgur.com/kgnZgVq.jpg"
FELIZ1 =  "https://i.imgur.com/fADJqIx.jpg"
FELIZ2 ="https://i.imgur.com/s60ZiT1.jpg"
FOME1 ="https://i.imgur.com/s8IfPKT.jpg"
FOME2 ="https://i.imgur.com/xbWe7BC.jpg"
SONO1 = "https://i.imgur.com/aAiB0rs.jpg"
SONO2 ="https://i.imgur.com/DF0UOvo.jpg"
SORRISOMAIS1 = "https://i.imgur.com/WCWBdwU.jpg"
SORRISOMAIS2 = "https://i.imgur.com/xZ5mpcS.jpg"
SORRISO1 = "https://i.imgur.com/M4LKzQL.jpg"
SORRISO2 = "https://i.imgur.com/XpVabA8.jpg"
SUJO1 = "https://i.imgur.com/A64jbtF.jpg"
SUJO2 = "https://i.imgur.com/5Vfq64q.jpg"
TRISTE1 = "https://i.imgur.com/RslYMn9.jpg"
TRISTE2 = "https://i.imgur.com/PzDcx3q.jpg"
TABELAFASE1 = "https://i.imgur.com/EMLDBhH.jpg"
TABELAFASE2 = "https://i.imgur.com/yaeq5Ua.jpg"
tabelafase1 = Cena(img=TABELAFASE1)
    

def faseum ():
    tabelafase1 = Cena(img=TABELAFASE1)
    tabelafase1.vai()    

faseum()

class Baralho ():
    def __init__ (self, bloco, left=0, top=0, ileft=0, itop=0,
                 size=dict(width=100, height=100)):
        self.suporte = None
        w, h = size.values()
        self.fid = fid = "baralho_{}_{}".format(ileft, itop)
        self.casa = "casa_{}_{}".format(left, top)
        ileft, itop = "%dpx" % (-ileft*w), "%dpx" % (-itop*h)
        style = {'position': 'absolute', 'overflow': 'hidden',
                'background-image': 'url({})'.format(bloco.img),
                'background-position': '{} {}'.format(ileft, itop),
                'background-size': '{}px {}px'.format(*bloco.size),
        }
        style.update({k:'{}px'.format(v) for k, v in size.items() })
        style.update(left="%dpx" % (left*(w+10)), top="%dpx" % (top*(h+10)))
        self.folha = html.DIV(Id=fid, style=style, draggable=True)        
        bloco.folha <= self.folha
        self.folha.ondragstart = self.drag_start
        self.folha.onmouseover = self.mouse_over
        bloco.folhas[fid]=self
        #INVENTARIO.score(casa=self.casa, carta=self.fid, move="INIT", ponto=0, valor=0)


