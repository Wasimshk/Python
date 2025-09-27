
# OS
import os
print(os.listdir("../python-concepts")) #list all the files inside dir
print(os.getcwd()) #lists current working dir
print(os.path.exists("os_shutil")) #prints true if the file exist
print(os.path.join("this", "is", "the path to join")) #join the whole path
# os.remove("samplefile.txt") #delete a file
# os.rmdir("os_shutil") #deletes empty directory, for non empty directory it throws "OSError: [WinError 145] The directory is not empty: 'os_shutil'"

# shutil
# it is similar to os module but its a bit powerful
import shutil
shutil.copy("mytext.txt", "samplefile.txt") #copies all the content of source to destination, if destination file or directory is not available then it will create
os.remove("os/samplefile.txt") #delete a file
shutil.move("samplefile.txt", "os/") #copies the file to the desired directory
# be cautious with rmtree method
# shutil.rmtree('os_shutil') #it delete the complete directory tree, it does not matter if it is empty or not

