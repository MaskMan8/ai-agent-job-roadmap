
file = open("message.txt", "w")
file.write("hello world")
file.close()

file = open("message.txt", "r")
content = file.read()
print(content)
file.close()