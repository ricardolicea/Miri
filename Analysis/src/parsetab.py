
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ACTDECR ACTDECRVALOR ACTINCR ACTINCRVALOR AND ASSGN BOOL COLON COMMA CYCLE DECLARE DIVIDE DO DOT ELSE END EQ FLOAT FLOATNUMB FOR FUNCTION GRTR GRTREQ ID IF INT INTEGER LEFTBRACK LEFTBRACK LEFTKEY LEFTPAR LESS LESSEQ MAIN MINUS MULTP NOTEQ NUMBER OR PROGRAM QUOTE READ RETURN RIGHTBRACK RIGHTKEY RIGHTPAR SEMICOLON SPACE STRING SUM TYPE VOID WHILE WRITE newlineprogram : PROGRAM ID altaPrograma SEMICOLON program2 goToMainQuad cuerpo END SEMICOLONgoToMainQuad : altaPrograma : program2 : declare program3program2 : emptydeclare : DECLARE declareRecursivo declare : emptydeclareRecursivo : type ID altaVarGlobal assignmentDecl declare2 declare3 SEMICOLON declareRecursivodeclare2 : arraydeclare3 : COMMA  ID altaVarGlobal declare3 program3 : funct program3funct : FUNCTION type ID altaModulo LEFTPAR funct2  RIGHTPAR LEFTKEY est functReturn RIGHTKEYfunctReturn : RETURN NUMBER SEMICOLONfunctReturn : RETURN ID SEMICOLONfunctReturn : emptyaltaModulo : funct2 : type ID altaVarLocal funct3funct3 : COMMA type ID  altaVarLocal funct3funct2 : emptyfunct3 : emptyprogram3 : emptyaltaVarGlobal : declareRecursivo : emptydeclare3 : emptyarray : LEFTBRACK exp RIGHTBRACK arrayarray : emptytype : type2type2 : INTtype2 : FLOATtype2 : STRINGtype2 : BOOLtype2 : VOIDcuerpo : MAIN LEFTPAR RIGHTPAR LEFTKEY llenaMain altaModuloMain est RIGHTKEYllenaMain : altaModuloMain : est : conditional est est : declareLocal estest : cycles estest : input estest : output estest : assignment estest : llamadaAFunct estest : emptyllamadaAFunct : ID LEFTPAR llamadaAFunct2 RIGHTPARllamadaAFunct : emptyllamadaAFunct2 : ID llamadaAFunct3llamadaAFunct3 : COMMA IDllamadaAFunct3 : emptyllamadaAFunct2 : emptydeclareLocal : DECLARE declareRecursivoLocal declareRecursivoLocal : type ID altaVarLocal assignmentDecl declare2Local declare3Local SEMICOLON declareRecursivoLocalassignmentDecl : ASSGN exp number : INTEGER meteNumnumber : FLOAT meteNumnumber : emptyassignmentDecl : emptydeclare2Local : arraydeclare3Local : COMMA ID altaVarLocal assignmentDecl declare3Local declareRecursivoLocal : emptydeclareLocal : emptydeclare2Local : emptydeclare3Local : emptyaltaVarLocal : assignment : ID ASSGN meteVar exp generaCuad SEMICOLONassignment : ID ASSGN meteVar llamadaAFunct SEMICOLONmeteVar : assignment : emptyconditional : IF LEFTPAR conditional2 RIGHTPAR gotoFCuad LEFTKEY est RIGHTKEY gotoCuad conditionalElse gotoFCuad : gotoCuad : conditionalElse : ELSE LEFTKEY est RIGHTKEY llenaGotollenaGoto : conditionalElse : emptyconditional2 : exp conditional2conditional2 : emptycycles : whilecycles : emptycycles : forcycles : do-whiledo-while : DO meteSalto LEFTKEY est RIGHTKEY WHILE LEFTPAR while2 RIGHTPAR gotoVCuad gotoVCuad : meteSalto : while : WHILE LEFTPAR while2 RIGHTPAR gotoFCuad LEFTKEY est RIGHTKEY llenaCuadF llenaCuadF : while2 : exp while2while2 : emptyfor : FOR LEFTPAR for2 SEMICOLON for4 SEMICOLON parte3For RIGHTPAR LEFTKEY est RIGHTKEYfor2 : ID ASSGN cuadFor number generaCuad for3cuadFor : for3 : COMMA for2for3 : emptyfor4 : expForparte3For : ID meteID ACTINCR meteOpermeteID : parte3For : ID meteID ACTINCRVALOR meteOperparte3For : ID meteID ACTDECRVALOR meteOperexpFor : ID meteExp expFor2expFor : numberexpFor2 : LESS meteOper expForexpFor2 : GRTR meteOper expForexpFor2 : EQ meteOper expForexpFor2 : NOTEQ meteOper expForexpFor2 : AND meteOper expForexpFor2 : OR meteOper expForexpFor2 : expFor2 : emptyexp : ID meteExp exp2exp : LEFTPAR metePar exp RIGHTPAR sacaPar exp2 generaCuadmetePar : sacaPar : meteExp : generaCuad : exp : number exp2meteNum : exp : emptyexp2 : LESS meteOper expexp2 : GRTR meteOper expexp2 : EQ meteOper expexp2 : NOTEQ meteOper expexp2 : AND meteOper expexp2 : OR meteOper expexp2 : SUM meteOper expmeteOper : exp2 : MINUS meteOper expexp2 : MULTP meteOper expexp2 : DIVIDE meteOper expexp2 : emptyoutput : WRITE LEFTPAR output2 RIGHTPAR SEMICOLONoutput2 : ID output2output2 : QUOTE ID QUOTE output2output2 : emptyinput : READ LEFTPAR ID RIGHTPAR SEMICOLONempty :circulo : LEFTPAR INTEGER COMMA STRING COMMA BOOL COMMA INTEGER COMMA INTEGER RIGHTPAR SEMICOLONcuadro : LEFTPAR INTEGER COMMA STRING COMMA BOOL COMMA INTEGER COMMA INTEGER RIGHTPAR SEMICOLONtriangulo : LEFTPAR INTEGER COMMA INTEGER COMMA INTEGER COMMA STRING COMMA BOOL COMMA INTEGER COMMA INTEGER COMMA INTEGER RIGHTPAR SEMICOLONlinea : LEFTPAR INTEGER COMMA STRING COMMA INTEGER COMMA INTEGER COMMA INTEGER COMMA INTEGER RIGHTPAR SEMICOLONrectangulo : LEFTPAR INTEGER COMMA INTEGER COMMA STRING COMMA BOOL COMMA INTEGER COMMA INTEGER COMMA INTEGER RIGHTPAR SEMICOLON'
    
_lr_action_items = {'DO':([39,52,76,96,98,100,101,102,104,107,109,110,111,112,113,128,142,144,155,192,205,213,215,224,229,233,253,266,267,268,269,276,282,283,284,290,291,293,295,297,298,],[-34,-35,94,94,-79,-78,94,94,94,-133,94,-76,-45,94,94,94,-50,-59,94,-44,-132,-128,-65,94,-64,94,-84,-133,-70,-81,-83,94,-51,-133,-80,-68,-73,-87,94,-72,-71,]),'ASSGN':([26,31,106,161,170,196,265,281,],[-22,35,140,184,-63,35,-63,35,]),'FLOAT':([7,20,35,40,41,42,44,45,46,47,51,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,77,78,79,80,81,82,83,84,85,86,88,90,107,114,115,116,117,118,119,120,121,122,123,124,133,140,145,149,153,158,159,166,171,173,174,183,184,199,212,235,237,238,239,241,242,244,254,255,256,257,258,259,266,],[14,14,41,-133,-114,-109,-114,-111,-55,41,14,-123,-123,-123,-123,-113,-123,-123,-123,-123,-123,-123,-127,-54,41,-53,-133,41,41,41,41,41,41,41,41,41,41,-107,14,14,-120,-126,-116,-119,-122,-124,-117,-125,-118,-121,-110,41,-66,41,-133,14,41,-55,41,-55,41,-112,41,-89,-108,41,41,-123,-123,-123,-123,-123,-123,41,41,41,41,41,41,14,]),'RETURN':([96,98,100,101,102,104,107,109,110,111,112,113,128,132,135,136,138,142,144,146,147,148,151,192,205,213,215,229,253,266,267,268,269,282,283,284,290,291,293,297,298,],[-133,-79,-78,-133,-133,-133,-133,-133,-76,-43,-133,-133,-133,-36,-42,-39,-41,-50,-59,-38,-40,-37,175,-44,-132,-128,-65,-64,-84,-133,-70,-81,-83,-51,-133,-80,-68,-73,-87,-72,-71,]),'ACTINCR':([246,261,],[-94,277,]),'LESS':([35,40,41,42,44,45,46,47,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,77,78,79,80,81,82,83,84,85,86,88,114,115,116,117,118,119,120,121,122,123,124,133,140,145,149,158,159,166,171,173,174,190,191,199,209,225,235,],[-133,55,-114,-109,-114,-111,-55,-133,-123,-123,-123,-123,-113,-123,-123,-123,-123,-123,-123,-127,-54,-133,-53,55,-133,-133,-133,-133,-133,-133,-133,-133,-133,-133,-107,-120,-126,-116,-119,-122,-124,-117,-125,-118,-121,-110,-133,-66,-133,55,-133,-55,-133,-55,-133,-112,-111,-55,-108,-111,238,-133,]),'NOTEQ':([35,40,41,42,44,45,46,47,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,77,78,79,80,81,82,83,84,85,86,88,114,115,116,117,118,119,120,121,122,123,124,133,140,145,149,158,159,166,171,173,174,190,191,199,209,225,235,],[-133,56,-114,-109,-114,-111,-55,-133,-123,-123,-123,-123,-113,-123,-123,-123,-123,-123,-123,-127,-54,-133,-53,56,-133,-133,-133,-133,-133,-133,-133,-133,-133,-133,-107,-120,-126,-116,-119,-122,-124,-117,-125,-118,-121,-110,-133,-66,-133,56,-133,-55,-133,-55,-133,-112,-111,-55,-108,-111,239,-133,]),'VOID':([7,20,51,90,107,153,266,],[13,13,13,13,13,13,13,]),'NUMBER':([175,],[200,]),'WHILE':([39,52,76,96,98,100,101,102,104,107,109,110,111,112,113,128,142,144,155,192,204,205,213,215,224,229,233,253,266,267,268,269,276,282,283,284,290,291,293,295,297,298,],[-34,-35,97,97,-79,-78,97,97,97,-133,97,-76,-45,97,97,97,-50,-59,97,-44,223,-132,-128,-65,97,-64,97,-84,-133,-70,-81,-83,97,-51,-133,-80,-68,-73,-87,97,-72,-71,]),'PROGRAM':([0,],[2,]),'MULTP':([35,40,41,42,44,45,46,47,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,77,78,79,80,81,82,83,84,85,86,88,114,115,116,117,118,119,120,121,122,123,124,133,140,145,149,158,159,166,171,173,174,190,191,199,235,],[-133,61,-114,-109,-114,-111,-55,-133,-123,-123,-123,-123,-113,-123,-123,-123,-123,-123,-123,-127,-54,-133,-53,61,-133,-133,-133,-133,-133,-133,-133,-133,-133,-133,-107,-120,-126,-116,-119,-122,-124,-117,-125,-118,-121,-110,-133,-66,-133,61,-133,-55,-133,-55,-133,-112,-111,-55,-108,-133,]),'MINUS':([35,40,41,42,44,45,46,47,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,77,78,79,80,81,82,83,84,85,86,88,114,115,116,117,118,119,120,121,122,123,124,133,140,145,149,158,159,166,171,173,174,190,191,199,235,],[-133,59,-114,-109,-114,-111,-55,-133,-123,-123,-123,-123,-113,-123,-123,-123,-123,-123,-123,-127,-54,-133,-53,59,-133,-133,-133,-133,-133,-133,-133,-133,-133,-133,-107,-120,-126,-116,-119,-122,-124,-117,-125,-118,-121,-110,-133,-66,-133,59,-133,-55,-133,-55,-133,-112,-111,-55,-108,-133,]),'DIVIDE':([35,40,41,42,44,45,46,47,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,77,78,79,80,81,82,83,84,85,86,88,114,115,116,117,118,119,120,121,122,123,124,133,140,145,149,158,159,166,171,173,174,190,191,199,235,],[-133,54,-114,-109,-114,-111,-55,-133,-123,-123,-123,-123,-113,-123,-123,-123,-123,-123,-123,-127,-54,-133,-53,54,-133,-133,-133,-133,-133,-133,-133,-133,-133,-133,-107,-120,-126,-116,-119,-122,-124,-117,-125,-118,-121,-110,-133,-66,-133,54,-133,-55,-133,-55,-133,-112,-111,-55,-108,-133,]),'RIGHTKEY':([39,52,76,96,98,99,100,101,102,104,107,109,110,111,112,113,128,132,135,136,138,142,144,146,147,148,151,155,176,177,179,192,205,213,215,220,221,224,229,233,236,251,253,266,267,268,269,276,282,283,284,285,290,291,293,295,296,297,298,],[-34,-35,-133,-133,-79,134,-78,-133,-133,-133,-133,-133,-76,-43,-133,-133,-133,-36,-42,-39,-41,-50,-59,-38,-40,-37,-133,-133,202,-15,204,-44,-132,-128,-65,-13,-14,-133,-64,-133,253,267,-84,-133,-70,-81,-83,-133,-51,-133,-80,293,-68,-73,-87,-133,297,-72,-71,]),'SEMICOLON':([3,4,26,29,31,35,36,37,40,41,43,44,45,46,48,49,50,53,54,55,56,57,58,59,60,61,62,63,64,65,67,68,70,72,77,78,79,80,81,82,83,84,85,86,88,89,91,114,115,116,117,118,119,120,121,122,123,124,125,127,140,149,150,160,166,170,174,180,183,184,185,188,189,190,191,192,196,199,200,201,207,208,209,210,211,212,216,218,225,227,230,231,232,237,238,239,240,241,242,243,244,247,249,250,254,255,256,257,258,259,263,264,265,270,271,272,273,274,275,280,281,289,294,],[-3,5,-22,33,-133,-133,-133,-56,-133,-114,-52,-114,-111,-55,-133,-9,-26,-123,-123,-123,-123,-113,-123,-123,-123,-123,-123,-123,-127,-54,-53,-133,90,-24,-133,-133,-133,-133,-133,-133,-133,-133,-133,-133,-107,-133,-22,-120,-126,-116,-119,-122,-124,-117,-125,-118,-121,-110,-25,-133,-66,-133,-10,183,-133,-63,-112,205,-133,-89,213,215,-112,-111,-45,-44,-133,-108,220,221,-98,-92,-111,-55,226,-133,229,-133,-105,-112,-133,-57,-26,-123,-123,-123,-97,-123,-123,-106,-123,-133,-62,266,-133,-133,-133,-133,-133,-133,-88,-91,-63,-103,-99,-102,-100,-101,-104,-90,-133,-133,-58,]),'ACTINCRVALOR':([246,261,],[-94,278,]),'QUOTE':([139,164,186,214,],[163,163,214,163,]),'ACTDECRVALOR':([246,261,],[-94,279,]),'RIGHTPAR':([30,40,41,42,44,45,46,51,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,73,75,77,78,79,80,81,82,83,84,85,86,87,88,93,114,115,116,117,118,119,120,121,122,123,124,129,133,139,141,145,149,152,154,156,157,158,159,162,164,165,167,168,169,171,172,173,174,182,187,193,195,198,199,203,214,217,222,228,234,235,245,252,277,278,279,286,287,288,],[34,-133,-114,-109,-114,-111,-55,-133,-123,-123,-123,-123,-113,-123,-123,-123,-123,-123,-123,-127,-54,-133,-53,-133,92,-19,-133,-133,-133,-133,-133,-133,-133,-133,-133,-133,124,-107,-63,-120,-126,-116,-119,-122,-124,-117,-125,-118,-121,-110,-133,-133,-133,-133,-133,-133,-17,-20,180,181,-133,-55,185,-133,-131,192,-133,-49,-55,197,-133,-112,-85,-129,-46,-48,-74,-108,-63,-133,-47,-133,-130,-18,-133,260,268,-123,-123,-123,-93,-95,-96,]),'READ':([39,52,76,96,98,100,101,102,104,107,109,110,111,112,113,128,142,144,155,192,205,213,215,224,229,233,253,266,267,268,269,276,282,283,284,290,291,293,295,297,298,],[-34,-35,95,95,-79,-78,95,95,95,-133,95,-76,-45,95,95,95,-50,-59,95,-44,-132,-128,-65,95,-64,95,-84,-133,-70,-81,-83,95,-51,-133,-80,-68,-73,-87,95,-72,-71,]),'COMMA':([26,31,35,36,37,40,41,43,44,45,46,48,49,50,53,54,55,56,57,58,59,60,61,62,63,64,65,67,68,77,78,79,80,81,82,83,84,85,86,88,89,91,93,114,115,116,117,118,119,120,121,122,123,124,125,127,129,149,168,170,174,184,196,199,203,210,212,218,222,227,230,231,232,247,265,281,289,],[-22,-133,-133,-133,-56,-133,-114,-52,-114,-111,-55,71,-9,-26,-123,-123,-123,-123,-113,-123,-123,-123,-123,-123,-123,-127,-54,-53,-133,-133,-133,-133,-133,-133,-133,-133,-133,-133,-133,-107,-133,-22,-63,-120,-126,-116,-119,-122,-124,-117,-125,-118,-121,-110,-25,71,153,-133,194,-63,-112,-89,-133,-108,-63,-55,-133,-133,153,-112,248,-57,-26,262,-63,-133,248,]),'INTEGER':([35,40,41,42,44,45,46,47,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,77,78,79,80,81,82,83,84,85,86,88,114,115,116,117,118,119,120,121,122,123,124,133,140,145,149,158,159,166,171,173,174,183,184,199,212,235,237,238,239,241,242,244,254,255,256,257,258,259,],[44,-133,-114,-109,-114,-111,-55,44,-123,-123,-123,-123,-113,-123,-123,-123,-123,-123,-123,-127,-54,44,-53,-133,44,44,44,44,44,44,44,44,44,44,-107,-120,-126,-116,-119,-122,-124,-117,-125,-118,-121,-110,44,-66,44,-133,44,-55,44,-55,44,-112,44,-89,-108,44,44,-123,-123,-123,-123,-123,-123,44,44,44,44,44,44,]),'IF':([39,52,76,96,98,100,101,102,104,107,109,110,111,112,113,128,142,144,155,192,205,213,215,224,229,233,253,266,267,268,269,276,282,283,284,290,291,293,295,297,298,],[-34,-35,108,108,-79,-78,108,108,108,-133,108,-76,-45,108,108,108,-50,-59,108,-44,-132,-128,-65,108,-64,108,-84,-133,-70,-81,-83,108,-51,-133,-80,-68,-73,-87,108,-72,-71,]),'SUM':([35,40,41,42,44,45,46,47,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,77,78,79,80,81,82,83,84,85,86,88,114,115,116,117,118,119,120,121,122,123,124,133,140,145,149,158,159,166,171,173,174,190,191,199,235,],[-133,58,-114,-109,-114,-111,-55,-133,-123,-123,-123,-123,-113,-123,-123,-123,-123,-123,-123,-127,-54,-133,-53,58,-133,-133,-133,-133,-133,-133,-133,-133,-133,-133,-107,-120,-126,-116,-119,-122,-124,-117,-125,-118,-121,-110,-133,-66,-133,58,-133,-55,-133,-55,-133,-112,-111,-55,-108,-133,]),'$end':([1,33,],[0,-1,]),'FUNCTION':([5,7,8,9,16,18,21,90,126,202,],[-133,-133,20,-7,-6,-23,20,-133,-8,-12,]),'RIGHTBRACK':([40,41,44,45,46,47,53,54,55,56,57,58,59,60,61,62,63,64,65,67,68,69,77,78,79,80,81,82,83,84,85,86,88,114,115,116,117,118,119,120,121,122,123,124,149,174,199,],[-133,-114,-114,-111,-55,-133,-123,-123,-123,-123,-113,-123,-123,-123,-123,-123,-123,-127,-54,-53,-133,89,-133,-133,-133,-133,-133,-133,-133,-133,-133,-133,-107,-120,-126,-116,-119,-122,-124,-117,-125,-118,-121,-110,-133,-112,-108,]),'END':([24,134,],[29,-33,]),'STRING':([7,20,51,90,107,153,266,],[11,11,11,11,11,11,11,]),'FOR':([39,52,76,96,98,100,101,102,104,107,109,110,111,112,113,128,142,144,155,192,205,213,215,224,229,233,253,266,267,268,269,276,282,283,284,290,291,293,295,297,298,],[-34,-35,103,103,-79,-78,103,103,103,-133,103,-76,-45,103,103,103,-50,-59,103,-44,-132,-128,-65,103,-64,103,-84,-133,-70,-81,-83,103,-51,-133,-80,-68,-73,-87,103,-72,-71,]),'ELSE':([267,283,],[-70,292,]),'WRITE':([39,52,76,96,98,100,101,102,104,107,109,110,111,112,113,128,142,144,155,192,205,213,215,224,229,233,253,266,267,268,269,276,282,283,284,290,291,293,295,297,298,],[-34,-35,105,105,-79,-78,105,105,105,-133,105,-76,-45,105,105,105,-50,-59,105,-44,-132,-128,-65,105,-64,105,-84,-133,-70,-81,-83,105,-51,-133,-80,-68,-73,-87,105,-72,-71,]),'GRTR':([35,40,41,42,44,45,46,47,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,77,78,79,80,81,82,83,84,85,86,88,114,115,116,117,118,119,120,121,122,123,124,133,140,145,149,158,159,166,171,173,174,190,191,199,209,225,235,],[-133,60,-114,-109,-114,-111,-55,-133,-123,-123,-123,-123,-113,-123,-123,-123,-123,-123,-123,-127,-54,-133,-53,60,-133,-133,-133,-133,-133,-133,-133,-133,-133,-133,-107,-120,-126,-116,-119,-122,-124,-117,-125,-118,-121,-110,-133,-66,-133,60,-133,-55,-133,-55,-133,-112,-111,-55,-108,-111,241,-133,]),'ID':([2,11,12,13,14,15,17,19,27,35,39,40,41,42,44,45,46,47,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,71,74,76,77,78,79,80,81,82,83,84,85,86,88,96,98,100,101,102,104,107,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,128,131,133,137,139,140,141,142,143,144,145,149,155,158,159,163,164,166,171,173,174,175,178,183,192,194,199,205,213,214,215,224,226,229,233,235,237,238,239,241,242,244,248,253,254,255,256,257,258,259,262,266,267,268,269,276,282,283,284,290,291,293,295,297,298,],[3,-30,-28,-32,-29,-31,26,-27,32,45,-34,-133,-114,-109,-114,-111,-55,45,-35,-123,-123,-123,-123,-113,-123,-123,-123,-123,-123,-123,-127,-54,45,-53,-133,91,93,106,45,45,45,45,45,45,45,45,45,45,-107,106,-79,-78,106,106,106,-133,106,-76,-45,106,106,-120,-126,-116,-119,-122,-124,-117,-125,-118,-121,-110,106,156,45,161,164,-66,168,-50,170,-59,45,-133,106,45,-55,186,164,190,-55,45,-112,201,203,209,-44,217,-108,-132,-128,164,-65,106,246,-64,106,45,-123,-123,-123,-123,-123,-123,265,-84,209,209,209,209,209,209,161,-133,-70,-81,-83,106,-51,-133,-80,-68,-73,-87,106,-72,-71,]),'EQ':([35,40,41,42,44,45,46,47,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,77,78,79,80,81,82,83,84,85,86,88,114,115,116,117,118,119,120,121,122,123,124,133,140,145,149,158,159,166,171,173,174,190,191,199,209,225,235,],[-133,62,-114,-109,-114,-111,-55,-133,-123,-123,-123,-123,-113,-123,-123,-123,-123,-123,-123,-127,-54,-133,-53,62,-133,-133,-133,-133,-133,-133,-133,-133,-133,-133,-107,-120,-126,-116,-119,-122,-124,-117,-125,-118,-121,-110,-133,-66,-133,62,-133,-55,-133,-55,-133,-112,-111,-55,-108,-111,242,-133,]),'DECLARE':([5,39,52,76,96,98,100,101,102,104,107,109,110,111,112,113,128,142,144,155,192,205,213,215,224,229,233,253,266,267,268,269,276,282,283,284,290,291,293,295,297,298,],[7,-34,-35,107,107,-79,-78,107,107,107,-133,107,-76,-45,107,107,107,-50,-59,107,-44,-132,-128,-65,107,-64,107,-84,-133,-70,-81,-83,107,-51,-133,-80,-68,-73,-87,107,-72,-71,]),'LEFTKEY':([34,92,94,130,181,197,206,219,260,292,],[39,128,-82,155,-69,-69,224,233,276,295,]),'AND':([35,40,41,42,44,45,46,47,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,77,78,79,80,81,82,83,84,85,86,88,114,115,116,117,118,119,120,121,122,123,124,133,140,145,149,158,159,166,171,173,174,190,191,199,209,225,235,],[-133,53,-114,-109,-114,-111,-55,-133,-123,-123,-123,-123,-113,-123,-123,-123,-123,-123,-123,-127,-54,-133,-53,53,-133,-133,-133,-133,-133,-133,-133,-133,-133,-133,-107,-120,-126,-116,-119,-122,-124,-117,-125,-118,-121,-110,-133,-66,-133,53,-133,-55,-133,-55,-133,-112,-111,-55,-108,-111,237,-133,]),'INT':([7,20,51,90,107,153,266,],[12,12,12,12,12,12,12,]),'LEFTBRACK':([26,31,35,36,37,40,41,43,44,45,46,53,54,55,56,57,58,59,60,61,62,63,64,65,67,68,77,78,79,80,81,82,83,84,85,86,88,89,114,115,116,117,118,119,120,121,122,123,124,149,170,174,196,199,218,],[-22,-133,-133,47,-56,-133,-114,-52,-114,-111,-55,-123,-123,-123,-123,-113,-123,-123,-123,-123,-123,-123,-127,-54,-53,-133,-133,-133,-133,-133,-133,-133,-133,-133,-133,-133,-107,47,-120,-126,-116,-119,-122,-124,-117,-125,-118,-121,-110,-133,-63,-112,-133,-108,47,]),'LEFTPAR':([25,32,35,38,40,41,42,44,45,46,47,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,77,78,79,80,81,82,83,84,85,86,88,95,97,103,105,106,108,114,115,116,117,118,119,120,121,122,123,124,133,140,145,149,158,159,166,171,173,174,190,199,223,235,],[30,-16,42,51,-133,-114,-109,-114,-111,-55,42,-123,-123,-123,-123,-113,-123,-123,-123,-123,-123,-123,-127,-54,42,-53,-133,42,42,42,42,42,42,42,42,42,42,-107,131,133,137,139,141,145,-120,-126,-116,-119,-122,-124,-117,-125,-118,-121,-110,42,-66,42,-133,42,-55,42,-55,42,-112,141,-108,235,42,]),'BOOL':([7,20,51,90,107,153,266,],[15,15,15,15,15,15,15,]),'MAIN':([5,6,7,8,9,10,16,18,21,22,23,28,90,126,202,],[-133,-2,-133,-133,-5,25,-6,-23,-133,-4,-21,-11,-133,-8,-12,]),'OR':([35,40,41,42,44,45,46,47,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,77,78,79,80,81,82,83,84,85,86,88,114,115,116,117,118,119,120,121,122,123,124,133,140,145,149,158,159,166,171,173,174,190,191,199,209,225,235,],[-133,63,-114,-109,-114,-111,-55,-133,-123,-123,-123,-123,-113,-123,-123,-123,-123,-123,-123,-127,-54,-133,-53,63,-133,-133,-133,-133,-133,-133,-133,-133,-133,-133,-107,-120,-126,-116,-119,-122,-124,-117,-125,-118,-121,-110,-133,-66,-133,63,-133,-55,-133,-55,-133,-112,-111,-55,-108,-111,244,-133,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'meteOper':([53,54,55,56,58,59,60,61,62,63,237,238,239,241,242,244,277,278,279,],[77,78,79,80,81,82,83,84,85,86,254,255,256,257,258,259,286,287,288,]),'sacaPar':([124,],[149,]),'funct':([8,21,],[21,21,]),'output2':([139,164,214,],[162,187,228,]),'llamadaAFunct2':([141,],[167,]),'conditional':([76,96,101,102,104,109,112,113,128,155,224,233,276,295,],[96,96,96,96,96,96,96,96,96,96,96,96,96,96,]),'number':([35,47,66,77,78,79,80,81,82,83,84,85,86,133,145,158,166,173,183,212,235,254,255,256,257,258,259,],[40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,207,227,40,207,207,207,207,207,207,]),'expFor':([183,254,255,256,257,258,259,],[208,270,271,272,273,274,275,]),'while2':([133,158,235,],[157,182,252,]),'meteExp':([45,190,209,],[68,68,225,]),'llenaGoto':([297,],[298,]),'for3':([247,],[263,]),'declareRecursivoLocal':([107,266,],[142,282,]),'for2':([137,262,],[160,280,]),'array':([36,89,218,],[49,125,231,]),'functReturn':([151,],[176,]),'altaVarGlobal':([26,91,],[31,127,]),'type2':([7,20,51,90,107,153,266,],[19,19,19,19,19,19,19,]),'est':([76,96,101,102,104,109,112,113,128,155,224,233,276,295,],[99,132,135,136,138,146,147,148,151,179,236,251,285,296,]),'conditionalElse':([283,],[290,]),'program2':([5,],[6,]),'program3':([8,21,],[22,28,]),'exp2':([40,68,149,],[57,88,174,]),'llamadaAFunct':([76,96,101,102,104,109,112,113,128,155,166,224,233,276,295,],[101,101,101,101,101,101,101,101,101,101,188,101,101,101,101,]),'do-while':([76,96,101,102,104,109,112,113,128,155,224,233,276,295,],[98,98,98,98,98,98,98,98,98,98,98,98,98,98,]),'llamadaAFunct3':([168,],[193,]),'funct2':([51,],[73,]),'program':([0,],[1,]),'meteSalto':([94,],[130,]),'input':([76,96,101,102,104,109,112,113,128,155,224,233,276,295,],[102,102,102,102,102,102,102,102,102,102,102,102,102,102,]),'for4':([183,],[211,]),'type':([7,20,51,90,107,153,266,],[17,27,74,17,143,178,143,]),'empty':([5,7,8,21,31,35,36,40,47,48,51,66,68,76,77,78,79,80,81,82,83,84,85,86,89,90,96,101,102,104,107,109,112,113,127,128,129,133,139,141,145,149,151,155,158,164,166,168,173,183,196,212,214,218,222,224,225,230,233,235,247,254,255,256,257,258,259,266,276,281,283,289,295,],[9,18,23,23,37,46,50,64,46,72,75,46,64,111,46,46,46,46,46,46,46,46,46,46,50,18,111,111,111,111,144,111,111,111,72,111,154,159,165,169,171,64,177,111,159,165,191,195,171,210,37,210,165,232,154,111,243,249,111,159,264,210,210,210,210,210,210,144,111,37,291,249,111,]),'gotoVCuad':([268,],[284,]),'llenaMain':([39,],[52,]),'funct3':([129,222,],[152,234,]),'declare2Local':([218,],[230,]),'assignment':([76,96,101,102,104,109,112,113,128,155,224,233,276,295,],[104,104,104,104,104,104,104,104,104,104,104,104,104,104,]),'llenaCuadF':([253,],[269,]),'assignmentDecl':([31,196,281,],[36,218,289,]),'generaCuad':([174,189,227,],[199,216,247,]),'cuerpo':([10,],[24,]),'altaVarLocal':([93,170,203,265,],[129,196,222,281,]),'cycles':([76,96,101,102,104,109,112,113,128,155,224,233,276,295,],[109,109,109,109,109,109,109,109,109,109,109,109,109,109,]),'declare2':([36,],[48,]),'declare3':([48,127,],[70,150,]),'gotoCuad':([267,],[283,]),'meteNum':([41,44,],[65,67,]),'gotoFCuad':([181,197,],[206,219,]),'declare3Local':([230,289,],[250,294,]),'declareLocal':([76,96,101,102,104,109,112,113,128,155,224,233,276,295,],[113,113,113,113,113,113,113,113,113,113,113,113,113,113,]),'parte3For':([226,],[245,]),'for':([76,96,101,102,104,109,112,113,128,155,224,233,276,295,],[100,100,100,100,100,100,100,100,100,100,100,100,100,100,]),'goToMainQuad':([6,],[10,]),'cuadFor':([184,],[212,]),'altaModuloMain':([52,],[76,]),'altaModulo':([32,],[38,]),'expFor2':([225,],[240,]),'meteVar':([140,],[166,]),'while':([76,96,101,102,104,109,112,113,128,155,224,233,276,295,],[110,110,110,110,110,110,110,110,110,110,110,110,110,110,]),'altaPrograma':([3,],[4,]),'declareRecursivo':([7,90,],[16,126,]),'conditional2':([145,173,],[172,198,]),'exp':([35,47,66,77,78,79,80,81,82,83,84,85,86,133,145,158,166,173,235,],[43,69,87,114,115,116,117,118,119,120,121,122,123,158,173,158,189,173,158,]),'meteID':([246,],[261,]),'output':([76,96,101,102,104,109,112,113,128,155,224,233,276,295,],[112,112,112,112,112,112,112,112,112,112,112,112,112,112,]),'metePar':([42,],[66,]),'declare':([5,],[8,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> PROGRAM ID altaPrograma SEMICOLON program2 goToMainQuad cuerpo END SEMICOLON','program',9,'p_program','parser.py',48),
  ('goToMainQuad -> <empty>','goToMainQuad',0,'p_goToMainQuad','parser.py',51),
  ('altaPrograma -> <empty>','altaPrograma',0,'p_altaPrograma','parser.py',56),
  ('program2 -> declare program3','program2',2,'p_program2','parser.py',66),
  ('program2 -> empty','program2',1,'p_program2Empty','parser.py',69),
  ('declare -> DECLARE declareRecursivo','declare',2,'p_declare','parser.py',72),
  ('declare -> empty','declare',1,'p_declareEmpty','parser.py',76),
  ('declareRecursivo -> type ID altaVarGlobal assignmentDecl declare2 declare3 SEMICOLON declareRecursivo','declareRecursivo',8,'p_declareRecursivo','parser.py',79),
  ('declare2 -> array','declare2',1,'p_declare2','parser.py',83),
  ('declare3 -> COMMA ID altaVarGlobal declare3','declare3',4,'p_declare3','parser.py',86),
  ('program3 -> funct program3','program3',2,'p_program3','parser.py',90),
  ('funct -> FUNCTION type ID altaModulo LEFTPAR funct2 RIGHTPAR LEFTKEY est functReturn RIGHTKEY','funct',11,'p_funct','parser.py',93),
  ('functReturn -> RETURN NUMBER SEMICOLON','functReturn',3,'p_functReturn','parser.py',97),
  ('functReturn -> RETURN ID SEMICOLON','functReturn',3,'p_functReturnID','parser.py',101),
  ('functReturn -> empty','functReturn',1,'p_functReturnEmpty','parser.py',105),
  ('altaModulo -> <empty>','altaModulo',0,'p_altaModulo','parser.py',108),
  ('funct2 -> type ID altaVarLocal funct3','funct2',4,'p_funct2','parser.py',120),
  ('funct3 -> COMMA type ID altaVarLocal funct3','funct3',5,'p_funct3','parser.py',124),
  ('funct2 -> empty','funct2',1,'p_funct2Empty','parser.py',128),
  ('funct3 -> empty','funct3',1,'p_funct3Empty','parser.py',131),
  ('program3 -> empty','program3',1,'p_program3Empty','parser.py',134),
  ('altaVarGlobal -> <empty>','altaVarGlobal',0,'p_altaVarGlobal','parser.py',137),
  ('declareRecursivo -> empty','declareRecursivo',1,'p_declareResursivoEmpty','parser.py',147),
  ('declare3 -> empty','declare3',1,'p_declare3Empty','parser.py',150),
  ('array -> LEFTBRACK exp RIGHTBRACK array','array',4,'p_array','parser.py',153),
  ('array -> empty','array',1,'p_arrayEmpty','parser.py',157),
  ('type -> type2','type',1,'p_type','parser.py',160),
  ('type2 -> INT','type2',1,'p_type2','parser.py',163),
  ('type2 -> FLOAT','type2',1,'p_type2Float','parser.py',169),
  ('type2 -> STRING','type2',1,'p_type2String','parser.py',175),
  ('type2 -> BOOL','type2',1,'p_type2Bool','parser.py',181),
  ('type2 -> VOID','type2',1,'p_type2Void','parser.py',187),
  ('cuerpo -> MAIN LEFTPAR RIGHTPAR LEFTKEY llenaMain altaModuloMain est RIGHTKEY','cuerpo',8,'p_cuerpo','parser.py',193),
  ('llenaMain -> <empty>','llenaMain',0,'p_llenaMain','parser.py',197),
  ('altaModuloMain -> <empty>','altaModuloMain',0,'p_altaModuloMain','parser.py',201),
  ('est -> conditional est','est',2,'p_est','parser.py',211),
  ('est -> declareLocal est','est',2,'p_estVars','parser.py',214),
  ('est -> cycles est','est',2,'p_estCycle','parser.py',217),
  ('est -> input est','est',2,'p_estRead','parser.py',220),
  ('est -> output est','est',2,'p_estWrite','parser.py',223),
  ('est -> assignment est','est',2,'p_estAassignment','parser.py',226),
  ('est -> llamadaAFunct est','est',2,'p_estFunct','parser.py',229),
  ('est -> empty','est',1,'p_estEmpty','parser.py',232),
  ('llamadaAFunct -> ID LEFTPAR llamadaAFunct2 RIGHTPAR','llamadaAFunct',4,'p_llamadaAFunct','parser.py',235),
  ('llamadaAFunct -> empty','llamadaAFunct',1,'p_llamadaAFunctEmpty','parser.py',239),
  ('llamadaAFunct2 -> ID llamadaAFunct3','llamadaAFunct2',2,'p_llamadaAFunct2','parser.py',242),
  ('llamadaAFunct3 -> COMMA ID','llamadaAFunct3',2,'p_llamadaAFunct3','parser.py',246),
  ('llamadaAFunct3 -> empty','llamadaAFunct3',1,'p_llamadaAFunct3Empty','parser.py',250),
  ('llamadaAFunct2 -> empty','llamadaAFunct2',1,'p_llamadaAFunct2Empty','parser.py',253),
  ('declareLocal -> DECLARE declareRecursivoLocal','declareLocal',2,'p_declareLocal','parser.py',256),
  ('declareRecursivoLocal -> type ID altaVarLocal assignmentDecl declare2Local declare3Local SEMICOLON declareRecursivoLocal','declareRecursivoLocal',8,'p_declareRecursivoLocal','parser.py',260),
  ('assignmentDecl -> ASSGN exp','assignmentDecl',2,'p_assignmentDeclare','parser.py',264),
  ('number -> INTEGER meteNum','number',2,'p_number','parser.py',268),
  ('number -> FLOAT meteNum','number',2,'p_numberFloat','parser.py',272),
  ('number -> empty','number',1,'p_numberEmpty','parser.py',275),
  ('assignmentDecl -> empty','assignmentDecl',1,'p_assignmentDeclareEmpty','parser.py',279),
  ('declare2Local -> array','declare2Local',1,'p_declare2Local','parser.py',282),
  ('declare3Local -> COMMA ID altaVarLocal assignmentDecl declare3Local','declare3Local',5,'p_declare3Local','parser.py',285),
  ('declareRecursivoLocal -> empty','declareRecursivoLocal',1,'p_declareResursivoEmptyLocal','parser.py',288),
  ('declareLocal -> empty','declareLocal',1,'p_declareEmptyLocal','parser.py',291),
  ('declare2Local -> empty','declare2Local',1,'p_declar2EmptyLocal','parser.py',294),
  ('declare3Local -> empty','declare3Local',1,'p_declare3EmptyLocal','parser.py',297),
  ('altaVarLocal -> <empty>','altaVarLocal',0,'p_altaVarLocal','parser.py',300),
  ('assignment -> ID ASSGN meteVar exp generaCuad SEMICOLON','assignment',6,'p_assignment','parser.py',311),
  ('assignment -> ID ASSGN meteVar llamadaAFunct SEMICOLON','assignment',5,'p_assignmentFUNCT','parser.py',315),
  ('meteVar -> <empty>','meteVar',0,'p_meteVar','parser.py',321),
  ('assignment -> empty','assignment',1,'p_assignmentEmpty','parser.py',343),
  ('conditional -> IF LEFTPAR conditional2 RIGHTPAR gotoFCuad LEFTKEY est RIGHTKEY gotoCuad conditionalElse','conditional',10,'p_conditional','parser.py',346),
  ('gotoFCuad -> <empty>','gotoFCuad',0,'p_gotoFCuad','parser.py',350),
  ('gotoCuad -> <empty>','gotoCuad',0,'p_goToCuad','parser.py',354),
  ('conditionalElse -> ELSE LEFTKEY est RIGHTKEY llenaGoto','conditionalElse',5,'p_conditionalElse','parser.py',358),
  ('llenaGoto -> <empty>','llenaGoto',0,'p_llenaGoto','parser.py',362),
  ('conditionalElse -> empty','conditionalElse',1,'p_conditionalElseEmpty','parser.py',366),
  ('conditional2 -> exp conditional2','conditional2',2,'p_conditional2','parser.py',369),
  ('conditional2 -> empty','conditional2',1,'p_conditional2Empty','parser.py',372),
  ('cycles -> while','cycles',1,'p_cycles','parser.py',375),
  ('cycles -> empty','cycles',1,'p_cyclesEmpty','parser.py',378),
  ('cycles -> for','cycles',1,'p_cyclesFor','parser.py',381),
  ('cycles -> do-while','cycles',1,'p_cyclesDoWhile','parser.py',384),
  ('do-while -> DO meteSalto LEFTKEY est RIGHTKEY WHILE LEFTPAR while2 RIGHTPAR gotoVCuad','do-while',10,'p_doWhile','parser.py',387),
  ('gotoVCuad -> <empty>','gotoVCuad',0,'p_gotoVCuad','parser.py',390),
  ('meteSalto -> <empty>','meteSalto',0,'p_meteSalto','parser.py',394),
  ('while -> WHILE LEFTPAR while2 RIGHTPAR gotoFCuad LEFTKEY est RIGHTKEY llenaCuadF','while',9,'p_whileClass','parser.py',398),
  ('llenaCuadF -> <empty>','llenaCuadF',0,'p_llenaCuadF','parser.py',401),
  ('while2 -> exp while2','while2',2,'p_while2','parser.py',405),
  ('while2 -> empty','while2',1,'p_while2Empty','parser.py',408),
  ('for -> FOR LEFTPAR for2 SEMICOLON for4 SEMICOLON parte3For RIGHTPAR LEFTKEY est RIGHTKEY','for',11,'p_forClass','parser.py',411),
  ('for2 -> ID ASSGN cuadFor number generaCuad for3','for2',6,'p_for2','parser.py',415),
  ('cuadFor -> <empty>','cuadFor',0,'p_cuadFor','parser.py',419),
  ('for3 -> COMMA for2','for3',2,'p_for3','parser.py',422),
  ('for3 -> empty','for3',1,'p_for3Empty','parser.py',426),
  ('for4 -> expFor','for4',1,'p_for4','parser.py',429),
  ('parte3For -> ID meteID ACTINCR meteOper','parte3For',4,'p_parte3ForSUM','parser.py',432),
  ('meteID -> <empty>','meteID',0,'p_meteID','parser.py',436),
  ('parte3For -> ID meteID ACTINCRVALOR meteOper','parte3For',4,'p_parte3ForINCRVAL','parser.py',444),
  ('parte3For -> ID meteID ACTDECRVALOR meteOper','parte3For',4,'p_parte3ForMINUS','parser.py',448),
  ('expFor -> ID meteExp expFor2','expFor',3,'p_expFor','parser.py',451),
  ('expFor -> number','expFor',1,'p_expForNumber','parser.py',454),
  ('expFor2 -> LESS meteOper expFor','expFor2',3,'p_expFor2','parser.py',457),
  ('expFor2 -> GRTR meteOper expFor','expFor2',3,'p_exprFor2Grtr','parser.py',461),
  ('expFor2 -> EQ meteOper expFor','expFor2',3,'p_expFor2Equal','parser.py',465),
  ('expFor2 -> NOTEQ meteOper expFor','expFor2',3,'p_expFor2NotEq','parser.py',469),
  ('expFor2 -> AND meteOper expFor','expFor2',3,'p_expFor2And','parser.py',473),
  ('expFor2 -> OR meteOper expFor','expFor2',3,'p_expFor2OR','parser.py',477),
  ('expFor2 -> <empty>','expFor2',0,'p_expForActCont','parser.py',481),
  ('expFor2 -> empty','expFor2',1,'p_expFor2Empty','parser.py',484),
  ('exp -> ID meteExp exp2','exp',3,'p_exp','parser.py',487),
  ('exp -> LEFTPAR metePar exp RIGHTPAR sacaPar exp2 generaCuad','exp',7,'p_expPar','parser.py',491),
  ('metePar -> <empty>','metePar',0,'p_metePar','parser.py',494),
  ('sacaPar -> <empty>','sacaPar',0,'p_sacaPar','parser.py',498),
  ('meteExp -> <empty>','meteExp',0,'p_meteExp','parser.py',502),
  ('generaCuad -> <empty>','generaCuad',0,'p_generaCuad','parser.py',525),
  ('exp -> number exp2','exp',2,'p_expNUMERO','parser.py',529),
  ('meteNum -> <empty>','meteNum',0,'p_meteNum','parser.py',533),
  ('exp -> empty','exp',1,'p_expVACIA','parser.py',541),
  ('exp2 -> LESS meteOper exp','exp2',3,'p_exp2','parser.py',544),
  ('exp2 -> GRTR meteOper exp','exp2',3,'p_expr2Grtr','parser.py',548),
  ('exp2 -> EQ meteOper exp','exp2',3,'p_exp2Equal','parser.py',552),
  ('exp2 -> NOTEQ meteOper exp','exp2',3,'p_exp2NotEq','parser.py',556),
  ('exp2 -> AND meteOper exp','exp2',3,'p_exp2And','parser.py',560),
  ('exp2 -> OR meteOper exp','exp2',3,'p_exp2OR','parser.py',564),
  ('exp2 -> SUM meteOper exp','exp2',3,'p_exp2SUM','parser.py',569),
  ('meteOper -> <empty>','meteOper',0,'p_meteOper','parser.py',575),
  ('exp2 -> MINUS meteOper exp','exp2',3,'p_exp2MINUS','parser.py',579),
  ('exp2 -> MULTP meteOper exp','exp2',3,'p_exp2MULTP','parser.py',583),
  ('exp2 -> DIVIDE meteOper exp','exp2',3,'p_exp2DIVIDE','parser.py',587),
  ('exp2 -> empty','exp2',1,'p_exp2Empty','parser.py',591),
  ('output -> WRITE LEFTPAR output2 RIGHTPAR SEMICOLON','output',5,'p_output','parser.py',596),
  ('output2 -> ID output2','output2',2,'p_output2','parser.py',600),
  ('output2 -> QUOTE ID QUOTE output2','output2',4,'p_output2Quotes','parser.py',604),
  ('output2 -> empty','output2',1,'p_output2Empty','parser.py',607),
  ('input -> READ LEFTPAR ID RIGHTPAR SEMICOLON','input',5,'p_input','parser.py',610),
  ('empty -> <empty>','empty',0,'p_empty','parser.py',614),
  ('circulo -> LEFTPAR INTEGER COMMA STRING COMMA BOOL COMMA INTEGER COMMA INTEGER RIGHTPAR SEMICOLON','circulo',12,'p_circle','parser.py',619),
  ('cuadro -> LEFTPAR INTEGER COMMA STRING COMMA BOOL COMMA INTEGER COMMA INTEGER RIGHTPAR SEMICOLON','cuadro',12,'p_square','parser.py',622),
  ('triangulo -> LEFTPAR INTEGER COMMA INTEGER COMMA INTEGER COMMA STRING COMMA BOOL COMMA INTEGER COMMA INTEGER COMMA INTEGER RIGHTPAR SEMICOLON','triangulo',18,'p_triangle','parser.py',625),
  ('linea -> LEFTPAR INTEGER COMMA STRING COMMA INTEGER COMMA INTEGER COMMA INTEGER COMMA INTEGER RIGHTPAR SEMICOLON','linea',14,'p_line','parser.py',628),
  ('rectangulo -> LEFTPAR INTEGER COMMA INTEGER COMMA STRING COMMA BOOL COMMA INTEGER COMMA INTEGER COMMA INTEGER RIGHTPAR SEMICOLON','rectangulo',16,'p_rectangle','parser.py',631),
]
