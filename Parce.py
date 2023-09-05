import Lexer as lexer
import Rules as rules

def read_file(file_name: str):
    
    all_phrases = []
    
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
        i+=1

    return bool_parser, all_phrases

def check_all(file_name: str):
    
    final_bool = True
    
    bool_parser, all_phrases = read_file(file_name)
    
    if bool_parser:
        
        try:
        
            i= 0
            while i < len(all_phrases) and final_bool:
                
                if all_phrases[i][0] == "DEFPROC":
                    
                    if all_phrases[i + 1][0] != "LEFTBRACE":
                        
                        final_bool = False
                
                i+=1
        except:
            final_bool = False
            
    else:
        return bool_parser
    
    return final_bool
        
        

    #recorrido sobre la matriz de tokenized_code

    
    
    
    
    
    
    
