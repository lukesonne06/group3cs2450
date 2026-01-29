
memory = [0] * 100

def load_words():
    print("Enter words (type -99999 to finish):")
    
    i = 0
    while True:
        word = input()

        try:
            word = int(word)   # convert to int
        except ValueError:
            print("Invalid input, please enter a integer.")
            continue

        if word == -99999:
            break

        if i >= len(memory):
            print("Memory full!")
            break

        if word < -9999 or word > 9999:
            print("Invalid input, please enter a four digit integer.")
        else:
            memory[i] = word
            i += 1

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


