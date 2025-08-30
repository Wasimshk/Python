# write to a file

# if filehandling.txt is present then write function will replace the content, but if the file is not present then it will create a new file with the provided content
with open("filehandling.txt", "w") as writerObj:
    s = """
    this file is created directly through the write method, 
    if the file is present write mode will replace the whole content if not 
    then it will create a new file with the content we provided.
    """
    writerObj.write(s)
    # writerObj.close() we do not need to close the file in with open it automatically closes

# in case of read, if the file is not present then it will through a FileNotFoundError
with open("filehandling.txt", "r") as readerObj:
    print(readerObj.read())

# readlines will create list of lines
with open("filehandling.txt", "r") as readerObj:
    listofLines = readerObj.readlines()

# adding the content in reverse order
with open("filehandling.txt", "w") as writerObj:
    for line in reversed(listofLines):
        writerObj.write(line)

# # normal way but need to close the file explicitly
#
# reader = open("filehandling.txt", "r")
# # print(reader.read())
# for line in reader:
#     print(line)
# reader.close()