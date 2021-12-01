my_file = open("input.txt", "r")
content = my_file.read()
content_list = content.split()
numbers = [ int(x) for x in content_list ]

def part1():
    k = 0
    for i, j in enumerate(numbers):
        if j > numbers[i - 1]:
            k += 1  
    print(f"Part1: {k}")

def part2():
    k = 0
    for i, j in enumerate(numbers):
        if i == len(numbers) - 3:
            break
        a = numbers[i] + numbers[i + 1] + numbers[i + 2]
        b = numbers[i + 1] + numbers[i + 2] + numbers[i + 3]
        if b > a:
            k += 1 

    print(f"Part2: {k}")

part1()
part2()
