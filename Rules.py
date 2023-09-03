def general_analizer(tokened_phrase: list):
    
    if tokened_phrase[0] == "DEFVAR":
        return analize_variable(tokened_phrase)
    elif tokened_phrase[0] == "DEFPROC":
        return analize_procedure(tokened_phrase)
    

def analize_variable(tokened_phrase: list):
    
    checker_bool = True
    
    if tokened_phrase[1] != "VAR" and tokened_phrase[2] != ("VAR" or "NUM"):
        checker_bool = False
        
    return checker_bool

def analize_procedure(tokened_phrase: list):
    
    checker_bool = True
    
    if tokened_phrase[1] != 'VAR':
        checker_bool = False
    else:
        if tokened_phrase[2] != "LEFTPAR" and tokened_phrase[len(tokened_phrase) - 1] != "RIGHTPAR":
            checker_bool = False
        else:
            try:
                if tokened_phrase[3] != "RIGHTPAR":
                    if tokened_phrase[len(tokened_phrase) - 2] != "VAR":
                        checker_bool = False
                    else:
                        sliced_list = tokened_phrase[3: len(tokened_phrase) - 2]
                        i = 0
                        while i < len(sliced_list) and checker_bool:
                            if i % 2 == 0:
                                if sliced_list[i] != "VAR":
                                    checker_bool = False
                            else:
                                if sliced_list[i] != "COMMA":
                                    checker_bool = False
                            i += 1
            except:
                checker_bool = False
        
    return checker_bool 

def analize_condictional(tokened_phrase: list):
    pass

def analize_commands(tokened_phrase: list):

    checker_bool = True

    if tokened_phrase[0] == "JUMP":
        if tokened_phrase[1] != "LEFTPAR" or (tokened_phrase[2] != "NUM" and tokened_phrase[2] != "VAR") or tokened_phrase[3] != "COMMA" or (tokened_phrase[4] != "NUM" and tokened_phrase[4] != "VAR") or tokened_phrase[5] != "RIGHTPAR":
            checker_bool = False

    elif tokened_phrase[0] == "WALK":
        if len(tokened_phrase) == 4:
            if tokened_phrase[1] != "LEFTPAR" or (tokened_phrase[2] != "NUM" and tokened_phrase[2] != "VAR") or tokened_phrase[3] != "RIGHTPAR":
                checker_bool = False
        elif len(tokened_phrase) == 6:
            if tokened_phrase[1] != "LEFTPAR" or (tokened_phrase[2] != "NUM" and tokened_phrase[2] != "VAR") or tokened_phrase[3] != "COMMA" or (tokened_phrase[4] != "DIRECTION" and tokened_phrase[4] != "ORIENTATION") or tokened_phrase[5] != "RIGHTPAR":
                checker_bool = False
        else:
            checker_bool = False

    #elif tokened_phrase[0] == "LEAP":
