# fp = open("text.txt", "x")    #creating a file
# fp.close()


#
# fp = open("text.txt", "w")            #adding contents to file
# fp.write("hi i am Fetsus Sabu")
# fp.close()




import os
# print(os.listdir())   #list of files from a working directory
#
# print(os.path.isfile("text.txt"))   #verify file exist
#
#
# with open(r"E:\New folder\python.txt", 'w') as fp:
#     fp.write("howdy")




# import os
# print(os.listdir(r"E:\New folder"))
# print(os.path.isfile(r"E:\New folder\python.txt"))  #verify file exist


#
# import os
# file_path = r"E:\New folder\python.txt"
# if os.path.exists(file_path):
#     print("file path exist")
#
# else:
#     with open(file_path, "w") as fp:
#         fp.write("this is first line")
#
#

#
# from datetime import datetime
#
# x = datetime.now()
#
# file_name = x.strftime("%d/%m/%Y")
# with open(r"E:\New folder\python.txt", "w") as fp:
#     fp.write(file_name)
#     print(file_name)
#
#
#
# file_name2 =r"E:\New folder\python2.txt" +"\t" + x.strftime("%d/%M/%H")
# with open(r'e:\New folder\python2.txt', "w") as wp:
#     wp.write(file_name2)



# file_name2 =r"E:\New folder\python2.txt" +"\t" + x.strftime("%d/%M/%H")
# with open(r'e:\New folder\python2.txt', "r") as wp:
#     wp.read()
#     print(file_name2)
#
# with open("text.txt", 'r') as rf:
#     line1 = rf.readline()
#     print(line1)


# with open("text.txt", 'r') as rf:
#     for i in range(3):
#         print(rf.readline().strip())     #strip for removing the space




# with open("text.txt", 'r') as rf:
#     line1 = rf.readline()
#     for last in rf:
#         pass
#     print(line1.strip())
#     print(last)


# n = 2
# with open("text.txt", 'r') as rf:
#     line = rf.readlines()[n:]
#     print(line)


#
# with open("text.txt", 'r') as rf:
#     line = rf.readlines()[::-1]      #reversing the file
#     print(line)
#
#     print("\t")
#
#     for i in reversed(line):
#         print(i.strip())




# text = "welcome to banglr"
#
# with open("text2.txt", "w") as fp:
#     fp.write(text)
#     print("done writing")
#
# with open("text2.txt", "r") as fp:
#     print(fp.read())
#
#
#
# name = "emma"
# personal_data = ["\nadress: amballoor", "\ncity: kerala"]
#
# with open("text2.txt", "w")as fp:
#     fp.write(name)
#     fp.writelines(personal_data)



#
# with open("text2.txt", "r") as fp:
#     fp.seek(2)
#     print(fp.read())
#
#
#
# with open("text2.txt", "r+")as fp:
#     fp.seek(0,2)
#     fp.write("\nthis content added to the end of the list")
#
#     fp.seek(0)
#     print(fp.read())

#
# with open("text2.txt", "r+") as fp:
#
#
#     #moving the file to the end of the file
#     fp.seek(0, 2)
#
#
#     #getting the file handle position
#     print("file handle at",fp.tell())
#
#
#     #writing new content
#     fp.write("\ndemonstrting tell")
#
#
#     #get the file handle position
#     print("file handle at", fp.tell())
#
#     #move to the beginning
#     fp.seek(0)
#
#
#     #get the file handle position
#     print("file handle at", fp.tell())
#
#
#
#     #read entire file
#     print("***printing file content***")
#     print(fp.read())
#     print("***done***")
#
#     # get the file handle position
#     print("file handle at", fp.tell())





# import os
#
#
# old_name = r"E:\New folder\python.txt"
# new_name = r"E:\New folder\python(renamed).txt"
#
# os.rename(old_name, new_name)




# import os
# old_name = r"E:\New folder\python.txt"
# new_name = r"E:\New folder\python(renamed).txt"
#
# if os.path.isfile(new_name):
#     print("THE FILE ALDREDY EXIST")
#
# else:
#     os.rename(old_name, new_name)
#
#
#
#
#           # OR
#
#
#
#
# import os
# old_name = r"E:\New folder\python.txt"
# new_name = r"E:\New folder\python(renamed).txt"
#
#
# try:
#     os.rename(old_name, new_name)
# except FileExistsError:
#     print("file already exist")
#     print("removing existing file...")
#
#     #for forcefully renaming
#     os.remove(new_name)
#     os.rename(old_name, new_name)





# import  os
# folder = r'E:\New folder\\'
# count = 1
#
#
# for text in os.listdir(folder):
#     source = folder + text
#
#
#     add = folder + "python file_" + str(count) + ".txt"
#
#
#     os.rename(source, add)
#     count+=1
#
# print(os.listdir(folder))





# import os
#
# file_name_to_be_renamed = ["python.txt", "python_1.txt"]
# folder = r"E:\New folder\\"
#
# for text in os.listdir(folder):
#
#
#     if text in file_name_to_be_renamed:
#
#         old_name= os.path.join(folder, text)
#
#         only_name = os.path.splitext(text)[0]
#
#         new_base = only_name + "_new" + ".txt"
#
#         new_name = os.path.join(folder, new_base)
#
#         os.rename(old_name, new_name)


#REMOVE#

# import os

# os.remove("/media/festus/STORAGE/test files for python/lil.txt")
#
# import os
#
# file_path = "/media/festus/STORAGE/test python/python2/test.txt"
# if os.path.exists(file_path):
#     os.remove(file_path)
# else:
#     print("there is no such file path")

# try:
#     file_path = "/media/festus/STORAGE/test python/python2/test.txt"
#     os.remove(file_path)
# except:
#     print("there is no such file path")


# import os
# os.unlink("test.py")

#
# import pathlib
# #
# file = pathlib.Path("/media/festus/STORAGE/test python/test files for python/test.txt")
# file.unlink()
#
#
# import os
#
# path = pathlib.Path("/media/festus/STORAGE/test python/test files for python/test.txt")
# for file_name in os.listdir(path):
#     file = file + file_name
#     if os.path.isfile(file):
#         os.remove(file)
#
#
# import os
# path = "/media/festus/STORAGE/test python/deel file"
# os.rmdir(path)
# print("deleted '%s' directory successfully" % path)
#
#
#
# import pathlib
#
# empty_dir = "/media/festus/STORAGE/test python/deel file"
# path = pathlib.Path(empty_dir)
# path.rmdir()

#
# import os
# import shutil
#
# def delete(path):
#     #path will be either relative or absolute
#     if os.path.isfile(path) or os.path.islink(path):
#         os.remove(path)
#     elif os.path.isdir(path):
#         shutil.rmtree(path)
#     else:
#         raise ValueError("path {} is not a file or directory".format(path))
## directory
# delete(..path..)

## path
# delete(..path..)





#COPY#

# import shutil
# scr_path = "/media/festus/STORAGE/test python/test files for python/test.txt"
# dst_path = "/media/festus/STORAGE/test python/.txt"
# shutil.copy(scr_path, dst_path)



# import os
# import shutil
#
# source_folder ="/media/festus/STORAGE/test python/test files for python//"
# destination_folder = "/media/festus/STORAGE/test python//"
#
# for file in os.listdir(source_folder):
#     source = source_folder + file
#     destination = destination_folder + file
#
#     if os.path.isfile(source):
#         shutil.copy(source, destination)




# import shutil
# source_dir = "/media/festus/STORAGE/test python/test files for python"
# destination_dir = "/media/festus/STORAGE/test python/python2"
# shutil.copytree(source_dir, destination_dir)



# import sys
# source_dir = "/media/festus/STORAGE/test python/test files for python/file1.txt"
# size = sys.getsizeof(source_dir)
# print(size)




