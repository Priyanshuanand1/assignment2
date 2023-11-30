with open('file1.txt', 'r') as file:
    content = file.read()
reversed_content = content[::-1]
with open('file1.txt', 'w') as file:
    file.write(reversed_content)
