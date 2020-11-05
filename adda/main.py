# betty.adda.main.py
#import serial
from datetime import timedelta
from datetime import date
from datetime import datetime
from _spy.vpython.main import *
from browser import doc
#from sys import stdout
#from time import sleep
TAM = (-1, 0, 1)
SP = 9
SZ = 4

# leitura = serial.Serial('COM7', 9600)

data_atual = date.today()
data_texto = data_atual.strftime("%d/%m/%Y")
#print(data_texto)

# Gera o cronômetro
# segundos = int(input('Inicie digitando 0: '))
# tempo = timedelta(seconds=segundos)
pontos_suc = int(0)
pontos_sim = int(0)


class FakeSerial:
    def readline(self):
        from random import shuffle
        line = [10]*27
        pecas = list(range(10,40))
        lugares = list(range(27))
        shuffle(pecas)
        shuffle(lugares)
        for lugar in lugares[:6]:
            line[lugar] = pecas[lugar]
        return "\t".join(["{}".format(dado) for dado in line]).encode("utf8")
        
leitura = FakeSerial()

'''
class Casa:
    CASAS = {}  # esta coleção serve para achar o objeto casa a partir de sua posicão

    def __init__(self, x, y, z):
        self.pos = (x*SP, y*SP, z*SP)
        tam = SZ /2
        self.e_casa = sphere(pos=self.pos, size=(tam, tam, tam), opacity=0.2)
        Casa.CASAS[self.pos] = self  # adiciona esta casa na coleção de casas
        self.peca = None

    def recebe(self, algo3d):
        self.peca = algo3d
        vencedores = self.testa_ganhou()
        if vencedores:
            #print("ganhou")
            #self.pinta_vencedores(vencedores)
            Tabuleiro.TABULEIRO.ganhou(vencedores)
            return True
        return False

    def tipo_peca(self):
        #print("tipo_peca", self.peca.tipo if self.peca is not None else 0)
        return self.peca.tipo if self.peca else 0

    def clicou(self):
        coluna, linha, camada = self.pos  # aposição da peça vai ser a posição da casa
        Tabuleiro.TABULEIRO.registra_jogada_na_historia(self.pos)
        #peca = Peca(pecas.pop(), coluna, linha, camada, cores.pop())  # cria uma peça aqui
        peca = Tabuleiro.TABULEIRO.joga(coluna, linha, camada)  # cria uma peça aqui
        #Casa.CASAS.pop(self.pos)  # remove esta da lista de casas para não ser clicada
        return self.recebe(peca)  # avisa a casa que ela esta é a peça que está nela
        #print(self.pos)

    def testa_ganhou(self):
        return Tabuleiro.TABULEIRO.ganhou()
'''

class Tabuleiro():
    TABULEIRO = None

    def __init__(self):
        # self.leitor = list(leitura.readline().decode("utf8"))
        # isto deve ser um metodo, pois é uma ação de ler
        def calcula_casas_alinhadas():
            casas = range(27)
            linhas_x = [alinhadas for alinhadas in zip(casas[::3], casas[1::3], casas[2::3])]
            linhas_y = [alinhadas for n in (0,1,2) for alinhadas in zip(casas[n::9], casas[n+3::9], casas[n+6::9])]
            linhas_z = [alinhadas for alinhadas in zip(casas, casas[9:], casas[18:])]
            # ainda faltam as diagonais
            diag_f_x = [alinhadas for alinhadas in zip(casas[::9], casas[4::9], casas[8::9])]
            diag_b_x = [alinhadas for alinhadas in zip(casas[2::9], casas[4::9], casas[6::9])]
            diag_f_y = [alinhadas for alinhadas in zip(casas, casas[12:], casas[25:])]
            diag_b_y = [alinhadas for alinhadas in zip(casas[6:9], casas[12:15], casas[18:21])]
            diag_f_z = [alinhadas for alinhadas in zip(casas[::3], casas[10::3], casas[20::3])]
            diag_b_z = [alinhadas for alinhadas in zip(casas[2::9], casas[10::3], casas[18::3])]
            diag_xyz = [(0,13,26), (2, 13, 24),(5,13,20), (7, 13, 18)]
            diags = diag_f_x +diag_b_x +diag_f_y +diag_b_y +diag_f_z +diag_b_z+diag_xyz
            # print(diags)
            return linhas_x + linhas_y + linhas_z + diags

        Tabuleiro.TABULEIRO = self
        self.valor = []
        """ Aqui ficarão armazenados os valores lidos da porta serial"""
        self.acertos = calcula_casas_alinhadas()
        """ conjunto de todas as casas alinhadas três a três"""
        alinhados = ((0, 1), (0, 2), (1, 2))
        self.promessas = [(lin[a], lin[b]) for a,b in alinhados for lin in self.acertos]
        """ conjunto de todas as casas alinhadas dois a dois"""
        self.pinos = []
        doc['pydiv'].html = ""
        _gs = Glow('pydiv')
        cena = canvas()
        cena.width = 900
        cena.height = 600
        #self._casas = [Casa(coluna, linha, camada)
                 #for coluna in TAM for linha in TAM for camada in TAM]

        
    def calcula_propriedade_peca(self, peca):
        """
        Usando a artmética de módulo cria um byte para representar as propriedades da peça
        cada bit do byte representa cor e forma da peça na seguinte ordem:
        q= quadrado, c= circulo, g = grande, p=pequeno, f = furado, n= negro, b= branco
        bqp,bqg,bcf,bcg,bcp,nqp,nqg,ncf,ncg,ncp, vermelho, verde, purpura, laranja, amarelo, azul
        """
        if peca < 11:
            return 0
        else: 
            peca -= 11
        cor = peca // 5
        forma = peca % 5
        return (1<<cor) + (1 << (forma + 6 * (peca//15 + 1) ))
         
        
    def leitor(self):
        return leitura.readline().decode("utf8")
        
    def formata_leitura(self, linha_lida):
        """ Pega o texto lido e converte em um vetor de inteiros
        
        O dado vem como um texto continuo com os valores separados por tab
        """
        self.pinos = [self.calcula_propriedade_peca(int(dado)) for dado in linha_lida.split("\t")]
        """ o metodo split quebra o texto em um vetor de strings qe estavam separadas pelo tab"""
        return self.pinos

    def velho_formata_leitura(self, valor):
        global valor_int
        self.valor = self.leitor
        n_remove = '\n'
        valor.remove(n_remove)
        val_remove = '\t'
        while val_remove in valor:
            valor.remove(val_remove)
            VALOR = valor
            VALOR = VALOR[0] + VALOR[1], VALOR[2] + VALOR[3], VALOR[4] + VALOR[5], VALOR[6] + VALOR[7], \
                    VALOR[8] + VALOR[9], VALOR[10] + VALOR[11], VALOR[12] + VALOR[13], VALOR[14] + VALOR[15], \
                    VALOR[16] + VALOR[17], VALOR[18] + VALOR[19], VALOR[20] + VALOR[21], VALOR[22] + VALOR[23], \
                    VALOR[24] + VALOR[25], VALOR[26] + VALOR[27], VALOR[28] + VALOR[29], VALOR[30] + VALOR[31], \
                    VALOR[32] + VALOR[33], VALOR[34] + VALOR[35], VALOR[36] + VALOR[37], VALOR[38] + VALOR[39], \
                    VALOR[40] + VALOR[41], VALOR[42] + VALOR[43], VALOR[44] + VALOR[45], VALOR[46] + VALOR[47], \
                    VALOR[48] + VALOR[49], VALOR[50] + VALOR[51], VALOR[52] + VALOR[53]
            valor_int = []
            for val in VALOR:
                valor_int.append(int(val))
            for m in range(len(valor_int)):
                if valor_int[m] == 10:
                    valor_int[m] = valor_int[m] - 10

    def atualiza_leitura(self, novo_valor_leitura=""):
        #novo_valor_leitura = self.novo_valor_leitura
        # self.novo_valor_leitura = list(leitura.readline().decode("utf8"))
        novo_valor_leitura = self.formata_leitura(self.leitor())

        if self.valor != novo_valor_leitura:
            self.valor = novo_valor_leitura
            hora_atual = datetime.now()
            hora_texto = hora_atual.strftime("%H:%M:%S")
            # print(self.valor, hora_texto)
            # print( "promessas = {}".format(self.proc_sucessivo()))

        else:
            self.valor = novo_valor_leitura
            #self.valor = self.formata_leitura(self.novo_valor_leitura)
            #self.novo_valor_leitura.proc_suc_azul()
            #self.novo_valor_leitura.proc_suc_amar()
            
    def proc_sucessivo(self):
        pinos = self.pinos
        promete = sum( 1 if bool(pinos[a] & pinos[b]) else 0 for a, b in self.promessas)
        return promete


    # inicio de formação sequencial peças azuis: ponto de Processamento Sucessivo
    def proc_suc_azul(self, prim_casa, seg_casa):
        global pontos_suc
        if (valor_int[prim_casa] == 11 or valor_int[prim_casa] == 12 or valor_int[prim_casa] == 13 or
            valor_int[prim_casa] == 14 or valor_int[prim_casa] == 15) and (not (
                not (valor_int[seg_casa] == 11) and not (valor_int[seg_casa] == 12) and not (
                valor_int[seg_casa] == 13)) or valor_int[seg_casa] == 14 or valor_int[seg_casa] == 15):
            pontos_suc += 1
            hora_atual = datetime.now()
            hora_texto = hora_atual.strftime("%H:%M:%S")
            print(valor_int, hora_texto, ' %i Ponto de Proc. Sucessivo peças azuis: ' % pontos_suc, flush=True)

    # inicio de formação sequencial peças azuis: ponto de Processamento Sucessivo
    def proc_suc_amar(self, prim_casa, seg_casa):
        global pontos_suc
        if (valor_int[prim_casa] == 16 or valor_int[prim_casa] == 17 or valor_int[prim_casa] == 18 or
            valor_int[prim_casa] == 19 or valor_int[prim_casa] == 20) and (not (
                not (valor_int[seg_casa] == 16) and not (valor_int[seg_casa] == 17) and not (
                valor_int[seg_casa] == 18)) or valor_int[seg_casa] == 19 or valor_int[seg_casa] == 20):
            pontos_suc += 1
            hora_atual = datetime.now()
            hora_texto = hora_atual.strftime("%H:%M:%S")
            print(valor_int, hora_texto, ' %i Ponto de Proc. Sucessivo peças amarelas: ' % pontos_suc, flush=True)


def main():
    tabuleiro = Tabuleiro()
    return tabuleiro


if __name__ == '__main__':
    tabuleiro = main()
    for i in range(200):
        tabuleiro.atualiza_leitura()