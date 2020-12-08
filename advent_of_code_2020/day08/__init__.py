def parse_input(input_):
    code = []

    for raw_instructions in input_.split("\n"):
        op, arg = raw_instructions.split(" ")
        code.append((op, int(arg)))

    return code


class Device:
    def __init__(self, code, index=0, accumulator=0):
        self.code = code
        self.index = index

        self.accumulator = accumulator
        self.accessed = set()

    def execute(self):
        op, arg = self.code[self.index]
        
        getattr(self, op)(arg)

    def acc(self, arg):
        self.accessed.add(self.index)
        self.accumulator += arg
        self.index += 1

    def jmp(self, arg):
        self.accessed.add(self.index)
        self.index += arg

    def nop(self, arg):
        self.accessed.add(self.index)
        self.index += 1


def part1(code):
    device = Device(code)

    while True:
        if device.index in device.accessed:
            return device.accumulator
        else:
            device.execute()


def part2(entries):
    pass
