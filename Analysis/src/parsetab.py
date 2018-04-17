
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND ASSGN BOOL COLON COMMA CYCLE DECLARE DIVIDE DO DOT ELSE END EQ FLOAT FOR FUNCTION GRTR GRTREQ ID IF INT LEFTBRACK LEFTBRACK LEFTKEY LEFTPAR LESS LESSEQ MAIN MINUS MULTP NOTEQ NUMBER OR PROGRAM QUOTE READ RIGHTBRACK RIGHTKEY RIGHTPAR SEMICOLON SPACE STRING SUM TYPE VOID WHILE WRITE newlineprogram : PROGRAM ID  SEMICOLON program2 cuerpo END SEMICOLONprogram2 : declare program3program2 : emptyprogram3 : funct program3program3 : emptydeclare : DECLARE declareRecursivo declareRecursivo : type ID declare2 declare3 SEMICOLON declareRecursivodeclareRecursivo : emptydeclare : emptydeclare2 : arraydeclare2 : emptydeclare3 : COMMA  ID declare3 declare3 : emptyarray : LEFTBRACK exp RIGHTBRACK arrayarray : emptytype : type2type2 : INTtype2 : FLOATtype2 : STRINGtype2 : BOOLtype2 : VOIDcuerpo : MAIN LEFTPAR RIGHTPAR LEFTKEY cuerpo2 est RIGHTKEYcuerpo2 : cuerpocuerpo2 : emptyest : conditionalest : cyclesest : inputest : outputest : assignmentest : functest : emptyassignment : ID ASSGN ID SEMICOLONconditional : IF LEFTPAR conditional2 RIGHTPAR LEFTKEY est RIGHTKEY ELSE est RIGHTKEYconditional2 : exp conditional2conditional2 : emptycycles : whilecycles : forcycles : do-whiledo-while : DO LEFTKEY est RIGHTKEY WHILE LEFTPAR while2 RIGHTPARwhile : WHILE LEFTPAR while2 RIGHTPAR WHILE LEFTKEY est RIGHTKEYwhile2 : exp while2while2 : emptyfor : FOR LEFTPAR for2 SEMICOLON for3 SEMICOLON ID arithmeticOp arithmeticOp RIGHTPAR LEFTKEY est RIGHTKEYarithmeticOp : SUMarithmeticOp : MINUSfor2 : ID ASSGN ID for2for2 : emptyfor3 : exp for3for3 : emptyexp : ID array exp2 SEMICOLONexp2 : LESSexp2 : GRTRexp2 : EQexp2 : NOTEQexp2 : ANDexp2 : ORexp2 : arithmeticExparithmeticExp : ID EQ ID arithmeticOp ID arithmeticExparithmeticExp : emptyexp2 : emptyoutput : WRITE LEFTPAR output2 QUOTE exp QUOTE RIGHTPAR SEMICOLONoutput2 : ID output2output2 : emptyinput : READ LEFTPAR ID RIGHTPAR SEMICOLONfunct : FUNCTION type ID LEFTPAR type ID funct2 RIGHTPAR LEFTKEY est RIGHTKEYfunct2 : COMMA funct type ID funct2funct2 : emptyempty :'
    
_lr_action_items = {'DO':([36,43,44,45,84,87,129,139,144,163,168,],[-68,-23,52,-24,52,-22,52,52,52,52,52,]),'FLOAT':([6,20,42,49,114,152,],[14,14,14,14,14,-65,]),'LESS':([38,46,47,48,70,],[-68,-68,73,-15,-14,]),'READ':([36,43,44,45,84,87,129,139,144,163,168,],[-68,-23,54,-24,54,-22,54,54,54,54,54,]),'VOID':([6,20,42,49,114,152,],[13,13,13,13,13,-65,]),'WHILE':([36,43,44,45,84,87,115,117,129,139,144,163,168,],[-68,-23,56,-24,56,-22,131,133,56,56,56,56,56,]),'PROGRAM':([0,],[2,]),'RIGHTKEY':([36,43,44,45,53,55,57,58,59,60,62,66,67,68,69,84,87,97,123,129,132,139,141,144,149,152,155,159,160,162,163,165,167,168,169,170,],[-68,-23,-68,-24,-30,-25,-38,87,-37,-27,-29,-36,-31,-28,-26,-68,-22,115,-32,-68,-64,-68,152,-68,158,-65,160,-39,-40,-61,-68,167,-33,-68,170,-43,]),'MINUS':([112,127,128,156,161,],[128,-44,-45,128,128,]),'SEMICOLON':([3,24,26,32,33,34,38,39,41,46,47,48,50,70,71,72,73,74,75,76,77,78,80,82,88,92,102,104,108,116,119,134,135,136,137,140,145,147,150,151,157,],[4,29,-68,-68,-10,-11,-68,49,-13,-68,-68,-15,-68,-14,-55,-57,-51,-54,92,-56,-52,-53,-59,-12,-68,-50,119,-47,123,132,-68,-68,146,-49,-68,-68,-48,-46,-58,-59,162,]),'QUOTE':([89,92,105,106,107,122,138,],[-68,-50,121,-68,-63,-62,148,]),'RIGHTPAR':([25,83,86,91,92,94,96,98,99,100,101,109,110,111,118,124,127,128,142,143,148,153,154,164,],[30,-68,-68,-68,-50,113,-67,116,117,-68,-42,-35,-68,125,-41,-34,-44,-45,-68,-68,157,-66,159,166,]),'NOTEQ':([38,46,47,48,70,],[-68,-68,74,-15,-14,]),'COMMA':([26,32,33,34,46,48,50,70,83,142,],[-68,40,-10,-11,-68,-15,40,-14,95,95,]),'IF':([36,43,44,45,84,87,129,139,144,163,168,],[-68,-23,65,-24,65,-22,65,65,65,65,65,]),'SUM':([112,127,128,156,161,],[127,-44,-45,127,127,]),'$end':([1,29,],[0,-1,]),'FUNCTION':([4,6,7,8,16,18,21,36,43,44,45,49,81,84,87,95,129,139,144,152,163,168,],[-68,-68,20,-9,-6,-8,20,-68,-23,20,-24,-68,-7,20,-22,20,20,20,20,-65,20,20,]),'RIGHTBRACK':([37,92,],[46,-50,]),'END':([9,87,],[24,-22,]),'STRING':([6,20,42,49,114,152,],[11,11,11,11,11,-65,]),'FOR':([36,43,44,45,84,87,129,139,144,163,168,],[-68,-23,61,-24,61,-22,61,61,61,61,61,]),'ELSE':([158,],[163,]),'WRITE':([36,43,44,45,84,87,129,139,144,163,168,],[-68,-23,63,-24,63,-22,63,63,63,63,63,]),'GRTR':([38,46,47,48,70,],[-68,-68,77,-15,-14,]),'ID':([2,11,12,13,14,15,17,19,27,31,36,38,40,43,44,45,46,47,48,51,70,84,85,86,87,88,89,90,91,92,93,100,106,110,119,120,121,126,127,128,129,130,134,137,139,140,143,144,146,163,168,],[3,-19,-17,-21,-18,-20,26,-16,35,38,-68,-68,50,-23,64,-24,-68,79,-15,83,-14,64,98,38,-22,103,106,108,38,-50,112,38,106,38,38,137,38,140,-44,-45,64,142,38,103,64,79,38,64,156,64,64,]),'EQ':([38,46,47,48,70,79,],[-68,-68,78,-15,-14,93,]),'DECLARE':([4,],[6,]),'LEFTKEY':([30,52,113,125,133,166,],[36,84,129,139,144,168,]),'AND':([38,46,47,48,70,],[-68,-68,71,-15,-14,]),'ASSGN':([64,103,],[90,120,]),'INT':([6,20,42,49,114,152,],[12,12,12,12,12,-65,]),'LEFTBRACK':([26,38,46,],[31,31,31,]),'LEFTPAR':([10,35,54,56,61,63,65,131,],[25,42,85,86,88,89,91,143,]),'BOOL':([6,20,42,49,114,152,],[15,15,15,15,15,-65,]),'MAIN':([4,5,6,7,8,16,18,21,22,23,28,36,49,81,152,],[-68,10,-68,-68,-3,-6,-8,-68,-2,-5,-4,10,-68,-7,-65,]),'OR':([38,46,47,48,70,],[-68,-68,76,-15,-14,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'funct':([7,21,44,84,95,129,139,144,163,168,],[21,21,53,53,114,53,53,53,53,53,]),'output2':([89,106,],[105,122,]),'conditional':([44,84,129,139,144,163,168,],[55,55,55,55,55,55,55,]),'while2':([86,100,143,],[99,118,154,]),'do-while':([44,84,129,139,144,163,168,],[57,57,57,57,57,57,57,]),'for3':([119,134,],[135,145,]),'for2':([88,137,],[102,147,]),'array':([26,38,46,],[33,47,70,]),'type2':([6,20,42,49,114,],[19,19,19,19,19,]),'est':([44,84,129,139,144,163,168,],[58,97,141,149,155,165,169,]),'arithmeticExp':([47,140,],[72,150,]),'for':([44,84,129,139,144,163,168,],[59,59,59,59,59,59,59,]),'program3':([7,21,],[22,28,]),'exp2':([47,],[75,]),'funct2':([83,142,],[94,153,]),'program':([0,],[1,]),'cuerpo2':([36,],[44,]),'input':([44,84,129,139,144,163,168,],[60,60,60,60,60,60,60,]),'type':([6,20,42,49,114,],[17,27,51,17,130,]),'empty':([4,6,7,21,26,32,36,38,44,46,47,49,50,83,84,86,88,89,91,100,106,110,119,129,134,137,139,140,142,143,144,163,168,],[8,18,23,23,34,41,45,48,67,48,80,18,41,96,67,101,104,107,109,101,107,109,136,67,136,104,67,151,96,101,67,67,67,]),'arithmeticOp':([112,156,161,],[126,161,164,]),'assignment':([44,84,129,139,144,163,168,],[62,62,62,62,62,62,62,]),'cuerpo':([5,36,],[9,43,]),'declare2':([26,],[32,]),'declare3':([32,50,],[39,82,]),'program2':([4,],[5,]),'while':([44,84,129,139,144,163,168,],[66,66,66,66,66,66,66,]),'declareRecursivo':([6,49,],[16,81,]),'conditional2':([91,110,],[111,124,]),'exp':([31,86,91,100,110,119,121,134,143,],[37,100,110,100,110,134,138,134,100,]),'output':([44,84,129,139,144,163,168,],[68,68,68,68,68,68,68,]),'cycles':([44,84,129,139,144,163,168,],[69,69,69,69,69,69,69,]),'declare':([4,],[7,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> PROGRAM ID SEMICOLON program2 cuerpo END SEMICOLON','program',7,'p_program','parser.py',24),
  ('program2 -> declare program3','program2',2,'p_program2','parser.py',29),
  ('program2 -> empty','program2',1,'p_program2Empty','parser.py',34),
  ('program3 -> funct program3','program3',2,'p_program3','parser.py',39),
  ('program3 -> empty','program3',1,'p_program3Empty','parser.py',44),
  ('declare -> DECLARE declareRecursivo','declare',2,'p_declare','parser.py',49),
  ('declareRecursivo -> type ID declare2 declare3 SEMICOLON declareRecursivo','declareRecursivo',6,'p_declareRecursivo','parser.py',54),
  ('declareRecursivo -> empty','declareRecursivo',1,'p_declareResursivoEmpty','parser.py',59),
  ('declare -> empty','declare',1,'p_declareEmpty','parser.py',64),
  ('declare2 -> array','declare2',1,'p_declare2','parser.py',69),
  ('declare2 -> empty','declare2',1,'p_declar2Empty','parser.py',74),
  ('declare3 -> COMMA ID declare3','declare3',3,'p_declare3','parser.py',79),
  ('declare3 -> empty','declare3',1,'p_declare3Empty','parser.py',84),
  ('array -> LEFTBRACK exp RIGHTBRACK array','array',4,'p_array','parser.py',89),
  ('array -> empty','array',1,'p_arrayEmpty','parser.py',94),
  ('type -> type2','type',1,'p_type','parser.py',99),
  ('type2 -> INT','type2',1,'p_type2','parser.py',104),
  ('type2 -> FLOAT','type2',1,'p_type2Float','parser.py',109),
  ('type2 -> STRING','type2',1,'p_type2String','parser.py',114),
  ('type2 -> BOOL','type2',1,'p_type2Bool','parser.py',119),
  ('type2 -> VOID','type2',1,'p_type2Void','parser.py',124),
  ('cuerpo -> MAIN LEFTPAR RIGHTPAR LEFTKEY cuerpo2 est RIGHTKEY','cuerpo',7,'p_cuerpo','parser.py',129),
  ('cuerpo2 -> cuerpo','cuerpo2',1,'p_cuerpo2','parser.py',134),
  ('cuerpo2 -> empty','cuerpo2',1,'p_cuerpo2Empty','parser.py',139),
  ('est -> conditional','est',1,'p_est','parser.py',144),
  ('est -> cycles','est',1,'p_estCycle','parser.py',149),
  ('est -> input','est',1,'p_estRead','parser.py',154),
  ('est -> output','est',1,'p_estWrite','parser.py',159),
  ('est -> assignment','est',1,'p_estAassignment','parser.py',164),
  ('est -> funct','est',1,'p_estFunct','parser.py',169),
  ('est -> empty','est',1,'p_estEmpty','parser.py',173),
  ('assignment -> ID ASSGN ID SEMICOLON','assignment',4,'p_assignment','parser.py',178),
  ('conditional -> IF LEFTPAR conditional2 RIGHTPAR LEFTKEY est RIGHTKEY ELSE est RIGHTKEY','conditional',10,'p_conditional','parser.py',183),
  ('conditional2 -> exp conditional2','conditional2',2,'p_conditional2','parser.py',188),
  ('conditional2 -> empty','conditional2',1,'p_conditional2Empty','parser.py',193),
  ('cycles -> while','cycles',1,'p_cycles','parser.py',198),
  ('cycles -> for','cycles',1,'p_cyclesFor','parser.py',203),
  ('cycles -> do-while','cycles',1,'p_cyclesDoWhile','parser.py',208),
  ('do-while -> DO LEFTKEY est RIGHTKEY WHILE LEFTPAR while2 RIGHTPAR','do-while',8,'p_doWhile','parser.py',213),
  ('while -> WHILE LEFTPAR while2 RIGHTPAR WHILE LEFTKEY est RIGHTKEY','while',8,'p_whileClass','parser.py',217),
  ('while2 -> exp while2','while2',2,'p_while2','parser.py',222),
  ('while2 -> empty','while2',1,'p_while2Empty','parser.py',227),
  ('for -> FOR LEFTPAR for2 SEMICOLON for3 SEMICOLON ID arithmeticOp arithmeticOp RIGHTPAR LEFTKEY est RIGHTKEY','for',13,'p_forClass','parser.py',232),
  ('arithmeticOp -> SUM','arithmeticOp',1,'p_arithmeticOpPlus','parser.py',237),
  ('arithmeticOp -> MINUS','arithmeticOp',1,'p_arithmeticOpMinus','parser.py',242),
  ('for2 -> ID ASSGN ID for2','for2',4,'p_for2','parser.py',249),
  ('for2 -> empty','for2',1,'p_for2empty','parser.py',254),
  ('for3 -> exp for3','for3',2,'p_for3','parser.py',259),
  ('for3 -> empty','for3',1,'p_for3empty','parser.py',264),
  ('exp -> ID array exp2 SEMICOLON','exp',4,'p_exp','parser.py',269),
  ('exp2 -> LESS','exp2',1,'p_exp2','parser.py',274),
  ('exp2 -> GRTR','exp2',1,'p_expr2Grtr','parser.py',279),
  ('exp2 -> EQ','exp2',1,'p_exp2Equal','parser.py',285),
  ('exp2 -> NOTEQ','exp2',1,'p_exp2NotEq','parser.py',290),
  ('exp2 -> AND','exp2',1,'p_exp2And','parser.py',295),
  ('exp2 -> OR','exp2',1,'p_exp2OR','parser.py',300),
  ('exp2 -> arithmeticExp','exp2',1,'p_exp2Arithemti','parser.py',305),
  ('arithmeticExp -> ID EQ ID arithmeticOp ID arithmeticExp','arithmeticExp',6,'p_arithmeticExp','parser.py',310),
  ('arithmeticExp -> empty','arithmeticExp',1,'p_arithmeticExpEmpty','parser.py',315),
  ('exp2 -> empty','exp2',1,'p_exp2Empty','parser.py',320),
  ('output -> WRITE LEFTPAR output2 QUOTE exp QUOTE RIGHTPAR SEMICOLON','output',8,'p_output','parser.py',325),
  ('output2 -> ID output2','output2',2,'p_output2','parser.py',330),
  ('output2 -> empty','output2',1,'p_output2Empty','parser.py',335),
  ('input -> READ LEFTPAR ID RIGHTPAR SEMICOLON','input',5,'p_input','parser.py',340),
  ('funct -> FUNCTION type ID LEFTPAR type ID funct2 RIGHTPAR LEFTKEY est RIGHTKEY','funct',11,'p_funct','parser.py',345),
  ('funct2 -> COMMA funct type ID funct2','funct2',5,'p_funct2','parser.py',350),
  ('funct2 -> empty','funct2',1,'p_funct2Empty','parser.py',355),
  ('empty -> <empty>','empty',0,'p_empty','parser.py',360),
]
