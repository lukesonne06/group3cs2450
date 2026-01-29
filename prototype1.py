
memory = [0] * 100

def load_words(file_name):
    i = 0
    try:
        with open(file_name, "r") as file:
            for line in file:
                if i >= len(memory):
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
                    memory[i] = word
                    i += 1

    except FileNotFoundError:
        print(f"Error: file '{file_name}' not found.")
        
def execute_program():
    pc = 0
    accumulator = 0

    while pc < len(memory):
        instruction = memory[pc]

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
                        memory[operand] = value
                        break
                    else:
                        print("Please enter a four digit integer.")
                except ValueError:
                    print("Invalid input.")

        elif opcode == 11:
            print(memory[operand])

        elif opcode == 20:
            accumulator = memory[operand]

        elif opcode == 21:
            memory[operand] = accumulator

        elif opcode == 30:
            accumulator += memory[operand]

        elif opcode == 31:
            accumulator -= memory[operand]

        elif opcode == 32:
            if memory[operand] == 0:
                print("Error: Division by zero.")
                break
            accumulator //= memory[operand]
        
        elif opcode == 33:
            accumulator *= memory[operand]

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



