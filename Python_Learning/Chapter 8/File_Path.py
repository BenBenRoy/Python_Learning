import os

#Automatically write a path according to OS
os.path.join('/','Users', 'Roy', 'Desktop','Python_Learning','File')   #Notice that the '/' is unnessesary for Windows OS
#Get Current Working Directory
os.getcwd()
#Change Working Directory
os.chdir(os.path.join('/','Users', 'Roy', 'Desktop','Python_Learning','Chapter 8'))
#Create New Folder in your OS
os.makedirs(os.path.join('/','Users', 'Roy', 'Desktop','Python_Learning','Practise_New_Directory','New_Subfolder'))

'''-----------------------------------
0. path starting with '.', or '..' is called 「relative path」; full path is called 「absoluate path」
1. '.' means 'this (working) directory'; '..' means 'parent (working) directory
2. os.path.abspath() returns the absolute path
3. os.path.isabs() returns True of False 


'''
os.path.isabs(os.path.abspath('.'))
