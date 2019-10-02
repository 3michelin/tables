def writeTableToFile(display):
    fileName = input("What do you want to name your file (the file name cannot contain: / \ : * ? \" < > |): ")
    while '/' in fileName or '\\' in fileName or ':' in fileName or '*' in fileName or '?' in fileName or '\"' in fileName or '<' in fileName or  '>' in fileName or '|' in fileName:
        fileName = input("What do you want to name your file (the file name cannot contain: / \ : * ? \" < > |): ")
    
    f = open(fileName + ".txt", "w")
    f.write(display)
    f.close()
    print("File saved.")

def ask(display):
    while True:
        yn = input("Do you want to save this truth table to a .txt file? (Y to save /  N to forget): ").lower()
        if yn == 'y':
            writeTableToFile(display)
            break
        elif yn == 'n':
            print("Ok. See you next time.")
            break
        else:
            print("That\'s not an option. Please choose an available option.")

