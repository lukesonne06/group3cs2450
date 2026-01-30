from prototype1 import UVSimulator
import sys


def main():
    file_name = sys.argv[1]
    simulator = UVSimulator(file_name)
    simulator.load_words()
    simulator.execute_program()
    
    

if __name__ == "__main__":
    main()
