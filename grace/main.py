# betty.grace.main.py
from _spy.vitollino.main import Cena, Texto, Elemento, STYLE, INVENTARIO
#colocar codog soraya.main e import bloco
from browser import document, alert, html
STYLE["width"]=1100
STYLE["height"]="600px"
FUNDO_BRANCO ="https://i.imgur.com/92bebxa.jpg"
FUNDO_BRANCO_TESTE ="https://i.imgur.com/BxBeCrY.jpg"
CLIQUEAQUI ="https://i.imgur.com/j8nkqpT.jpg"
ALIMENTO_FASE1_1 ="https://i.imgur.com/C2sTazM.jpg"
DESCANSO_FASE1_2 ="https://i.imgur.com/ruxtdF1.jpg"
DIVERSAO_FASE1_3 = "https://i.imgur.com/usgSqOU.jpg"
EXCREMENTO_FASE1_4 ="https://i.imgur.com/RqQOALU.jpg"
ALIMENTO_FASE1_5 ="https://i.imgur.com/i8u03BA.jpg"
DESCANSO_FASE1_6 ="https://i.imgur.com/CBYMr6w.jpg"
DIVERSAO_FASE1_7 ="https://i.imgur.com/bKn7iba.jpg"
EXCREMENTO_FASE1_8 ="https://i.imgur.com/CH5iGGZ.jpg"
ALIMENTO_FASE1_9 ="https://i.imgur.com/gn9cGsu.jpg"
DESCANSO_FASE1_10 ="https://i.imgur.com/8Ufyps0.jpg"
DIVERSAO_FASE1_11 ="https://i.imgur.com/8jJkqbp.jpg"
EXCREMENTO_FASE1_12 ="https://i.imgur.com/jopwq9M.jpg"
ALIMENTO_FASE1_13 ="https://i.imgur.com/qPPddW9.jpg"
DESCANSO_FASE1_14 ="https://i.imgur.com/Wx18Rc9.jpg"
DIVERSAO_FASE1_15 ="https://i.imgur.com/mmXE6vl.jpg"
EXCREMENTO_FASE1_16 ="https://i.imgur.com/xYci2H4.jpg"
EXCREMENTO2 ="https://i.imgur.com/kgnZgVq.jpg"
FELIZ1 ="https://i.imgur.com/fADJqIx.jpg"
FELIZ2 ="https://i.imgur.com/s60ZiT1.jpg"
FOME1 ="https://i.imgur.com/s8IfPKT.jpg"
FOME2 ="https://i.imgur.com/xbWe7BC.jpg"
SONO1 ="https://i.imgur.com/aAiB0rs.jpg"
SONO2 ="https://i.imgur.com/DF0UOvo.jpg"
RESP_SORRISOMAIS_FASE1 ="https://i.imgur.com/kjQFRv8.jpg"
RESP_SORRISO_FASE1 ="https://i.imgur.com/r5ZovCe.jpg"
RESP_TRISTE_FASE1 ="https://i.imgur.com/CbrmJpE.jpg"
SORRISOMAIS2 ="https://i.imgur.com/xZ5mpcS.jpg"
SORRISO2 ="https://i.imgur.com/XpVabA8.jpg"
SUJO1 ="https://i.imgur.com/A64jbtF.jpg"
SUJO2 ="https://i.imgur.com/5Vfq64q.jpg"
TRISTE1 ="https://i.imgur.com/CbrmJpE.jpg"
TRISTE2 ="https://i.imgur.com/PzDcx3q.jpg"
TABELAFASE1 ="https://i.imgur.com/sp2gLBu.jpg"
TABELAFASE2 ="https://i.imgur.com/SYkuH9o.jpg"
tabelafase1 = Cena(img=TABELAFASE1)
TBRESPY, TBRESPX =  55, 751
RESPOSTA = [RESP_TRISTE_FASE1, RESP_SORRISO_FASE1, RESP_SORRISOMAIS_FASE1]

class Tabuleiro:

    def __init__ (self):
        def move_carta(casa):
            print(casa.target.id)
            print(list(self.tabuleiro.keys()))
            carta_a_mover = self.lista_de_cartas.pop()
            casa_destino = casa.target.id
            elemento_casa_do_tabuleiro = self.tabuleiro[casa_destino].elt
            cx, cy =  carta_a_mover.posicao_certa
            tx, ty =  self.tabuleiro[casa_destino].posicao_certa
            pontos = (1 if cx == tx else 0) + (1 if ty == cy else 0)
            #alert(pontos)
            carta_a_mover.elt.style.left = x = elemento_casa_do_tabuleiro.style.left
            carta_a_mover.elt.style.top = y = elemento_casa_do_tabuleiro.style.top
            pos = elemento_casa_do_tabuleiro.title
            print(elemento_casa_do_tabuleiro.style.left, elemento_casa_do_tabuleiro.style.top)
            print(carta_a_mover.elt.style.left, carta_a_mover.elt.style.top)
            ordem_da_carta = 15 - len(self.lista_de_cartas)
            dica_do_valor = Elemento(RESPOSTA[pontos], style=dict(
               width="60px", height="87px", left= TBRESPX+(ordem_da_carta%4)*TBRX, top= TBRESPY+(ordem_da_carta//4)*TBRY ))
            """left=751, top=55))"""
            dica_do_valor.entra(self.tabela_fase1)
        
        self.tabela_fase1 = tabelafase1 = Cena(img=TABELAFASE1)
        self.pilha = Elemento(ALIMENTO_FASE1_1, tit='Alimento1', style=dict(
            width="100px", height="50px", left=10, top=10))
            
        self.lista_de_cartas =[]
        Pilha_Cartas = [EXCREMENTO_FASE1_16, DIVERSAO_FASE1_15, DESCANSO_FASE1_14, ALIMENTO_FASE1_13,\
        EXCREMENTO_FASE1_12, DIVERSAO_FASE1_11, DESCANSO_FASE1_10,ALIMENTO_FASE1_9,\
        EXCREMENTO_FASE1_8, DIVERSAO_FASE1_7, DESCANSO_FASE1_6, ALIMENTO_FASE1_5,\
        EXCREMENTO_FASE1_4, DIVERSAO_FASE1_3, DESCANSO_FASE1_2, ALIMENTO_FASE1_1]
        Resposta_Cartas = [(ALIMENTO_FASE1_1,"0_1","0_2 0_3 0_0"), (DESCANSO_FASE1_2, "3_0","0_2 0_3 0_0"),\
        (DIVERSAO_FASE1_3, "2_2","0_2 0_3 0_0"), (EXCREMENTO_FASE1_4, "1_3","0_2 0_3 0_0")]
        respostas= "1_3,2_2,3_0,0_1,1_3,2_2,3_0,0_1,1_3,2_2,3_0,0_1,1_3,2_2,3_0,0_1"
        self.resposta_certa = {nome:pos.split("_") for nome,pos in zip(Pilha_Cartas,respostas.split(","))}
        
             
            
                
        """if Resposta_Carta =[(ALIMENTO_FASE1_1,"0_1"), (DESCANSO_FASE1_2, "3_0")]:
        else: valor_resposta = Elemento(RESP_SORRISOMAIS_FASE1, style=dict(width="60px", height="87px", left= TBRY, Top= TBRX ))
            valor_resposta.entra(self.tabela_fase1)"""
            
                   
        
       
       ### TABULEIRO RESPOSTA ####
        TBRX, TBRY = 80, 130
        self.casa0 = Elemento(RESP_SORRISOMAIS_FASE1, tit='0_0', style=dict(
            width=TBRX, height=TBRY, left=751, top=55))
        self.casa = Elemento(RESP_SORRISOMAIS_FASE1, tit='0_1', style=dict(
            width=TBRX, height=TBRY, left=800, top=55))
        self.tabuleiro_respostas = {}
        
        inicio_resp_x, inicio_resp_y = 754, 62
        for coluna in range(4):
            for linha in range(4):
                nome = "{}_{}".format(linha, coluna)
                self.tabuleiro_respostas[nome] = Elemento(FUNDO_BRANCO, tit=nome+"_", style=dict(
                    width=TBRX-11, height="{}px".format(TBRY-52), left=inicio_resp_x+coluna*TBRX, top=inicio_resp_y+linha*TBRY))
                self.tabuleiro_respostas[nome].entra(tabelafase1)
                self.tabuleiro_respostas[nome].img.id = nome
                self.tabuleiro_respostas[nome].elt.onclick = move_carta
                
       
        
        ### TABULEIRO ####
        TBX, TBY = 140, 84
        self.casa0 = Elemento(ALIMENTO_FASE1_1, tit='0_0', style=dict(
            width=TBX, height=TBY, left=220, top=140))
        self.casa = Elemento(ALIMENTO_FASE1_1, tit='0_1', style=dict(
            width=TBX, height=TBY, left=400, top=140))
        self.tabuleiro = {}
       
        inicio_x, inicio_y = 165, 218
        for coluna in range(4):
            for linha in range(4):
                nome = "{}_{}".format(linha, coluna)
                self.tabuleiro[nome] = Elemento(FUNDO_BRANCO, tit=nome+"_", style=dict(
                    width=TBX-15, height="{}px".format(TBY-8), left=inicio_x+coluna*TBX, top=inicio_y+linha*TBY))
                self.tabuleiro[nome].entra(tabelafase1)
                self.tabuleiro[nome].posicao_certa = nome.split("_")
                self.tabuleiro[nome].img.id = nome
                self.tabuleiro[nome].elt.onclick = move_carta
               
                              
        
        ### PILHA DE CARTAS ###
        for carta in Pilha_Cartas:
            a_carta_a_ser_empilhada = Elemento (carta, tit= carta, style=dict(
            width="115px", height="79px", left=40, top=40))
            a_carta_a_ser_empilhada.posicao_certa = self.resposta_certa[carta]
            self.lista_de_cartas.append(a_carta_a_ser_empilhada)
            a_carta_a_ser_empilhada.entra(tabelafase1)
        self.cliqueaqui = Elemento (CLIQUEAQUI, style=dict(width="170px", height="100px", left=40, top=40))
        self.cliqueaqui.entra (tabelafase1)
            
        def remove_clique_aqui(_):
            self.cliqueaqui.elt.remove()
        self.cliqueaqui.elt.onclick = remove_clique_aqui
               
        def recoloca_clique_aqui(_):
            self.cliqueaqui.entra(tabelafase1)
        self.tabuleiro[nome].elt.onclick = recoloca_clique_aqui
         
                
        
        
        tabelafase1.vai()

Tabuleiro()
