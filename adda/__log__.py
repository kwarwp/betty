
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