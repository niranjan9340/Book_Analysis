import re

with open('book.txt', 'r', encoding='UTF-8') as file:
    file_content = file.read()

pattern = re.compile('Chapter [0-9]')

matches = pattern.findall(file_content)

for match in matches:
    print(match)
