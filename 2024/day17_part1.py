def solve():
    N = 5         # number of lines of input
    registers = []
    instructions = ''

    for _ in range(N):
        t = input()
        if not t:
            continue
        if t[0] == 'R':
            registers.append(int(t.split()[-1]))
        else:
            instructions = list(map(int, t.split()[-1].split(',')))


    def output_from_program(instructions):

        def get_operand(operand):
            match operand:
                case 0 | 1 | 2 | 3:
                    return operand
                case 4 | 5 | 6:
                    return registers[operand - 4]

        def perform_instruction(idx, opcode, operand):
            match opcode:
                case 0:
                    operand = get_operand(operand)
                    registers[0] //= pow(2, operand)
                case 1:
                    registers[1] ^= operand
                case 2:
                    operand = get_operand(operand)
                    registers[1] = operand % 8
                case 3:
                    if registers[0] != 0:
                        return operand
                case 4:
                    registers[1] ^= registers[2]
                case 5:
                    operand = get_operand(operand)
                    ret.append(operand % 8)
                case 6:
                    operand = get_operand(operand)
                    registers[1] = registers[0] // pow(2, operand)
                case 7:
                    operand = get_operand(operand)
                    registers[2] = registers[0] // pow(2, operand)

            return idx + 2

        idx = 0
        ret = []

        while idx + 1 < len(instructions):
            opcode, operand = instructions[idx], instructions[idx + 1]
            idx = perform_instruction(idx, opcode, operand)
    
        return ret
    
    return output_from_program(instructions)


print(solve())