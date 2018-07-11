# betty.grace.main.py
from _spy.vitollino.main import Cena, Texto, Elemento, STYLE, INVENTARIO
#colocar codog soraya.main e import bloco
from browser import document, alert, html
STYLE["width"]=900
STYLE["height"]="600px"
FUNDO_BRANCO = "https://i.imgur.com/92bebxa.jpg"
CARINHAF ="https://i.imgur.com/n6b2S6t.png"
ALIMENTO2 = "https://i.imgur.com/kUlL42h.jpg"
ALIMENTO1 = "https://i.imgur.com/wPCVCa4.jpg"
DESCANSO1 =  "https://i.imgur.com/kALoNiv.jpg"
DESCANSO2 = "https://i.imgur.com/uLJYxzK.jpg"
DIVERSAO1 = "https://i.imgur.com/qXk60ff.jpg"
DIVERSAO2 ="https://i.imgur.com/PkJbh6T.jpg"
EXCREMENTO1 = "https://i.imgur.com/6bhgxtG.jpg"
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
    

class Tabuleiro:

    def __init__ (self):
        def move_carta(carta):
            print(carta.target.id)
            acarta = self.lista_de_cartas[carta.target.id]
            acarta.elt.style.left = "250px"
            acarta.elt.style.top = "250px"
        
        tabelafase1 = Cena(img=TABELAFASE1)
        self.pilha0 = Elemento(DESCANSO1, tit='descanso1', style=dict(
            width="120px", height="90px", left=10, top=10))
        self.pilha = Elemento(ALIMENTO1, tit='alimento1', style=dict(
            width="120px", height="90px", left=10, top=10))
        self.pilha0.img.Id,  self.pilha.img.Id = 'descanso1', 'alimento1'
        self.lista_de_cartas = {'descanso1':self.pilha0, 'alimento1':self.pilha}
        
        #self.pilha0.vai = move_carta
        #self.pilha.vai = move_carta
        self.pilha0.entra(tabelafase1)
        self.pilha.entra(tabelafase1)
        
        ### TABULEIRO ####
        TBX, TBY = 153, 103
        self.casa0 = Elemento(SONO1, tit='0_0', style=dict(
            width=TBX, height=TBY, left=220, top=140))
        self.casa = Elemento(SONO1, tit='0_1', style=dict(
            width=TBX, height=TBY, left=400, top=140))
        self.tabuleiro = {}
        #self.casa0.entra(tabelafase1)
        #self.casa.entra(tabelafase1)
        inicio_x, inicio_y = 220, 145
        for coluna in range(4):
            for linha in range(4):
                nome = "{}_{}".format(linha, coluna)
                self.tabuleiro[nome] = Elemento(FUNDO_BRANCO, tit=nome, style=dict(
                    width=TBX-8, height="{}px".format(TBY-8), left=inicio_x+coluna*TBX, top=inicio_y+linha*TBY))
                self.tabuleiro[nome].entra(tabelafase1)
                self.tabuleiro[nome].onclick = move_carta

        tabelafase1.vai()

Tabuleiro()

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


