import Lexer as lexer
import Rules as rules

all_phrases = []

def read_file(file_name: str):
    
    phrases = []
    i = 0
    
    file = open(file_name, "r", encoding="utf-8")
    
    line = file.readline()
    
    while line != '':
        line = line.replace("\n", " ")
        line = line.lower()
        phrases.append(line)
        line = file.readline()
    
    file.close()
    
    while i < len(phrases):
        
        tok_phrase = lexer.tokenize_file(phrases[i])
        all_phrases.append(tok_phrase)
        rules.analize_variable(tok_phrase)
        

    #recorrido sobre la matriz de tokenized_code

    
    
    
    
    
    
    
