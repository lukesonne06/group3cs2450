class UVSimulator:
    def __init__(self, memory_size=100):
        # Initialize the simulator with file and memory size
        self.memory = [0] * memory_size    # Memory assigned as a list of zeros

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
            if value == -99999:
                break
            if value < -9999 or value > 9999:
                print(f"Invalid input (not four digits): {value}")
            else:
                self.memory[i] = value
                i += 1
            
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








