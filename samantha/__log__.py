
{'date': 'Tue Nov 19 2019 10:55:27.336 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 4
  def dragonballz()
                    ^
SyntaxError: invalid syntax
'''},
{'date': 'Tue Nov 19 2019 11:20:55.943 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
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
  module <module> line 15
    dragonballz()
  module <module> line 12
    	elemento_Battle.entra(Cena_Campo)
NameError: name 'elemento_Battle' is not defined
'''},