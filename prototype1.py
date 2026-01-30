class UVSimulator:
    def __init__(self, file_name=None, memory_size=100):
        self.memory = [0] * memory_size
        self.file_name = file_name

    def load_words(self):
        i = 0
        try:
            with open(self.file_name, "r") as file:
                for line in file:
                    if i >= len(self.memory):
                        print("Memory full!")
                        break

                    line = line.strip()

                    try:
                        word = int(line)
                    except ValueError:
                        print(f"Invalid input in file (not an integer): {line}")
                        continue

                    if word == -99999:
                        break

                    if word < -9999 or word > 9999:
                        print(f"Invalid input (not four digits): {word}")
                    else:
                        self.memory[i] = word
                        i += 1

        except FileNotFoundError:
            print(f"Error: file '{self.file_name}' not found.")
            
    def execute_program(self):
        pc = 0
        accumulator = 0

        while pc < len(self.memory):
            instruction = self.memory[pc]

            if instruction < 0:
                print("Error: Negative instruction value.")
                break

            opcode = instruction // 100
            operand = instruction % 100

            if opcode == 10:
                while True:
                    try:
                        print("Enter an interger:")
                        value = int(input())
                        if -9999 <= value <= 9999:
                            self.memory[operand] = value
                            break
                        else:
                            print("Please enter a four digit integer.")
                    except ValueError:
                        print("Invalid input.")

            elif opcode == 11:
                print(self.memory[operand])

            elif opcode == 20:
                accumulator = self.memory[operand]

            elif opcode == 21:
                self.memory[operand] = accumulator

            elif opcode == 30:
                accumulator += self.memory[operand]

            elif opcode == 31:
                accumulator -= self.memory[operand]
            elif opcode == 32:
                if self.memory[operand] == 0:
                    print("Error: Division by zero.")
                    break
                accumulator //= self.memory[operand]
            
            elif opcode == 33:
                accumulator *= self.memory[operand]

            elif opcode == 40:
                pc = operand-1

            elif opcode == 41:
                if accumulator < 0:
                    pc = operand-1
            
            elif opcode == 42:
                if accumulator == 0:
                    pc = operand-1
            
            elif opcode == 43:
                print("Halting execution.")
                break

            else:
                print(f"Invalid opcode {opcode} at address {pc}")
                break

            pc += 1



