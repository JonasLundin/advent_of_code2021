with open("input_test.txt") as load_file:
    data = [tuple(line.split()) for line in load_file]

depth = 0
horizonal_position = 0

for i, tuple in enumerate(data):
    command = tuple[0]
    value = tuple[1]
    print(command,value)
    if command == "down":
        depth = depth + int(value)
    elif command == "up":
        depth = depth - int(value)
    else:
        horizonal_position = horizonal_position + value
