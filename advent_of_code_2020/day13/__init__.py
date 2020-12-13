def parse_bus_ids(raw_bus_ids):
    bus_ids = []

    for raw_bus_id in raw_bus_ids.split(","):
        try:
            bus_id = int(raw_bus_id)
        except ValueError:
            bus_id = None
        finally:
            bus_ids.append(bus_id)

    return bus_ids


def parse_input(input_):
    raw_timestamp, raw_bus_ids = input_.split("\n")

    return int(raw_timestamp), parse_bus_ids(raw_bus_ids)


def part1(data):
    start_time, bus_ids = data
    valid_bus_ids = list(filter(None, bus_ids))
    wait_time = 1  # Note `0 % bus_id` will always equal zero.

    while True:
        for bus_id in valid_bus_ids:
            if (start_time + wait_time) % bus_id == 0:  # Normal division produces a float that cannot equal zero!
                return bus_id * wait_time

        wait_time += 1


def part2(data):
    _, bus_ids = data
    constrained_bus_ids = {}

    for offset, bus_id in enumerate(bus_ids):
        if bus_id is not None:
            constrained_bus_ids[bus_id] = offset

    num = 0
    while True:
        check = 0
        valids = []

        for bus_id, offset in constrained_bus_ids.items():
            if (num + offset) % bus_id == 0:
                check += 1
                valids.append(bus_id)

        if check:
            print(num, check, valids)

        if check == len(constrained_bus_ids):
            return num
        else:
            num += 1
