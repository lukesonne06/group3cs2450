class UVSimulator:
    def __init__(self, memory_size=250, file_name=None):
        # Initialize the simulator with file and memory size
        self.memory = [0] * memory_size    # Memory assigned as a list of zeros
        self.file_name = file_name
        
    def load_words(self):
        # Reads self.file_name into memory via load_from_text(); prints an error if the file is not found.
        try:
            with open(self.file_name, 'r') as f:
                text = f.read()
            self.load_from_text(text)
        except FileNotFoundError:
            print(f"Error: File '{self.file_name}' not found.")
            
    def load_from_text(self, text):
        i = 0
        words = text.split()   # handles spaces and new lines

        for word in words:
            if i >= len(self.memory):
                print("Memory full!")
                break
            try:
                value = int(word)
            except ValueError:
                print(f"Invalid input (not an integer): {word}")
                continue
            if value == -999999:
                break
            if value < -999999 or value > 999999:
                print(f"Invalid input (not 6 digits): {value}")
            else:
                self.memory[i] = value
                i += 1
            
    def execute_program(self):
        # Execute program
        pc = 0 # Program counter
        accumulator = 0    # Accumulator counter

        while pc < len(self.memory):
            instruction = self.memory[pc]    # Fetch instruction

            opcode = instruction // 1000   # First 3 digits = operation code
            operand = instruction % 1000    # Last 3 digits = memory address

            if operand < 0 or operand >= len(self.memory):
                print(f"Error: Invalid memory address {operand}.")
                break
            
            # --- Opcodes ---
            if opcode == 10:    # Read: input from user into memory
                while True:
                    try:
                        print("Enter an interger:")    # Prompt user
                        value = int(input())
                        if -999999 <= value <= 999999:     # Confirm number is 4 digits
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
                accumulator = int(accumulator / self.memory[operand])
            
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

            # overflow check for 6 digit values
            if accumulator < -999999 or accumulator > 999999:
                print("Error: Accumulator overflow.")
                break

            pc += 1    # Move to next job
