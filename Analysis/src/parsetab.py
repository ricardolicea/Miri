
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND ASSGN BOOL COLON COMMA CYCLE DECLARE DIVIDE DO DOT ELSE END EQ FLOAT FLOATNUMB FOR FUNCTION GRTR GRTREQ ID IF INT INTEGER LEFTBRACK LEFTBRACK LEFTKEY LEFTPAR LESS LESSEQ MAIN MINUS MULTP NOTEQ NUMBER OR PROGRAM QUOTE READ RETURN RIGHTBRACK RIGHTKEY RIGHTPAR SEMICOLON SPACE STRING SUM TYPE VOID WHILE WRITE newlineprogram : PROGRAM ID altaPrograma SEMICOLON program2 goToMainQuad cuerpo END SEMICOLONgoToMainQuad : altaPrograma : program2 : declare program3program2 : emptydeclare : DECLARE declareRecursivo declare : emptydeclareRecursivo : type ID altaVarGlobal assignmentDecl declare2 declare3 SEMICOLON declareRecursivodeclare2 : arraydeclare3 : COMMA  ID altaVarGlobal declare3 program3 : funct program3funct : FUNCTION type ID altaModulo LEFTPAR funct2  RIGHTPAR LEFTKEY est functReturn RIGHTKEYfunctReturn : RETURN NUMBER SEMICOLONfunctReturn : RETURN ID SEMICOLONfunctReturn : emptyaltaModulo : funct2 : type ID altaVarLocal funct3funct3 : COMMA type ID  altaVarLocal funct3funct2 : emptyfunct3 : emptyprogram3 : emptyaltaVarGlobal : declareRecursivo : emptydeclare3 : emptyarray : LEFTBRACK exp RIGHTBRACK arrayarray : emptytype : type2type2 : INTtype2 : FLOATtype2 : STRINGtype2 : BOOLtype2 : VOIDcuerpo : MAIN LEFTPAR RIGHTPAR LEFTKEY altaModuloMain est RIGHTKEYaltaModuloMain : est : conditional est est : declareLocal estest : cycles estest : input estest : output estest : assignment estest : llamadaAFunct estest : emptyllamadaAFunct : ID LEFTPAR llamadaAFunct2 RIGHTPARllamadaAFunct : emptyllamadaAFunct2 : ID llamadaAFunct3llamadaAFunct3 : COMMA IDllamadaAFunct3 : emptyllamadaAFunct2 : emptydeclareLocal : DECLARE declareRecursivoLocal declareRecursivoLocal : type ID altaVarLocal assignmentDecl declare2Local declare3Local SEMICOLON declareRecursivoLocalassignmentDecl : ASSGN exp number : INTEGER number2number2 : DOT INTEGERnumber2 : emptyassignmentDecl : emptydeclare2Local : arraydeclare3Local : COMMA ID altaVarLocal assignmentDecl declare3Local declareRecursivoLocal : emptydeclareLocal : emptydeclare2Local : emptydeclare3Local : emptyaltaVarLocal : assignment : ID quad1 ASSGN exp SEMICOLONquad1 : assignment : ID ASSGN llamadaAFunct SEMICOLONassignment : emptyconditional : IF LEFTPAR conditional2 RIGHTPAR LEFTKEY est RIGHTKEY conditionalElse conditionalElse : ELSE LEFTKEY est RIGHTKEYconditionalElse : emptyconditional2 : exp conditional2conditional2 : emptycycles : whilecycles : emptycycles : forcycles : do-whiledo-while : DO LEFTKEY est RIGHTKEY WHILE LEFTPAR while2 RIGHTPAR while : WHILE LEFTPAR while2 RIGHTPAR LEFTKEY est RIGHTKEYwhile2 : exp while2while2 : emptyfor : FOR LEFTPAR for2 SEMICOLON for4 SEMICOLON parte3For RIGHTPAR LEFTKEY est RIGHTKEYfor2 : ID ASSGN number for3for3 : COMMA for2for3 : emptyfor4 : expForparte3For : ID SUM SUMparte3For : ID MINUS MINUSexpFor : ID expFor2expFor : numberexpFor2 : LESS expForexpFor2 : GRTR expForexpFor2 : EQ expForexpFor2 : NOTEQ expForexpFor2 : AND expForexpFor2 : OR expForexpFor2 : emptyexp : ID exp2exp : number exp2exp : emptyexp2 : LESS expexp2 : GRTR expexp2 : EQ expexp2 : NOTEQ expexp2 : AND expexp2 : OR expexp2 : SUM expexp2 : MINUS expexp2 : MULTP expexp2 : DIVIDE expexp2 : emptyoutput : WRITE LEFTPAR output2 RIGHTPAR SEMICOLONoutput2 : ID output2output2 : QUOTE ID QUOTE output2output2 : emptyinput : READ LEFTPAR ID RIGHTPAR SEMICOLONempty :'
    
_lr_action_items = {'ASSGN':([26,31,86,121,141,153,177,244,252,],[-22,35,120,149,167,-62,35,-62,35,]),'FLOAT':([7,20,49,87,106,160,245,],[14,14,14,14,14,14,14,]),'RETURN':([76,78,80,81,82,84,87,89,90,91,92,93,112,115,116,118,123,125,127,128,129,133,158,171,173,185,192,194,225,238,240,245,246,248,253,258,260,],[-115,-75,-74,-115,-115,-115,-115,-115,-72,-42,-115,-115,-35,-41,-38,-40,-49,-58,-37,-39,-36,-115,180,-65,-43,-114,-110,-63,-77,-115,-76,-115,-67,-69,-50,-80,-68,]),'DO':([39,50,76,78,80,81,82,84,87,89,90,91,92,93,110,123,125,133,171,173,185,186,192,194,197,225,238,240,245,246,248,249,253,254,258,260,],[-34,74,74,-75,-74,74,74,74,-115,74,-72,-44,74,74,74,-49,-58,74,-65,-43,-114,74,-110,-63,74,-77,-115,-76,-115,-67,-69,74,-50,74,-80,-68,]),'READ':([39,50,76,78,80,81,82,84,87,89,90,91,92,93,110,123,125,133,171,173,185,186,192,194,197,225,238,240,245,246,248,249,253,254,258,260,],[-34,75,75,-75,-74,75,75,75,-115,75,-72,-44,75,75,75,-49,-58,75,-65,-43,-114,75,-110,-63,75,-77,-115,-76,-115,-67,-69,75,-50,75,-80,-68,]),'VOID':([7,20,49,87,106,160,245,],[13,13,13,13,13,13,13,]),'NUMBER':([180,],[198,]),'WHILE':([39,50,76,78,80,81,82,84,87,89,90,91,92,93,110,123,125,133,162,171,173,185,186,192,194,197,225,238,240,245,246,248,249,253,254,258,260,],[-34,77,77,-75,-74,77,77,77,-115,77,-72,-44,77,77,77,-49,-58,77,184,-65,-43,-114,77,-110,-63,77,-77,-115,-76,-115,-67,-69,77,-50,77,-80,-68,]),'PROGRAM':([0,],[2,]),'RIGHTKEY':([39,50,76,78,79,80,81,82,84,87,89,90,91,92,93,110,112,115,116,118,123,125,127,128,129,133,135,158,171,173,181,182,185,186,192,194,197,203,220,221,222,225,238,240,245,246,248,249,253,254,255,257,258,260,],[-34,-115,-115,-75,114,-74,-115,-115,-115,-115,-115,-72,-42,-115,-115,-115,-35,-41,-38,-40,-49,-58,-37,-39,-36,-115,162,-115,-65,-43,200,-15,-114,-115,-110,-63,-115,225,238,-13,-14,-77,-115,-76,-115,-67,-69,-115,-50,-115,258,260,-80,-68,]),'MINUS':([40,42,43,63,64,104,233,243,],[57,-115,57,-52,-54,-53,243,251,]),'DOT':([42,],[65,]),'DIVIDE':([40,42,43,63,64,104,],[52,-115,52,-52,-54,-53,]),'MULTP':([40,42,43,63,64,104,],[59,-115,59,-52,-54,-53,]),'SEMICOLON':([3,4,26,29,31,35,36,37,40,41,42,43,44,46,47,48,51,52,53,54,55,56,57,58,59,60,61,62,63,64,66,68,70,94,95,96,97,98,99,100,101,102,103,104,105,107,120,130,132,140,146,148,149,153,157,163,168,172,173,177,187,188,189,190,191,196,198,199,207,210,214,215,217,218,219,226,227,228,229,230,231,234,236,237,244,252,256,259,],[-3,5,-22,33,-115,-115,-115,-55,-115,-51,-115,-115,-98,-115,-9,-26,-115,-115,-115,-115,-97,-115,-115,-115,-115,-115,-115,-109,-52,-54,-96,106,-24,-103,-108,-99,-102,-105,-106,-100,-107,-101,-104,-53,-115,-22,-115,-25,-115,166,171,-44,-115,-62,-10,185,192,194,-43,-115,-88,-84,-115,212,-115,-115,221,222,-87,-95,-81,-83,-115,-56,-26,-93,-89,-92,-90,-91,-94,-82,-61,245,-62,-115,-115,-57,]),'QUOTE':([119,144,169,193,],[143,143,193,143,]),'LESS':([40,42,43,63,64,104,189,],[53,-115,53,-52,-54,-53,205,]),'RIGHTPAR':([30,40,42,43,44,49,51,52,53,54,55,56,57,58,59,60,61,62,63,64,66,71,73,94,95,96,97,98,99,100,101,102,103,104,109,113,119,122,126,134,136,137,138,139,142,144,145,150,151,152,154,155,156,159,161,165,170,174,176,178,193,195,201,202,216,223,224,232,239,250,251,],[34,-115,-115,-115,-98,-115,-115,-115,-115,-115,-97,-115,-115,-115,-115,-115,-115,-109,-52,-54,-96,108,-19,-103,-108,-99,-102,-105,-106,-100,-107,-101,-104,-53,-62,-115,-115,-115,-115,-115,163,164,-115,-79,168,-115,-113,173,-115,-48,-71,-115,179,-17,-20,-78,-111,-45,-47,-70,-115,-46,-62,-115,-112,-115,240,241,-18,-85,-86,]),'NOTEQ':([40,42,43,63,64,104,189,],[54,-115,54,-52,-54,-53,206,]),'COMMA':([26,31,35,36,37,40,41,42,43,44,46,47,48,51,52,53,54,55,56,57,58,59,60,61,62,63,64,66,94,95,96,97,98,99,100,101,102,103,104,105,107,109,130,132,134,151,153,177,191,196,201,217,218,219,223,244,252,256,],[-22,-115,-115,-115,-55,-115,-51,-115,-115,-98,69,-9,-26,-115,-115,-115,-115,-97,-115,-115,-115,-115,-115,-115,-109,-52,-54,-96,-103,-108,-99,-102,-105,-106,-100,-107,-101,-104,-53,-115,-22,-62,-25,69,160,175,-62,-115,213,-115,-62,235,-56,-26,160,-62,-115,235,]),'INTEGER':([35,40,42,43,44,45,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,94,95,96,97,98,99,100,101,102,103,104,113,126,138,139,149,154,155,166,167,202,204,205,206,208,209,211,],[42,-115,-115,-115,-98,42,42,42,42,42,-97,42,42,42,42,42,42,-109,-52,-54,104,-96,-103,-108,-99,-102,-105,-106,-100,-107,-101,-104,-53,42,42,42,-98,42,-98,42,42,42,42,42,42,42,42,42,42,]),'IF':([39,50,76,78,80,81,82,84,87,89,90,91,92,93,110,123,125,133,171,173,185,186,192,194,197,225,238,240,245,246,248,249,253,254,258,260,],[-34,88,88,-75,-74,88,88,88,-115,88,-72,-44,88,88,88,-49,-58,88,-65,-43,-114,88,-110,-63,88,-77,-115,-76,-115,-67,-69,88,-50,88,-80,-68,]),'SUM':([40,42,43,63,64,104,233,242,],[56,-115,56,-52,-54,-53,242,250,]),'$end':([1,33,],[0,-1,]),'FUNCTION':([5,7,8,9,16,18,21,106,131,200,],[-115,-115,20,-7,-6,-23,20,-115,-8,-12,]),'RIGHTBRACK':([40,42,43,44,45,51,52,53,54,55,56,57,58,59,60,61,62,63,64,66,67,94,95,96,97,98,99,100,101,102,103,104,],[-115,-115,-115,-98,-115,-115,-115,-115,-115,-97,-115,-115,-115,-115,-115,-115,-109,-52,-54,-96,105,-103,-108,-99,-102,-105,-106,-100,-107,-101,-104,-53,]),'END':([24,114,],[29,-33,]),'STRING':([7,20,49,87,106,160,245,],[11,11,11,11,11,11,11,]),'FOR':([39,50,76,78,80,81,82,84,87,89,90,91,92,93,110,123,125,133,171,173,185,186,192,194,197,225,238,240,245,246,248,249,253,254,258,260,],[-34,83,83,-75,-74,83,83,83,-115,83,-72,-44,83,83,83,-49,-58,83,-65,-43,-114,83,-110,-63,83,-77,-115,-76,-115,-67,-69,83,-50,83,-80,-68,]),'ELSE':([238,],[247,]),'WRITE':([39,50,76,78,80,81,82,84,87,89,90,91,92,93,110,123,125,133,171,173,185,186,192,194,197,225,238,240,245,246,248,249,253,254,258,260,],[-34,85,85,-75,-74,85,85,85,-115,85,-72,-44,85,85,85,-49,-58,85,-65,-43,-114,85,-110,-63,85,-77,-115,-76,-115,-67,-69,85,-50,85,-80,-68,]),'GRTR':([40,42,43,63,64,104,189,],[58,-115,58,-52,-54,-53,208,]),'ID':([2,11,12,13,14,15,17,19,27,35,39,40,42,43,44,45,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,66,69,72,76,78,80,81,82,84,87,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,110,111,113,117,119,120,122,123,124,125,126,133,138,139,143,144,149,154,155,166,171,173,175,180,183,185,186,192,193,194,197,202,204,205,206,208,209,211,212,213,225,235,238,240,245,246,248,249,253,254,258,260,],[3,-30,-28,-32,-29,-31,26,-27,32,43,-34,-115,-115,-115,-98,43,86,43,43,43,43,-97,43,43,43,43,43,43,-109,-52,-54,-96,107,109,86,-75,-74,86,86,86,-115,86,-72,-44,86,86,-103,-108,-99,-102,-105,-106,-100,-107,-101,-104,-53,86,136,43,141,144,147,151,-49,153,-58,43,86,43,-98,169,144,43,-98,43,189,-65,-43,195,199,201,-114,86,-110,144,-63,86,43,189,189,189,189,189,189,233,141,-77,244,-115,-76,-115,-67,-69,86,-50,86,-80,-68,]),'EQ':([40,42,43,63,64,104,189,],[60,-115,60,-52,-54,-53,209,]),'DECLARE':([5,39,50,76,78,80,81,82,84,87,89,90,91,92,93,110,123,125,133,171,173,185,186,192,194,197,225,238,240,245,246,248,249,253,254,258,260,],[7,-34,87,87,-75,-74,87,87,87,-115,87,-72,-44,87,87,87,-49,-58,87,-65,-43,-114,87,-110,-63,87,-77,-115,-76,-115,-67,-69,87,-50,87,-80,-68,]),'LEFTKEY':([34,74,108,164,179,241,247,],[39,110,133,186,197,249,254,]),'AND':([40,42,43,63,64,104,189,],[51,-115,51,-52,-54,-53,204,]),'INT':([7,20,49,87,106,160,245,],[12,12,12,12,12,12,12,]),'LEFTBRACK':([26,31,35,36,37,40,41,42,43,44,51,52,53,54,55,56,57,58,59,60,61,62,63,64,66,94,95,96,97,98,99,100,101,102,103,104,105,153,177,196,],[-22,-115,-115,45,-55,-115,-51,-115,-115,-98,-115,-115,-115,-115,-97,-115,-115,-115,-115,-115,-115,-109,-52,-54,-96,-103,-108,-99,-102,-105,-106,-100,-107,-101,-104,-53,45,-62,-115,45,]),'LEFTPAR':([25,32,38,75,77,83,85,86,88,147,184,],[30,-16,49,111,113,117,119,122,126,122,202,]),'BOOL':([7,20,49,87,106,160,245,],[15,15,15,15,15,15,15,]),'MAIN':([5,6,7,8,9,10,16,18,21,22,23,28,106,131,200,],[-115,-2,-115,-115,-5,25,-6,-23,-115,-4,-21,-11,-115,-8,-12,]),'OR':([40,42,43,63,64,104,189,],[61,-115,61,-52,-54,-53,211,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'funct':([8,21,],[21,21,]),'output2':([119,144,193,],[142,170,216,]),'llamadaAFunct2':([122,],[150,]),'conditional':([50,76,81,82,84,89,92,93,110,133,186,197,249,254,],[76,76,76,76,76,76,76,76,76,76,76,76,76,76,]),'number':([35,45,51,52,53,54,56,57,58,59,60,61,113,126,138,149,155,166,167,202,204,205,206,208,209,211,],[40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,187,191,40,187,187,187,187,187,187,]),'expFor':([166,204,205,206,208,209,211,],[188,226,227,228,229,230,231,]),'while2':([113,138,202,],[137,165,224,]),'do-while':([50,76,81,82,84,89,92,93,110,133,186,197,249,254,],[78,78,78,78,78,78,78,78,78,78,78,78,78,78,]),'declareRecursivoLocal':([87,245,],[123,253,]),'for2':([117,213,],[140,234,]),'array':([36,105,196,],[47,130,218,]),'functReturn':([158,],[181,]),'altaVarGlobal':([26,107,],[31,132,]),'type2':([7,20,49,87,106,160,245,],[19,19,19,19,19,19,19,]),'est':([50,76,81,82,84,89,92,93,110,133,186,197,249,254,],[79,112,115,116,118,127,128,129,135,158,203,220,255,257,]),'conditionalElse':([238,],[246,]),'program2':([5,],[6,]),'program3':([8,21,],[22,28,]),'exp2':([40,43,],[55,66,]),'llamadaAFunct':([50,76,81,82,84,89,92,93,110,120,133,186,197,249,254,],[81,81,81,81,81,81,81,81,81,146,81,81,81,81,81,]),'llamadaAFunct3':([151,],[174,]),'funct2':([49,],[71,]),'program':([0,],[1,]),'input':([50,76,81,82,84,89,92,93,110,133,186,197,249,254,],[82,82,82,82,82,82,82,82,82,82,82,82,82,82,]),'for4':([166,],[190,]),'type':([7,20,49,87,106,160,245,],[17,27,72,124,17,183,124,]),'empty':([5,7,8,21,31,35,36,40,42,43,45,46,49,50,51,52,53,54,56,57,58,59,60,61,76,81,82,84,87,89,92,93,105,106,110,113,119,120,122,126,132,133,134,138,144,149,151,155,158,177,186,189,191,193,196,197,202,217,223,238,245,249,252,254,256,],[9,18,23,23,37,44,48,62,64,62,44,70,73,91,44,44,44,44,44,44,44,44,44,44,91,91,91,91,125,91,91,91,48,18,91,139,145,148,152,154,70,91,161,139,145,44,176,154,182,37,91,210,215,145,219,91,139,236,161,248,125,91,37,91,236,]),'funct3':([134,223,],[159,239,]),'declare2Local':([196,],[217,]),'assignment':([50,76,81,82,84,89,92,93,110,133,186,197,249,254,],[84,84,84,84,84,84,84,84,84,84,84,84,84,84,]),'assignmentDecl':([31,177,252,],[36,196,256,]),'parte3For':([212,],[232,]),'cuerpo':([10,],[24,]),'altaVarLocal':([109,153,201,244,],[134,177,223,252,]),'quad1':([86,],[121,]),'number2':([42,],[63,]),'declare3':([46,132,],[68,157,]),'output':([50,76,81,82,84,89,92,93,110,133,186,197,249,254,],[92,92,92,92,92,92,92,92,92,92,92,92,92,92,]),'declare3Local':([217,256,],[237,259,]),'cycles':([50,76,81,82,84,89,92,93,110,133,186,197,249,254,],[89,89,89,89,89,89,89,89,89,89,89,89,89,89,]),'for':([50,76,81,82,84,89,92,93,110,133,186,197,249,254,],[80,80,80,80,80,80,80,80,80,80,80,80,80,80,]),'goToMainQuad':([6,],[10,]),'altaModuloMain':([39,],[50,]),'altaModulo':([32,],[38,]),'expFor2':([189,],[207,]),'while':([50,76,81,82,84,89,92,93,110,133,186,197,249,254,],[90,90,90,90,90,90,90,90,90,90,90,90,90,90,]),'altaPrograma':([3,],[4,]),'declareRecursivo':([7,106,],[16,131,]),'conditional2':([126,155,],[156,178,]),'exp':([35,45,51,52,53,54,56,57,58,59,60,61,113,126,138,149,155,202,],[41,67,94,95,96,97,98,99,100,101,102,103,138,155,138,172,155,138,]),'for3':([191,],[214,]),'declare2':([36,],[46,]),'declareLocal':([50,76,81,82,84,89,92,93,110,133,186,197,249,254,],[93,93,93,93,93,93,93,93,93,93,93,93,93,93,]),'declare':([5,],[8,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> PROGRAM ID altaPrograma SEMICOLON program2 goToMainQuad cuerpo END SEMICOLON','program',9,'p_program','parser.py',46),
  ('goToMainQuad -> <empty>','goToMainQuad',0,'p_goToMainQuad','parser.py',49),
  ('altaPrograma -> <empty>','altaPrograma',0,'p_altaPrograma','parser.py',54),
  ('program2 -> declare program3','program2',2,'p_program2','parser.py',64),
  ('program2 -> empty','program2',1,'p_program2Empty','parser.py',67),
  ('declare -> DECLARE declareRecursivo','declare',2,'p_declare','parser.py',70),
  ('declare -> empty','declare',1,'p_declareEmpty','parser.py',74),
  ('declareRecursivo -> type ID altaVarGlobal assignmentDecl declare2 declare3 SEMICOLON declareRecursivo','declareRecursivo',8,'p_declareRecursivo','parser.py',77),
  ('declare2 -> array','declare2',1,'p_declare2','parser.py',81),
  ('declare3 -> COMMA ID altaVarGlobal declare3','declare3',4,'p_declare3','parser.py',84),
  ('program3 -> funct program3','program3',2,'p_program3','parser.py',88),
  ('funct -> FUNCTION type ID altaModulo LEFTPAR funct2 RIGHTPAR LEFTKEY est functReturn RIGHTKEY','funct',11,'p_funct','parser.py',91),
  ('functReturn -> RETURN NUMBER SEMICOLON','functReturn',3,'p_functReturn','parser.py',95),
  ('functReturn -> RETURN ID SEMICOLON','functReturn',3,'p_functReturnID','parser.py',99),
  ('functReturn -> empty','functReturn',1,'p_functReturnEmpty','parser.py',103),
  ('altaModulo -> <empty>','altaModulo',0,'p_altaModulo','parser.py',106),
  ('funct2 -> type ID altaVarLocal funct3','funct2',4,'p_funct2','parser.py',117),
  ('funct3 -> COMMA type ID altaVarLocal funct3','funct3',5,'p_funct3','parser.py',121),
  ('funct2 -> empty','funct2',1,'p_funct2Empty','parser.py',125),
  ('funct3 -> empty','funct3',1,'p_funct3Empty','parser.py',128),
  ('program3 -> empty','program3',1,'p_program3Empty','parser.py',131),
  ('altaVarGlobal -> <empty>','altaVarGlobal',0,'p_altaVarGlobal','parser.py',134),
  ('declareRecursivo -> empty','declareRecursivo',1,'p_declareResursivoEmpty','parser.py',143),
  ('declare3 -> empty','declare3',1,'p_declare3Empty','parser.py',146),
  ('array -> LEFTBRACK exp RIGHTBRACK array','array',4,'p_array','parser.py',149),
  ('array -> empty','array',1,'p_arrayEmpty','parser.py',153),
  ('type -> type2','type',1,'p_type','parser.py',156),
  ('type2 -> INT','type2',1,'p_type2','parser.py',159),
  ('type2 -> FLOAT','type2',1,'p_type2Float','parser.py',165),
  ('type2 -> STRING','type2',1,'p_type2String','parser.py',171),
  ('type2 -> BOOL','type2',1,'p_type2Bool','parser.py',177),
  ('type2 -> VOID','type2',1,'p_type2Void','parser.py',183),
  ('cuerpo -> MAIN LEFTPAR RIGHTPAR LEFTKEY altaModuloMain est RIGHTKEY','cuerpo',7,'p_cuerpo','parser.py',189),
  ('altaModuloMain -> <empty>','altaModuloMain',0,'p_altaModuloMain','parser.py',193),
  ('est -> conditional est','est',2,'p_est','parser.py',203),
  ('est -> declareLocal est','est',2,'p_estVars','parser.py',206),
  ('est -> cycles est','est',2,'p_estCycle','parser.py',209),
  ('est -> input est','est',2,'p_estRead','parser.py',212),
  ('est -> output est','est',2,'p_estWrite','parser.py',215),
  ('est -> assignment est','est',2,'p_estAassignment','parser.py',218),
  ('est -> llamadaAFunct est','est',2,'p_estFunct','parser.py',221),
  ('est -> empty','est',1,'p_estEmpty','parser.py',224),
  ('llamadaAFunct -> ID LEFTPAR llamadaAFunct2 RIGHTPAR','llamadaAFunct',4,'p_llamadaAFunct','parser.py',227),
  ('llamadaAFunct -> empty','llamadaAFunct',1,'p_llamadaAFunctEmpty','parser.py',231),
  ('llamadaAFunct2 -> ID llamadaAFunct3','llamadaAFunct2',2,'p_llamadaAFunct2','parser.py',234),
  ('llamadaAFunct3 -> COMMA ID','llamadaAFunct3',2,'p_llamadaAFunct3','parser.py',238),
  ('llamadaAFunct3 -> empty','llamadaAFunct3',1,'p_llamadaAFunct3Empty','parser.py',242),
  ('llamadaAFunct2 -> empty','llamadaAFunct2',1,'p_llamadaAFunct2Empty','parser.py',245),
  ('declareLocal -> DECLARE declareRecursivoLocal','declareLocal',2,'p_declareLocal','parser.py',248),
  ('declareRecursivoLocal -> type ID altaVarLocal assignmentDecl declare2Local declare3Local SEMICOLON declareRecursivoLocal','declareRecursivoLocal',8,'p_declareRecursivoLocal','parser.py',252),
  ('assignmentDecl -> ASSGN exp','assignmentDecl',2,'p_assignmentDeclareFloat','parser.py',256),
  ('number -> INTEGER number2','number',2,'p_number','parser.py',260),
  ('number2 -> DOT INTEGER','number2',2,'p_number2','parser.py',264),
  ('number2 -> empty','number2',1,'p_number2Empty','parser.py',268),
  ('assignmentDecl -> empty','assignmentDecl',1,'p_assignmentDeclareEmpty','parser.py',271),
  ('declare2Local -> array','declare2Local',1,'p_declare2Local','parser.py',274),
  ('declare3Local -> COMMA ID altaVarLocal assignmentDecl declare3Local','declare3Local',5,'p_declare3Local','parser.py',277),
  ('declareRecursivoLocal -> empty','declareRecursivoLocal',1,'p_declareResursivoEmptyLocal','parser.py',280),
  ('declareLocal -> empty','declareLocal',1,'p_declareEmptyLocal','parser.py',283),
  ('declare2Local -> empty','declare2Local',1,'p_declar2EmptyLocal','parser.py',286),
  ('declare3Local -> empty','declare3Local',1,'p_declare3EmptyLocal','parser.py',289),
  ('altaVarLocal -> <empty>','altaVarLocal',0,'p_altaVarLocal','parser.py',292),
  ('assignment -> ID quad1 ASSGN exp SEMICOLON','assignment',5,'p_assignment','parser.py',301),
  ('quad1 -> <empty>','quad1',0,'p_quad1','parser.py',305),
  ('assignment -> ID ASSGN llamadaAFunct SEMICOLON','assignment',4,'p_assignmentFUNCT','parser.py',309),
  ('assignment -> empty','assignment',1,'p_assignmentEmpty','parser.py',313),
  ('conditional -> IF LEFTPAR conditional2 RIGHTPAR LEFTKEY est RIGHTKEY conditionalElse','conditional',8,'p_conditional','parser.py',316),
  ('conditionalElse -> ELSE LEFTKEY est RIGHTKEY','conditionalElse',4,'p_conditionalElse','parser.py',320),
  ('conditionalElse -> empty','conditionalElse',1,'p_conditionalElseEmpty','parser.py',324),
  ('conditional2 -> exp conditional2','conditional2',2,'p_conditional2','parser.py',327),
  ('conditional2 -> empty','conditional2',1,'p_conditional2Empty','parser.py',330),
  ('cycles -> while','cycles',1,'p_cycles','parser.py',333),
  ('cycles -> empty','cycles',1,'p_cyclesEmpty','parser.py',336),
  ('cycles -> for','cycles',1,'p_cyclesFor','parser.py',339),
  ('cycles -> do-while','cycles',1,'p_cyclesDoWhile','parser.py',342),
  ('do-while -> DO LEFTKEY est RIGHTKEY WHILE LEFTPAR while2 RIGHTPAR','do-while',8,'p_doWhile','parser.py',345),
  ('while -> WHILE LEFTPAR while2 RIGHTPAR LEFTKEY est RIGHTKEY','while',7,'p_whileClass','parser.py',348),
  ('while2 -> exp while2','while2',2,'p_while2','parser.py',351),
  ('while2 -> empty','while2',1,'p_while2Empty','parser.py',354),
  ('for -> FOR LEFTPAR for2 SEMICOLON for4 SEMICOLON parte3For RIGHTPAR LEFTKEY est RIGHTKEY','for',11,'p_forClass','parser.py',357),
  ('for2 -> ID ASSGN number for3','for2',4,'p_for2','parser.py',361),
  ('for3 -> COMMA for2','for3',2,'p_for3','parser.py',365),
  ('for3 -> empty','for3',1,'p_for3Empty','parser.py',369),
  ('for4 -> expFor','for4',1,'p_for4','parser.py',372),
  ('parte3For -> ID SUM SUM','parte3For',3,'p_parte3ForSUM','parser.py',375),
  ('parte3For -> ID MINUS MINUS','parte3For',3,'p_parte3ForMINUS','parser.py',379),
  ('expFor -> ID expFor2','expFor',2,'p_expFor','parser.py',383),
  ('expFor -> number','expFor',1,'p_expForNumber','parser.py',386),
  ('expFor2 -> LESS expFor','expFor2',2,'p_expFor2','parser.py',389),
  ('expFor2 -> GRTR expFor','expFor2',2,'p_exprFor2Grtr','parser.py',393),
  ('expFor2 -> EQ expFor','expFor2',2,'p_expFor2Equal','parser.py',397),
  ('expFor2 -> NOTEQ expFor','expFor2',2,'p_expFor2NotEq','parser.py',401),
  ('expFor2 -> AND expFor','expFor2',2,'p_expFor2And','parser.py',405),
  ('expFor2 -> OR expFor','expFor2',2,'p_expFor2OR','parser.py',409),
  ('expFor2 -> empty','expFor2',1,'p_expFor2Empty','parser.py',413),
  ('exp -> ID exp2','exp',2,'p_exp','parser.py',416),
  ('exp -> number exp2','exp',2,'p_expNUMERO','parser.py',420),
  ('exp -> empty','exp',1,'p_expVACIA','parser.py',423),
  ('exp2 -> LESS exp','exp2',2,'p_exp2','parser.py',426),
  ('exp2 -> GRTR exp','exp2',2,'p_expr2Grtr','parser.py',430),
  ('exp2 -> EQ exp','exp2',2,'p_exp2Equal','parser.py',434),
  ('exp2 -> NOTEQ exp','exp2',2,'p_exp2NotEq','parser.py',438),
  ('exp2 -> AND exp','exp2',2,'p_exp2And','parser.py',442),
  ('exp2 -> OR exp','exp2',2,'p_exp2OR','parser.py',446),
  ('exp2 -> SUM exp','exp2',2,'p_exp2SUM','parser.py',450),
  ('exp2 -> MINUS exp','exp2',2,'p_exp2MINUS','parser.py',454),
  ('exp2 -> MULTP exp','exp2',2,'p_exp2MULTP','parser.py',458),
  ('exp2 -> DIVIDE exp','exp2',2,'p_exp2DIVIDE','parser.py',462),
  ('exp2 -> empty','exp2',1,'p_exp2Empty','parser.py',466),
  ('output -> WRITE LEFTPAR output2 RIGHTPAR SEMICOLON','output',5,'p_output','parser.py',469),
  ('output2 -> ID output2','output2',2,'p_output2','parser.py',473),
  ('output2 -> QUOTE ID QUOTE output2','output2',4,'p_output2Quotes','parser.py',477),
  ('output2 -> empty','output2',1,'p_output2Empty','parser.py',480),
  ('input -> READ LEFTPAR ID RIGHTPAR SEMICOLON','input',5,'p_input','parser.py',483),
  ('empty -> <empty>','empty',0,'p_empty','parser.py',487),
]
