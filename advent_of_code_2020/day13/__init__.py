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
