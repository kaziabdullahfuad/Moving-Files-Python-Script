import os

# try:
#     os.mkdir("dasd")
# except:
#     print("Already made")

# for i in range(3):
#     try:
#         os.mkdir("file"+str(i))
#     except:
#         print("Already exists")

#print(os.path.exists("D:\Python\OS module stuff\\file2"))
# holder=[23,32,55]
# print(type(holder))
# print("First number will show {0} and second {1} and third {2}".format(*holder))

#print(os.path.exists("D:\\New random for script\\bd flag zashra.png"))

# print(os.getcwd())

# print(os.listdir())

# holder=os.listdir()

# print(type(holder))

path_hold="D:\\New random for script"
images_holder=['.png','.jpeg']
for i in os.listdir(path_hold):
    #print(i.split('.'))
    new_dir=path_hold+"\\"+i
    #print(os.path.exists(new_dir))
    print(new_dir)
    #print(os.path.splitext(new_dir))
    root,extension=os.path.splitext(new_dir)
    if extension in images_holder:
        print("YES")
    print(i)


print(os.path.splitext("house draw.png"))

# print(os.listdir(path_hold))

# print(os.chdir(path_hold))

# print(os.getcwd())

print(os.path.exists(path_hold+"\\"+"tests"))
    #os.mkdir(path_hold+"\\"+"test")