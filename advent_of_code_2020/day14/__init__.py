def parse_input(input_):
    program = []

    for line in input_.split("\n"):
        instruction, value = line.split(" = ")

        if instruction == "mask":
            program.append((instruction, value))
        else:
            instruction, address = instruction[:-1].split("[")
            program.append((instruction, int(address), int(value)))

    return program


class SeaportComputer:
    def __init__(self, program):
        self.program = program.copy()
        self.index = 0

        self.memory = {}
        self.current_mask = None

    def __iter__(self):
        return self

    def __next__(self):
        current_instruction = self.program[self.index]

        if current_instruction[0] == "mask":
            self.current_mask = current_instruction[1]
        else: # if current_instruction[1] == "mem"
            address, value = current_instruction[1:]

            self.apply_mask(address, value)

        self.index += 1

    def apply_mask(self, address, value):
        bits = ["0"] * 36
        bin_value = bin(value)[2:]

        for i in range(len(bits)):
            bit = None
            mask_bit = self.current_mask[-i-1]

            if mask_bit != "X":
                bit = mask_bit
            elif i < len(bin_value):
                bit = bin_value[-i-1]

            if bit is not None:
                bits[-i-1] = bit

        self.memory[address] = int("".join(bits), base=2)


class SeaportComputerV2(SeaportComputer):
    raise NotImplementedError


def part1(program):
    computer = SeaportComputer(program)

    while True:
        try:
            next(computer)
        except IndexError:
            return sum(computer.memory.values())


def part2(program):
    computer = SeaportComputerV2(program)

    while True:
        try:
            next(computer)
        except IndexError:
            return sum(computer.memory.values())
