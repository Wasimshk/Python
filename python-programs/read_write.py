

with open("mytext.txt", "r") as readerobj:
    mylist = readerobj.readlines()
    print(mylist)

    with open("mytext.txt", "w") as writerObj:
        # writerObj.write("age-29") #replace the whole text file content with new age-29 text
        for line in reversed(mylist):
            writerObj.write(line)
