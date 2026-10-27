# os module to check file exist or not
import os

filename = input("Enter filename to open: ")

if os.path.exists(filename):
    with open(filename,'r') as f:
        print(f.read())
else:
    print("File not found.Please check the filename.")