def general_analyzer(tokenized_phrase: list):

    tokens_commands = ["JUMP", "WALK", "LEAP", "TURN", "TURNTO", "DROP", "GET", "GRAB", "LETGO", "NOP", "EQUALS"]
    
    if tokenized_phrase[0] == "DEFVAR":
        return analyze_variable(tokenized_phrase)
    elif tokenized_phrase[0] == "DEFPROC":
        return analyze_procedure(tokenized_phrase)
    elif tokenized_phrase[0] == "WHILE":
        return analyze_while(tokenized_phrase)
    elif tokenized_phrase[0] == "REPEAT":
        return analyze_repeat(tokenized_phrase)
    elif tokenized_phrase[0] == "VAR":
        return analyze_equality(tokenized_phrase)
    elif tokenized_phrase[0] in tokens_commands:
        return analyze_commands(tokenized_phrase)
    elif tokenized_phrase[0] == 'IF':
        return analyze_conditionals(tokenized_phrase)
    
    
#SIRVE
def analyze_variable(tokenized_phrase: list):
    
    checker_bool = True

    if len(tokenized_phrase) != 3:
        checker_bool = False
    else:
        if tokenized_phrase[1] != "VAR" or (tokenized_phrase[2] != "VAR" and tokenized_phrase[2] != "NUM"):
            checker_bool = False
        
    return checker_bool

def analyze_procedure(tokenized_phrase: list):
    
    checker_bool = True
    
    if tokenized_phrase[1] != 'VAR':
        checker_bool = False
    else:
        if tokenized_phrase[2] != "LEFTPAR" and tokenized_phrase[len(tokenized_phrase) - 1] != "RIGHTPAR":
            checker_bool = False
        else:
            try:
                if tokenized_phrase[3] != "RIGHTPAR":
                    if tokenized_phrase[len(tokenized_phrase) - 2] != "VAR":
                        checker_bool = False
                    else:
                        sliced_list = tokenized_phrase[3: len(tokenized_phrase) - 2]
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
def analyze_commands(tokenized_phrase: list):

    checker_bool = True

    if tokenized_phrase[0] == "JUMP":
        try:
            if tokenized_phrase[1] != "LEFTPAR" or (tokenized_phrase[2] != "NUM" and tokenized_phrase[2] != "VAR") or tokenized_phrase[3] != "COMMA" or (tokenized_phrase[4] != "NUM" and tokenized_phrase[4] != "VAR") or tokenized_phrase[5] != "RIGHTPAR":
                checker_bool = False
        except:
            checker_bool = False

    elif tokenized_phrase[0] == "WALK":

        if len(tokenized_phrase) == 4:
            if tokenized_phrase[1] != "LEFTPAR" or (tokenized_phrase[2] != "NUM" and tokenized_phrase[2] != "VAR") or tokenized_phrase[3] != "RIGHTPAR":
                checker_bool = False
        elif len(tokenized_phrase) == 6:
            if tokenized_phrase[1] != "LEFTPAR" or (tokenized_phrase[2] != "NUM" and tokenized_phrase[2] != "VAR") or tokenized_phrase[3] != "COMMA" or (tokenized_phrase[4] != "DIRECTION" and tokenized_phrase[4] != "ORIENTATION") or tokenized_phrase[5] != "RIGHTPAR":
                checker_bool = False
        else:
            checker_bool = False

    elif tokenized_phrase[0] == "LEAP":
        if len(tokenized_phrase) == 4:
             if tokenized_phrase[1] != "LEFTPAR" or (tokenized_phrase[2] != "NUM" and tokenized_phrase[2] != "VAR") or tokenized_phrase[3] != "RIGHTPAR":
                checker_bool = False
        elif len(tokenized_phrase) == 6:
            if tokenized_phrase[1] != "LEFTPAR" or (tokenized_phrase[2] != "NUM" and tokenized_phrase[2] != "VAR") or tokenized_phrase[3] != "COMMA" or (tokenized_phrase[4] != "DIRECTION" and tokenized_phrase[4] != "ORIENTATION") or tokenized_phrase[5] != "RIGHTPAR":
                checker_bool = False
        else:
            checker_bool = False

    elif tokenized_phrase[0] == "TURN":
        try:
            if tokenized_phrase[1] != "LEFTPAR" or tokenized_phrase[2] != "DIRECTION" or tokenized_phrase[3] != "RIGHTPAR":
                checker_bool = False
        except:
            checker_bool = False
            
    elif tokenized_phrase[0] == "TURNTO":
        try: 
            if tokenized_phrase[1] != "LEFTPAR" or tokenized_phrase[2] != "ORIENTATION" or tokenized_phrase[3] != "RIGHTPAR":
                checker_bool = False
        except:
            checker_bool = False

    elif tokenized_phrase[0] == "DROP":
        try:
            if tokenized_phrase[1] != "LEFTPAR" or (tokenized_phrase[2] != "NUM" and tokenized_phrase[2] != "VAR") or tokenized_phrase[3] != "RIGHTPAR":
                    checker_bool = False
        except:
            checker_bool = False
    
    elif tokenized_phrase[0] == "GET":
        try:
            if tokenized_phrase[1] != "LEFTPAR" or (tokenized_phrase[2] != "NUM" and tokenized_phrase[2] != "VAR") or tokenized_phrase[3] != "RIGHTPAR":
                checker_bool = False
        except:
            checker_bool = False

    elif tokenized_phrase[0] == "GRAB":
        try: 
            if tokenized_phrase[1] != "LEFTPAR" or (tokenized_phrase[2] != "NUM" and tokenized_phrase[2] != "VAR") or tokenized_phrase[3] != "RIGHTPAR":
                checker_bool = False
        except:
            checker_bool = False
    
    elif tokenized_phrase[0] == "LETGO":
        try:
            if tokenized_phrase[1] != "LEFTPAR" or (tokenized_phrase[2] != "NUM" and tokenized_phrase[2] != "VAR") or tokenized_phrase[3] != "RIGHTPAR":
                checker_bool = False
        except:
            checker_bool = False

    elif tokenized_phrase[0] == "NOP":
        try:
            if tokenized_phrase[1] != "LEFTPAR" or tokenized_phrase[2] != "RIGHTPAR":
                checker_bool = False
        except:
            checker_bool = False


    return checker_bool

#SIRVE
def analyze_condition(tokenized_phrase: list):

    tokens_commands = ["JUMP", "WALK", "LEAP", "TURN", "TURNTO", "DROP", "GET", "GRAB", "LETGO", "NOP", "EQUALS"]

    checker_bool = True
    
    if tokenized_phrase[0] == "FACING":
        try: 
            if tokenized_phrase[1] != "LEFTPAR" or tokenized_phrase[2] != "ORIENTATION" or tokenized_phrase[3] != "RIGHTPAR":
                checker_bool = False
        except:
            checker_bool = False

    elif tokenized_phrase[0] == "CAN":
        if (tokenized_phrase[1] != "LEFTPAR") or (tokenized_phrase[2] not in tokens_commands) or (tokenized_phrase[len(tokenized_phrase) - 1] != "RIGHTPAR"):
            checker_bool = False
        else:
            sliced_list = tokenized_phrase[2: len(tokenized_phrase) - 1]
            bool_command = analyze_commands(sliced_list)
            checker_bool = bool_command
    
    elif tokenized_phrase[0] == "NOT":
        if tokenized_phrase[1] != "COLON":
            checker_bool = False
        else:
            if tokenized_phrase[2] != "FACING" and tokenized_phrase[2] != "CAN" and tokenized_phrase[2] != "NOT":
                checker_bool = False
            else:
                sliced_list = tokenized_phrase[2: len(tokenized_phrase)]
                bool_condition = analyze_condition(sliced_list)
                checker_bool = bool_condition

    return checker_bool

#SIRVE HASTA ACA TOKENIZED
def analyze_while(tokenized_phrase: list):

    tokens_conditions = ["FACING", "CAN", "NOT"]

    checker_bool = True
        
    if "LEFTBRACE" in tokenized_phrase:

        brace_position = tokenized_phrase.index("LEFTBRACE")
            
        sliced_list = tokenized_phrase[1: brace_position]

        if sliced_list[0] not in tokens_conditions:
            checker_bool = False
            
        else:
            checker_bool = analyze_condition(sliced_list)
                
            if checker_bool == True and tokenized_phrase[len(tokenized_phrase) - 1] == "RIGHTBRACE" and tokenized_phrase[len(tokenized_phrase) - 2] == "RIGHTPAR":

                sliced_list_brace = tokenized_phrase[brace_position + 1: len(tokenized_phrase)-1]

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
                    checker_bool = general_analyzer(little_code)

                    i+= 1

            else:
                checker_bool = False
        
    else:
        checker_bool = False
    
    return checker_bool

def analyze_repeat(tokenized_phrase: list):

    checker_bool = True

    if (tokenized_phrase[1] != "NUM" and tokenized_phrase[1] != "VAR"):

        checker_bool = False

    else:

        if  tokenized_phrase[2] != "TIMES":

            checker_bool = False

        else:
            
            if tokenized_phrase[3] != "LEFTBRACE":

                checker_bool = False

            else:
                #ver esto en el while xd
                if tokenized_phrase[len(tokenized_phrase) - 1] == "RIGHTBRACE" and tokenized_phrase[len(tokenized_phrase) - 2] == "RIGHTPAR":
                        brace_position = tokenized_phrase.index("RIGHTBRACE")

                        sliced_list = tokenized_phrase[4: brace_position -1]

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
                            checker_bool = general_analyzer(little_code)

                            i+= 1

    return checker_bool

def analyze_equality(tokenized_phrase: list):

    checker_bool = True

    if len(tokenized_phrase) == 3:

        if tokenized_phrase[1] != "EQUALS":
            checker_bool = False
        else:
            if (tokenized_phrase[2] != "NUM" and tokenized_phrase[2] != "VAR"):
                checker_bool = False

    elif tokenized_phrase[1] == "LEFTPAR":

        sliced_list = tokenized_phrase[2:len(tokenized_phrase)-2]

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

def analyze_conditionals(tokenized_phrase: list):
    
    checker_bool = True
    
    tokens_conditions = ["FACING", "CAN", "NOT"]
    
    if "ELSE" not in tokenized_phrase:
        checker_bool = False
    else:
        index_else = tokenized_phrase.index("ELSE")
        
        first_part = tokenized_phrase[0: index_else]
        second_part = tokenized_phrase[index_else: len(tokenized_phrase)]
        
        if first_part[1] not in tokens_conditions or ("LEFTBRACE" not in first_part) or ("LEFTBRACE" not in second_part) or (first_part[len(first_part) -1] != "RIGHTBRACE") or (second_part[len(second_part) -1] != "RIGHTBRACE"):
            checker_bool = False
        else:
            
            brace_position_first = first_part.index("LEFTBRACE")
            sliced_condition = first_part[1: brace_position_first]
            
            bool_condition = analyze_condition(sliced_condition)
            checker_bool = bool_condition
            
            if checker_bool:
                
                brace_position_second = second_part.index("LEFTBRACE")
                
                sliced_block_one = first_part[brace_position_first + 1: len(first_part) -1]
                sliced_block_two = second_part[brace_position_second +1: len(second_part)-1]
                
                #FIRST LIST
                sub_lists_one = []
                temporal_sub_list_one = []

                for token in sliced_block_one:
                    if token == "SEMICOL":
                        sub_lists_one.append(temporal_sub_list_one)
                        temporal_sub_list_one = []
                        
                    else:
                        temporal_sub_list_one.append(token)
                    
                if temporal_sub_list_one:
                    sub_lists_one.append(temporal_sub_list_one)
                    
                i = 0
                while i < len(sub_lists_one) and checker_bool != False: 
                    little_code = sub_lists_one[i]
                    checker_bool = general_analyzer(little_code)

                    i+= 1
                
                if checker_bool:
                
                
                    #SECOND LIST
                    sub_lists_two = []
                    temporal_sub_list_two = []

                    for token in sliced_block_two:
                        if token == "SEMICOL":
                            sub_lists_two.append(temporal_sub_list_two)
                            temporal_sub_list_two = []
                            
                        else:
                            temporal_sub_list_two.append(token)
                        
                    if temporal_sub_list_two:
                        sub_lists_two.append(temporal_sub_list_two)
                        
                    i = 0
                    while i < len(sub_lists_two) and checker_bool != False: 
                        little_code = sub_lists_two[i]
                        checker_bool = general_analyzer(little_code)

                        i+= 1
    
    return checker_bool
    
def analyze_blocks(tokenized_phrase)



#MENSAJE DE COSAS PERSONALIZADAS
# YA -> VAR EQUALS NUM O VAR EQUALS VAR --- 
# BRACES CON LA MATRIZ
# CONDITIONALS
# YA -> SE PUEDE CON FUNCIONES DADAS POR UNO MISMO --. 
# AL DEFINIR LAS FUNCIONES LA ULTIMA COSITA NO PUEDE TENER UN PUNTO Y COMA