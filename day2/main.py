with open("input.txt") as load_file:
    data = [tuple(line.split()) for line in load_file]

def part1():
    depth = 0
    horizonal_position = 0

    for i, tuple in enumerate(data):
        command = tuple[0]
        value = tuple[1]
        if command == "down":
            depth = depth + int(value)
        elif command == "up":
            depth = depth - int(value)
        else:
            horizonal_position = horizonal_position + int(value)
    print(f"Depth: {depth}. Horizontal position {horizonal_position}")
    print(f"Result: {depth * horizonal_position}.")

def part2():
    depth = 0
    horizonal_position = 0
    aim = 0

    for i, tuple in enumerate(data):
        command = tuple[0]
        value = tuple[1]
        if command == "down":
            aim = aim + int(value)
        elif command == "up":
            aim = aim - int(value)
        else:
            horizonal_position = horizonal_position + int(value)
            depth = depth + aim*int(value)
    print(f"Depth: {depth}. Horizontal position {horizonal_position}. Aim: {aim}")
    print(f"Result: {depth * horizonal_position}.")
part1()
part2()
