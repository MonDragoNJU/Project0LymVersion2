import Lexer as lexer

def read_file(file_name: str):
    
    file = open(file_name, "r", encoding="utf-8")
    
    line = file.read()
    line = line.replace("\n", " ")
    
    line = line.lower()
    
    file.close()
    
    
    
    
    
    
    
