class UVSimulator:
    def __init__(self, file_name=None, memory_size=100):
        # Initialize the simulator with file and memory size
        self.memory = [0] * memory_size    # Memory assigned as a list of zeros
        self.file_name = file_name

    def load_words(self):
        # Load integer words from the file to memory
        i = 0
        try:
            with open(self.file_name, "r") as file:
                for line in file:
                    if i >= len(self.memory):    # Check if memory is full
                        print("Memory full!")
                        break

                    line = line.strip()    # Remove whitespace

                    # Attempt to convert line to an integer
                    try:
                        word = int(line)
                    except ValueError:
                        print(f"Invalid input in file (not an integer): {line}")
                        continue
                    # Stop reading at -99999
                    if word == -99999:
                        break
                    # Check that the integer is a valid 4 digit word
                    if word < -9999 or word > 9999:
                        print(f"Invalid input (not four digits): {word}")
                    else:
                        self.memory[i] = word    # Store word in memory
                        i += 1

        except FileNotFoundError:
            # Output if file does not exist
            print(f"Error: file '{self.file_name}' not found.")
            
    def execute_program(self):
        # Execute program
        pc = 0 # Program counter
        accumulator = 0    # Accumulator counter

        while pc < len(self.memory):
            instruction = self.memory[pc]    # Fetch instruction

            if instruction < 0:
                # Negative instruction value is invalid
                print("Error: Negative instruction value.")
                break

            opcode = instruction // 100    # Frist two digits = operation code
            operand = instruction % 100    # Last two digits = memory address

            # --- Opcodes ---
            if opcode == 10:    # Read: input from user into memory
                while True:
                    try:
                        print("Enter an interger:")    # Prompt user
                        value = int(input())
                        if -9999 <= value <= 9999:     # Confirm number is 4 digits
                            self.memory[operand] = value
                            break
                        else:
                            print("Please enter a four digit integer.")
                    except ValueError:
                        print("Invalid input.")

            elif opcode == 11:    # Write: Output memory value to console
                print(self.memory[operand])

            elif opcode == 20:    # Load: load memory value to accumlator
                accumulator = self.memory[operand]

            elif opcode == 21:    # Store: store accumulator value to memory
                self.memory[operand] = accumulator

            elif opcode == 30:    # Add: add memory value to accumulator
                accumulator += self.memory[operand]

            elif opcode == 31:    # Subtract: subtract memory value from accumulator
                accumulator -= self.memory[operand]
                
            elif opcode == 32:    # Divide: divide accumulator by memory value
                if self.memory[operand] == 0:
                    print("Error: Division by zero.")
                    break
                accumulator //= self.memory[operand]
            
            elif opcode == 33:    # Multiply: multiply accumlator by memory value
                accumulator *= self.memory[operand]

            elif opcode == 40:    # Branch: unconditional jump
                pc = operand-1

            elif opcode == 41:    # Branch: jump if accumulator is < 0
                if accumulator < 0:
                    pc = operand-1
            
            elif opcode == 42:    # Branch: Jump is accumlator == 0
                if accumulator == 0:
                    pc = operand-1
            
            elif opcode == 43:    # Stop program execution
                print("Halting execution.")
                break

            else:
                print(f"Invalid opcode {opcode} at address {pc}")
                break

            pc += 1    # Move to next job





