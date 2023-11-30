number_to_text = {
    '0': 'zero',
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine'
}
with open('file2.txt', 'r') as file:
    content = file.read()
for digit, text in number_to_text.items():
    content = content.replace(digit, text)
with open('file2.txt', 'w') as file:
    file.write(content)
