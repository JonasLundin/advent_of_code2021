my_file = open("input.txt", "r")
content = my_file.read()
content_list = content.split()

def part1():
    k = 1

    for i, j in enumerate(content_list):
        if j > content_list[i - 1]:
            k += 1  
    print(f"Part1: {k}")

def part2():
    k = 0

    for i, j in enumerate(content_list):
        if i == len(content_list) - 3:
            break
        a = content_list[i] + content_list[i + 1] + content_list[i + 2]
        b = content_list[i + 1] + content_list[i + 2] + content_list[i + 3]
        if b > a:
            k += 1 

    print(f"Part2: {k}")
part1()
part2()
