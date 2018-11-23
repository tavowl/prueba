import ply.lex as lex
import ply.yacc as yacc
import Diccionario as di

aux = {}
aux.update(di.subject)
aux.update(di.verbspr)
aux.update(di.verbspast)
aux.update(di.verbpastToBe)
aux.update(di.verbcontpast)
aux.update(di.article)
aux.update(di.adjetive)
aux.update(di.word)

tokens = [
   'SUBJECT',
   'VERB_Spresent',
   'VERB_Spast',
   'VERB_pastToBe',
   'VERB_Contpast',
   'WORD',
   'UNKNOWN',
] 


# Regular expression rules for simple tokens

# A regular expression rule with some action code

def t_WORD(t):
    r'[a-z]{2}[a-z]*'
    if aux.get(t.value) != None:
        t.type = di.types.get(t.value)
        t.value = aux.get(t.value)
    else:
        t.type = 'UNKNOWN'
        t_VERB(t)
    return t
   
def t_SUBJECT(t):
    r'[A-Z][a-z]*'
    if aux.get(t.value) != None:
        t.type = di.types.get(t.value)
        t.value = aux.get(t.value)
    else:
        t.type = 'UNKNOWN'
    
    return t

#MODIFUCADO: EL RECONOCIMIENTO DE LOS ARTICULOS ESTA AQUI
def t_VERB(t):
    r'[a-z]{2}[a-z]*'
    if aux.get(t.value) != None:
        t.type = di.types.get(t.value)
        t.value = aux.get(t.value)
    else:
        t.type='UNKNOWN'
    return t
    
# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


#Reglas Gramaticales

def p_textoSP(p):
    'texto : frase_presenteSimple texto'
    p[0] = p[1] + " " + p[2]

def p_textoSPast(p):
    'texto : frase_pasadoSimple texto'
    p[0] = p[1] + " " + p[2]

def p_textoPastCont(p):
    'texto : frase_pasadoContinuo texto'
    p[0] = p[1] + " " + p[2]

def p_textoOPT(p):
    'texto : empty'
    p[0] = p[1]

def p_Frase_SP(p):
    'frase_presenteSimple : SUBJECT VERB_Spresent predicated'
    p[0] = p[1] + " " + p[2] + p[3]

def p_Frase_PastCont(p):
    'frase_pasadoContinuo : SUBJECT VERB_pastToBe VERB_Contpast predicated'
    p[0] = p[1] +" "+ p[2] +" "+ p[3]+ p[4]

def p_Frase_SPast(p):
    'frase_pasadoSimple : SUBJECT VERB_Spast predicated'
    p[0] = p[1] + " " + p[2] + p[3]

def p_Predicado(p):
    'predicated : WORDOPT predicated'
    p[0] = " " + p[1] + p[2]

def p_Predicado_Word(p):
    'predicated : WORDOPT'
    p[0] = " "+ p[1]

def p_Word_Opt1(p):
    'WORDOPT : WORD'
    p[0] =  p[1]

def p_Word_OptE(p):
    'WORDOPT : empty'
    p[0] = p[1]

def p_empty(p):
    'empty :'
    p[0] = ""

# Error rule for syntax errors
def p_error(p):
    if p:
         print("Error token ", p.type , " - palabra desconocida: '",p.value, "'")
    else:
         print("Error de sintaxis at EOF")


# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

def mein(data):
    # Build the lexer
    lexer = lex.lex()
    # Give the lexer some input
    #data=input()
    lexer.input(data)
    # Tokenize
    while True:
        tok = lexer.token()
        if not tok: 
            break      # No more input
        print(tok)
    print("\n")

    # Build the parser
    parser = yacc.yacc()
    s=data
    result= parser.parse(s)
    return result


   
