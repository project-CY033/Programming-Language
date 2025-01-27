# file handling (read , write , creat )
# r =read 
# w=weite 
# a  = append 
# r+ = Both read and write 
# b = binary mode 

# now creat a text file in python foilder or at desktop
# "\\n" represents a literal backslash followed by the letter "n".  

f = open("D:\\VS\\vs stdio\\python  files\\a.txt", "w")
f.write("helloe musharraf how are you : ")
# write in new line in a.txt file 

f.write("\n where are you \n writre all linux command  ")


# read file contain in terminal 
f=open("D:\\VS\\vs stdio\\python  files\\a.txt","r")
#  print(f.read(100))       100 is the size of the character 

# use readline()
print(f.readline())


# use readlines()
print(f.readlines())      # show all contains in the "list " fome 




# if we want to read  the conaian of that file whichis not exit 
try:
    f=open("D:\\VS\\vs stdio\\python  files\\a.txt","r")
    print(f.readlines())
except:
    print("file not found ")
else:
    # CLOSE FILE AFTE READ 
    f.close()
    print("file close ....")





# copy file in onther file
print("Copy file a.txt------>b.txt.................////")
try:
    with open("D:\\VS\\vs stdio\\python  files\\a.txt") as f2:
         with open("D:\\VS\\vs stdio\\python  files\\b.txt","w") as f3:
             for i in f2:
                f3.write(i)
except:
    print("file not available i in given location .....")
else:
    f2.close()
    print("file closed now.....")
    
    
    


# now delet this created file 
# import "os" module  because file save in memory 
print("file is being delete which is created in privious staps...........")
import os
if os.path.exists("D:\\VS\\vs stdio\\python  files\\d.txt"):
    os.remove("D:\\VS\\vs stdio\\python  files\\d.txt")
    print("File delete sucessfuly......")
    
else:
    print("File not found ! please enetr a valid file path....")