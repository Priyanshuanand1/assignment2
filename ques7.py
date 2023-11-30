my_dict = {}
with open('file3.txt', 'r') as file:
    lines = file.readlines()
for line in lines:
    key, value = line.strip().split(':')
    my_dict[key] = value
print(my_dict)
