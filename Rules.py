def general_analizer(tokened_phrase: list):

    tokens_commands = ["JUMP", "WALK", "LEAP", "TURN", "TURNTO", "DROP", "GET", "GRAB", "LETGO", "NOP", "EQUALS"]
    
    if tokened_phrase[0] == "DEFVAR":
        return analize_variable(tokened_phrase)
    elif tokened_phrase[0] == "DEFPROC":
        return analize_procedure(tokened_phrase)
    elif tokened_phrase[0] == "WHILE":
        return analize_while(tokened_phrase)
    elif tokened_phrase[0] == "REPEAT":
        return analize_repeat(tokened_phrase)
    elif tokened_phrase[0] == "VAR":
        return analize_equality(tokened_phrase)
    elif tokened_phrase[0] in tokens_commands:
        return analize_commands(tokened_phrase)
    
    
#SIRVE
def analize_variable(tokened_phrase: list):
    
    checker_bool = True

    if len(tokened_phrase) != 3:
        checker_bool = False
    else:
        if tokened_phrase[1] != "VAR" or (tokened_phrase[2] != "VAR" and tokened_phrase[2] != "NUM"):
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
                    
    
#SIRVE
def analize_commands(tokened_phrase: list):

    checker_bool = True

    if tokened_phrase[0] == "JUMP":
        try:
            if tokened_phrase[1] != "LEFTPAR" or (tokened_phrase[2] != "NUM" and tokened_phrase[2] != "VAR") or tokened_phrase[3] != "COMMA" or (tokened_phrase[4] != "NUM" and tokened_phrase[4] != "VAR") or tokened_phrase[5] != "RIGHTPAR":
                checker_bool = False
        except:
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

    elif tokened_phrase[0] == "LEAP":
        if len(tokened_phrase) == 4:
             if tokened_phrase[1] != "LEFTPAR" or (tokened_phrase[2] != "NUM" and tokened_phrase[2] != "VAR") or tokened_phrase[3] != "RIGHTPAR":
                checker_bool = False
        elif len(tokened_phrase) == 6:
            if tokened_phrase[1] != "LEFTPAR" or (tokened_phrase[2] != "NUM" and tokened_phrase[2] != "VAR") or tokened_phrase[3] != "COMMA" or (tokened_phrase[4] != "DIRECTION" and tokened_phrase[4] != "ORIENTATION") or tokened_phrase[5] != "RIGHTPAR":
                checker_bool = False
        else:
            checker_bool = False

    elif tokened_phrase[0] == "TURN":
        try:
            if tokened_phrase[1] != "LEFTPAR" or tokened_phrase[2] != "DIRECTION" or tokened_phrase[3] != "RIGHTPAR":
                checker_bool = False
        except:
            checker_bool = False
            
    elif tokened_phrase[0] == "TURNTO":
        try: 
            if tokened_phrase[1] != "LEFTPAR" or tokened_phrase[2] != "ORIENTATION" or tokened_phrase[3] != "RIGHTPAR":
                checker_bool = False
        except:
            checker_bool = False

    elif tokened_phrase[0] == "DROP":
        try:
            if tokened_phrase[1] != "LEFTPAR" or (tokened_phrase[2] != "NUM" and tokened_phrase[2] != "VAR") or tokened_phrase[3] != "RIGHTPAR":
                    checker_bool = False
        except:
            checker_bool = False
    
    elif tokened_phrase[0] == "GET":
        try:
            if tokened_phrase[1] != "LEFTPAR" or (tokened_phrase[2] != "NUM" and tokened_phrase[2] != "VAR") or tokened_phrase[3] != "RIGHTPAR":
                checker_bool = False
        except:
            checker_bool = False

    elif tokened_phrase[0] == "GRAB":
        try: 
            if tokened_phrase[1] != "LEFTPAR" or (tokened_phrase[2] != "NUM" and tokened_phrase[2] != "VAR") or tokened_phrase[3] != "RIGHTPAR":
                checker_bool = False
        except:
            checker_bool = False
    
    elif tokened_phrase[0] == "LETGO":
        try:
            if tokened_phrase[1] != "LEFTPAR" or (tokened_phrase[2] != "NUM" and tokened_phrase[2] != "VAR") or tokened_phrase[3] != "RIGHTPAR":
                checker_bool = False
        except:
            checker_bool = False

    elif tokened_phrase[0] == "NOP":
        try:
            if tokened_phrase[1] != "LEFTPAR" or tokened_phrase[2] != "RIGHTPAR":
                checker_bool = False
        except:
            checker_bool = False


    return checker_bool

#SIRVE
def analize_condition(tokened_phrase: list):

    tokens_commands = ["JUMP", "WALK", "LEAP", "TURN", "TURNTO", "DROP", "GET", "GRAB", "LETGO", "NOP", "EQUALS"]

    checker_bool = True
    
    if tokened_phrase[0] == "FACING":
        try: 
            if tokened_phrase[1] != "LEFTPAR" or tokened_phrase[2] != "ORIENTATION" or tokened_phrase[3] != "RIGHTPAR":
                checker_bool = False
        except:
            checker_bool = False

    elif tokened_phrase[0] == "CAN":
        if (tokened_phrase[1] != "LEFTPAR") and (tokened_phrase[2] not in tokens_commands) and (tokened_phrase[len(tokened_phrase) - 1] != "RIGHTPAR"):
            checker_bool = False
        else:
            sliced_list = tokened_phrase[2: len(tokened_phrase) - 1]
            bool_command = analize_commands(sliced_list)
            checker_bool = bool_command
    
    elif tokened_phrase[0] == "NOT":
        if tokened_phrase[1] != "COLON":
            checker_bool = False
        else:
            if tokened_phrase[2] != "FACING" and tokened_phrase[2] != "CAN":
                checker_bool = False
            else:
                sliced_list = tokened_phrase[2: len(tokened_phrase)]
                bool_condition = analize_condition(sliced_list)
                checker_bool = bool_condition

    return checker_bool

#SIRVE
def analize_while(tokened_phrase: list):

    tokens_conditions = ["FACING", "CAN", "NOT"]

    checker_bool = True
        
    if "LEFTBRACE" in tokened_phrase:

        brace_position = tokened_phrase.index("LEFTBRACE")
            
        sliced_list = tokened_phrase[1: brace_position]

        if sliced_list[0] not in tokens_conditions:
            checker_bool = False
            
        else:
            checker_bool = analize_condition(sliced_list)
                
            if checker_bool == True and tokened_phrase[len(tokened_phrase) - 1] == "RIGHTBRACE" and tokened_phrase[len(tokened_phrase) - 2] == "RIGHTPAR":

                sliced_list_brace = tokened_phrase[brace_position + 1: len(tokened_phrase)-1]

                #We create lists to separate code by semicolons

                sub_lists = []
                temporal_sub_list = []

                for token in sliced_list_brace:
                    if token == "SEMICOL":
                        sub_lists.append(temporal_sub_list)
                        temporal_sub_list = []
                        
                    else:
                        temporal_sub_list.append(token)
                    
                if temporal_sub_list:
                    sub_lists.append(temporal_sub_list)


                i = 0
                while i < len(sub_lists) and checker_bool != False: 
                    little_code = sub_lists[i]
                    checker_bool = general_analizer(little_code)

                    i+= 1

            else:
                checker_bool = False
        
    else:
        checker_bool = False
    
    return checker_bool

def analize_repeat(tokened_phrase: list):

    checker_bool = True

    if (tokened_phrase[1] != "NUM" and tokened_phrase[1] != "VAR"):

        checker_bool = False

    else:

        if  tokened_phrase[2] != "TIMES":

            checker_bool = False

        else:
            
            if tokened_phrase[3] != "LEFTBRACE":

                checker_bool = False

            else:
                #ver esto en el while xd
                if tokened_phrase[len(tokened_phrase) - 1] == "RIGHTBRACE" and tokened_phrase[len(tokened_phrase) - 2] == "RIGHTPAR":
                        brace_position = tokened_phrase.index("RIGHTBRACE")

                        sliced_list = tokened_phrase[4: brace_position -1]

                        sub_lists = []
                        temporal_sub_list = []

                        for token in sliced_list:
                            if token == "SEMICOL":
                                sub_lists.append(temporal_sub_list)
                                temporal_sub_list = []
                                
                            else:
                                temporal_sub_list.append(token)
                            
                        if temporal_sub_list:
                            sub_lists.append(temporal_sub_list)

                        i = 0

                        while i < len(sub_lists) and checker_bool != False: 
                            little_code = sub_lists[i]
                            checker_bool = general_analizer(little_code)

                            i+= 1

    return checker_bool

def analize_equality(tokened_phrase: list):

    checker_bool = True

    if len(tokened_phrase) == 3:

        if tokened_phrase[1] != "EQUALS":
            checker_bool = False
        else:
            if (tokened_phrase[2] != "NUM" and tokened_phrase[2] != "VAR"):
                checker_bool = False

    elif tokened_phrase[1] == "LEFTPAR":

        sliced_list = tokened_phrase[2:len(tokened_phrase)-2]

        i = 0

        while i < len(sliced_list) and checker_bool:
            if i%2 == 0:
                if sliced_list[i] != "VAR" and sliced_list[i] != "NUM":
                    checker_bool = False
            else:
                if sliced_list[i] != "COMMA":
                    checker_bool = False
            i += 1

    else:
        checker_bool = False 
    
    return checker_bool



#MENSAJE DE COSAS PERSONALIZADAS
# YA -> VAR EQUALS NUM O VAR EQUALS VAR --- 
# BRACES CON LA MATRIZ
# CONDITIONALS
# YA -> SE PUEDE CON FUNCIONES DADAS POR UNO MISMO --. 
# AL DEFINIR LAS FUNCIONES LA ULTIMA COSITA NO PUEDE TENER UN PUNTO Y COMA