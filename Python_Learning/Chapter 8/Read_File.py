import os
os.path.join('/','Users','Roy','Desktop','Python_Learning','File','Hello.txt')

# Assigning a Variable to File Object (a date type e.g. Tuple, Dic and et.al)

helloFile = open(os.path.join('/','Users','Roy','Desktop','Python_Learning','File','Hello.txt'))  #Open is function

# read file
helloContent= helloFile.read()


# write file

