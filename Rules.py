def general_analizer(tokened_phrase: list):
    
    if tokened_phrase[0] == "DEFVAR":
        analize_variable(tokened_phrase)
    

def analize_variable(tokened_phrase: list):
    
    checker_bool = True
    
    if tokened_phrase[1] != "VAR" and tokened_phrase[2] != ("VAR" or "NUM"):
        checker_bool == False
        
    return checker_bool