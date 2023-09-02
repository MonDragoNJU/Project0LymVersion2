
import ply.lex as lex



#List of tokens

tokens = [
    "DEFVAR", "DEFPROC", "VAR", "NUM", "IF", "ELSE", "WHILE", "REPEAT", "TIMES", "JUMP", "WALK",
    "LEAP", "TURN", "TURNTO", "DROP", "GET", "GRAB", "LETGO", "NOP", "EQUALS", "LEFTPAR",
    "RIGHTPAR", "COMMA", "SEMICOL", "FACING", "CAN", "NOT", "LEFTBRACE", "RIGHTBRACE", "ORIENTATION",
    "DIRECTION"]

#---Recognize control structures---#

def t_IF(word):
    r'if'
    return word

def t_ELSE(word):
    r'else'
    return word

def t_WHILE(word):
    r'while'
    return word

def t_REPEAT(word):
    r'repeat'
    return word

def t_TIMES(word):
    r'times'
    return word

def t_EQUALS(word):
    r'='
    return word

def t_LEFTPAR(word):
    r'\('
    return word

def t_RIGHTPAR(word):
    r'\)'
    return word

def t_COMMA(word):
    r','
    return word

def t_SEMICOL(word):
    r';'
    return word

def t_FACING(word):
    r'facing'
    return word

def t_CAN(word):
    r'can'
    return word

def t_NOT(word):
    r'not'
    return word

def t_LEFTBRACE(word):
    r'\{'
    return word

def t_RIGHTBRACE(word):
    r'\}'
    return word

t_ignore = ' \t'

def t_DEFVAR(word):
    r'defvar'
    return word

def t_DEFPROC(word):
    r'defproc'
    return word

#----Recognize tokens (procedures)----#

def t_JUMP(word):
    r'jump'
    return word

def t_WALK(word):
    r'walk'
    return word

def t_LEAP(word):
    r'leap'
    return word

def t_TURN(word):
    r'turn'
    return word

def t_TURNTO(word):
    r'turnto'
    return word

def t_DROP(word):
    r'drop'
    return word

def t_GET(word):
    r'get'
    return word

def t_GRAB(word):
    r'grab'
    return word

def t_LETGO(word):
    r'letgo'
    return word

def t_NOP(word):
    r'nop'
    return word

def t_ORIENTATION(word):
    r'west|east|north|south'
    return word

def t_DIRECTION(word):
    r'front|back|right|left'
    return word


#---Recognize tokens (variables)---#

#Recognize variable names
def t_VAR(word):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    return word

#Recognize numbers
def t_NUM(word):
    r'\d+'
    word.value = int(word.value)
    return word

#---Message of error---#
def t_error(word):
    print("An invalid character was found: " + " " + str(word.value[0]) + " " +"at position" + " " + str(word.lexpos))
    word.lexer.skip(1)

#Create the lexer
lexer = lex.lex()

def tokenize_file(phrase) -> list:
    
    tokens_line = []

    lexer.input(phrase)
    for token in lexer:
        tokens_line.append(token.type)
        
    return tokens_line
            
