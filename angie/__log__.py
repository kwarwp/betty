
{'date': 'Tue Dec 04 2018 15:38:13.697 GMt-0200 (Horário de Verão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 5
  #circus(<ponha aqui o número do desafio e descomente a linha>, <parâmetro indicado>)
                                                                                      ^
IndentationError: expected an indented block
'''},
{'date': 'Tue Dec 04 2018 15:38:55.14 GMt-0200 (Horário de Verão de Brasília) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 160
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 306
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 278
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 295
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 10
    circus(1, [[TOPO_ESQUERDA, TOPO_CENTRO, TOPO_DIREITA], [MEIO_ESQUERDA, CENTRO,
TypeError: 'module' object is not callable
'''},