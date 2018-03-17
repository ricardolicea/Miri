// Generated from /Users/ricardolicea/OneDrive/Tecnol?gico de Monterrey/8vo Semestre/EM18 Dise?o de Compiladores/MIRI/Miri.g4 by ANTLR 4.7.1
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class MiriLexer extends Lexer {
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
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	public static final String[] ruleNames = {
		"PROGRAM", "END", "DECLARE", "MAIN", "IF", "ELSE", "WHILE", "FOR", "DO_WHILE", 
		"WRITE", "READ", "FUNCTION", "ARCH", "CIRCLE", "SQUARE", "AND", "OR", 
		"RETURN", "PAINT", "BOOL", "FLOAT", "ID", "INT", "STRING", "ASSGN", "COMMA", 
		"SEMICOLON", "DOT", "COLON", "LEFTBRACK", "RIGHTBRACK", "LEFTPAR", "RIGHTPAR", 
		"LEFTKEY", "RIGHTKEY", "QUOTE", "SUM", "MINUS", "MULTP", "DIVIDE", "GRTR", 
		"LESS", "EQ", "NOTEQ", "GRTREQ", "LESSEQ"
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


	public MiriLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "Miri.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\60\u012d\b\1\4\2"+
		"\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4"+
		"\13\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22"+
		"\t\22\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31"+
		"\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t"+
		" \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t"+
		"+\4,\t,\4-\t-\4.\t.\4/\t/\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3"+
		"\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3"+
		"\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\n\3\n\3\n"+
		"\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r"+
		"\3\r\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\20"+
		"\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\23"+
		"\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25"+
		"\3\25\3\25\3\25\3\25\3\25\3\25\3\25\5\25\u00cf\n\25\3\26\6\26\u00d2\n"+
		"\26\r\26\16\26\u00d3\3\26\3\26\6\26\u00d8\n\26\r\26\16\26\u00d9\3\27\3"+
		"\27\7\27\u00de\n\27\f\27\16\27\u00e1\13\27\3\30\6\30\u00e4\n\30\r\30\16"+
		"\30\u00e5\3\31\3\31\3\31\3\31\7\31\u00ec\n\31\f\31\16\31\u00ef\13\31\3"+
		"\31\3\31\3\31\3\31\3\31\7\31\u00f6\n\31\f\31\16\31\u00f9\13\31\3\31\5"+
		"\31\u00fc\n\31\3\32\3\32\3\33\3\33\3\34\3\34\3\35\3\35\3\36\3\36\3\37"+
		"\3\37\3 \3 \3!\3!\3\"\3\"\3#\3#\3$\3$\3%\3%\3&\3&\3\'\3\'\3(\3(\3)\3)"+
		"\3*\3*\3+\3+\3,\3,\3,\3-\3-\3-\3.\3.\3.\3/\3/\3/\2\2\60\3\3\5\4\7\5\t"+
		"\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23"+
		"%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G"+
		"%I&K\'M(O)Q*S+U,W-Y.[/]\60\3\2\5\5\2\62;C\\c|\4\2))^^\4\2$$^^\2\u0136"+
		"\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2"+
		"\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2"+
		"\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2"+
		"\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2"+
		"\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3"+
		"\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2"+
		"\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2"+
		"U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\3_\3\2\2\2\5g\3"+
		"\2\2\2\7k\3\2\2\2\ts\3\2\2\2\13x\3\2\2\2\r{\3\2\2\2\17\u0080\3\2\2\2\21"+
		"\u0086\3\2\2\2\23\u008a\3\2\2\2\25\u008d\3\2\2\2\27\u0093\3\2\2\2\31\u0098"+
		"\3\2\2\2\33\u009e\3\2\2\2\35\u00a3\3\2\2\2\37\u00aa\3\2\2\2!\u00b1\3\2"+
		"\2\2#\u00b5\3\2\2\2%\u00b8\3\2\2\2\'\u00bf\3\2\2\2)\u00ce\3\2\2\2+\u00d1"+
		"\3\2\2\2-\u00db\3\2\2\2/\u00e3\3\2\2\2\61\u00fb\3\2\2\2\63\u00fd\3\2\2"+
		"\2\65\u00ff\3\2\2\2\67\u0101\3\2\2\29\u0103\3\2\2\2;\u0105\3\2\2\2=\u0107"+
		"\3\2\2\2?\u0109\3\2\2\2A\u010b\3\2\2\2C\u010d\3\2\2\2E\u010f\3\2\2\2G"+
		"\u0111\3\2\2\2I\u0113\3\2\2\2K\u0115\3\2\2\2M\u0117\3\2\2\2O\u0119\3\2"+
		"\2\2Q\u011b\3\2\2\2S\u011d\3\2\2\2U\u011f\3\2\2\2W\u0121\3\2\2\2Y\u0124"+
		"\3\2\2\2[\u0127\3\2\2\2]\u012a\3\2\2\2_`\7r\2\2`a\7t\2\2ab\7q\2\2bc\7"+
		"i\2\2cd\7t\2\2de\7c\2\2ef\7o\2\2f\4\3\2\2\2gh\7g\2\2hi\7p\2\2ij\7f\2\2"+
		"j\6\3\2\2\2kl\7f\2\2lm\7g\2\2mn\7e\2\2no\7n\2\2op\7c\2\2pq\7t\2\2qr\7"+
		"g\2\2r\b\3\2\2\2st\7o\2\2tu\7c\2\2uv\7k\2\2vw\7p\2\2w\n\3\2\2\2xy\7k\2"+
		"\2yz\7h\2\2z\f\3\2\2\2{|\7g\2\2|}\7n\2\2}~\7u\2\2~\177\7g\2\2\177\16\3"+
		"\2\2\2\u0080\u0081\7y\2\2\u0081\u0082\7j\2\2\u0082\u0083\7k\2\2\u0083"+
		"\u0084\7n\2\2\u0084\u0085\7g\2\2\u0085\20\3\2\2\2\u0086\u0087\7h\2\2\u0087"+
		"\u0088\7q\2\2\u0088\u0089\7t\2\2\u0089\22\3\2\2\2\u008a\u008b\7f\2\2\u008b"+
		"\u008c\7q\2\2\u008c\24\3\2\2\2\u008d\u008e\7y\2\2\u008e\u008f\7t\2\2\u008f"+
		"\u0090\7k\2\2\u0090\u0091\7v\2\2\u0091\u0092\7g\2\2\u0092\26\3\2\2\2\u0093"+
		"\u0094\7t\2\2\u0094\u0095\7g\2\2\u0095\u0096\7c\2\2\u0096\u0097\7f\2\2"+
		"\u0097\30\3\2\2\2\u0098\u0099\7h\2\2\u0099\u009a\7w\2\2\u009a\u009b\7"+
		"p\2\2\u009b\u009c\7e\2\2\u009c\u009d\7v\2\2\u009d\32\3\2\2\2\u009e\u009f"+
		"\7c\2\2\u009f\u00a0\7t\2\2\u00a0\u00a1\7e\2\2\u00a1\u00a2\7j\2\2\u00a2"+
		"\34\3\2\2\2\u00a3\u00a4\7e\2\2\u00a4\u00a5\7k\2\2\u00a5\u00a6\7t\2\2\u00a6"+
		"\u00a7\7e\2\2\u00a7\u00a8\7n\2\2\u00a8\u00a9\7g\2\2\u00a9\36\3\2\2\2\u00aa"+
		"\u00ab\7u\2\2\u00ab\u00ac\7s\2\2\u00ac\u00ad\7w\2\2\u00ad\u00ae\7c\2\2"+
		"\u00ae\u00af\7t\2\2\u00af\u00b0\7g\2\2\u00b0 \3\2\2\2\u00b1\u00b2\7c\2"+
		"\2\u00b2\u00b3\7p\2\2\u00b3\u00b4\7f\2\2\u00b4\"\3\2\2\2\u00b5\u00b6\7"+
		"q\2\2\u00b6\u00b7\7t\2\2\u00b7$\3\2\2\2\u00b8\u00b9\7t\2\2\u00b9\u00ba"+
		"\7g\2\2\u00ba\u00bb\7v\2\2\u00bb\u00bc\7w\2\2\u00bc\u00bd\7t\2\2\u00bd"+
		"\u00be\7p\2\2\u00be&\3\2\2\2\u00bf\u00c0\7r\2\2\u00c0\u00c1\7c\2\2\u00c1"+
		"\u00c2\7k\2\2\u00c2\u00c3\7p\2\2\u00c3\u00c4\7v\2\2\u00c4(\3\2\2\2\u00c5"+
		"\u00c6\7v\2\2\u00c6\u00c7\7t\2\2\u00c7\u00c8\7w\2\2\u00c8\u00cf\7g\2\2"+
		"\u00c9\u00ca\7h\2\2\u00ca\u00cb\7c\2\2\u00cb\u00cc\7n\2\2\u00cc\u00cd"+
		"\7u\2\2\u00cd\u00cf\7g\2\2\u00ce\u00c5\3\2\2\2\u00ce\u00c9\3\2\2\2\u00cf"+
		"*\3\2\2\2\u00d0\u00d2\4\62;\2\u00d1\u00d0\3\2\2\2\u00d2\u00d3\3\2\2\2"+
		"\u00d3\u00d1\3\2\2\2\u00d3\u00d4\3\2\2\2\u00d4\u00d5\3\2\2\2\u00d5\u00d7"+
		"\7\60\2\2\u00d6\u00d8\4\62;\2\u00d7\u00d6\3\2\2\2\u00d8\u00d9\3\2\2\2"+
		"\u00d9\u00d7\3\2\2\2\u00d9\u00da\3\2\2\2\u00da,\3\2\2\2\u00db\u00df\4"+
		"c|\2\u00dc\u00de\t\2\2\2\u00dd\u00dc\3\2\2\2\u00de\u00e1\3\2\2\2\u00df"+
		"\u00dd\3\2\2\2\u00df\u00e0\3\2\2\2\u00e0.\3\2\2\2\u00e1\u00df\3\2\2\2"+
		"\u00e2\u00e4\4\62;\2\u00e3\u00e2\3\2\2\2\u00e4\u00e5\3\2\2\2\u00e5\u00e3"+
		"\3\2\2\2\u00e5\u00e6\3\2\2\2\u00e6\60\3\2\2\2\u00e7\u00ed\7)\2\2\u00e8"+
		"\u00ec\n\3\2\2\u00e9\u00ea\7^\2\2\u00ea\u00ec\13\2\2\2\u00eb\u00e8\3\2"+
		"\2\2\u00eb\u00e9\3\2\2\2\u00ec\u00ef\3\2\2\2\u00ed\u00eb\3\2\2\2\u00ed"+
		"\u00ee\3\2\2\2\u00ee\u00f0\3\2\2\2\u00ef\u00ed\3\2\2\2\u00f0\u00fc\7)"+
		"\2\2\u00f1\u00f7\7$\2\2\u00f2\u00f6\n\4\2\2\u00f3\u00f4\7^\2\2\u00f4\u00f6"+
		"\13\2\2\2\u00f5\u00f2\3\2\2\2\u00f5\u00f3\3\2\2\2\u00f6\u00f9\3\2\2\2"+
		"\u00f7\u00f5\3\2\2\2\u00f7\u00f8\3\2\2\2\u00f8\u00fa\3\2\2\2\u00f9\u00f7"+
		"\3\2\2\2\u00fa\u00fc\7$\2\2\u00fb\u00e7\3\2\2\2\u00fb\u00f1\3\2\2\2\u00fc"+
		"\62\3\2\2\2\u00fd\u00fe\7?\2\2\u00fe\64\3\2\2\2\u00ff\u0100\7.\2\2\u0100"+
		"\66\3\2\2\2\u0101\u0102\7=\2\2\u01028\3\2\2\2\u0103\u0104\7\60\2\2\u0104"+
		":\3\2\2\2\u0105\u0106\7<\2\2\u0106<\3\2\2\2\u0107\u0108\7]\2\2\u0108>"+
		"\3\2\2\2\u0109\u010a\7_\2\2\u010a@\3\2\2\2\u010b\u010c\7*\2\2\u010cB\3"+
		"\2\2\2\u010d\u010e\7+\2\2\u010eD\3\2\2\2\u010f\u0110\7}\2\2\u0110F\3\2"+
		"\2\2\u0111\u0112\7\177\2\2\u0112H\3\2\2\2\u0113\u0114\7$\2\2\u0114J\3"+
		"\2\2\2\u0115\u0116\7-\2\2\u0116L\3\2\2\2\u0117\u0118\7/\2\2\u0118N\3\2"+
		"\2\2\u0119\u011a\7,\2\2\u011aP\3\2\2\2\u011b\u011c\7\61\2\2\u011cR\3\2"+
		"\2\2\u011d\u011e\7@\2\2\u011eT\3\2\2\2\u011f\u0120\7>\2\2\u0120V\3\2\2"+
		"\2\u0121\u0122\7?\2\2\u0122\u0123\7?\2\2\u0123X\3\2\2\2\u0124\u0125\7"+
		"#\2\2\u0125\u0126\7?\2\2\u0126Z\3\2\2\2\u0127\u0128\7@\2\2\u0128\u0129"+
		"\7?\2\2\u0129\\\3\2\2\2\u012a\u012b\7>\2\2\u012b\u012c\7?\2\2\u012c^\3"+
		"\2\2\2\r\2\u00ce\u00d3\u00d9\u00df\u00e5\u00eb\u00ed\u00f5\u00f7\u00fb"+
		"\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}