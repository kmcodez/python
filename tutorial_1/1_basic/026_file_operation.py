import os  # os includes the standard python modules
import shutil  # includes the module for copying files

path = "C:\\Users\\STRATAZON\\Downloads\\learning codez\\codez\\python\\Bro_Code_Python\\0_files\\test.txt"


# print('---------------------{:^20}----------------------'.format( "check if a file exists"))
# # check if a file exists and the type of the file(file / dir?)
# if os.path.exists(path):
#     print("that location exists")
#     if os.path.isfile(path):
#         print("that is a file")
#     elif os.path.isdir(path):
#         print("that is a folder")
# else:
#     print("that location does not exist")


# print('---------------------{:^20}----------------------'.format( "open and read a file"))
# # open and read a file, if you add "with", it will close the file automatically
# try:
#     with open(path) as file:
#         print(file.read())
# except FileNotFoundError as e:
#     print(e)
#     print("That file was not found")
# except Exception as e:
#     print(e)
#     print("something went wrong :(")

# # it will print true, which means the file has been already closed.
# # print(file.closed)


# print('---------------------{:^20}----------------------'.format("open then write a file"))
# # open then write a file
# # the second argument is 'r' which means 'read the file' by default, 'w' means 'overwrite the file', 'a' means 'append the file'

# with open(path, 'w') as file:
#     file.write("Yoooooooo\nThis is some text\nHave a good one!\n")
# with open(path, "a") as file:
#     file.write("Have a nice day! see you!")


# print('---------------------{:^20}----------------------'.format("copy files"))
# # copy files

# # copyfile()    = copies contents of a file
# # copy()        = copyfile() + permission mode + destination can be a directory
# # copy2()       = copy() + metadata (file's creation and modification times)


# # the first argument for the path of source, the second for the destination path
# # of course, you can use copy and copy2 methods to replace the copyfile method even without changing the parameters
# shutil.copyfile(path, "C:\\Users\\STRATAZON\\Downloads\\learning codez\\codez\\python\\Bro_Code_Python\\0_files\\test1.txt")
# shutil.copy(path, "C:\\Users\\STRATAZON\\Downloads\\learning codez\\codez\\python\\Bro_Code_Python\\0_files\\test2.txt")
# shutil.copy2(path, "C:\\Users\\STRATAZON\\Downloads\\learning codez\\codez\\python\\Bro_Code_Python\\0_files\\test3.txt")


# print('---------------------{:^20}----------------------'.format("move files"))
# # move the file

# # the destination path
# destination = "C:\\Users\\STRATAZON\\Downloads\\text_1.txt"
# try:
#     if os.path.exists(destination):
#         print("There is already a file there")
#     else:
#         os.replace(path, destination)
#         print(path + " was moved")
# except FileNotFoundError:
#     print(path + " was not found")


# print('---------------------{:^20}----------------------'.format("delete files"))
# # delete files

# try:
#     # # delete the file
#     # os.remove(path)

#     # # delete an empty directory
#     # os.rmdir(path)

#     # # delete the directory containing files
#     # shutil.rmtree(path)
# except FileNotFoundError:
#     print("That file was not found")
# except PermissionError:
#     print("You don't have permission to delete that")
# except OSError:
#     print("You can't delete that using that function")
# else:
#     print(path + "was deleted")



