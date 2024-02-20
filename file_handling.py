file = open("test.txt" "r")

Content = file.read()

for line in file:
    print(line.strip)

