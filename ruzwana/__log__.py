
{'date': 'Thu Aug 08 2019 18:28:30.701 GMt-0300 (GMT-03:00) -X- SuPyGirls -X-',
'error': '''
RuntimeError: too much recursion
  module '$exec_514' line 30
Agenda()
'''},
{'date': 'Sat Oct 05 2019 17:24:09.618 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
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
  module <module> line 30
    Agenda()
  module <module> line 10
    self.menu()
  module <module> line 15
    self.consulta_numero()
  module <module> line 27
    self.tel = self.agenda[self.nome]
KeyError: isa
'''},