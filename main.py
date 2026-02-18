from prototype1 import UVSimulator    # Import UVUSimlator class


def main():
    # Get the file name from the command-line arguments
    # sys.argv[1] is the first argument after the script name
    #file_name = sys.argv[1]

    # Create the simulator instance using the input file
    simulator = UVSimulator()
    # Take user input for program words and load them into memory
    simulator.load_from_text(input("Enter your program words (separated by spaces, newlines, or tabs): "))
    # Execute the program stored in memory
    simulator.execute_program()
    
    
# This confirms main() only runs when this file is executed
if __name__ == "__main__":
    main()

