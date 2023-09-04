import Lexer as lexer
import Rules as rules



all_phrases = []

def read_file(file_name: str):
    
    phrases = []
    
    file = open(file_name, "r", encoding="utf-8")
    
    line = file.readline()
    
    while line != '':
        line = line.replace("\n", " ")
        line = line.lower()
        phrases.append(line)
        line = file.readline()
    
    file.close()
    
    i = 0
    bool_parser = True
    
    while i < len(phrases) and bool_parser:
        
        tokened_phrase = lexer.tokenize_file(phrases[i])
        all_phrases.append(tokened_phrase)
        bool_parser = rules.general_analyzer(tokened_phrase)

    return bool_parser
        
        

    #recorrido sobre la matriz de tokenized_code

    
    
    
    
    
    
    
