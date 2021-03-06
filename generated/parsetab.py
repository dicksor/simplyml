
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "leftCOMP_OPleftADD_OPleftMUL_OPADD_OP BULLETEDLIST COMP_OP FOR FROM IDENTIFIER IF MUL_OP NUMBER STRING TABLE TABLEROW TO WHILE programme : statement programme : statement ';' programme  statement : assignation \n        | expression\n        | structure  structure : WHILE expression '{' programme '}'  structure : FOR IDENTIFIER FROM expression TO expression '{' programme '}'  structure : IF expression '{' programme '}'  structure : BULLETEDLIST '{' programme '}'  structure : TABLE '{' programme '}'  structure : TABLEROW '{' programme '}'  expression : '(' expression ')'  expression : NUMBER \n        | STRING\n        | array\n        | function  expression : IDENTIFIER  expression : expression ADD_OP expression \n        | expression MUL_OP expression \n        | expression COMP_OP expression  assignation : IDENTIFIER '=' expression  array : '[' parameter ']'  function : IDENTIFIER '(' parameter ')'  expression : IDENTIFIER '[' IDENTIFIER ']'  parameter : expression \n        | expression ',' parameter "
    
_lr_action_items = {'IDENTIFIER':([0,7,12,13,14,15,19,20,21,22,23,24,25,33,34,35,45,46,47,48,62,65,],[6,27,27,27,31,27,6,27,27,27,27,41,27,6,6,6,27,6,27,6,27,6,]),'(':([0,6,7,12,13,15,19,20,21,22,23,25,27,33,34,35,45,46,47,48,62,65,],[7,25,7,7,7,7,7,7,7,7,7,7,25,7,7,7,7,7,7,7,7,7,]),'NUMBER':([0,7,12,13,15,19,20,21,22,23,25,33,34,35,45,46,47,48,62,65,],[8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,]),'STRING':([0,7,12,13,15,19,20,21,22,23,25,33,34,35,45,46,47,48,62,65,],[9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,]),'WHILE':([0,19,33,34,35,46,48,65,],[13,13,13,13,13,13,13,13,]),'FOR':([0,19,33,34,35,46,48,65,],[14,14,14,14,14,14,14,14,]),'IF':([0,19,33,34,35,46,48,65,],[15,15,15,15,15,15,15,15,]),'BULLETEDLIST':([0,19,33,34,35,46,48,65,],[16,16,16,16,16,16,16,16,]),'TABLE':([0,19,33,34,35,46,48,65,],[17,17,17,17,17,17,17,17,]),'TABLEROW':([0,19,33,34,35,46,48,65,],[18,18,18,18,18,18,18,18,]),'[':([0,6,7,12,13,15,19,20,21,22,23,25,27,33,34,35,45,46,47,48,62,65,],[12,24,12,12,12,12,12,12,12,12,12,12,24,12,12,12,12,12,12,12,12,12,]),'$end':([1,2,3,4,5,6,8,9,10,11,27,36,37,38,39,40,43,44,52,53,58,59,60,61,63,67,],[0,-1,-3,-4,-5,-17,-13,-14,-15,-16,-17,-2,-18,-19,-20,-21,-12,-22,-24,-23,-9,-10,-11,-6,-8,-7,]),'}':([2,3,4,5,6,8,9,10,11,27,36,37,38,39,40,43,44,49,50,51,52,53,55,57,58,59,60,61,63,66,67,],[-1,-3,-4,-5,-17,-13,-14,-15,-16,-17,-2,-18,-19,-20,-21,-12,-22,58,59,60,-24,-23,61,63,-9,-10,-11,-6,-8,67,-7,]),';':([2,3,4,5,6,8,9,10,11,27,37,38,39,40,43,44,52,53,58,59,60,61,63,67,],[19,-3,-4,-5,-17,-13,-14,-15,-16,-17,-18,-19,-20,-21,-12,-22,-24,-23,-9,-10,-11,-6,-8,-7,]),'ADD_OP':([4,6,8,9,10,11,26,27,29,30,32,37,38,39,40,43,44,52,53,56,64,],[20,-17,-13,-14,-15,-16,20,-17,20,20,20,-18,-19,20,20,-12,-22,-24,-23,20,20,]),'MUL_OP':([4,6,8,9,10,11,26,27,29,30,32,37,38,39,40,43,44,52,53,56,64,],[21,-17,-13,-14,-15,-16,21,-17,21,21,21,21,-19,21,21,-12,-22,-24,-23,21,21,]),'COMP_OP':([4,6,8,9,10,11,26,27,29,30,32,37,38,39,40,43,44,52,53,56,64,],[22,-17,-13,-14,-15,-16,22,-17,22,22,22,-18,-19,-20,22,-12,-22,-24,-23,22,22,]),'=':([6,],[23,]),')':([8,9,10,11,26,27,29,37,38,39,42,43,44,52,53,54,],[-13,-14,-15,-16,43,-17,-25,-18,-19,-20,53,-12,-22,-24,-23,-26,]),',':([8,9,10,11,27,29,37,38,39,43,44,52,53,],[-13,-14,-15,-16,-17,45,-18,-19,-20,-12,-22,-24,-23,]),']':([8,9,10,11,27,28,29,37,38,39,41,43,44,52,53,54,],[-13,-14,-15,-16,-17,44,-25,-18,-19,-20,52,-12,-22,-24,-23,-26,]),'{':([8,9,10,11,16,17,18,27,30,32,37,38,39,43,44,52,53,64,],[-13,-14,-15,-16,33,34,35,-17,46,48,-18,-19,-20,-12,-22,-24,-23,65,]),'TO':([8,9,10,11,27,37,38,39,43,44,52,53,56,],[-13,-14,-15,-16,-17,-18,-19,-20,-12,-22,-24,-23,62,]),'FROM':([31,],[47,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'programme':([0,19,33,34,35,46,48,65,],[1,36,49,50,51,55,57,66,]),'statement':([0,19,33,34,35,46,48,65,],[2,2,2,2,2,2,2,2,]),'assignation':([0,19,33,34,35,46,48,65,],[3,3,3,3,3,3,3,3,]),'expression':([0,7,12,13,15,19,20,21,22,23,25,33,34,35,45,46,47,48,62,65,],[4,26,29,30,32,4,37,38,39,40,29,4,4,4,29,4,56,4,64,4,]),'structure':([0,19,33,34,35,46,48,65,],[5,5,5,5,5,5,5,5,]),'array':([0,7,12,13,15,19,20,21,22,23,25,33,34,35,45,46,47,48,62,65,],[10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,]),'function':([0,7,12,13,15,19,20,21,22,23,25,33,34,35,45,46,47,48,62,65,],[11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,]),'parameter':([12,25,45,],[28,42,54,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> programme","S'",1,None,None,None),
  ('programme -> statement','programme',1,'p_programme_statement','parser_sml.py',13),
  ('programme -> statement ; programme','programme',3,'p_programme_recursive','parser_sml.py',17),
  ('statement -> assignation','statement',1,'p_statement','parser_sml.py',21),
  ('statement -> expression','statement',1,'p_statement','parser_sml.py',22),
  ('statement -> structure','statement',1,'p_statement','parser_sml.py',23),
  ('structure -> WHILE expression { programme }','structure',5,'p_structure_while','parser_sml.py',27),
  ('structure -> FOR IDENTIFIER FROM expression TO expression { programme }','structure',9,'p_structure_for','parser_sml.py',31),
  ('structure -> IF expression { programme }','structure',5,'p_structure_if','parser_sml.py',48),
  ('structure -> BULLETEDLIST { programme }','structure',4,'p_structure_bulleted_list','parser_sml.py',52),
  ('structure -> TABLE { programme }','structure',4,'p_structure_table','parser_sml.py',56),
  ('structure -> TABLEROW { programme }','structure',4,'p_structure_table_row','parser_sml.py',60),
  ('expression -> ( expression )','expression',3,'p_expression_paren','parser_sml.py',64),
  ('expression -> NUMBER','expression',1,'p_expression','parser_sml.py',68),
  ('expression -> STRING','expression',1,'p_expression','parser_sml.py',69),
  ('expression -> array','expression',1,'p_expression','parser_sml.py',70),
  ('expression -> function','expression',1,'p_expression','parser_sml.py',71),
  ('expression -> IDENTIFIER','expression',1,'p_expression_identifier','parser_sml.py',81),
  ('expression -> expression ADD_OP expression','expression',3,'p_expression_op','parser_sml.py',85),
  ('expression -> expression MUL_OP expression','expression',3,'p_expression_op','parser_sml.py',86),
  ('expression -> expression COMP_OP expression','expression',3,'p_expression_op','parser_sml.py',87),
  ('assignation -> IDENTIFIER = expression','assignation',3,'p_assign','parser_sml.py',91),
  ('array -> [ parameter ]','array',3,'p_array','parser_sml.py',95),
  ('function -> IDENTIFIER ( parameter )','function',4,'p_function','parser_sml.py',99),
  ('expression -> IDENTIFIER [ IDENTIFIER ]','expression',4,'p_array_value','parser_sml.py',103),
  ('parameter -> expression','parameter',1,'p_parameter','parser_sml.py',109),
  ('parameter -> expression , parameter','parameter',3,'p_parameter','parser_sml.py',110),
]
