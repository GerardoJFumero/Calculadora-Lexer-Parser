
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftPLUSMINUSleftFACTORIALPLUSDIVIDErightUMINUSCALCULATE DIVIDE FACTORIAL FIN FLOAT INT LEFTBRA LEFTPAR MINUS MULTIPLY PLUS RIGHTBRA RIGHTPAR\n    expressions  : expression expressions\n                | expression \n                | empty\n    expression : CALCULATE LEFTBRA expression RIGHTBRA FIN\n    expression  : expression MULTIPLY expression\n                | expression DIVIDE expression \n                | expression PLUS expression\n                | expression MINUS expression \n                | FACTORIAL expression\n    \n    expression  : INT\n                | FLOAT \n    expression : MINUS expression %prec UMINUSexpression : LEFTPAR expression RIGHTPAR\n    empty : \n    '
    
_lr_action_items = {'CALCULATE':([0,2,5,6,7,8,9,11,12,13,14,15,16,17,19,20,21,22,24,25,27,28,],[4,4,4,4,-10,-11,4,4,4,4,4,4,-12,-9,-5,-6,-7,-8,4,-13,-8,-4,]),'FACTORIAL':([0,2,5,6,7,8,9,11,12,13,14,15,16,17,19,20,21,22,24,25,27,28,],[6,6,6,6,-10,-11,6,6,6,6,6,6,-12,-9,-5,-6,-7,-8,6,-13,-8,-4,]),'INT':([0,2,5,6,7,8,9,11,12,13,14,15,16,17,19,20,21,22,24,25,27,28,],[7,7,7,7,-10,-11,7,7,7,7,7,7,-12,-9,-5,-6,-7,-8,7,-13,-8,-4,]),'FLOAT':([0,2,5,6,7,8,9,11,12,13,14,15,16,17,19,20,21,22,24,25,27,28,],[8,8,8,8,-10,-11,8,8,8,8,8,8,-12,-9,-5,-6,-7,-8,8,-13,-8,-4,]),'MINUS':([0,2,5,6,7,8,9,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,27,28,],[5,14,5,5,-10,-11,5,5,5,5,5,5,-12,-9,24,24,-6,-7,-8,24,5,-13,-8,-4,]),'LEFTPAR':([0,2,5,6,7,8,9,11,12,13,14,15,16,17,19,20,21,22,24,25,27,28,],[9,9,9,9,-10,-11,9,9,9,9,9,9,-12,-9,-5,-6,-7,-8,9,-13,-8,-4,]),'$end':([0,1,2,3,7,8,10,16,17,19,20,21,22,25,27,28,],[-14,0,-2,-3,-10,-11,-1,-12,-9,-5,-6,-7,-8,-13,-8,-4,]),'MULTIPLY':([2,7,8,16,17,18,19,20,21,22,23,25,27,28,],[11,-10,-11,-12,-9,11,11,-6,-7,-8,11,-13,-8,-4,]),'DIVIDE':([2,7,8,16,17,18,19,20,21,22,23,25,27,28,],[12,-10,-11,-12,-9,12,12,-6,12,12,12,-13,12,-4,]),'PLUS':([2,7,8,16,17,18,19,20,21,22,23,25,27,28,],[13,-10,-11,-12,-9,13,13,-6,-7,-8,13,-13,-8,-4,]),'LEFTBRA':([4,],[15,]),'RIGHTPAR':([7,8,16,17,18,19,20,21,25,27,28,],[-10,-11,-12,-9,25,-5,-6,-7,-13,-8,-4,]),'RIGHTBRA':([7,8,16,17,19,20,21,23,25,27,28,],[-10,-11,-12,-9,-5,-6,-7,26,-13,-8,-4,]),'FIN':([26,],[28,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expressions':([0,2,],[1,10,]),'expression':([0,2,5,6,9,11,12,13,14,15,24,],[2,2,16,17,18,19,20,21,22,23,27,]),'empty':([0,2,],[3,3,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expressions","S'",1,None,None,None),
  ('expressions -> expression expressions','expressions',2,'p_calculat','Calculadora.py',94),
  ('expressions -> expression','expressions',1,'p_calculat','Calculadora.py',95),
  ('expressions -> empty','expressions',1,'p_calculat','Calculadora.py',96),
  ('expression -> CALCULATE LEFTBRA expression RIGHTBRA FIN','expression',5,'p_solutio','Calculadora.py',100),
  ('expression -> expression MULTIPLY expression','expression',3,'p_expression_solution','Calculadora.py',106),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression_solution','Calculadora.py',107),
  ('expression -> expression PLUS expression','expression',3,'p_expression_solution','Calculadora.py',108),
  ('expression -> expression MINUS expression','expression',3,'p_expression_solution','Calculadora.py',109),
  ('expression -> FACTORIAL expression','expression',2,'p_expression_solution','Calculadora.py',110),
  ('expression -> INT','expression',1,'p_expressions_int_floa','Calculadora.py',121),
  ('expression -> FLOAT','expression',1,'p_expressions_int_floa','Calculadora.py',122),
  ('expression -> MINUS expression','expression',2,'p_negativ','Calculadora.py',128),
  ('expression -> LEFTPAR expression RIGHTPAR','expression',3,'p_expressions_parenthesi','Calculadora.py',133),
  ('empty -> <empty>','empty',0,'p_empt','Calculadora.py',139),
]