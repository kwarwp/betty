# betty.heather.main.py
import serial
from datetime import timedelta
from datetime import date
from datetime import datetime
from sys import stdout
from time import sleep

leitura = serial.Serial('COM7', 9600)

data_atual = date.today()
data_texto = data_atual.strftime("%d/%m/%Y")
print(data_texto)

# Gera o cronômetro
segundos = int(input('Inicie digitando 0: '))
#tempo = timedelta(seconds=segundos)
pontos_suc = int(0)
pontos_sim = int(0)

for i in range(200):
    novo_valor_leitura = list(leitura.readline().decode("utf8"))
    #stdout.flush()
    #tempo = tempo + timedelta(seconds=0.5)
    sleep(0.5)
    #stdout.flush()

    for j in range(1):
        valor = list(leitura.readline().decode("utf8"))
        def Formata_leitura():
            global valor_int
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
                #return valor_int

        if valor == novo_valor_leitura:
           Formata_leitura()
           hora_atual = datetime.now()
           hora_texto = hora_atual.strftime("%H:%M:%S")
           print(valor_int, hora_texto)

        else:
            Formata_leitura()
            # inicio de formação sequencial peças azuis: ponto de Processamento Sucessivo
            def Processamento_Sucessivo(prim_casa, seg_casa):
                global pontos_suc
                if (valor_int[prim_casa] == 11 or valor_int[prim_casa] == 12 or valor_int[prim_casa] == 13 or
                    valor_int[prim_casa] == 14 or valor_int[prim_casa] == 15) and (valor_int[seg_casa] == 11
                    or valor_int[seg_casa] == 12 or valor_int[seg_casa] == 13 or valor_int[seg_casa] == 14
                    or valor_int[seg_casa] == 15):
                    pontos_suc += 1
                    hora_atual = datetime.now()
                    hora_texto = hora_atual.strftime("%H:%M:%S")
                    print(valor_int, hora_texto, ' %i Ponto de Proc. Sucessivo peças azuis: ' % pontos_suc, flush=True)

            def Processamento_Simultaneo(prim_casa, seg_casa, terc_casa):
                global pontos_sim
                if (valor_int[prim_casa] == 11 or valor_int[prim_casa] == 12 or valor_int[prim_casa] == 13 or
                    valor_int[prim_casa] == 14 or valor_int[prim_casa] == 15) and (valor_int[seg_casa] == 11
                    or valor_int[seg_casa] == 12 or valor_int[seg_casa] == 13 or valor_int[seg_casa] == 14
                    or valor_int[seg_casa] == 15) and (valor_int[terc_casa] == 11 or valor_int[terc_casa] == 12 or
                    valor_int[terc_casa] == 13 or valor_int[terc_casa] == 14 or valor_int[terc_casa] == 15):

                    pontos_sim += 1
                    hora_atual = datetime.now()
                    hora_texto = hora_atual.strftime("%H:%M:%S")
                    print(valor_int, hora_texto, ' %i Ponto de Proc. Simultaneo peças azuis: ' % pontos_sim, flush=True)


            Processamento_Sucessivo(0, 1)
            Processamento_Sucessivo(1, 2)
            Processamento_Sucessivo(3, 4)
            Processamento_Sucessivo(4, 5)
            Processamento_Sucessivo(6, 7)
            Processamento_Sucessivo(7, 8)

            Processamento_Sucessivo(0, 3)
            Processamento_Sucessivo(3, 6)
            Processamento_Sucessivo(1, 4)
            Processamento_Sucessivo(4, 7)
            Processamento_Sucessivo(2, 5)
            Processamento_Sucessivo(5, 8)

            Processamento_Sucessivo(0, 4)
            Processamento_Sucessivo(4, 8)
            Processamento_Sucessivo(2, 4)
            Processamento_Sucessivo(4, 6)

            Processamento_Sucessivo(9, 10)
            Processamento_Sucessivo(10, 11)
            Processamento_Sucessivo(12, 13)
            Processamento_Sucessivo(13, 14)
            Processamento_Sucessivo(15, 16)
            Processamento_Sucessivo(16, 17)