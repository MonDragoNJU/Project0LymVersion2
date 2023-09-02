import ply.lex as lex

entradas = input("metala: ")


#List of tokens

tokens = [
    "DEFVAR", "DEFPROC", "VAR", "NUM", "IF", "ELSE", "WHILE", "REPEAT", "TIMES", "JUMP", "WALK",
    "LEAP", "TURN", "TURNTO", "DROP", "GET", "GRAB", "LETGO", "NOP", "EQUALS", "LEFTPAR",
    "RIGHTPAR", "COMMA", "SEMICOL", "FACING", "CAN", "NOT", "LEFTBRACE", "RIGHTBRACE"]

#---Recognize control structures---#

t_DEFVAR = r'DEFVAR'
t_DEFPROC = r'DEFPROC'
t_IF = r'IF'
t_ELSE = r'ELSE'
t_WHILE = r'WHILE'
t_REPEAT = r'REPEAT'
t_TIMES = r'TIMES'
t_EQUALS = r'='
t_LEFTPAR = r'\('
t_RIGHTPAR = r'\)'
t_COMMA = r','
t_SEMICOL = r';'
t_FACING = r'FACING'
t_CAN = r'CAN'
t_NOT = r'NOT'
t_LEFTBRACE = r'\{'
t_RIGHTBRACE = r'\}'
t_ignore = ' \t'

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
    r'letGo'
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
    print("An invalid character was found: " + str(word.value[0]) + "at position" + str(word.lexpos))
    word.lexer.skip(1)

#Create the lexer
lexer = lex.lex()


lexer.input(entradas)
for token in lexer:
    print(token)


    
    

 





