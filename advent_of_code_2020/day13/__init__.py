from collections import namedtuple
import math
import operator


Bus = namedtuple("Bus", ["id", "offset"])


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


def find_first_occurence(buses):
    lcm = math.lcm(*(bus.id for bus in buses))
    sorted_buses = sorted(buses, key=operator.itemgetter(0))
    largest = sorted_buses.pop()
    num = -largest.offset

    while num < lcm:
        check = 0
        valids = []

        for bus in buses:
            if (num + bus.offset) % bus.id == 0:
                check += 1
                valids.append(bus.id)

        if check:
            print(num, check, valids)

        if check == len(buses):
            return num
        else:
            num += largest.id


def part2(data):
    _, bus_ids = data
    buses = []

    for offset, bus_id in enumerate(bus_ids):
        if bus_id is not None:
            buses.append(Bus(bus_id, offset))

    return find_first_occurence(buses)
