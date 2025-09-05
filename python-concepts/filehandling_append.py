# write to a file

# if filehandling.txt is present then write function will append the content to the existing one, but if the file is not present then it will create a new file with the provided content
with open("filehandling.txt", "a") as appendObj:
    s = """
    this is the new text that will be appended to the existing text
    hello 
    this is wasim
    a test automation QA engineer
    hope you are good!
    """
    appendObj.write(s)
    # appendObj.close()