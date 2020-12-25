def parse_input(input_):
    return [int(i) for i in input_.split("\n")]


class EncryptionKey:
    def __init__(self, subject_number):
        self.subject_number = subject_number
        self._cache = []

    def transform(self, value, *, divisor=20201227):
        value *= self.subject_number

        return value % divisor

    def get_loop_size(self, key):
        loop_size = 0
        value = 1

        if key in self._cache:
            return self._cache.index(key) + 1

        # Cannot do `while value < key`.
        while True:
            try:
                value = self._cache[loop_size]
            except IndexError:
                value = self.transform(value)
                self._cache.append(value)

            loop_size += 1

            if value == key:
                return loop_size


def part1(keys):
    card_key, door_key = keys

    encryption = EncryptionKey(7)
    card_loop_size = encryption.get_loop_size(card_key)
    door_loop_size = encryption.get_loop_size(door_key)

    card_encryption = EncryptionKey(card_key)
    encryption_key = 1

    for i in range(door_loop_size):
        encryption_key = card_encryption.transform(encryption_key)

    return encryption_key


def part2(entries):
    pass
