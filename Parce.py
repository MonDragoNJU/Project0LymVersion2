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

    #otro recorrido sobre phrases para irlo metiendo en tokens_line = lexer.tokenize_file(lineaDePhrases)

    #eso nos va a regresar la lista de tokens de cada linea

    #cada lista de tokens la vamos metiendo en una lista que se llame tokenized_code = [[],[],[],[]]

    #recorrido sobre la matriz de tokenized_code

    
    lexer.tokenize_file(phrases)

    
    
    
    
    
    
    
