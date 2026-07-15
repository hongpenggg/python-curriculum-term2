# Reading

# method 1
file = open("words.txt", "r")
line = file.read()
print(line)
file.close()

# method 2 

with open("words.txt", "r") as file:
    line = file.read()
    print(line)

print("-------------")
# read, readline, readlines

# read reads the whole file as a string
with open("words.txt", "r") as file:
    line = file.read()
    print(line)
    print(repr(line))

print("-------------")

# readline reads the first line as a string, calling it again will cause it to go to the next line
with open("words.txt", "r") as file:
    line1 = file.readline()
    line2 = file.readline()
    print(line1)
    print(repr(line1))
    print(line2)
    print(repr(line2))


print("-------------")

# read lines reads the whole file as an array
with open("words.txt", "r") as file:
    line = file.readlines()
    print(line)
    for i in line:
        print(repr(i))

print("-------------")

# Writing

# write writes one line at a time
# writelines take an array of strings, and writes them to the file
# remember your \n, because python will not automatically add it 

# method 1
file = open("words.txt", "w")
file.write("Hi")
file.write("Hello\n")
file.write("what is up")
file.close()

# method 2 
words = ["chocolate", "vanilla", "strawberry"]

with open("words.txt", "w") as file:
    file.writelines(words)