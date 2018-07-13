# betty.grace.main.py
from _spy.vitollino.main import Cena, Texto, Elemento, STYLE, INVENTARIO
#colocar codog soraya.main e import bloco
from browser import document, alert, html
STYLE["width"]=1100
STYLE["height"]="600px"
FUNDO_BRANCO = "https://i.imgur.com/92bebxa.jpg"
FUNDO_BRANCO_TESTE ="https://i.imgur.com/BxBeCrY.jpg"
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
TABELAFASE1 = "https://i.imgur.com/sp2gLBu.jpg"
TABELAFASE2 = "https://i.imgur.com/SYkuH9o.jpg"
tabelafase1 = Cena(img=TABELAFASE1)
    

class Tabuleiro:

    def __init__ (self):
        def move_carta(casa):
            print(casa.target.id)
            print(list(self.tabuleiro.keys()))
            carta_a_mover = self.lista_de_cartas.pop()
            casa_destino = casa.target.id
            elemento_casa_do_tabuleiro = self.tabuleiro[casa_destino].elt
            carta_a_mover.elt.style.left = elemento_casa_do_tabuleiro.style.left
            carta_a_mover.elt.style.top = elemento_casa_do_tabuleiro.style.top
            print(elemento_casa_do_tabuleiro.style.left, elemento_casa_do_tabuleiro.style.top)
            print(carta_a_mover.elt.style.left, carta_a_mover.elt.style.top)
            dica_do_valor = Elemento(SORRISOMAIS1, style=dict(left=950))
            dica_do_valor.entra(self.tabela_fase1)
        
        self.tabela_fase1 = tabelafase1 = Cena(img=TABELAFASE1)
        self.pilha = Elemento(DESCANSO1, tit='descanso1', style=dict(
            width="120px", height="90px", left=10, top=10))
            
        self.lista_de_cartas =[]
        Pilha_Cartas = [ALIMENTO1, DESCANSO1, DIVERSAO1, EXCREMENTO1]
        Resposta_Cartas = [(ALIMENTO1,"0_1","0_2 0_3 0_0"), DESCANSO1, DIVERSAO1, EXCREMENTO1]
        
        
        #self.pilha0.vai = move_carta
        #self.pilha.vai = move_carta
        #self.pilha.entra(tabelafase1)
       
        
        ### TABULEIRO ####
        TBX, TBY = 140, 84
        self.casa0 = Elemento(SONO1, tit='0_0', style=dict(
            width=TBX, height=TBY, left=220, top=140))
        self.casa = Elemento(SONO1, tit='0_1', style=dict(
            width=TBX, height=TBY, left=400, top=140))
        self.tabuleiro = {}
        #self.casa0.entra(tabelafase1)
        #self.casa.entra(tabelafase1)
        inicio_x, inicio_y = 165, 218
        for coluna in range(4):
            for linha in range(4):
                nome = "{}_{}".format(linha, coluna)
                self.tabuleiro[nome] = Elemento(FUNDO_BRANCO, tit=nome+"_", style=dict(
                    width=TBX-15, height="{}px".format(TBY-8), left=inicio_x+coluna*TBX, top=inicio_y+linha*TBY))
                self.tabuleiro[nome].entra(tabelafase1)
                self.tabuleiro[nome].img.id = nome
                self.tabuleiro[nome].elt.onclick = move_carta

        for carta in Pilha_Cartas:
            a_carta_a_ser_empilhada = Elemento (carta, tit= carta, style=dict(
            width="120px", height="90px", left=10, top=10))
            self.lista_de_cartas.append(a_carta_a_ser_empilhada)
            a_carta_a_ser_empilhada.entra(tabelafase1)

        tabelafase1.vai()

Tabuleiro()
