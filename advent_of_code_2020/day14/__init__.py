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
    def get_float(self, value):
        bits = ["0"] * 36
        bin_value = bin(value)[2:]

        for i in range(len(bits)):
            bit = None
            mask_bit = self.current_mask[-i-1]

            if i < len(bin_value):
                bits[-i-1] = bin_value[-i-1]

            if mask_bit != "0":
                bit = mask_bit

            if bit is not None:
                bits[-i-1] = bit

        return bits

    def apply_mask(self, address, value):
        floats = [self.get_float(address)]
        addresses = []

        while len(floats):
            float_ = floats.pop()

            if "X" in float_:
                x_index = float_.index("X")

                for i in range(2):
                    lst = float_.copy()
                    lst[x_index] = str(i)  # lol have to convert to `str` to `join()`
                    floats.append(lst)
            else:
                addresses.append(int("".join(float_), base=2))

        for address in addresses:
            self.memory[address] = value


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
