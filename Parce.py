import Lexer as lexer

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
    
    return phrases

lexer.tokenize_file(read_file("Test.txt"))


    
    
    
    
    
    
    
