
{'date': 'Wed Nov 04 2020 16:13:19.166 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 59
  else 
        ^
SyntaxError: invalid syntax
'''},
{'date': 'Wed Nov 04 2020 16:13:35.552 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 63
  return (1<<cor) + (1 << (forma + 6 * (peca//15 + 1) )
                                                                                                                                                                                                                                                                                                                                                                                      ^
SyntaxError: invalid syntax
'''},
{'date': 'Wed Nov 04 2020 16:14:55.312 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''04/11/2020
Traceback (most recent call last):
  module _core.main line 180
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 310
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 282
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 299
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 155
    tabuleiro = main()
  module <module> line 150
    tabuleiro = Tabuleiro()
  module <module> line 43
    self.acertos = calcula_casas_alinhadas()
  module <module> line 39
    return linha_x + linhas_y + linhas_z
NameError: name 'linha_x' is not defined
'''},
{'date': 'Wed Nov 04 2020 16:15:20.942 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''04/11/2020
Traceback (most recent call last):
  module _core.main line 180
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 310
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 282
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 299
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 157
    tabuleiro.atualiza_leitura()
  module <module> line 107
    self.valor = self.formata_leitura(novo_valor_leitura)
  module <module> line 74
    self.pinos = [self.calcula_propriedade_peca(int(dado)) for dado in linha_lida.split("\t")]
AttributeError: 'list' object has no attribute 'split'
'''},
{'date': 'Wed Nov 04 2020 16:16:27.224 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''04/11/2020
Traceback (most recent call last):
  module _core.main line 180
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 310
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 282
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 299
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 157
    tabuleiro.atualiza_leitura()
  module <module> line 107
    self.valor = self.formata_leitura(novo_valor_leitura)
  module <module> line 74
    self.pinos = [self.calcula_propriedade_peca(int(dado)) for dado in linha_lida.split("\t")]
ValueError: invalid literal for int() with base 10: '{dado}'
'''},
{'date': 'Wed Nov 04 2020 16:17:32.74 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''04/11/2020
Traceback (most recent call last):
  module _core.main line 180
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 310
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 282
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 299
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 157
    tabuleiro.atualiza_leitura()
  module <module> line 104
    novo_valor_leitura = self.leitor()
  module <module> line 67
    return leitura.readline().decode("utf8")
  module <module> line 25
    return "\t".join([f"{dado}" for dado in line]).encode("utf8")
TypeError: sequence item 0: expected str instance, int found
'''},
{'date': 'Wed Nov 04 2020 19:36:45.191 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 26
  pecas = list(range(10:40))
                        ^
SyntaxError: invalid syntax
'''},
{'date': 'Thu Nov 05 2020 15:31:38.892 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''05/11/2020
Traceback (most recent call last):
  module _core.main line 180
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 310
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 282
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 299
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 171
    tabuleiro = main()
  module <module> line 166
    tabuleiro = Tabuleiro()
  module <module> line 58
    self.acertos = calcula_casas_alinhadas()
  module <module> line 53
    diags = diag_f_x +diag_b_x +diag_f_y +diag_b_y +diag_f_z +diag_b_z+diag_xyz
NameError: name 'diag_xyz' is not defined
'''},
{'date': 'Thu Nov 05 2020 15:31:55.964 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''05/11/2020
Traceback (most recent call last):
  module _core.main line 180
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 310
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 282
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 299
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 171
    tabuleiro = main()
  module <module> line 166
    tabuleiro = Tabuleiro()
  module <module> line 58
    self.acertos = calcula_casas_alinhadas()
  module <module> line 54
    return linhas_x + linhas_y + linhas_z + diagz
NameError: name 'diagz' is not defined
'''},
{'date': 'Thu Nov 05 2020 15:32:23.17 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''05/11/2020
[0, 0, 0, 132, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 130, 258, 0, 0, 0, 0, 0, 0, 0, 65, 0, 8208, 66] 15:32:22
Traceback (most recent call last):
  module _core.main line 180
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 310
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 282
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 299
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 173
    tabuleiro.atualiza_leitura()
  module <module> line 126
    print( "promessas = {}".format(self.proc_sucessivo()))
  module <module> line 136
    promete = sum( 1 if bool(pinos[a] & pinos[b]) else 0 for a, b in self.promessas)
IndexError: list index out of range
'''},
{'date': 'Thu Nov 05 2020 15:34:28.79 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''05/11/2020
Traceback (most recent call last):
  module _core.main line 180
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 310
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 282
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 299
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 172
    tabuleiro = main()
  module <module> line 167
    tabuleiro = Tabuleiro()
  module <module> line 64
    print(diags)
NameError: name 'diags' is not defined
'''},
{'date': 'Thu Nov 05 2020 16:02:06.690 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''05/11/2020

Exception: <TypeError: window.__context is undefined>
'''},
{'date': 'Thu Nov 05 2020 16:03:20.111 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
Exception: <SyntaxError: missing ] in computed property name>
'''},
{'date': 'Thu Nov 05 2020 16:05:20.239 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
Exception: <SyntaxError: missing ] in computed property name>
'''},
{'date': 'Thu Nov 05 2020 16:09:15.881 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
Exception: <SyntaxError: missing ] in computed property name>
'''},
{'date': 'Thu Nov 05 2020 16:12:49.464 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
Exception: <SyntaxError: missing ] in computed property name>
'''},
{'date': 'Thu Nov 05 2020 16:13:25.364 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
Exception: <SyntaxError: missing ] in computed property name>
'''},
{'date': 'Thu Nov 05 2020 16:14:11.876 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
Exception: <SyntaxError: missing ] in computed property name>
'''},
{'date': 'Thu Nov 05 2020 16:16:35.831 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
Exception: <SyntaxError: Unexpected token ','>
'''},
{'date': 'Thu Nov 05 2020 16:18:08.99 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
Exception: <SyntaxError: Unexpected token ','>
'''},
{'date': 'Thu Nov 05 2020 16:18:29.343 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
Exception: <SyntaxError: Unexpected token ','>
'''},
{'date': 'Thu Nov 05 2020 16:22:25.684 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
Exception: <SyntaxError: Unexpected token ','>
'''},
{'date': 'Thu Nov 05 2020 16:31:04.231 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 118
  curve((-2,0,0), (2,0,0)
                                         ^
SyntaxError: invalid syntax
'''},
{'date': 'Thu Nov 05 2020 16:31:16.15 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
Exception: <SyntaxError: Unexpected token ','>
'''},
{'date': 'Thu Nov 05 2020 16:31:42.743 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 180
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 310
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 282
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 299
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 227
    tabuleiro = main()
  module <module> line 222
    tabuleiro = Tabuleiro()
  module <module> line 118
    curve((-2,0,0), (2,0,0))
TypeError: __init__() takes 1 positional arguments but more were given
'''},
{'date': 'Thu Nov 05 2020 16:33:03.726 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 180
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 310
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 282
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 299
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 227
    tabuleiro = main()
  module <module> line 222
    tabuleiro = Tabuleiro()
  module <module> line 118
    curve(vec(-2,0,0), vec(2,0,0))
TypeError: __init__() takes 1 positional arguments but more were given
'''},
{'date': 'Thu Nov 05 2020 16:42:23.3 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
Exception: <Error: A pos of a curve object must be a vector.>
'''},
{'date': 'Thu Nov 05 2020 16:46:43.114 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 180
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 310
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 282
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 299
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 227
    tabuleiro = main()
  module <module> line 222
    tabuleiro = Tabuleiro()
  module <module> line 118
    curve((-4,0,0), (4,0,0))
  module _spy.vpython.primitive line 214
    primitive.__init__(self, window.glowscript.curve, *args)
TypeError: __init__() takes 2 positional argument but more were given
'''},
{'date': 'Thu Nov 05 2020 16:54:13.463 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
Exception: <Error: A pos of a curve object must be a vector.>
'''},
{'date': 'Thu Nov 05 2020 16:55:24.101 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
Exception: <Error: A curve object point must include a pos.>
'''},
{'date': 'Thu Nov 05 2020 17:07:39.895 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 180
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 310
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 282
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 299
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 233
    tabuleiro = main()
  module <module> line 228
    tabuleiro = Tabuleiro()
  module <module> line 120
    self._casas = [Casa(coluna, linha, camada)
  module <module> line 51
    Casa.ACASA.append[self]
AttributeError: 'method' object has no attribute '__getitem__'
'''},
{'date': 'Thu Nov 05 2020 17:09:00.373 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 180
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 310
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 282
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 299
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 233
    tabuleiro = main()
  module <module> line 228
    tabuleiro = Tabuleiro()
  module <module> line 120
    self._casas = [Casa(coluna, linha, camada)
  module <module> line 51
    Casa.ACASA.append[self]
AttributeError: 'method' object has no attribute '__getitem__'
'''},
{'date': 'Thu Nov 05 2020 17:10:26.494 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 180
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 310
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 282
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 299
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 233
    tabuleiro = main()
  module <module> line 228
    tabuleiro = Tabuleiro()
  module <module> line 124
    [line(vec(pos_casas(a)), vec(pos_casas(b)), vec(pos_casas(c))) for a, b, c in self.acertos]
TypeError: 'list' object is not callable
'''},
{'date': 'Thu Nov 05 2020 18:30:25.882 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
Exception: <SyntaxError: Unexpected token ','>
'''},
{'date': 'Thu Nov 05 2020 18:30:38.311 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''[(0, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11), (12, 13, 14), (15, 16, 17), (18, 19, 20), (21, 22, 23), (24, 25, 26), (0, 3, 6), (9, 12, 15), (18, 21, 24), (1, 4, 7), (10, 13, 16), (19, 22, 25), (2, 5, 8), (11, 14, 17), (20, 23, 26), (0, 9, 18), (1, 10, 19), (2, 11, 20), (3, 12, 21), (4, 13, 22), (5, 14, 23), (6, 15, 24), (7, 16, 25), (8, 17, 26), (0, 4, 8), (9, 13, 17), (18, 22, 26), (2, 4, 6), (11, 13, 15), (20, 22, 24), (0, 12, 25), (1, 13, 26), (6, 12, 18), (7, 13, 19), (8, 14, 20), (0, 10, 20), (3, 13, 23), (6, 16, 26), (2, 10, 18), (11, 13, 21), (20, 16, 24), (0, 13, 26), (2, 13, 24), (5, 13, 20), (7, 13, 18)]

Exception: <TypeError: Cannot read property 'canvas_selected' of undefined>
'''},
{'date': 'Thu Nov 05 2020 18:31:19.693 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
Exception: <SyntaxError: Unexpected token ','>
'''},
{'date': 'Thu Nov 05 2020 18:31:39.323 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''[(0, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11), (12, 13, 14), (15, 16, 17), (18, 19, 20), (21, 22, 23), (24, 25, 26), (0, 3, 6), (9, 12, 15), (18, 21, 24), (1, 4, 7), (10, 13, 16), (19, 22, 25), (2, 5, 8), (11, 14, 17), (20, 23, 26), (0, 9, 18), (1, 10, 19), (2, 11, 20), (3, 12, 21), (4, 13, 22), (5, 14, 23), (6, 15, 24), (7, 16, 25), (8, 17, 26), (0, 4, 8), (9, 13, 17), (18, 22, 26), (2, 4, 6), (11, 13, 15), (20, 22, 24), (0, 12, 25), (1, 13, 26), (6, 12, 18), (7, 13, 19), (8, 14, 20), (0, 10, 20), (3, 13, 23), (6, 16, 26), (2, 10, 18), (11, 13, 21), (20, 16, 24), (0, 13, 26), (2, 13, 24), (5, 13, 20), (7, 13, 18)]

Exception: <TypeError: Cannot read property 'canvas_selected' of undefined>
'''},
{'date': 'Thu Nov 05 2020 18:37:08.361 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
Exception: <SyntaxError: Unexpected token ','>
'''},
{'date': 'Thu Nov 05 2020 18:57:44.495 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
Exception: <SyntaxError: Unexpected token ','>
'''},
{'date': 'Thu Nov 05 2020 19:01:45.750 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
Exception: <SyntaxError: Unexpected token ','>
'''},
{'date': 'Thu Nov 05 2020 19:23:36.827 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 13
  CORES = {1<<bit: cor for bit, cor in enumerate("blue orange yellow purple green red".split())
                                                                                                 ^
SyntaxError: invalid syntax
'''},
{'date': 'Thu Nov 05 2020 19:24:07.810 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 180
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 310
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 282
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 299
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 14
    FORMA = ((cube,L,Z), (cube,S,Z), (cylinder,L,Z), (cylinder,S,Z), (cylinder,L,S))
NameError: name 'cube' is not defined
'''},
{'date': 'Thu Nov 05 2020 19:25:06.517 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
Exception: <SyntaxError: Unexpected token ','>
'''},
{'date': 'Thu Nov 05 2020 19:25:23.625 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 13
  CORES = {1<<bit: cor for bit, cor in enumerate("blue orange yellow purple green red".split())
                                                                                                 ^
SyntaxError: invalid syntax
'''},
{'date': 'Thu Nov 05 2020 19:26:04.385 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 180
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 310
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 282
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 299
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 14
    FORMA = ((box,L,Z), (box,S,Z), (cylinder,L,Z), (cylinder,S,Z), (cylinder,L,S))
NameError: name 'L' is not defined
'''},
{'date': 'Thu Nov 05 2020 19:48:40.432 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 180
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 310
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 282
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 299
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 261
    tabuleiro = main()
  module <module> line 256
    tabuleiro = Tabuleiro()
  module <module> line 135
    self.casas()
  module <module> line 152
    Cubo(-2,0,0,self.calcula_propriedade_peca(20))
  module <module> line 55
    forma, gran, peq = FORMA[tipo >> 6]
IndexError: list index out of range
'''},
{'date': 'Thu Nov 05 2020 19:50:28.180 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 180
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 310
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 282
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 299
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 261
    tabuleiro = main()
  module <module> line 256
    tabuleiro = Tabuleiro()
  module <module> line 135
    self.casas()
  module <module> line 152
    Cubo(-2,0,0,self.calcula_propriedade_peca(20))
  module <module> line 55
    forma, gran, peq = FORMAS[tipo >> 6]
KeyError: 16
'''},
{'date': 'Thu Nov 05 2020 19:56:55.601 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 180
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 310
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 282
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 299
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 261
    tabuleiro = main()
  module <module> line 256
    tabuleiro = Tabuleiro()
  module <module> line 135
    self.casas()
  module <module> line 152
    Cubo(-2,0,0,self.calcula_propriedade_peca(19))
  module <module> line 55
    forma, gran, peq = FORMAS[tipo >> 6]
KeyError: 8
'''},
{'date': 'Thu Nov 05 2020 20:01:43.950 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
Exception: <TypeError: Cannot read property '$nat' of undefined>
'''},
{'date': 'Thu Nov 05 2020 20:02:12.960 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
Exception: <TypeError: Cannot read property '$nat' of undefined>
'''},
{'date': 'Thu Nov 05 2020 20:03:21.33 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
Exception: <TypeError: Cannot read property '$nat' of undefined>
'''},
{'date': 'Thu Nov 05 2020 20:05:16.839 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
Exception: <SyntaxError: Unexpected token ','>
'''},
{'date': 'Thu Nov 05 2020 20:05:48.549 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
Exception: <TypeError: Cannot read property '$nat' of undefined>
'''},
{'date': 'Thu Nov 05 2020 20:07:23.143 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
Exception: <TypeError: Cannot read property '$nat' of undefined>
'''},
{'date': 'Thu Nov 05 2020 20:08:49.596 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
Exception: <SyntaxError: Unexpected token ','>
'''},
{'date': 'Thu Nov 05 2020 20:09:23.307 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 180
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 310
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 282
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 299
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 263
    tabuleiro = main()
  module <module> line 258
    tabuleiro = Tabuleiro()
  module <module> line 136
    print([k, v for k,v in FORMAS.items()])
TypeError: append() takes 2 positional argument but more were given
'''},