// Generated from /Users/ricardolicea/OneDrive/Tecnol?gico de Monterrey/8vo Semestre/EM18 Dise?o de Compiladores/MIRI/Miri.g4 by ANTLR 4.7.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class MiriParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.7.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		PROGRAM=1, END=2, DECLARE=3, MAIN=4, IF=5, ELSE=6, WHILE=7, FOR=8, DO_WHILE=9, 
		WRITE=10, READ=11, FUNCTION=12, ARCH=13, CIRCLE=14, SQUARE=15, AND=16, 
		OR=17, RETURN=18, PAINT=19, BOOL=20, FLOAT=21, ID=22, INT=23, STRING=24, 
		ASSGN=25, COMMA=26, SEMICOLON=27, DOT=28, COLON=29, LEFTBRACK=30, RIGHTBRACK=31, 
		LEFTPAR=32, RIGHTPAR=33, LEFTKEY=34, RIGHTKEY=35, QUOTE=36, SUM=37, MINUS=38, 
		MULTP=39, DIVIDE=40, GRTR=41, LESS=42, EQ=43, NOTEQ=44, GRTREQ=45, LESSEQ=46;
	public static final int
		RULE_program = 0, RULE_declare = 1, RULE_dataType = 2, RULE_array = 3, 
		RULE_cuerpo = 4, RULE_estatutos = 5, RULE_assignment = 6, RULE_conditional = 7, 
		RULE_cycle = 8, RULE_while = 9, RULE_do_while = 10, RULE_for = 11, RULE_exp = 12, 
		RULE_output = 13, RULE_inputData = 14, RULE_llamada_f = 15, RULE_arithmeticOperator = 16, 
		RULE_geofig = 17, RULE_circle = 18, RULE_square = 19, RULE_arch = 20;
	public static final String[] ruleNames = {
		"program", "declare", "dataType", "array", "cuerpo", "estatutos", "assignment", 
		"conditional", "cycle", "while", "do_while", "for", "exp", "output", "inputData", 
		"llamada_f", "arithmeticOperator", "geofig", "circle", "square", "arch"
	};

	private static final String[] _LITERAL_NAMES = {
		null, "'program'", "'end'", "'declare'", "'main'", "'if'", "'else'", "'while'", 
		"'for'", "'do'", "'write'", "'read'", "'funct'", "'arch'", "'circle'", 
		"'square'", "'and'", "'or'", "'return'", "'paint'", null, null, null, 
		null, null, "'='", "','", "';'", "'.'", "':'", "'['", "']'", "'('", "')'", 
		"'{'", "'}'", "'\"'", "'+'", "'-'", "'*'", "'/'", "'>'", "'<'", "'=='", 
		"'!='", "'>='", "'<='"
	};
	private static final String[] _SYMBOLIC_NAMES = {
		null, "PROGRAM", "END", "DECLARE", "MAIN", "IF", "ELSE", "WHILE", "FOR", 
		"DO_WHILE", "WRITE", "READ", "FUNCTION", "ARCH", "CIRCLE", "SQUARE", "AND", 
		"OR", "RETURN", "PAINT", "BOOL", "FLOAT", "ID", "INT", "STRING", "ASSGN", 
		"COMMA", "SEMICOLON", "DOT", "COLON", "LEFTBRACK", "RIGHTBRACK", "LEFTPAR", 
		"RIGHTPAR", "LEFTKEY", "RIGHTKEY", "QUOTE", "SUM", "MINUS", "MULTP", "DIVIDE", 
		"GRTR", "LESS", "EQ", "NOTEQ", "GRTREQ", "LESSEQ"
	};
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "Miri.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public MiriParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}
	public static class ProgramContext extends ParserRuleContext {
		public TerminalNode PROGRAM() { return getToken(MiriParser.PROGRAM, 0); }
		public TerminalNode ID() { return getToken(MiriParser.ID, 0); }
		public List<TerminalNode> SEMICOLON() { return getTokens(MiriParser.SEMICOLON); }
		public TerminalNode SEMICOLON(int i) {
			return getToken(MiriParser.SEMICOLON, i);
		}
		public TerminalNode END() { return getToken(MiriParser.END, 0); }
		public TerminalNode DECLARE() { return getToken(MiriParser.DECLARE, 0); }
		public Llamada_fContext llamada_f() {
			return getRuleContext(Llamada_fContext.class,0);
		}
		public CuerpoContext cuerpo() {
			return getRuleContext(CuerpoContext.class,0);
		}
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_program);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(42);
			match(PROGRAM);
			setState(43);
			match(ID);
			setState(44);
			match(SEMICOLON);
			setState(48);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case DECLARE:
				{
				setState(45);
				match(DECLARE);
				setState(46);
				llamada_f();
				}
				break;
			case MAIN:
				{
				setState(47);
				cuerpo();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			setState(50);
			match(END);
			setState(51);
			match(SEMICOLON);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class DeclareContext extends ParserRuleContext {
		public TerminalNode DECLARE() { return getToken(MiriParser.DECLARE, 0); }
		public DataTypeContext dataType() {
			return getRuleContext(DataTypeContext.class,0);
		}
		public TerminalNode ID() { return getToken(MiriParser.ID, 0); }
		public TerminalNode COLON() { return getToken(MiriParser.COLON, 0); }
		public TerminalNode SEMICOLON() { return getToken(MiriParser.SEMICOLON, 0); }
		public ArrayContext array() {
			return getRuleContext(ArrayContext.class,0);
		}
		public DeclareContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_declare; }
	}

	public final DeclareContext declare() throws RecognitionException {
		DeclareContext _localctx = new DeclareContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_declare);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(53);
			match(DECLARE);
			setState(54);
			dataType();
			setState(55);
			match(ID);
			setState(59);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case COLON:
				{
				setState(56);
				match(COLON);
				}
				break;
			case SEMICOLON:
				{
				setState(57);
				match(SEMICOLON);
				}
				break;
			case LEFTBRACK:
				{
				setState(58);
				array();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class DataTypeContext extends ParserRuleContext {
		public TerminalNode INT() { return getToken(MiriParser.INT, 0); }
		public TerminalNode FLOAT() { return getToken(MiriParser.FLOAT, 0); }
		public TerminalNode STRING() { return getToken(MiriParser.STRING, 0); }
		public TerminalNode BOOL() { return getToken(MiriParser.BOOL, 0); }
		public DataTypeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_dataType; }
	}

	public final DataTypeContext dataType() throws RecognitionException {
		DataTypeContext _localctx = new DataTypeContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_dataType);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(61);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << BOOL) | (1L << FLOAT) | (1L << INT) | (1L << STRING))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ArrayContext extends ParserRuleContext {
		public List<TerminalNode> LEFTBRACK() { return getTokens(MiriParser.LEFTBRACK); }
		public TerminalNode LEFTBRACK(int i) {
			return getToken(MiriParser.LEFTBRACK, i);
		}
		public List<ExpContext> exp() {
			return getRuleContexts(ExpContext.class);
		}
		public ExpContext exp(int i) {
			return getRuleContext(ExpContext.class,i);
		}
		public List<TerminalNode> RIGHTBRACK() { return getTokens(MiriParser.RIGHTBRACK); }
		public TerminalNode RIGHTBRACK(int i) {
			return getToken(MiriParser.RIGHTBRACK, i);
		}
		public TerminalNode SEMICOLON() { return getToken(MiriParser.SEMICOLON, 0); }
		public ArrayContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_array; }
	}

	public final ArrayContext array() throws RecognitionException {
		ArrayContext _localctx = new ArrayContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_array);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(63);
			match(LEFTBRACK);
			setState(64);
			exp();
			setState(70);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,2,_ctx) ) {
			case 1:
				{
				setState(65);
				match(RIGHTBRACK);
				setState(66);
				match(LEFTBRACK);
				setState(67);
				exp();
				setState(68);
				match(RIGHTBRACK);
				}
				break;
			}
			setState(72);
			match(RIGHTBRACK);
			setState(73);
			match(SEMICOLON);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class CuerpoContext extends ParserRuleContext {
		public TerminalNode MAIN() { return getToken(MiriParser.MAIN, 0); }
		public TerminalNode LEFTPAR() { return getToken(MiriParser.LEFTPAR, 0); }
		public TerminalNode RIGHTPAR() { return getToken(MiriParser.RIGHTPAR, 0); }
		public TerminalNode LEFTKEY() { return getToken(MiriParser.LEFTKEY, 0); }
		public EstatutosContext estatutos() {
			return getRuleContext(EstatutosContext.class,0);
		}
		public TerminalNode RIGHTKEY() { return getToken(MiriParser.RIGHTKEY, 0); }
		public CuerpoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_cuerpo; }
	}

	public final CuerpoContext cuerpo() throws RecognitionException {
		CuerpoContext _localctx = new CuerpoContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_cuerpo);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(75);
			match(MAIN);
			setState(76);
			match(LEFTPAR);
			setState(77);
			match(RIGHTPAR);
			setState(78);
			match(LEFTKEY);
			setState(79);
			estatutos();
			setState(80);
			match(RIGHTKEY);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class EstatutosContext extends ParserRuleContext {
		public ConditionalContext conditional() {
			return getRuleContext(ConditionalContext.class,0);
		}
		public CycleContext cycle() {
			return getRuleContext(CycleContext.class,0);
		}
		public TerminalNode READ() { return getToken(MiriParser.READ, 0); }
		public TerminalNode WRITE() { return getToken(MiriParser.WRITE, 0); }
		public AssignmentContext assignment() {
			return getRuleContext(AssignmentContext.class,0);
		}
		public Llamada_fContext llamada_f() {
			return getRuleContext(Llamada_fContext.class,0);
		}
		public EstatutosContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_estatutos; }
	}

	public final EstatutosContext estatutos() throws RecognitionException {
		EstatutosContext _localctx = new EstatutosContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_estatutos);
		try {
			setState(88);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case IF:
				enterOuterAlt(_localctx, 1);
				{
				setState(82);
				conditional();
				}
				break;
			case WHILE:
			case FOR:
			case DO_WHILE:
				enterOuterAlt(_localctx, 2);
				{
				setState(83);
				cycle();
				}
				break;
			case READ:
				enterOuterAlt(_localctx, 3);
				{
				setState(84);
				match(READ);
				}
				break;
			case WRITE:
				enterOuterAlt(_localctx, 4);
				{
				setState(85);
				match(WRITE);
				}
				break;
			case ID:
				enterOuterAlt(_localctx, 5);
				{
				setState(86);
				assignment();
				}
				break;
			case FUNCTION:
				enterOuterAlt(_localctx, 6);
				{
				setState(87);
				llamada_f();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class AssignmentContext extends ParserRuleContext {
		public List<TerminalNode> ID() { return getTokens(MiriParser.ID); }
		public TerminalNode ID(int i) {
			return getToken(MiriParser.ID, i);
		}
		public TerminalNode ASSGN() { return getToken(MiriParser.ASSGN, 0); }
		public TerminalNode SEMICOLON() { return getToken(MiriParser.SEMICOLON, 0); }
		public TerminalNode FUNCTION() { return getToken(MiriParser.FUNCTION, 0); }
		public ArrayContext array() {
			return getRuleContext(ArrayContext.class,0);
		}
		public AssignmentContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assignment; }
	}

	public final AssignmentContext assignment() throws RecognitionException {
		AssignmentContext _localctx = new AssignmentContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_assignment);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(90);
			match(ID);
			setState(92);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==LEFTBRACK) {
				{
				setState(91);
				array();
				}
			}

			setState(94);
			match(ASSGN);
			setState(95);
			_la = _input.LA(1);
			if ( !(_la==FUNCTION || _la==ID) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(96);
			match(SEMICOLON);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ConditionalContext extends ParserRuleContext {
		public TerminalNode IF() { return getToken(MiriParser.IF, 0); }
		public TerminalNode LEFTPAR() { return getToken(MiriParser.LEFTPAR, 0); }
		public TerminalNode RIGHTPAR() { return getToken(MiriParser.RIGHTPAR, 0); }
		public List<TerminalNode> LEFTKEY() { return getTokens(MiriParser.LEFTKEY); }
		public TerminalNode LEFTKEY(int i) {
			return getToken(MiriParser.LEFTKEY, i);
		}
		public List<EstatutosContext> estatutos() {
			return getRuleContexts(EstatutosContext.class);
		}
		public EstatutosContext estatutos(int i) {
			return getRuleContext(EstatutosContext.class,i);
		}
		public List<TerminalNode> RIGHTKEY() { return getTokens(MiriParser.RIGHTKEY); }
		public TerminalNode RIGHTKEY(int i) {
			return getToken(MiriParser.RIGHTKEY, i);
		}
		public List<ExpContext> exp() {
			return getRuleContexts(ExpContext.class);
		}
		public ExpContext exp(int i) {
			return getRuleContext(ExpContext.class,i);
		}
		public TerminalNode ELSE() { return getToken(MiriParser.ELSE, 0); }
		public ConditionalContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_conditional; }
	}

	public final ConditionalContext conditional() throws RecognitionException {
		ConditionalContext _localctx = new ConditionalContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_conditional);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(98);
			match(IF);
			setState(99);
			match(LEFTPAR);
			setState(101); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(100);
				exp();
				}
				}
				setState(103); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==ID || _la==ASSGN );
			setState(105);
			match(RIGHTPAR);
			setState(106);
			match(LEFTKEY);
			setState(107);
			estatutos();
			setState(108);
			match(RIGHTKEY);
			setState(114);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ELSE) {
				{
				setState(109);
				match(ELSE);
				setState(110);
				match(LEFTKEY);
				setState(111);
				estatutos();
				setState(112);
				match(RIGHTKEY);
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class CycleContext extends ParserRuleContext {
		public WhileContext while() {
			return getRuleContext(WhileContext.class,0);
		}
		public Do_whileContext do_while() {
			return getRuleContext(Do_whileContext.class,0);
		}
		public ForContext for() {
			return getRuleContext(ForContext.class,0);
		}
		public CycleContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_cycle; }
	}

	public final CycleContext cycle() throws RecognitionException {
		CycleContext _localctx = new CycleContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_cycle);
		try {
			setState(119);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case WHILE:
				enterOuterAlt(_localctx, 1);
				{
				setState(116);
				while();
				}
				break;
			case DO_WHILE:
				enterOuterAlt(_localctx, 2);
				{
				setState(117);
				do_while();
				}
				break;
			case FOR:
				enterOuterAlt(_localctx, 3);
				{
				setState(118);
				for();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class WhileContext extends ParserRuleContext {
		public TerminalNode WHILE() { return getToken(MiriParser.WHILE, 0); }
		public TerminalNode LEFTPAR() { return getToken(MiriParser.LEFTPAR, 0); }
		public ExpContext exp() {
			return getRuleContext(ExpContext.class,0);
		}
		public TerminalNode RIGHTPAR() { return getToken(MiriParser.RIGHTPAR, 0); }
		public TerminalNode LEFTKEY() { return getToken(MiriParser.LEFTKEY, 0); }
		public EstatutosContext estatutos() {
			return getRuleContext(EstatutosContext.class,0);
		}
		public TerminalNode RIGHTKEY() { return getToken(MiriParser.RIGHTKEY, 0); }
		public WhileContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_while; }
	}

	public final WhileContext while() throws RecognitionException {
		WhileContext _localctx = new WhileContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_while);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(121);
			match(WHILE);
			setState(122);
			match(LEFTPAR);
			setState(123);
			exp();
			setState(124);
			match(RIGHTPAR);
			setState(125);
			match(LEFTKEY);
			setState(126);
			estatutos();
			setState(127);
			match(RIGHTKEY);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Do_whileContext extends ParserRuleContext {
		public TerminalNode DO_WHILE() { return getToken(MiriParser.DO_WHILE, 0); }
		public TerminalNode LEFTKEY() { return getToken(MiriParser.LEFTKEY, 0); }
		public EstatutosContext estatutos() {
			return getRuleContext(EstatutosContext.class,0);
		}
		public TerminalNode RIGHTKEY() { return getToken(MiriParser.RIGHTKEY, 0); }
		public TerminalNode WHILE() { return getToken(MiriParser.WHILE, 0); }
		public TerminalNode LEFTPAR() { return getToken(MiriParser.LEFTPAR, 0); }
		public ExpContext exp() {
			return getRuleContext(ExpContext.class,0);
		}
		public TerminalNode RIGHTPAR() { return getToken(MiriParser.RIGHTPAR, 0); }
		public Do_whileContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_do_while; }
	}

	public final Do_whileContext do_while() throws RecognitionException {
		Do_whileContext _localctx = new Do_whileContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_do_while);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(129);
			match(DO_WHILE);
			setState(130);
			match(LEFTKEY);
			setState(131);
			estatutos();
			setState(132);
			match(RIGHTKEY);
			setState(133);
			match(WHILE);
			setState(134);
			match(LEFTPAR);
			setState(135);
			exp();
			setState(136);
			match(RIGHTPAR);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ForContext extends ParserRuleContext {
		public TerminalNode FOR() { return getToken(MiriParser.FOR, 0); }
		public TerminalNode LEFTPAR() { return getToken(MiriParser.LEFTPAR, 0); }
		public List<TerminalNode> SEMICOLON() { return getTokens(MiriParser.SEMICOLON); }
		public TerminalNode SEMICOLON(int i) {
			return getToken(MiriParser.SEMICOLON, i);
		}
		public TerminalNode RIGHTPAR() { return getToken(MiriParser.RIGHTPAR, 0); }
		public TerminalNode LEFTKEY() { return getToken(MiriParser.LEFTKEY, 0); }
		public EstatutosContext estatutos() {
			return getRuleContext(EstatutosContext.class,0);
		}
		public TerminalNode RIGHTKEY() { return getToken(MiriParser.RIGHTKEY, 0); }
		public List<TerminalNode> ID() { return getTokens(MiriParser.ID); }
		public TerminalNode ID(int i) {
			return getToken(MiriParser.ID, i);
		}
		public List<TerminalNode> ASSGN() { return getTokens(MiriParser.ASSGN); }
		public TerminalNode ASSGN(int i) {
			return getToken(MiriParser.ASSGN, i);
		}
		public List<ExpContext> exp() {
			return getRuleContexts(ExpContext.class);
		}
		public ExpContext exp(int i) {
			return getRuleContext(ExpContext.class,i);
		}
		public List<ArithmeticOperatorContext> arithmeticOperator() {
			return getRuleContexts(ArithmeticOperatorContext.class);
		}
		public ArithmeticOperatorContext arithmeticOperator(int i) {
			return getRuleContext(ArithmeticOperatorContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(MiriParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(MiriParser.COMMA, i);
		}
		public ForContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_for; }
	}

	public final ForContext for() throws RecognitionException {
		ForContext _localctx = new ForContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_for);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(138);
			match(FOR);
			setState(139);
			match(LEFTPAR);
			setState(148);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==ID) {
				{
				{
				setState(140);
				match(ID);
				setState(141);
				match(ASSGN);
				setState(142);
				match(ID);
				{
				setState(144);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==COMMA) {
					{
					setState(143);
					match(COMMA);
					}
				}

				}
				}
				}
				setState(150);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(151);
			match(SEMICOLON);
			setState(158);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==ID || _la==ASSGN) {
				{
				{
				setState(152);
				exp();
				{
				setState(154);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==COMMA) {
					{
					setState(153);
					match(COMMA);
					}
				}

				}
				}
				}
				setState(160);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(161);
			match(SEMICOLON);
			setState(170);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==ID) {
				{
				{
				setState(162);
				match(ID);
				setState(163);
				arithmeticOperator();
				setState(164);
				arithmeticOperator();
				{
				setState(166);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==COMMA) {
					{
					setState(165);
					match(COMMA);
					}
				}

				}
				}
				}
				setState(172);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(173);
			match(RIGHTPAR);
			setState(174);
			match(LEFTKEY);
			setState(175);
			estatutos();
			setState(176);
			match(RIGHTKEY);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ExpContext extends ParserRuleContext {
		public TerminalNode ASSGN() { return getToken(MiriParser.ASSGN, 0); }
		public List<TerminalNode> ID() { return getTokens(MiriParser.ID); }
		public TerminalNode ID(int i) {
			return getToken(MiriParser.ID, i);
		}
		public List<TerminalNode> GRTR() { return getTokens(MiriParser.GRTR); }
		public TerminalNode GRTR(int i) {
			return getToken(MiriParser.GRTR, i);
		}
		public List<TerminalNode> LESS() { return getTokens(MiriParser.LESS); }
		public TerminalNode LESS(int i) {
			return getToken(MiriParser.LESS, i);
		}
		public List<TerminalNode> GRTREQ() { return getTokens(MiriParser.GRTREQ); }
		public TerminalNode GRTREQ(int i) {
			return getToken(MiriParser.GRTREQ, i);
		}
		public List<TerminalNode> LESSEQ() { return getTokens(MiriParser.LESSEQ); }
		public TerminalNode LESSEQ(int i) {
			return getToken(MiriParser.LESSEQ, i);
		}
		public List<TerminalNode> EQ() { return getTokens(MiriParser.EQ); }
		public TerminalNode EQ(int i) {
			return getToken(MiriParser.EQ, i);
		}
		public List<TerminalNode> NOTEQ() { return getTokens(MiriParser.NOTEQ); }
		public TerminalNode NOTEQ(int i) {
			return getToken(MiriParser.NOTEQ, i);
		}
		public List<TerminalNode> AND() { return getTokens(MiriParser.AND); }
		public TerminalNode AND(int i) {
			return getToken(MiriParser.AND, i);
		}
		public List<TerminalNode> OR() { return getTokens(MiriParser.OR); }
		public TerminalNode OR(int i) {
			return getToken(MiriParser.OR, i);
		}
		public List<ArithmeticOperatorContext> arithmeticOperator() {
			return getRuleContexts(ArithmeticOperatorContext.class);
		}
		public ArithmeticOperatorContext arithmeticOperator(int i) {
			return getRuleContext(ArithmeticOperatorContext.class,i);
		}
		public List<ArrayContext> array() {
			return getRuleContexts(ArrayContext.class);
		}
		public ArrayContext array(int i) {
			return getRuleContext(ArrayContext.class,i);
		}
		public ExpContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_exp; }
	}

	public final ExpContext exp() throws RecognitionException {
		ExpContext _localctx = new ExpContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_exp);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(195);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==ID) {
				{
				{
				setState(178);
				match(ID);
				setState(180);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==LEFTBRACK) {
					{
					setState(179);
					array();
					}
				}

				setState(191);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case GRTR:
					{
					setState(182);
					match(GRTR);
					}
					break;
				case LESS:
					{
					setState(183);
					match(LESS);
					}
					break;
				case GRTREQ:
					{
					setState(184);
					match(GRTREQ);
					}
					break;
				case LESSEQ:
					{
					setState(185);
					match(LESSEQ);
					}
					break;
				case EQ:
					{
					setState(186);
					match(EQ);
					}
					break;
				case NOTEQ:
					{
					setState(187);
					match(NOTEQ);
					}
					break;
				case AND:
					{
					setState(188);
					match(AND);
					}
					break;
				case OR:
					{
					setState(189);
					match(OR);
					}
					break;
				case ASSGN:
				case SUM:
				case MINUS:
				case MULTP:
				case DIVIDE:
					{
					setState(190);
					arithmeticOperator();
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				}
				}
				setState(197);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(198);
			match(ASSGN);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class OutputContext extends ParserRuleContext {
		public TerminalNode WRITE() { return getToken(MiriParser.WRITE, 0); }
		public TerminalNode LEFTPAR() { return getToken(MiriParser.LEFTPAR, 0); }
		public TerminalNode RIGHTPAR() { return getToken(MiriParser.RIGHTPAR, 0); }
		public TerminalNode SEMICOLON() { return getToken(MiriParser.SEMICOLON, 0); }
		public List<TerminalNode> QUOTE() { return getTokens(MiriParser.QUOTE); }
		public TerminalNode QUOTE(int i) {
			return getToken(MiriParser.QUOTE, i);
		}
		public List<ExpContext> exp() {
			return getRuleContexts(ExpContext.class);
		}
		public ExpContext exp(int i) {
			return getRuleContext(ExpContext.class,i);
		}
		public List<TerminalNode> ID() { return getTokens(MiriParser.ID); }
		public TerminalNode ID(int i) {
			return getToken(MiriParser.ID, i);
		}
		public List<GeofigContext> geofig() {
			return getRuleContexts(GeofigContext.class);
		}
		public GeofigContext geofig(int i) {
			return getRuleContext(GeofigContext.class,i);
		}
		public OutputContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_output; }
	}

	public final OutputContext output() throws RecognitionException {
		OutputContext _localctx = new OutputContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_output);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(200);
			match(WRITE);
			setState(201);
			match(LEFTPAR);
			{
			{
			setState(208); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				setState(208);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case QUOTE:
					{
					setState(202);
					match(QUOTE);
					setState(203);
					exp();
					setState(204);
					match(QUOTE);
					}
					break;
				case ID:
					{
					setState(206);
					match(ID);
					}
					break;
				case ARCH:
				case CIRCLE:
				case SQUARE:
					{
					setState(207);
					geofig();
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				}
				setState(210); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << ARCH) | (1L << CIRCLE) | (1L << SQUARE) | (1L << ID) | (1L << QUOTE))) != 0) );
			}
			}
			setState(212);
			match(RIGHTPAR);
			setState(213);
			match(SEMICOLON);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class InputDataContext extends ParserRuleContext {
		public TerminalNode READ() { return getToken(MiriParser.READ, 0); }
		public TerminalNode LEFTPAR() { return getToken(MiriParser.LEFTPAR, 0); }
		public TerminalNode RIGHTPAR() { return getToken(MiriParser.RIGHTPAR, 0); }
		public TerminalNode SEMICOLON() { return getToken(MiriParser.SEMICOLON, 0); }
		public List<TerminalNode> ID() { return getTokens(MiriParser.ID); }
		public TerminalNode ID(int i) {
			return getToken(MiriParser.ID, i);
		}
		public List<ArrayContext> array() {
			return getRuleContexts(ArrayContext.class);
		}
		public ArrayContext array(int i) {
			return getRuleContext(ArrayContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(MiriParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(MiriParser.COMMA, i);
		}
		public InputDataContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_inputData; }
	}

	public final InputDataContext inputData() throws RecognitionException {
		InputDataContext _localctx = new InputDataContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_inputData);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(215);
			match(READ);
			setState(216);
			match(LEFTPAR);
			setState(224); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(217);
				match(ID);
				setState(219);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==LEFTBRACK) {
					{
					setState(218);
					array();
					}
				}

				setState(222);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==COMMA) {
					{
					setState(221);
					match(COMMA);
					}
				}

				}
				}
				setState(226); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==ID );
			setState(228);
			match(RIGHTPAR);
			setState(229);
			match(SEMICOLON);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Llamada_fContext extends ParserRuleContext {
		public TerminalNode FUNCTION() { return getToken(MiriParser.FUNCTION, 0); }
		public List<DataTypeContext> dataType() {
			return getRuleContexts(DataTypeContext.class);
		}
		public DataTypeContext dataType(int i) {
			return getRuleContext(DataTypeContext.class,i);
		}
		public List<TerminalNode> ID() { return getTokens(MiriParser.ID); }
		public TerminalNode ID(int i) {
			return getToken(MiriParser.ID, i);
		}
		public TerminalNode LEFTPAR() { return getToken(MiriParser.LEFTPAR, 0); }
		public TerminalNode RIGHTPAR() { return getToken(MiriParser.RIGHTPAR, 0); }
		public TerminalNode LEFTKEY() { return getToken(MiriParser.LEFTKEY, 0); }
		public EstatutosContext estatutos() {
			return getRuleContext(EstatutosContext.class,0);
		}
		public TerminalNode RIGHTKEY() { return getToken(MiriParser.RIGHTKEY, 0); }
		public Llamada_fContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_llamada_f; }
	}

	public final Llamada_fContext llamada_f() throws RecognitionException {
		Llamada_fContext _localctx = new Llamada_fContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_llamada_f);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(231);
			match(FUNCTION);
			setState(232);
			dataType();
			setState(233);
			match(ID);
			setState(234);
			match(LEFTPAR);
			setState(238);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << BOOL) | (1L << FLOAT) | (1L << INT) | (1L << STRING))) != 0)) {
				{
				setState(235);
				dataType();
				setState(236);
				match(ID);
				}
			}

			setState(240);
			match(RIGHTPAR);
			setState(241);
			match(LEFTKEY);
			setState(242);
			estatutos();
			setState(243);
			match(RIGHTKEY);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ArithmeticOperatorContext extends ParserRuleContext {
		public TerminalNode SUM() { return getToken(MiriParser.SUM, 0); }
		public TerminalNode MINUS() { return getToken(MiriParser.MINUS, 0); }
		public TerminalNode MULTP() { return getToken(MiriParser.MULTP, 0); }
		public TerminalNode DIVIDE() { return getToken(MiriParser.DIVIDE, 0); }
		public TerminalNode ASSGN() { return getToken(MiriParser.ASSGN, 0); }
		public ArithmeticOperatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_arithmeticOperator; }
	}

	public final ArithmeticOperatorContext arithmeticOperator() throws RecognitionException {
		ArithmeticOperatorContext _localctx = new ArithmeticOperatorContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_arithmeticOperator);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(245);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << ASSGN) | (1L << SUM) | (1L << MINUS) | (1L << MULTP) | (1L << DIVIDE))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class GeofigContext extends ParserRuleContext {
		public CircleContext circle() {
			return getRuleContext(CircleContext.class,0);
		}
		public SquareContext square() {
			return getRuleContext(SquareContext.class,0);
		}
		public ArchContext arch() {
			return getRuleContext(ArchContext.class,0);
		}
		public GeofigContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_geofig; }
	}

	public final GeofigContext geofig() throws RecognitionException {
		GeofigContext _localctx = new GeofigContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_geofig);
		try {
			setState(250);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case CIRCLE:
				enterOuterAlt(_localctx, 1);
				{
				setState(247);
				circle();
				}
				break;
			case SQUARE:
				enterOuterAlt(_localctx, 2);
				{
				setState(248);
				square();
				}
				break;
			case ARCH:
				enterOuterAlt(_localctx, 3);
				{
				setState(249);
				arch();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class CircleContext extends ParserRuleContext {
		public TerminalNode CIRCLE() { return getToken(MiriParser.CIRCLE, 0); }
		public TerminalNode LEFTPAR() { return getToken(MiriParser.LEFTPAR, 0); }
		public List<ExpContext> exp() {
			return getRuleContexts(ExpContext.class);
		}
		public ExpContext exp(int i) {
			return getRuleContext(ExpContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(MiriParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(MiriParser.COMMA, i);
		}
		public TerminalNode RIGHTPAR() { return getToken(MiriParser.RIGHTPAR, 0); }
		public TerminalNode SEMICOLON() { return getToken(MiriParser.SEMICOLON, 0); }
		public CircleContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_circle; }
	}

	public final CircleContext circle() throws RecognitionException {
		CircleContext _localctx = new CircleContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_circle);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(252);
			match(CIRCLE);
			setState(253);
			match(LEFTPAR);
			setState(254);
			exp();
			setState(255);
			match(COMMA);
			setState(256);
			exp();
			setState(257);
			match(COMMA);
			setState(258);
			exp();
			setState(259);
			match(COMMA);
			setState(260);
			exp();
			setState(261);
			match(COMMA);
			setState(262);
			exp();
			setState(263);
			match(RIGHTPAR);
			setState(264);
			match(SEMICOLON);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class SquareContext extends ParserRuleContext {
		public TerminalNode SQUARE() { return getToken(MiriParser.SQUARE, 0); }
		public TerminalNode LEFTPAR() { return getToken(MiriParser.LEFTPAR, 0); }
		public List<ExpContext> exp() {
			return getRuleContexts(ExpContext.class);
		}
		public ExpContext exp(int i) {
			return getRuleContext(ExpContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(MiriParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(MiriParser.COMMA, i);
		}
		public TerminalNode RIGHTPAR() { return getToken(MiriParser.RIGHTPAR, 0); }
		public TerminalNode SEMICOLON() { return getToken(MiriParser.SEMICOLON, 0); }
		public SquareContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_square; }
	}

	public final SquareContext square() throws RecognitionException {
		SquareContext _localctx = new SquareContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_square);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(266);
			match(SQUARE);
			setState(267);
			match(LEFTPAR);
			setState(268);
			exp();
			setState(269);
			match(COMMA);
			setState(270);
			exp();
			setState(271);
			match(COMMA);
			setState(272);
			exp();
			setState(273);
			match(COMMA);
			setState(274);
			exp();
			setState(275);
			match(COMMA);
			setState(276);
			exp();
			setState(277);
			match(COMMA);
			setState(278);
			exp();
			setState(279);
			match(RIGHTPAR);
			setState(280);
			match(SEMICOLON);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ArchContext extends ParserRuleContext {
		public TerminalNode ARCH() { return getToken(MiriParser.ARCH, 0); }
		public TerminalNode LEFTPAR() { return getToken(MiriParser.LEFTPAR, 0); }
		public List<ExpContext> exp() {
			return getRuleContexts(ExpContext.class);
		}
		public ExpContext exp(int i) {
			return getRuleContext(ExpContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(MiriParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(MiriParser.COMMA, i);
		}
		public TerminalNode RIGHTPAR() { return getToken(MiriParser.RIGHTPAR, 0); }
		public TerminalNode SEMICOLON() { return getToken(MiriParser.SEMICOLON, 0); }
		public ArchContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_arch; }
	}

	public final ArchContext arch() throws RecognitionException {
		ArchContext _localctx = new ArchContext(_ctx, getState());
		enterRule(_localctx, 40, RULE_arch);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(282);
			match(ARCH);
			setState(283);
			match(LEFTPAR);
			setState(284);
			exp();
			setState(285);
			match(COMMA);
			setState(286);
			exp();
			setState(287);
			match(COMMA);
			setState(288);
			exp();
			setState(289);
			match(COMMA);
			setState(290);
			exp();
			setState(291);
			match(COMMA);
			setState(292);
			exp();
			setState(293);
			match(RIGHTPAR);
			setState(294);
			match(SEMICOLON);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\60\u012b\4\2\t\2"+
		"\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13"+
		"\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\3\2\3\2\3\2\3\2\3\2\3\2\5\2\63"+
		"\n\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\5\3>\n\3\3\4\3\4\3\5\3\5\3\5"+
		"\3\5\3\5\3\5\3\5\5\5I\n\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\7"+
		"\3\7\3\7\3\7\3\7\3\7\5\7[\n\7\3\b\3\b\5\b_\n\b\3\b\3\b\3\b\3\b\3\t\3\t"+
		"\3\t\6\th\n\t\r\t\16\ti\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\5\tu\n\t\3"+
		"\n\3\n\3\n\5\nz\n\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3"+
		"\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\5\r\u0093\n\r\7\r\u0095"+
		"\n\r\f\r\16\r\u0098\13\r\3\r\3\r\3\r\5\r\u009d\n\r\7\r\u009f\n\r\f\r\16"+
		"\r\u00a2\13\r\3\r\3\r\3\r\3\r\3\r\5\r\u00a9\n\r\7\r\u00ab\n\r\f\r\16\r"+
		"\u00ae\13\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\5\16\u00b7\n\16\3\16\3\16\3"+
		"\16\3\16\3\16\3\16\3\16\3\16\3\16\5\16\u00c2\n\16\7\16\u00c4\n\16\f\16"+
		"\16\16\u00c7\13\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\6"+
		"\17\u00d3\n\17\r\17\16\17\u00d4\3\17\3\17\3\17\3\20\3\20\3\20\3\20\5\20"+
		"\u00de\n\20\3\20\5\20\u00e1\n\20\6\20\u00e3\n\20\r\20\16\20\u00e4\3\20"+
		"\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21\5\21\u00f1\n\21\3\21\3\21"+
		"\3\21\3\21\3\21\3\22\3\22\3\23\3\23\3\23\5\23\u00fd\n\23\3\24\3\24\3\24"+
		"\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25"+
		"\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\26"+
		"\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26"+
		"\2\2\27\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*\2\5\4\2\26\27\31"+
		"\32\4\2\16\16\30\30\4\2\33\33\'*\2\u013c\2,\3\2\2\2\4\67\3\2\2\2\6?\3"+
		"\2\2\2\bA\3\2\2\2\nM\3\2\2\2\fZ\3\2\2\2\16\\\3\2\2\2\20d\3\2\2\2\22y\3"+
		"\2\2\2\24{\3\2\2\2\26\u0083\3\2\2\2\30\u008c\3\2\2\2\32\u00c5\3\2\2\2"+
		"\34\u00ca\3\2\2\2\36\u00d9\3\2\2\2 \u00e9\3\2\2\2\"\u00f7\3\2\2\2$\u00fc"+
		"\3\2\2\2&\u00fe\3\2\2\2(\u010c\3\2\2\2*\u011c\3\2\2\2,-\7\3\2\2-.\7\30"+
		"\2\2.\62\7\35\2\2/\60\7\5\2\2\60\63\5 \21\2\61\63\5\n\6\2\62/\3\2\2\2"+
		"\62\61\3\2\2\2\63\64\3\2\2\2\64\65\7\4\2\2\65\66\7\35\2\2\66\3\3\2\2\2"+
		"\678\7\5\2\289\5\6\4\29=\7\30\2\2:>\7\37\2\2;>\7\35\2\2<>\5\b\5\2=:\3"+
		"\2\2\2=;\3\2\2\2=<\3\2\2\2>\5\3\2\2\2?@\t\2\2\2@\7\3\2\2\2AB\7 \2\2BH"+
		"\5\32\16\2CD\7!\2\2DE\7 \2\2EF\5\32\16\2FG\7!\2\2GI\3\2\2\2HC\3\2\2\2"+
		"HI\3\2\2\2IJ\3\2\2\2JK\7!\2\2KL\7\35\2\2L\t\3\2\2\2MN\7\6\2\2NO\7\"\2"+
		"\2OP\7#\2\2PQ\7$\2\2QR\5\f\7\2RS\7%\2\2S\13\3\2\2\2T[\5\20\t\2U[\5\22"+
		"\n\2V[\7\r\2\2W[\7\f\2\2X[\5\16\b\2Y[\5 \21\2ZT\3\2\2\2ZU\3\2\2\2ZV\3"+
		"\2\2\2ZW\3\2\2\2ZX\3\2\2\2ZY\3\2\2\2[\r\3\2\2\2\\^\7\30\2\2]_\5\b\5\2"+
		"^]\3\2\2\2^_\3\2\2\2_`\3\2\2\2`a\7\33\2\2ab\t\3\2\2bc\7\35\2\2c\17\3\2"+
		"\2\2de\7\7\2\2eg\7\"\2\2fh\5\32\16\2gf\3\2\2\2hi\3\2\2\2ig\3\2\2\2ij\3"+
		"\2\2\2jk\3\2\2\2kl\7#\2\2lm\7$\2\2mn\5\f\7\2nt\7%\2\2op\7\b\2\2pq\7$\2"+
		"\2qr\5\f\7\2rs\7%\2\2su\3\2\2\2to\3\2\2\2tu\3\2\2\2u\21\3\2\2\2vz\5\24"+
		"\13\2wz\5\26\f\2xz\5\30\r\2yv\3\2\2\2yw\3\2\2\2yx\3\2\2\2z\23\3\2\2\2"+
		"{|\7\t\2\2|}\7\"\2\2}~\5\32\16\2~\177\7#\2\2\177\u0080\7$\2\2\u0080\u0081"+
		"\5\f\7\2\u0081\u0082\7%\2\2\u0082\25\3\2\2\2\u0083\u0084\7\13\2\2\u0084"+
		"\u0085\7$\2\2\u0085\u0086\5\f\7\2\u0086\u0087\7%\2\2\u0087\u0088\7\t\2"+
		"\2\u0088\u0089\7\"\2\2\u0089\u008a\5\32\16\2\u008a\u008b\7#\2\2\u008b"+
		"\27\3\2\2\2\u008c\u008d\7\n\2\2\u008d\u0096\7\"\2\2\u008e\u008f\7\30\2"+
		"\2\u008f\u0090\7\33\2\2\u0090\u0092\7\30\2\2\u0091\u0093\7\34\2\2\u0092"+
		"\u0091\3\2\2\2\u0092\u0093\3\2\2\2\u0093\u0095\3\2\2\2\u0094\u008e\3\2"+
		"\2\2\u0095\u0098\3\2\2\2\u0096\u0094\3\2\2\2\u0096\u0097\3\2\2\2\u0097"+
		"\u0099\3\2\2\2\u0098\u0096\3\2\2\2\u0099\u00a0\7\35\2\2\u009a\u009c\5"+
		"\32\16\2\u009b\u009d\7\34\2\2\u009c\u009b\3\2\2\2\u009c\u009d\3\2\2\2"+
		"\u009d\u009f\3\2\2\2\u009e\u009a\3\2\2\2\u009f\u00a2\3\2\2\2\u00a0\u009e"+
		"\3\2\2\2\u00a0\u00a1\3\2\2\2\u00a1\u00a3\3\2\2\2\u00a2\u00a0\3\2\2\2\u00a3"+
		"\u00ac\7\35\2\2\u00a4\u00a5\7\30\2\2\u00a5\u00a6\5\"\22\2\u00a6\u00a8"+
		"\5\"\22\2\u00a7\u00a9\7\34\2\2\u00a8\u00a7\3\2\2\2\u00a8\u00a9\3\2\2\2"+
		"\u00a9\u00ab\3\2\2\2\u00aa\u00a4\3\2\2\2\u00ab\u00ae\3\2\2\2\u00ac\u00aa"+
		"\3\2\2\2\u00ac\u00ad\3\2\2\2\u00ad\u00af\3\2\2\2\u00ae\u00ac\3\2\2\2\u00af"+
		"\u00b0\7#\2\2\u00b0\u00b1\7$\2\2\u00b1\u00b2\5\f\7\2\u00b2\u00b3\7%\2"+
		"\2\u00b3\31\3\2\2\2\u00b4\u00b6\7\30\2\2\u00b5\u00b7\5\b\5\2\u00b6\u00b5"+
		"\3\2\2\2\u00b6\u00b7\3\2\2\2\u00b7\u00c1\3\2\2\2\u00b8\u00c2\7+\2\2\u00b9"+
		"\u00c2\7,\2\2\u00ba\u00c2\7/\2\2\u00bb\u00c2\7\60\2\2\u00bc\u00c2\7-\2"+
		"\2\u00bd\u00c2\7.\2\2\u00be\u00c2\7\22\2\2\u00bf\u00c2\7\23\2\2\u00c0"+
		"\u00c2\5\"\22\2\u00c1\u00b8\3\2\2\2\u00c1\u00b9\3\2\2\2\u00c1\u00ba\3"+
		"\2\2\2\u00c1\u00bb\3\2\2\2\u00c1\u00bc\3\2\2\2\u00c1\u00bd\3\2\2\2\u00c1"+
		"\u00be\3\2\2\2\u00c1\u00bf\3\2\2\2\u00c1\u00c0\3\2\2\2\u00c2\u00c4\3\2"+
		"\2\2\u00c3\u00b4\3\2\2\2\u00c4\u00c7\3\2\2\2\u00c5\u00c3\3\2\2\2\u00c5"+
		"\u00c6\3\2\2\2\u00c6\u00c8\3\2\2\2\u00c7\u00c5\3\2\2\2\u00c8\u00c9\7\33"+
		"\2\2\u00c9\33\3\2\2\2\u00ca\u00cb\7\f\2\2\u00cb\u00d2\7\"\2\2\u00cc\u00cd"+
		"\7&\2\2\u00cd\u00ce\5\32\16\2\u00ce\u00cf\7&\2\2\u00cf\u00d3\3\2\2\2\u00d0"+
		"\u00d3\7\30\2\2\u00d1\u00d3\5$\23\2\u00d2\u00cc\3\2\2\2\u00d2\u00d0\3"+
		"\2\2\2\u00d2\u00d1\3\2\2\2\u00d3\u00d4\3\2\2\2\u00d4\u00d2\3\2\2\2\u00d4"+
		"\u00d5\3\2\2\2\u00d5\u00d6\3\2\2\2\u00d6\u00d7\7#\2\2\u00d7\u00d8\7\35"+
		"\2\2\u00d8\35\3\2\2\2\u00d9\u00da\7\r\2\2\u00da\u00e2\7\"\2\2\u00db\u00dd"+
		"\7\30\2\2\u00dc\u00de\5\b\5\2\u00dd\u00dc\3\2\2\2\u00dd\u00de\3\2\2\2"+
		"\u00de\u00e0\3\2\2\2\u00df\u00e1\7\34\2\2\u00e0\u00df\3\2\2\2\u00e0\u00e1"+
		"\3\2\2\2\u00e1\u00e3\3\2\2\2\u00e2\u00db\3\2\2\2\u00e3\u00e4\3\2\2\2\u00e4"+
		"\u00e2\3\2\2\2\u00e4\u00e5\3\2\2\2\u00e5\u00e6\3\2\2\2\u00e6\u00e7\7#"+
		"\2\2\u00e7\u00e8\7\35\2\2\u00e8\37\3\2\2\2\u00e9\u00ea\7\16\2\2\u00ea"+
		"\u00eb\5\6\4\2\u00eb\u00ec\7\30\2\2\u00ec\u00f0\7\"\2\2\u00ed\u00ee\5"+
		"\6\4\2\u00ee\u00ef\7\30\2\2\u00ef\u00f1\3\2\2\2\u00f0\u00ed\3\2\2\2\u00f0"+
		"\u00f1\3\2\2\2\u00f1\u00f2\3\2\2\2\u00f2\u00f3\7#\2\2\u00f3\u00f4\7$\2"+
		"\2\u00f4\u00f5\5\f\7\2\u00f5\u00f6\7%\2\2\u00f6!\3\2\2\2\u00f7\u00f8\t"+
		"\4\2\2\u00f8#\3\2\2\2\u00f9\u00fd\5&\24\2\u00fa\u00fd\5(\25\2\u00fb\u00fd"+
		"\5*\26\2\u00fc\u00f9\3\2\2\2\u00fc\u00fa\3\2\2\2\u00fc\u00fb\3\2\2\2\u00fd"+
		"%\3\2\2\2\u00fe\u00ff\7\20\2\2\u00ff\u0100\7\"\2\2\u0100\u0101\5\32\16"+
		"\2\u0101\u0102\7\34\2\2\u0102\u0103\5\32\16\2\u0103\u0104\7\34\2\2\u0104"+
		"\u0105\5\32\16\2\u0105\u0106\7\34\2\2\u0106\u0107\5\32\16\2\u0107\u0108"+
		"\7\34\2\2\u0108\u0109\5\32\16\2\u0109\u010a\7#\2\2\u010a\u010b\7\35\2"+
		"\2\u010b\'\3\2\2\2\u010c\u010d\7\21\2\2\u010d\u010e\7\"\2\2\u010e\u010f"+
		"\5\32\16\2\u010f\u0110\7\34\2\2\u0110\u0111\5\32\16\2\u0111\u0112\7\34"+
		"\2\2\u0112\u0113\5\32\16\2\u0113\u0114\7\34\2\2\u0114\u0115\5\32\16\2"+
		"\u0115\u0116\7\34\2\2\u0116\u0117\5\32\16\2\u0117\u0118\7\34\2\2\u0118"+
		"\u0119\5\32\16\2\u0119\u011a\7#\2\2\u011a\u011b\7\35\2\2\u011b)\3\2\2"+
		"\2\u011c\u011d\7\17\2\2\u011d\u011e\7\"\2\2\u011e\u011f\5\32\16\2\u011f"+
		"\u0120\7\34\2\2\u0120\u0121\5\32\16\2\u0121\u0122\7\34\2\2\u0122\u0123"+
		"\5\32\16\2\u0123\u0124\7\34\2\2\u0124\u0125\5\32\16\2\u0125\u0126\7\34"+
		"\2\2\u0126\u0127\5\32\16\2\u0127\u0128\7#\2\2\u0128\u0129\7\35\2\2\u0129"+
		"+\3\2\2\2\32\62=HZ^ity\u0092\u0096\u009c\u00a0\u00a8\u00ac\u00b6\u00c1"+
		"\u00c5\u00d2\u00d4\u00dd\u00e0\u00e4\u00f0\u00fc";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}