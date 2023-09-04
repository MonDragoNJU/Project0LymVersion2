import Parce as parser

def main():
    
    print("")
    print("WELCOME to the syntax checker of the robot program.")
    print("")

    print("To check your program make sure to follow these instructions: ")
    print("")
    print("-- *CONDITIONALS AND LOOPS*--")
    print("Write ¨if-else¨, ¨repeat x times¨ and ¨while¨ instructions in just one code line.")
    print("")
    print("-- *DEFPROC* --")
    print("When adding a defproc, write one brace per line. Then, write the instructions block between both braces. Instructions must be written in just one code line. Here is an example: ")
    print("")
    print("Example: ")
    print("defProc goNorth()")
    print("{while can(walk(1,north)){walk(1,north)}}")

    print("")


    print("-- *CODE BLOCKS* --")
    print("If you have block of instructions you must write them in one code line.")
    print("For instance check: ")
    print("{jump (3 ,3) ; putCB (2 ,1)}")

    print("")

    print("WARNING!")

    print("Otherwise the verification process will fail")

    print("")

    print("Enjoy! :)")

    print(r"""
    /\_/\
    ( o.o )
    > ^ <
    """)
        
    file = input("Insert the path of the file you want to read: ")
    answer = parser.read_file(file)
    
    print(answer)

    
    
main()    
    
