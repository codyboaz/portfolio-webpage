import os

def rename_files():
    #1 Get files name from a foldeer
    file_list = os.listdir(r"/Users/Cody/Downloads/prank")
    #print(file_list)

    saved_path = os.getcwd()
    print("Current working directory is " + saved_path)
    os.chdir(r"/Users/Cody/Downloads/prank")
    #2 for each file, rename files
    for file_name in file_list:
        print("Old file name " + file_name)
        print("New file name " + file_name.translate(None, "0123456789"))
        os.rename(file_name, file_name.translate(None, "0123456789"))
    os.chdir(saved_path)
rename_files()
