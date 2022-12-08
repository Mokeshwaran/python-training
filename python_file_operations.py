read_only = open("text_file.txt", 'r')
text = read_only.read()
print(text)

write_only = open("file1.txt", 'w')
print(write_only.write(text))

append_only = open("file2.txt", 'a')
print(append_only.write(text))

read_write = open("file2.txt", 'r+')
print(read_write.read())
print(read_write.write(text))

write_read = open("file4.txt", 'w+')
print(write_read.read())
print(write_read.write(text))

read_write_append = open("file5.txt", 'a+')
print(read_write_append.read())
print(read_write_append.write(text))
read_write_append.close()

with open("file.txt") as file:
    for i in file:
        print(i)

print(file.write(text))
