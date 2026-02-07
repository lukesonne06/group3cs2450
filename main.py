from prototype1 import UVSimulator    # Import UVUSimlator class
import sys                            # Import sys to access command-line arguments


def main():
    # Get the file name from the command-line arguments
    # sys.argv[1] is the first argument after the script name
    file_name = sys.argv[1]

    # Create the simulator instance using the input file
    simulator = UVSimulator(file_name)

    # Load the program words from the file into memory
    simulator.load_words()

    # Execute the program stored in memory
    simulator.execute_program()
    
    
# This confirms main() only runs when this file is executed
if __name__ == "__main__":
    main()

