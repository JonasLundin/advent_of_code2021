import collections

my_file = open("input.txt", "r")
content = my_file.read()
content_list = content.split()
least=[]
most=[]

for i in range(12):
    least += [(collections.Counter(x[i] for x in content_list).most_common())[1]]
    most += [(collections.Counter(x[i] for x in content_list).most_common())[0]]


gamma_list = [a_tuple[0] for a_tuple in most]
epsilon_list = [a_tuple[0] for a_tuple in least]
gamma = ''.join([str(elem) for elem in gamma_list])
epsilon = ''.join([str(elem) for elem in epsilon_list])

print(f"Gamma: {gamma}")
print(f"Epsilon: {epsilon}")
result = int(gamma, 2) * int(epsilon, 2)
print(f"Answer {result}")
