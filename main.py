from prototype1 import load_words, memory, execute_program

def main():
    file_name = input("Enter the name of the file to load: ")
    load_words(file_name)
    execute_program()

if __name__ == "__main__":
    main()
