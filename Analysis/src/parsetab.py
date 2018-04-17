
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND ASSGN BOOL COLON COMMA CYCLE DECLARE DIVIDE DO DOT ELSE END EQ FLOAT FOR FUNCTION GRTR GRTREQ ID IF INT LEFTBRACK LEFTBRACK LEFTKEY LEFTPAR LESS LESSEQ MAIN MINUS MULTP NOTEQ NUMBER OR PROGRAM QUOTE READ RIGHTBRACK RIGHTKEY RIGHTPAR SEMICOLON SPACE STRING SUM TYPE VOID WHILE WRITE newlineprogram : PROGRAM createDirProc ID altaPrograma SEMICOLON program2 cuerpo END SEMICOLONcreateDirProc : altaPrograma : emptyprogram2 : declare program3declare : DECLARE declareRecursivo declareRecursivo : type ID altaVarGlobal declare2 declare3 SEMICOLON declareRecursivodeclare2 : arraydeclare3 : COMMA  ID altaVarGlobal declare3 program2 : emptyprogram3 : funct program3funct : FUNCTION type ID altaModulo LEFTPAR funct2  RIGHTPAR LEFTKEY est RIGHTKEYaltaModulo : funct2 : type ID funct3funct3 : COMMA funct type ID funct3funct2 : emptyfunct3 : emptyprogram3 : emptyaltaVarGlobal : declareRecursivo : emptydeclare : emptydeclare2 : emptydeclare3 : emptyarray : LEFTBRACK exp RIGHTBRACK arrayarray : emptytype : type2type2 : INTtype2 : FLOATtype2 : STRINGtype2 : BOOLtype2 : VOIDcuerpo : MAIN LEFTPAR RIGHTPAR LEFTKEY altaModuloMain  est RIGHTKEYaltaModuloMain : est : conditionalest : declareLocaldeclareLocal : DECLARE declareRecursivoLocal declareRecursivoLocal : type ID altaVarLocal declare2Local declare3Local SEMICOLON declareRecursivoLocaldeclare2Local : arraydeclare3Local : COMMA  ID altaVarLocal declare3Local declareRecursivoLocal : emptydeclareLocal : emptydeclare2Local : emptydeclare3Local : emptyaltaVarLocal : est : cyclesest : inputest : outputest : assignmentest : functest : emptyassignment : ID ASSGN ID SEMICOLONconditional : IF LEFTPAR conditional2 RIGHTPAR LEFTKEY est RIGHTKEY ELSE est RIGHTKEYconditional2 : exp conditional2conditional2 : emptycycles : whilecycles : forcycles : do-whiledo-while : DO LEFTKEY est RIGHTKEY WHILE LEFTPAR while2 RIGHTPARwhile : WHILE LEFTPAR while2 RIGHTPAR WHILE LEFTKEY est RIGHTKEYwhile2 : exp while2while2 : emptyfor : FOR LEFTPAR for2 SEMICOLON for3 SEMICOLON ID arithmeticOp arithmeticOp RIGHTPAR LEFTKEY est RIGHTKEYarithmeticOp : SUMarithmeticOp : MINUSfor2 : ID ASSGN ID for2for2 : emptyfor3 : exp for3for3 : emptyexp : ID array exp2 SEMICOLONexp2 : LESSexp2 : GRTRexp2 : EQexp2 : NOTEQexp2 : ANDexp2 : ORexp2 : arithmeticExparithmeticExp : ID EQ ID arithmeticOp ID arithmeticExparithmeticExp : emptyexp2 : emptyoutput : WRITE LEFTPAR output2 QUOTE exp QUOTE RIGHTPAR SEMICOLONoutput2 : ID output2output2 : emptyinput : READ LEFTPAR ID RIGHTPAR SEMICOLONempty :'
    
_lr_action_items = {'DO':([36,42,77,122,152,159,186,192,],[-32,49,49,49,49,49,49,49,]),'FLOAT':([9,23,48,62,72,140,156,175,],[17,17,17,17,17,17,-11,17,]),'LESS':([44,69,70,71,88,],[-83,-83,91,-24,-23,]),'READ':([36,42,77,122,152,159,186,192,],[-32,51,51,51,51,51,51,51,]),'VOID':([9,23,48,62,72,140,156,175,],[16,16,16,16,16,16,-11,16,]),'WHILE':([36,42,77,122,126,128,152,159,186,192,],[-32,53,53,53,141,143,53,53,53,53,]),'PROGRAM':([0,],[2,]),'RIGHTKEY':([36,42,50,52,54,55,56,57,59,62,64,65,66,67,68,77,84,86,103,122,134,139,142,152,156,159,167,171,175,180,181,183,185,186,189,191,192,193,194,],[-32,-83,-48,-33,-56,80,-55,-45,-47,-83,-44,-54,-40,-46,-34,-83,-35,-39,126,-83,-50,156,-82,-83,-11,-83,176,181,-83,-57,-58,-79,-36,-83,191,-51,-83,194,-61,]),'MINUS':([138,154,155,172,182,],[155,-62,-63,155,155,]),'SEMICOLON':([4,5,6,27,29,34,38,39,40,44,45,47,69,70,71,73,81,88,89,90,91,92,93,94,95,96,98,100,108,110,114,115,119,121,127,130,135,144,145,146,147,149,150,151,160,162,165,166,168,173,174,177,178,184,188,],[-83,7,-3,32,-18,-83,-83,-7,-21,-83,72,-22,-83,-83,-24,-18,-83,-23,-73,-75,-69,-72,119,-74,-70,-71,-77,-83,130,-65,134,-43,-68,-8,142,-83,-83,-83,161,-67,-83,-83,-37,-24,-66,-64,-42,175,-83,183,-43,-76,-77,-83,-38,]),'QUOTE':([82,111,112,113,119,133,148,],[-83,132,-83,-81,-68,-80,163,]),'RIGHTPAR':([28,48,74,76,79,87,102,104,105,106,107,116,117,118,119,123,125,129,136,154,155,158,163,169,170,179,187,],[33,-83,101,-15,-83,-83,-83,127,128,-83,-60,-53,-83,137,-68,-13,-16,-59,-52,-62,-63,-83,173,-83,180,-14,190,]),'NOTEQ':([44,69,70,71,88,],[-83,-83,92,-24,-23,]),'COMMA':([29,34,38,39,40,69,71,73,88,100,102,115,135,149,150,151,169,174,184,],[-18,-83,46,-7,-21,-83,-24,-18,-23,46,124,-43,-83,164,-37,-24,124,-43,164,]),'IF':([36,42,77,122,152,159,186,192,],[-32,63,63,63,63,63,63,63,]),'SUM':([138,154,155,172,182,],[154,-62,-63,154,154,]),'$end':([1,32,],[0,-1,]),'FUNCTION':([7,9,10,11,19,21,24,36,42,72,77,99,122,124,152,156,159,186,192,],[-83,-83,23,-20,-5,-19,23,-32,23,-83,23,-6,23,23,23,-11,23,23,23,]),'RIGHTBRACK':([43,119,],[69,-68,]),'END':([12,80,],[27,-31,]),'STRING':([9,23,48,62,72,140,156,175,],[14,14,14,14,14,14,-11,14,]),'FOR':([36,42,77,122,152,159,186,192,],[-32,58,58,58,58,58,58,58,]),'ELSE':([176,],[186,]),'WRITE':([36,42,77,122,152,159,186,192,],[-32,60,60,60,60,60,60,60,]),'GRTR':([44,69,70,71,88,],[-83,-83,95,-24,-23,]),'ID':([2,3,14,15,16,17,18,20,22,30,36,37,42,44,46,69,70,71,75,77,78,79,81,82,83,85,87,88,106,112,117,119,120,122,130,131,132,144,147,152,153,154,155,157,158,159,161,164,168,186,192,],[-2,4,-28,-26,-30,-27,-29,29,-25,35,-32,44,61,-83,73,-83,97,-24,102,61,104,44,109,112,114,115,44,-23,44,112,44,-68,138,61,44,147,44,44,109,61,168,-62,-63,169,44,61,172,174,97,61,61,]),'EQ':([44,69,70,71,88,97,],[-83,-83,96,-24,-23,120,]),'DECLARE':([7,36,42,77,122,152,159,186,192,],[9,-32,62,62,62,62,62,62,62,]),'LEFTKEY':([33,49,101,137,143,190,],[36,77,122,152,159,192,]),'AND':([44,69,70,71,88,],[-83,-83,89,-24,-23,]),'ASSGN':([61,109,],[83,131,]),'INT':([9,23,48,62,72,140,156,175,],[15,15,15,15,15,15,-11,15,]),'LEFTBRACK':([29,34,44,69,115,135,],[-18,37,37,37,-43,37,]),'LEFTPAR':([13,35,41,51,53,58,60,63,141,],[28,-12,48,78,79,81,82,87,158,]),'BOOL':([9,23,48,62,72,140,156,175,],[18,18,18,18,18,18,-11,18,]),'MAIN':([7,8,9,10,11,19,21,24,25,26,31,72,99,156,],[-83,13,-83,-83,-9,-5,-19,-83,-4,-17,-10,-83,-6,-11,]),'OR':([44,69,70,71,88,],[-83,-83,94,-24,-23,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'funct':([10,24,42,77,122,124,152,159,186,192,],[24,24,50,50,50,140,50,50,50,50,]),'output2':([82,112,],[111,133,]),'conditional':([42,77,122,152,159,186,192,],[52,52,52,52,52,52,52,]),'for3':([130,144,],[145,160,]),'while2':([79,106,158,],[105,129,170,]),'do-while':([42,77,122,152,159,186,192,],[54,54,54,54,54,54,54,]),'declareRecursivoLocal':([62,175,],[84,185,]),'for2':([81,147,],[108,162,]),'array':([34,44,69,135,],[39,70,88,150,]),'altaVarGlobal':([29,73,],[34,100,]),'arithmeticOp':([138,172,182,],[153,182,187,]),'type2':([9,23,48,62,72,140,175,],[22,22,22,22,22,22,22,]),'est':([42,77,122,152,159,186,192,],[55,103,139,167,171,189,193,]),'arithmeticExp':([70,168,],[90,177,]),'for':([42,77,122,152,159,186,192,],[56,56,56,56,56,56,56,]),'program3':([10,24,],[25,31,]),'exp2':([70,],[93,]),'funct2':([48,],[74,]),'program':([0,],[1,]),'input':([42,77,122,152,159,186,192,],[57,57,57,57,57,57,57,]),'type':([9,23,48,62,72,140,175,],[20,30,75,85,20,157,85,]),'empty':([4,7,9,10,24,34,38,42,44,48,62,69,70,72,77,79,81,82,87,100,102,106,112,117,122,130,135,144,147,149,152,158,159,168,169,175,184,186,192,],[6,11,21,26,26,40,47,66,71,76,86,71,98,21,66,107,110,113,116,47,125,107,113,116,66,146,151,146,110,165,66,107,66,178,125,86,165,66,66,]),'funct3':([102,169,],[123,179,]),'declare2Local':([135,],[149,]),'assignment':([42,77,122,152,159,186,192,],[59,59,59,59,59,59,59,]),'cuerpo':([8,],[12,]),'altaVarLocal':([115,174,],[135,184,]),'declare2':([34,],[38,]),'declare3':([38,100,],[45,121,]),'declare3Local':([149,184,],[166,188,]),'cycles':([42,77,122,152,159,186,192,],[64,64,64,64,64,64,64,]),'program2':([7,],[8,]),'createDirProc':([2,],[3,]),'altaModuloMain':([36,],[42,]),'altaModulo':([35,],[41,]),'while':([42,77,122,152,159,186,192,],[65,65,65,65,65,65,65,]),'altaPrograma':([4,],[5,]),'declareRecursivo':([9,72,],[19,99,]),'conditional2':([87,117,],[118,136,]),'exp':([37,79,87,106,117,130,132,144,158,],[43,106,117,106,117,144,148,144,106,]),'output':([42,77,122,152,159,186,192,],[67,67,67,67,67,67,67,]),'declareLocal':([42,77,122,152,159,186,192,],[68,68,68,68,68,68,68,]),'declare':([7,],[10,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> PROGRAM createDirProc ID altaPrograma SEMICOLON program2 cuerpo END SEMICOLON','program',9,'p_program','parser.py',31),
  ('createDirProc -> <empty>','createDirProc',0,'p_createDirProc','parser.py',35),
  ('altaPrograma -> empty','altaPrograma',1,'p_altaPrograma','parser.py',38),
  ('program2 -> declare program3','program2',2,'p_program2','parser.py',49),
  ('declare -> DECLARE declareRecursivo','declare',2,'p_declare','parser.py',53),
  ('declareRecursivo -> type ID altaVarGlobal declare2 declare3 SEMICOLON declareRecursivo','declareRecursivo',7,'p_declareRecursivo','parser.py',57),
  ('declare2 -> array','declare2',1,'p_declare2','parser.py',61),
  ('declare3 -> COMMA ID altaVarGlobal declare3','declare3',4,'p_declare3','parser.py',65),
  ('program2 -> empty','program2',1,'p_program2Empty','parser.py',69),
  ('program3 -> funct program3','program3',2,'p_program3','parser.py',73),
  ('funct -> FUNCTION type ID altaModulo LEFTPAR funct2 RIGHTPAR LEFTKEY est RIGHTKEY','funct',10,'p_funct','parser.py',77),
  ('altaModulo -> <empty>','altaModulo',0,'p_altaModulo','parser.py',81),
  ('funct2 -> type ID funct3','funct2',3,'p_funct2','parser.py',91),
  ('funct3 -> COMMA funct type ID funct3','funct3',5,'p_funct3','parser.py',95),
  ('funct2 -> empty','funct2',1,'p_funct2Empty','parser.py',99),
  ('funct3 -> empty','funct3',1,'p_funct3Empty','parser.py',103),
  ('program3 -> empty','program3',1,'p_program3Empty','parser.py',116),
  ('altaVarGlobal -> <empty>','altaVarGlobal',0,'p_altaVarGlobal','parser.py',121),
  ('declareRecursivo -> empty','declareRecursivo',1,'p_declareResursivoEmpty','parser.py',132),
  ('declare -> empty','declare',1,'p_declareEmpty','parser.py',136),
  ('declare2 -> empty','declare2',1,'p_declar2Empty','parser.py',141),
  ('declare3 -> empty','declare3',1,'p_declare3Empty','parser.py',146),
  ('array -> LEFTBRACK exp RIGHTBRACK array','array',4,'p_array','parser.py',150),
  ('array -> empty','array',1,'p_arrayEmpty','parser.py',154),
  ('type -> type2','type',1,'p_type','parser.py',158),
  ('type2 -> INT','type2',1,'p_type2','parser.py',162),
  ('type2 -> FLOAT','type2',1,'p_type2Float','parser.py',168),
  ('type2 -> STRING','type2',1,'p_type2String','parser.py',174),
  ('type2 -> BOOL','type2',1,'p_type2Bool','parser.py',180),
  ('type2 -> VOID','type2',1,'p_type2Void','parser.py',186),
  ('cuerpo -> MAIN LEFTPAR RIGHTPAR LEFTKEY altaModuloMain est RIGHTKEY','cuerpo',7,'p_cuerpo','parser.py',192),
  ('altaModuloMain -> <empty>','altaModuloMain',0,'p_altaModuloMain','parser.py',196),
  ('est -> conditional','est',1,'p_est','parser.py',206),
  ('est -> declareLocal','est',1,'p_estVars','parser.py',210),
  ('declareLocal -> DECLARE declareRecursivoLocal','declareLocal',2,'p_declareLocal','parser.py',214),
  ('declareRecursivoLocal -> type ID altaVarLocal declare2Local declare3Local SEMICOLON declareRecursivoLocal','declareRecursivoLocal',7,'p_declareRecursivoLocal','parser.py',218),
  ('declare2Local -> array','declare2Local',1,'p_declare2Local','parser.py',222),
  ('declare3Local -> COMMA ID altaVarLocal declare3Local','declare3Local',4,'p_declare3Local','parser.py',226),
  ('declareRecursivoLocal -> empty','declareRecursivoLocal',1,'p_declareResursivoEmptyLocal','parser.py',230),
  ('declareLocal -> empty','declareLocal',1,'p_declareEmptyLocal','parser.py',234),
  ('declare2Local -> empty','declare2Local',1,'p_declar2EmptyLocal','parser.py',239),
  ('declare3Local -> empty','declare3Local',1,'p_declare3EmptyLocal','parser.py',244),
  ('altaVarLocal -> <empty>','altaVarLocal',0,'p_altaVarLocal','parser.py',249),
  ('est -> cycles','est',1,'p_estCycle','parser.py',258),
  ('est -> input','est',1,'p_estRead','parser.py',262),
  ('est -> output','est',1,'p_estWrite','parser.py',266),
  ('est -> assignment','est',1,'p_estAassignment','parser.py',270),
  ('est -> funct','est',1,'p_estFunct','parser.py',274),
  ('est -> empty','est',1,'p_estEmpty','parser.py',278),
  ('assignment -> ID ASSGN ID SEMICOLON','assignment',4,'p_assignment','parser.py',282),
  ('conditional -> IF LEFTPAR conditional2 RIGHTPAR LEFTKEY est RIGHTKEY ELSE est RIGHTKEY','conditional',10,'p_conditional','parser.py',286),
  ('conditional2 -> exp conditional2','conditional2',2,'p_conditional2','parser.py',290),
  ('conditional2 -> empty','conditional2',1,'p_conditional2Empty','parser.py',294),
  ('cycles -> while','cycles',1,'p_cycles','parser.py',298),
  ('cycles -> for','cycles',1,'p_cyclesFor','parser.py',302),
  ('cycles -> do-while','cycles',1,'p_cyclesDoWhile','parser.py',306),
  ('do-while -> DO LEFTKEY est RIGHTKEY WHILE LEFTPAR while2 RIGHTPAR','do-while',8,'p_doWhile','parser.py',310),
  ('while -> WHILE LEFTPAR while2 RIGHTPAR WHILE LEFTKEY est RIGHTKEY','while',8,'p_whileClass','parser.py',314),
  ('while2 -> exp while2','while2',2,'p_while2','parser.py',318),
  ('while2 -> empty','while2',1,'p_while2Empty','parser.py',322),
  ('for -> FOR LEFTPAR for2 SEMICOLON for3 SEMICOLON ID arithmeticOp arithmeticOp RIGHTPAR LEFTKEY est RIGHTKEY','for',13,'p_forClass','parser.py',326),
  ('arithmeticOp -> SUM','arithmeticOp',1,'p_arithmeticOpPlus','parser.py',330),
  ('arithmeticOp -> MINUS','arithmeticOp',1,'p_arithmeticOpMinus','parser.py',334),
  ('for2 -> ID ASSGN ID for2','for2',4,'p_for2','parser.py',340),
  ('for2 -> empty','for2',1,'p_for2empty','parser.py',344),
  ('for3 -> exp for3','for3',2,'p_for3','parser.py',348),
  ('for3 -> empty','for3',1,'p_for3empty','parser.py',352),
  ('exp -> ID array exp2 SEMICOLON','exp',4,'p_exp','parser.py',356),
  ('exp2 -> LESS','exp2',1,'p_exp2','parser.py',360),
  ('exp2 -> GRTR','exp2',1,'p_expr2Grtr','parser.py',364),
  ('exp2 -> EQ','exp2',1,'p_exp2Equal','parser.py',369),
  ('exp2 -> NOTEQ','exp2',1,'p_exp2NotEq','parser.py',373),
  ('exp2 -> AND','exp2',1,'p_exp2And','parser.py',377),
  ('exp2 -> OR','exp2',1,'p_exp2OR','parser.py',381),
  ('exp2 -> arithmeticExp','exp2',1,'p_exp2Arithemti','parser.py',385),
  ('arithmeticExp -> ID EQ ID arithmeticOp ID arithmeticExp','arithmeticExp',6,'p_arithmeticExp','parser.py',389),
  ('arithmeticExp -> empty','arithmeticExp',1,'p_arithmeticExpEmpty','parser.py',393),
  ('exp2 -> empty','exp2',1,'p_exp2Empty','parser.py',397),
  ('output -> WRITE LEFTPAR output2 QUOTE exp QUOTE RIGHTPAR SEMICOLON','output',8,'p_output','parser.py',401),
  ('output2 -> ID output2','output2',2,'p_output2','parser.py',405),
  ('output2 -> empty','output2',1,'p_output2Empty','parser.py',409),
  ('input -> READ LEFTPAR ID RIGHTPAR SEMICOLON','input',5,'p_input','parser.py',413),
  ('empty -> <empty>','empty',0,'p_empty','parser.py',418),
]
