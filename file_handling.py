# how to open a file

#file = open("test.txt", 'r')

#content = file.read()

#print(content)

#for line in file:
    # print(line)

# to remove the space btw the two statement from print(line) we use a strip method
    #print(line.strip())

#file = open("example.txt", 'w')

#file.writelines("mkoppslsledjfjdj")

# when you use write mode to read a file it overrides the previous existing information on the read file

#file = open("text.txt", 'w')

#file.writelines("mkoppslsledjfjdj")
#file.close()

#with open("text.txt", 'r') as file:
    #for item in file:
        #print(item)

def fileopener(fileName, openMode):
    with open(fileName, openMode) as file:
         for line in file:
             print(line)

fileName = input("Enter the file name or path:")
openMode = ("open Mode? [w, r]:")

fileopener(fileName, openMode)








