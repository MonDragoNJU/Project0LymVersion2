import Parce as parser

def main():
    
    print()
    print("Welcome to the syntax checker of the robot program.")
    print()
    
    file = input("Insert the path of the file you want to read: ")
    answer = parser.read_file(file)
    
    print(answer)

    
    
#main()    
    
