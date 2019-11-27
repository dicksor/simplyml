
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "ADD_OP ARRAY ARRAYHEADER ARRAYROW BULLETEDLIST COMP_OP FOR FROM IDENTIFIER IF MUL_OP NUMBER STRING TO WHILE programme : statement programme : statement ';' programme  statement : assignation \n        | structure \n        | function  structure : WHILE expression '{' programme '}'  structure : FOR IDENTIFIER FROM NUMBER TO NUMBER '{' programme '}'  structure : IF expression '{' programme '}'  structure : BULLETEDLIST '{' programme '}'  structure : ARRAY '{' programme '}'  structure : ARRAYHEADER '{' programme '}'  structure : ARRAYROW '{' programme '}'  expression : '(' expression ')'  expression : NUMBER \n        | STRING expression : IDENTIFIER expression : expression ADD_OP expression \n        | expression MUL_OP expression \n        | expression COMP_OP expression  assignation : IDENTIFIER '=' expression  parameter : expression \n        | expression ',' parameter  function : IDENTIFIER '(' parameter ')' "
    
_lr_action_items = {'IDENTIFIER':([0,7,8,9,14,15,16,18,24,25,26,27,32,33,34,35,38,44,61,],[6,21,22,21,6,21,21,21,6,6,6,6,6,21,21,21,6,21,6,]),'WHILE':([0,14,24,25,26,27,32,38,61,],[7,7,7,7,7,7,7,7,7,]),'FOR':([0,14,24,25,26,27,32,38,61,],[8,8,8,8,8,8,8,8,8,]),'IF':([0,14,24,25,26,27,32,38,61,],[9,9,9,9,9,9,9,9,9,]),'BULLETEDLIST':([0,14,24,25,26,27,32,38,61,],[10,10,10,10,10,10,10,10,10,]),'ARRAY':([0,14,24,25,26,27,32,38,61,],[11,11,11,11,11,11,11,11,11,]),'ARRAYHEADER':([0,14,24,25,26,27,32,38,61,],[12,12,12,12,12,12,12,12,12,]),'ARRAYROW':([0,14,24,25,26,27,32,38,61,],[13,13,13,13,13,13,13,13,13,]),'$end':([1,2,3,4,5,19,20,21,28,29,43,46,47,48,49,52,53,54,55,57,59,63,],[0,-1,-3,-4,-5,-14,-15,-16,-2,-20,-23,-17,-18,-19,-13,-9,-10,-11,-12,-6,-8,-7,]),'}':([2,3,4,5,19,20,21,28,29,39,40,41,42,43,45,46,47,48,49,51,52,53,54,55,57,59,62,63,],[-1,-3,-4,-5,-14,-15,-16,-2,-20,52,53,54,55,-23,57,-17,-18,-19,-13,59,-9,-10,-11,-12,-6,-8,63,-7,]),';':([2,3,4,5,19,20,21,29,43,46,47,48,49,52,53,54,55,57,59,63,],[14,-3,-4,-5,-14,-15,-16,-20,-23,-17,-18,-19,-13,-9,-10,-11,-12,-6,-8,-7,]),'=':([6,],[15,]),'(':([6,7,9,15,16,18,33,34,35,44,],[16,18,18,18,18,18,18,18,18,18,]),'NUMBER':([7,9,15,16,18,33,34,35,37,44,58,],[19,19,19,19,19,19,19,19,50,19,60,]),'STRING':([7,9,15,16,18,33,34,35,44,],[20,20,20,20,20,20,20,20,20,]),'{':([10,11,12,13,17,19,20,21,23,46,47,48,49,60,],[24,25,26,27,32,-14,-15,-16,38,-17,-18,-19,-13,61,]),'ADD_OP':([17,19,20,21,23,29,31,36,46,47,48,49,],[33,-14,-15,-16,33,33,33,33,33,33,33,-13,]),'MUL_OP':([17,19,20,21,23,29,31,36,46,47,48,49,],[34,-14,-15,-16,34,34,34,34,34,34,34,-13,]),'COMP_OP':([17,19,20,21,23,29,31,36,46,47,48,49,],[35,-14,-15,-16,35,35,35,35,35,35,35,-13,]),',':([19,20,21,31,46,47,48,49,],[-14,-15,-16,44,-17,-18,-19,-13,]),')':([19,20,21,30,31,36,46,47,48,49,56,],[-14,-15,-16,43,-21,49,-17,-18,-19,-13,-22,]),'FROM':([22,],[37,]),'TO':([50,],[58,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'programme':([0,14,24,25,26,27,32,38,61,],[1,28,39,40,41,42,45,51,62,]),'statement':([0,14,24,25,26,27,32,38,61,],[2,2,2,2,2,2,2,2,2,]),'assignation':([0,14,24,25,26,27,32,38,61,],[3,3,3,3,3,3,3,3,3,]),'structure':([0,14,24,25,26,27,32,38,61,],[4,4,4,4,4,4,4,4,4,]),'function':([0,14,24,25,26,27,32,38,61,],[5,5,5,5,5,5,5,5,5,]),'expression':([7,9,15,16,18,33,34,35,44,],[17,23,29,31,36,46,47,48,31,]),'parameter':([16,44,],[30,56,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> programme","S'",1,None,None,None),
  ('programme -> statement','programme',1,'p_programme_statement','parser_sml.py',7),
  ('programme -> statement ; programme','programme',3,'p_programme_recursive','parser_sml.py',11),
  ('statement -> assignation','statement',1,'p_statement','parser_sml.py',15),
  ('statement -> structure','statement',1,'p_statement','parser_sml.py',16),
  ('statement -> function','statement',1,'p_statement','parser_sml.py',17),
  ('structure -> WHILE expression { programme }','structure',5,'p_structure_while','parser_sml.py',21),
  ('structure -> FOR IDENTIFIER FROM NUMBER TO NUMBER { programme }','structure',9,'p_structure_for','parser_sml.py',25),
  ('structure -> IF expression { programme }','structure',5,'p_structure_if','parser_sml.py',36),
  ('structure -> BULLETEDLIST { programme }','structure',4,'p_structure_bulleted_list','parser_sml.py',40),
  ('structure -> ARRAY { programme }','structure',4,'p_structure_array','parser_sml.py',44),
  ('structure -> ARRAYHEADER { programme }','structure',4,'p_structure_array_header','parser_sml.py',48),
  ('structure -> ARRAYROW { programme }','structure',4,'p_structure_array_row','parser_sml.py',52),
  ('expression -> ( expression )','expression',3,'p_expression_paren','parser_sml.py',56),
  ('expression -> NUMBER','expression',1,'p_expression','parser_sml.py',60),
  ('expression -> STRING','expression',1,'p_expression','parser_sml.py',61),
  ('expression -> IDENTIFIER','expression',1,'p_expression_identifier','parser_sml.py',65),
  ('expression -> expression ADD_OP expression','expression',3,'p_expression_op','parser_sml.py',69),
  ('expression -> expression MUL_OP expression','expression',3,'p_expression_op','parser_sml.py',70),
  ('expression -> expression COMP_OP expression','expression',3,'p_expression_op','parser_sml.py',71),
  ('assignation -> IDENTIFIER = expression','assignation',3,'p_assign','parser_sml.py',75),
  ('parameter -> expression','parameter',1,'p_parameter','parser_sml.py',79),
  ('parameter -> expression , parameter','parameter',3,'p_parameter','parser_sml.py',80),
  ('function -> IDENTIFIER ( parameter )','function',4,'p_function','parser_sml.py',87),
]
