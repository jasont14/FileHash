import os, hashlib

directory = 'c:\\users\\jason\\1\\'
directory2 = 'c:\\users\\jason\\2\\'
destination = 'c:\\users\\jason\\3\\'

list1 = os.listdir(directory)
list2 = os.listdir(directory2)

list1h = []

list1kvp = {}
list2kvp = {}

file_hash = hashlib.sha256() 
for f in list1:
    file = directory + f
    with open(file, 'rb') as f: 
        fb = f.read() 
        while len(fb) > 0: 
            file_hash.update(fb) 
            fb = f.read() 

        list1kvp[file_hash.hexdigest()] = file

file_hash2 = hashlib.sha256() 
for f2 in list2:
    file2 = directory2 + f2
    with open(file2, 'rb') as f3: 
        fb = f3.read() 
        while len(fb) > 0: 
            file_hash2.update(fb) 
            fb = f3.read() 

        list2kvp[file_hash2.hexdigest()] = file2

print (list1kvp.items()) 
print (list2kvp.items()) 